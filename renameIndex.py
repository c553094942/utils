# -*- coding:utf-8 -*-
import os

xmlpath = r'/media/yons/DATA/data/Caltech_1/Annotations'
imgpath = r'/media/yons/DATA/data/Caltech/JPEGImages'
index = 0
count = 0
emptyset = set()
xmlFiles = os.listdir(xmlpath)
imgFiles = os.listdir(imgpath)
print(len(xmlFiles), len(imgFiles))

for xml in xmlFiles:
    xmlname = os.path.splitext(xml)[0]
    print(xmlname)
    imgname = os.path.join(imgpath, xmlname + '.jpg')
    print(imgname)

    if os.path.exists(imgname):
        newName = str(index).zfill(6)
        # 重命名图像
        os.rename(imgname, os.path.join(imgpath, newName + '.jpg'))
        # 重命名xml文件
        os.rename(os.path.join(xmlpath, xml), os.path.join(xmlpath, newName + '.xml'))
        print('============================================')
        print('img', imgname, os.path.join(imgpath, newName + '.jpg '))
        print('__________________________________________')
        print('xml', os.path.join(xmlpath, xml), os.path.join(xmlpath, newName + '.xml'))
        print('============================================')

        index = index + 1
    else:
        count += 1
        emptyset.add(xmlname.split('_')[0] + '_' + xmlname.split('_')[1])

sortedSet = sorted(emptyset, key=lambda x: (x.split('_')[0], x.split('_')[1]))
for i in sortedSet:
    print(i)
print(count)
