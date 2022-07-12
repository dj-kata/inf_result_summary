#!/usr/bin/python3
# usage: ./gen_result_summary.py target_dir
import cv2, re, sys, os
import numpy as np
from glob import glob

if len(sys.argv) < 2:
    print(f"usage: {sys.argv[0]} target_dir")
    sys.exit()

target_dir = sys.argv[1]
os.system(f'mkdir -p {target_dir}/mod')

for f in glob(target_dir+'/*.png'):
    bg = np.zeros((251,484,3), np.uint8)
    img = cv2.imread(f)
    graph = img[47:223, 905:1255]   # 350 x 176
    title = img[630:705, 408:892]   # 484 x 75
    sdata = img[260:436, 1120:1254] # 134 x 184
    bg[0:176, 0:350] = graph
    bg[176:251, 0:484] = title
    bg[0:176, 350:484] = sdata
    filename = f"{target_dir}/mod/{re.sub('.*/', '', f)}"
    print(filename)
    cv2.imwrite(filename, bg)