#!/usr/bin/bash

python3 << EOF
import os
import subprocess
from pathlib import Path

n = 22291846172619859445381409012451
d = 14499309299673345844676003563183

home = Path.home()
pathname = os.path.join(home, 'Pictures')

for filename in os.listdir(pathname):
    if not filename.endswith('.jpg'):
        continue
    pyfile  = os.path.join('materials', 'rsa_decrypt.py')
    picture = os.path.join(pathname, filename)
    command = ['python3', pyfile, str(n), str(d), picture]
    subprocess.run(command)
EOF
