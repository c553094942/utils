import os
import random
import time

xmlfilepath = r'/media/yons/DATA/data/VOCtrain/VOC2007/labels'
saveBasePath = r'/media/yons/DATA/data/VOCtrain/VOC2007/ImageSets/Main'
if not os.path.exists(saveBasePath):
    os.makedirs(saveBasePath)
# 设置训练集和测试集的百分比
trainval_percent = 0.9
train_percent = 0.9
total_xml = os.listdir(xmlfilepath)  # 所有的

num = len(total_xml)  # xml文件的数量
index_list = range(num)  # 生成一个index列表
trainval_num = int(num * trainval_percent)
train_num = int(trainval_num * train_percent)
trainval_index = random.sample(index_list, trainval_num)
train_index = random.sample(trainval_index, train_num)

print("train and val size", trainval_num)
print("train size", train_num)

ftrainval = open(os.path.join(saveBasePath, 'trainval.txt'), 'w')
ftest = open(os.path.join(saveBasePath, 'test.txt'), 'w')
ftrain = open(os.path.join(saveBasePath, 'train.txt'), 'w')
fval = open(os.path.join(saveBasePath, 'val.txt'), 'w')

# Start time
start = time.time()
for i in index_list:
    name = os.path.splitext(total_xml[i])[0] + '\n'
    if i in trainval_index:
        ftrainval.write(name)
        if i in train_index:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)
# End time
end = time.time()
seconds = end - start
print("Time taken : {0} seconds".format(seconds))
ftrainval.close()
ftrain.close()
fval.close()
ftest.close()

