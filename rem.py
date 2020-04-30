import os, json, time
from uuid import uuid4
from dataclasses import dataclass
from shutil import copyfile

from templates import metadata_template, content_template, cmd_template

base = '/home/odin/sync/digitalpaper'
dest = '/home/odin/sync/rembackup'
mapfile = '/home/odin/sync/rembackup/uuid.json'
exts = ['.epub', '.pdf']

sec = int(time.time())

@dataclass
class UUIDMap:
    base: str
    mapfile: str
    def loadMap(self):
        self.uuidmap = {self.base: ''}
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

uuidmap = UUIDMap(base, mapfile)
uuidmap.loadMap()

def attemptCopy(s, d):
    if not os.path.exists(d):
        print(f"Copying {s}")
        copyfile(s, d)

def attemptWrite(f, data):
    if not os.path.exists(f):
        with open(f, 'w') as fp:
            fp.write(data)

def attemptThumbnail(f, pdf):
    if not os.path.exists(f):
        os.mkdir(f)
        os.system(cmd_template.format(pdf, f+'/0'))
    
def createNode(r, f, ext=''):
    fid, pid = uuidmap.getMap(r+'/'+f), uuidmap.getMap(r)
    if ext in exts:
        attemptCopy(r+'/'+f+ext, dest+'/'+fid+ext)
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
