import os
path = r"/media/yons/DATA/data/voc增样/xml"
path_txt = r"/media/yons/DATA/data/voc增样/label.txt"
for filename in os.listdir(path,):
    print(filename.split(".")[0])
    with open(path_txt, "a")as f:
        f.write(filename.split(".")[0]+"\n")

