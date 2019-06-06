from PIL import Image
for i in range(1,483):
    path_o = r"/media/yons/DATA/data/VOCtrain/VOC2007/JPEGImage/image-%03d.jpeg" % i
    path_s = r"/media/yons/DATA/data/VOCtrain/VOC2007/JPEGImages/image-%03d.jpg" % i
    img = Image.open(path_o)
    img.save(path_s)
