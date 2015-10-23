#!/usr/bin/python

import os
import numpy as np
import PIL
from PIL import Image

def get_avg_pixel(im):
    
    imarr = np.array(Image.open(im), dtype=np.float)

    return np.mean(imarr)

def main():
    
    #Get all the PNG files in the directory
    file_list = os.listdir(os.getcwd())
    imlist=[filename for filename in file_list if  filename[-4:] in [".png",".PNG"]]

    avg_vals = []

    for im in imlist:
        pix_val = get_avg_pixel(im)
        avg_vals.append(pix_val)

    print avg_vals
    
if __name__=="__main__":
    main()

