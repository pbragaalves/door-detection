import cv2
import numpy as np
import os
from os.path import isfile, join

pathIn= './f4_t30/'
pathOut = 'f4_t30.avi'
fps = 30

frame_array = []
files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f)) and f[-4:] == 'jpeg']

#for sorting the file names properly
files.sort()

for i in range(len(files)):
    filename=join(pathIn, files[i])
    #reading each files
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    
    #inserting the frames into an image array
    frame_array.append(img)

out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

for i in range(len(frame_array)):
    # writing to a image array
    out.write(frame_array[i])
out.release()