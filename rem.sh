#!/bin/bash
mkdir -p ~/sync/rembackup
eval "$(conda shell.bash hook)"
conda activate rem
python ~/base/code/rem/rem.py
rsync -r --rsync-path=/opt/bin/rsync ~/sync/rembackup/ remarkable:~/.local/share/remarkable/xochitl
