import os

path = r"/media/yons/DATA/data/VOCtrain/VOC2007/labels"
path_label = r"/media/yons/DATA/data/VOCtrain/VOC2007/ImageSets/Main/test.txt"


with open("test.txt", "a") as f:
    for i in os.listdir(path):
        print(i.split(".")[0].rstrip("\n"))
        for j in open(path_label, "r"):
            print(j)
            if j.rstrip("\n") == i.split(".")[0]:
                print(os.path.join(path, i))
                f.write(os.path.join(path, i).replace(".txt",".jpg").replace("labels", "JPEGImages")+"\n")


