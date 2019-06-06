#-*- coding:utf-8 -*-
import os
import shutil
if __name__ == "__main__":
    xmlpathin = '/media/yons/DATA/data/Caltech_1/Annotations/'
    xmlout = '/media/yons/DATA/data/Caltech/Annotations/'
    for subdir in os.listdir(xmlpathin):
        print(subdir)
        if subdir[:3] == 'set':
            for xmlfile in os.listdir(os.path.join(xmlpathin,subdir)):
                print('{}->{}'.format(os.path.join(xmlpathin,subdir,'bbox',xmlfile),os.path.join(xmlout,xmlfile)))
                shutil.copyfile(os.path.join(xmlpathin,subdir,'bbox',xmlfile),os.path.join(xmlout,xmlfile))
                


    # xmlpathin = '/media/yons/b8e254cc-f5ed-4d0d-8c4b-f47034e56b95/data/Caltech_1/Annotations'
    # xmlout = '/media/yons/b8e254cc-f5ed-4d0d-8c4b-f47034e56b95/data/Caltech/Annotations'
