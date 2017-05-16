from PIL import Image
import matplotlib.pyplot as plt
import os
import glob
import sys
from sys import argv
from datetime import *

Height = 224 #Required Height for resize
Width = 224 #Required Width for resize
outdir = './'


script,dir = argv

start = datetime.now()
counter = 0
for root, dirs, files in os.walk(dir, True, None, False):
    for f in files:
        if os.path.isfile(os.path.join(root,f)):
            ext = os.path.splitext(f)[1].lower()
            if ext in ('.jpg','.jpeg','.png','.gif'):
                counter += 1
                #print (f)
                try:
                    img = Image.open(os.path.join(root,f))
                    img = img.resize((Height,Width),Image.ANTIALIAS)
                    print os.path.join(root,f)
                    img.save(os.path.join(root,f))
                except Exception, e:
                    print 'e.message:\t', e


end = datetime.now()
print 'run time:',end -start
print 'images:',counter
