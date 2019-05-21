import shutil
from lxml.etree import Element, SubElement, tostring, ElementTree
import os


path = "result" #xml文件夹目录
photopath = 'photo'#原图片文件夹
photooutputpath = 'output'#目标图片文件夹
txtoutputpath = 'txtresult'#目标txt文件夹
tagget = ['car']#需要的类型


files= os.listdir(path)
for train_file in files:
    tree = ElementTree()
    tree.parse(path+'/'+train_file)
    root = tree.getroot()
    obj = root.findall('object')
    size = root.find('size')
    height = int(size.find('height').text)
    width = int(size.find('width').text)
    f = open('txtresult'+'/'+train_file.replace('xml','txt'),'w')
    tag = False
    for i in obj:
        if i.find('name').text in tagget:
            tag = True
            label = 0
            for t in tagget:
                if t == i.find('name').text:
                    break
                else:
                    label = label + 1
            f.write(str(label) + ' ')
            bb = i.find('bndbox')
            xmin = int(bb.find('xmin').text)
            ymin = int(bb.find('ymin').text)
            xmax = int(bb.find('xmax').text)
            ymax = int(bb.find('ymax').text)
            f.write('%.06f' % ((xmin + xmax) / 2 / width) + ' ')
            f.write('%.06f' % ((ymin + ymax) / 2 / height) + ' ')
            f.write('%.06f' % ((xmax - xmin) / width) + ' ')
            f.write('%.06f' % ((ymax - ymin) / height) + ' \n')


    f.close()


    if tag ==False:
        os.remove(txtoutputpath+'/'+train_file.replace('xml','txt'))
    else:
        shutil.copyfile(photopath+'/'+train_file.replace('xml','jpg'), photooutputpath+'/'+train_file.replace('xml','jpg'))