# -*- coding: utf-8 -*-
import cv2
import numpy as np
from draw import draw_boxes
from read_txt_file import txt_to_bbox_xyxy
from find_files import getFiles
dirs = getFiles("D:\\BaiduNetdiskDownload\\VisDrone2019-MOT-train\\sequences\\uav0000020_00406_v",".jpg")
#cv2.namedWindow("test", 0)
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
im = cv2.imread(dirs[0])
im_height,im_width = im.shape[0:2]
writer = cv2.VideoWriter("output/result.avi", fourcc, 20, (im_width, im_height))
for idx, dir in enumerate(dirs):
    im = cv2.imread(dir)
    aa = txt_to_bbox_xyxy(idx+1)
    im = draw_boxes(im, aa, identities=None, offset=(0,0))
    #cv2.imshow("test", im)
    #cv2.waitKey(1)
    writer.write(im)
    print(str(idx+1)+"/"+str(len(dirs)))
#cv2.destroyAllWindows()

