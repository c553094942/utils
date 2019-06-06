import os
from PIL import Image
path_xml = r"/media/yons/DATA/data/voc增样/slice_0530_xml"
path_jpeg = r"/media/yons/DATA/data/voc增样/slice_0530"

files_pic = os.listdir(path_jpeg)
files_xml = os.listdir(path_xml)

path_save_pic = r"/media/yons/DATA/data/voc增样/pic"
path_save_xml = r"/media/yons/DATA/data/voc增样/xml"

count = 3005

for i in files_pic:
    # print(i.split(".")[0])
    for j in files_xml:
        # print(j.split(".")[0])
        # print(os.path.splitext(j)[1])
        if i.split(".")[0] == j.split(".")[0]:
            img = Image.open(os.path.join(path_jpeg, i))
            img.save(r"/media/yons/DATA/data/voc增样/pic/image-%04d.jpg" % count)
            old = os.path.join(path_xml, j)
            print(old)
            new = os.path.join(path_save_xml, "image-"+str(count).zfill(4)+os.path.splitext(j)[1])
            print(new)
            os.rename(old, new)
            count += 1
            print("true")
