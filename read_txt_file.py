# -*- coding: utf-8 -*-
from find_files import getFiles
import numpy as np
def xywh_to_xyxy(bbox_xywh):
        x,y,w,h = bbox_xywh
        x1 = x
        x2 = x+w
        y1 = y
        y2 = y+h
        return x1,y1,x2,y2
def txt_to_bbox_xyxy(n):
    dir = getFiles("data",".txt")
    data = np.loadtxt(dir[3],dtype=int)
    kk = 1
    for box in data:
        bool_ = [False,False,True,True,True,True,False,False,False,False]
        boxywh = box[bool_]
        a = np.array([xywh_to_xyxy(boxywh)])
        if box[0]==n and box[6]==1 :
            if kk == 1:
                aa = a
                kk = 0
            aa=np.concatenate((aa,a),axis=0) 

    return aa