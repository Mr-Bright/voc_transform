from lxml.etree import Element, SubElement, tostring, ElementTree
import cv2
import os
import numpy as np
tagget = ['steelline']
tree = ElementTree()
tree.parse('test.xml')
root = tree.getroot()
obj = root.findall('object')
size = root.find('size')
height = int(size.find('height').text)
width = int(size.find('width').text)
f = open('test.txt','w')
for i in obj:
    if i.find('name').text in tagget:
        label = 0
        for t in tagget:
            if t==i.find('name').text:
                break
            else:
                label = label+1
        f.write(str(label)+' ')
        bb = i.find('bndbox')
        xmin = int(bb.find('xmin').text)
        ymin = int(bb.find('ymin').text)
        xmax = int(bb.find('xmax').text)
        ymax = int(bb.find('ymax').text)
        f.write('%.06f' %((xmin+xmax)/2/width)+' ')
        f.write('%.06f' %((ymin+ymax)/2/height)+' ')
        f.write('%.06f' %((xmax-xmin)/width)+' ')
        f.write('%.06f' %((ymax-ymin)/height)+' \n')
