import copy
from lxml.etree import Element, SubElement, tostring, ElementTree
import cv2
import os
import numpy as np
template_file = 'temp.xml'
path = "label" #文件夹目录
photopath = 'photo'
files= os.listdir(path)



for train_file in files:
    context = ''
    for line in open(path+'/'+train_file):
        context = context + line
    filename = train_file.replace('txt', 'jpg')
    information = context.split()
    label = 'car'
    xmin = information[1]
    ymin = information[2]
    xmax = information[3]
    ymax = information[4]

    tree = ElementTree()
    tree.parse(template_file)
    root = tree.getroot()
    root.find('filename').text = filename

    sz = root.find('size')
    im = cv2.imread('photo/'+filename)
    #print(filename)
    sz.find('height').text = str(im.shape[0])
    sz.find('width').text = str(im.shape[1])
    sz.find('depth').text = str(im.shape[2])

    obj = root.find('object')

    obj.find('name').text = label
    bb = obj.find('bndbox')
    bb.find('xmin').text = xmin
    bb.find('ymin').text = ymin
    bb.find('xmax').text = xmax
    bb.find('ymax').text = ymax

    xml_file = filename.replace('jpg', 'xml')

    tree.write('result/'+xml_file, encoding='utf-8')
