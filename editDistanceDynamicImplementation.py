#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Homework 2
    Implementation of edit distance problem using Dynamic Programming.

    @authors: Owen Bezick & Morgan Dunnigan
    Created on Wed Feb 26 14:10:15 2020
"""
def dynamicEditDistance(source, destination):
# make table
    notSecrettable = [[0 for x in range(1+ len(destination))] for y in range(1+len(source))] 
    secretTable = [[0 for x in range(1+ len(destination))] for y in range(1+len(source))]    
    notSecrettable[0][0] = 0
    
# initialize 1st row and column with copy or deletion cost
    for i in range(1, 1 + len(destination)):
        notSecrettable[0][i] = 1 + notSecrettable[0][i-1]
        secretTable[0][i] = 'D'
        
    for i in range(1, 1 + len(source)):
        notSecrettable[i][0] = notSecrettable[i-1][0] + 1
        secretTable[i][0] = 'I'
        
    for i in range(1, 1 + len(destination)):
        for j in range(1,1 +  len(source)):
            if destination[j-1] == source[i-1]:
                notSecrettable[j][i] = notSecrettable[j-1][i-1]
                secretTable[j][i] = 'C'
                
            else:
                deleteCost = notSecrettable[j][i-1] + 1
                insertCost = notSecrettable[j-1][i] + 1
                replaceCost = notSecrettable[j-1][i-1] + 1.5
                minCost = min(deleteCost, insertCost, replaceCost)
                
                notSecrettable[j][i] = minCost

                if minCost == replaceCost:
                    secretTable[j][i] = 'R'
                elif minCost == deleteCost:
                    secretTable[j][i] = 'D'
                else:
                    secretTable[j][i] = 'I'
                
    # Print tableeeeeee
    for i in range(1 +len(source)):
       print('i: ', i , notSecrettable[i])
       
    for i in range(1 +len(source)):
      print('i: ', i , secretTable[i])


  

    i = len(source)
    j = len(destination)
    transformationString =  secretTable[i][j]
    while i != 0 and j != 0:
        left = notSecrettable[i][j - 1]
        top = notSecrettable[i - 1][j]
        diag = notSecrettable[i -1][j -1]
        minCost = min(left, top, diag)

        if diag == notSecrettable[i][j]:
            transformationString = 'C' + transformationString 
            i = i - 1
            j = j - 1
        elif minCost == left:
            transformationString = 'I' + transformationString 
            j = j - 1
        elif minCost == top:
            transformationString = 'D' +  transformationString 
            i = i - 1
        else:
            transformationString =  'R' +  transformationString 
            i = i - 1
            j = j - 1
        
    #iterate over the transformation list 
    newString = ''
    i = 0
    c = 0
    while i < len(transformationString):
        print(newString)
        if transformationString[i] == 'C':
            newString = newString + destination[c]
            i+=1
            c+=1
        elif transformationString[i] == 'R':
            newString = newString + destination[c]
            i+=1
            c+=1
        elif transformationString[i] == 'I':
            newString = newString + destination[c]
            i+=1
            c+=1
        else:
            newString = newString + ' '
            i+=1
    print(newString)
    #create a new list
    
    
    

# start on bottom right and take the minumum of 
# the three around you and then that traces out the path

# Wrapper function
def main():
    source = "GATTACA"
    destination = "CATACAC"
    dynamicEditDistance(source, destination)

if __name__ == '__main__':
    main()