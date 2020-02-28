#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 15:23:39 2020

@author: owenbezick
"""

def editDistance(x1, y1, x2, y2, t, cost):
    if len(x1) == 0:
        values = [x1, y1, x2, y2, t, cost]
        print(values)
        return values
    
    if len(y1) == 0 and len(y1) != 0:
        return editDistance(x1, y1, x2 + ' ', y2 + y1[0], t + 'I', cost + 1)
    
    print('x: ', x1[0], 'y: ', y1[0])
    
    if x1[0] == y1[0]:
        # COPY
        return editDistance(x1[1:], y1[1:], x2 + y1[0], y2 + y1[0], t + 'C', cost)
        
    else:
        # REPLACE
        replace = editDistance(x1[1:], y1[1:], x2 + y1[0], y2 + y1[0], t + 'R', cost + 1.5)
        replaceCost = replace[5]
        min = replaceCost
        print('min1: ' , min)
        # DELETE
        delete = editDistance(x1, y1[1:], x2, y2 + ' ', t + 'D', cost + 1)
        deleteCost = delete[5]
        
        if min < deleteCost:
            min = deleteCost
        
        # INSERT
        insert = editDistance(x1, y1, x2 + ' ', y2 + y1[0], t + 'I', cost + 1)
        insertCost = insert[5]
        
        print('min2: ' , min)
        if min < insertCost:
            min = insertCost
        print('min3: ' , min)
     
        
        if min == insertCost:
            return editDistance(x1, y1, x2 + ' ', y2 + y1[0], t + 'I', cost + 1)
        elif min == deleteCost:
            return editDistance(x1, y1[1:], x2, y2 + ' ', t +  'D', cost + 1)
        else:
            return editDistance(x1[1:], y1[1:], x2 + y1[0], y2 + y1[0], t + 'R', cost + 1.5)
        
        
def main():
    x = 'GATTACA'
    y = 'CATACAC'
    cost = 0
    editDistance(x, y, '','','', cost)