#-*- coding:utf-8 -*-
import os
import shutil

import os
import glob
import shutil

if __name__ == "__main__":
    imgpathin = r'/media/yons/DATA/data/Caltech/JPEGImage/'
    imgout = '/media/yons/DATA/data/Caltech/JPEGImages'
    for subdir in os.listdir(imgpathin):
        print(subdir)
        file_path = os.path.join(imgpathin, subdir)
        for subdir1 in os.listdir(file_path):
            # print(subdir1)
            # jpg_files = glob.glob(os.path.join(file_path, subdir1, "*.jpg"))
            file_path1 = os.path.join(file_path, subdir1)
            print("file_path1",file_path1)
            for jpg_file in os.listdir(file_path1):
                # print jpg_file
                src = os.path.join(file_path1, jpg_file)
                print("src:",src)
                new_name = str(subdir + "_" + subdir1 + "_" + jpg_file)
                print("new_name:",new_name)
                dst = os.path.join(imgout, new_name)
                print("dst:",dst)
                os.rename(src, dst)
