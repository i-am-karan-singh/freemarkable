import os, json, time
from uuid import uuid4
from dataclasses import dataclass
from shutil import copyfile

from templates_live import metadata_template, content_template, cmd_template

base = '/home/root/digitalpaper'
dest = '/home/root/.local/share/remarkable/xochitl'
mapfile = '/home/root/.local/share/remarkable/xochitl/uuid.json'
exts = ['.epub', '.pdf']

sec = int(time.time())

@dataclass
class UUIDMap:
    mapfile: str
    def loadMap(self):
        self.uuidmap = {'/': ''}
        if os.path.exists(self.mapfile):
            with open(self.mapfile, 'r') as fp:
                self.uuidmap = json.load(fp)
                print(f"UUID map loaded from {self.mapfile}")
    def saveMap(self):
        with open(self.mapfile, 'w') as fp:
            json.dump(self.uuidmap, fp)
    def getMap(self, s):
        self.uuidmap[s] = self.uuidmap[s] if s in self.uuidmap else str(uuid4())
        return self.uuidmap[s]

uuidmap = UUIDMap(mapfile)
uuidmap.loadMap()

def attemptLink(s, d):
    if not os.path.lexists(d):
        print(f"Copying {s}")
        os.system(f'ln -s "{s}" {d}')

def attemptWrite(f, data):
    if not os.path.exists(f):
        with open(f, 'w') as fp:
            fp.write(data)

def attemptThumbnail(f, pdf):
    if not os.path.exists(f):
        os.mkdir(f)
        os.system(cmd_template.format(pdf, f+'/0'))
    
def createNode(r, f, ext=''):
    fid, pid = uuidmap.getMap((r+'/'+f)[len(base):]), uuidmap.getMap((r)[len(base):])
    if ext in exts:
        attemptLink(r+'/'+f+ext, dest+'/'+fid+ext)
        attemptWrite(dest+'/'+fid+'.metadata', metadata_template[ext].format(sec, pid, f))
        attemptWrite(dest+'/'+fid+'.content', content_template[ext].format(sec, pid, f))
        attemptThumbnail(dest+'/'+fid+'.thumbnails', dest+'/'+fid+ext)
        # Thumbnail generation can be slow for large files
    if ext == '':
        attemptWrite(dest+'/'+fid+'.metadata', metadata_template[ext].format(sec, pid, f))
        attemptWrite(dest+'/'+fid+'.content', content_template[ext].format(sec, pid, f))

for r, ds, fs in os.walk(base):
    for d in ds:
        createNode(r, d, '')
    for f in fs:
        sp = os.path.splitext(f)
        createNode(r, *sp)

uuidmap.saveMap()
