#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Homework 2 Corrections
    Quiz 3 Implementation
    Implementation of edit distance problem using Dynamic Programming.

    @authors: Owen Bezick
 
"""


def dynamicEditDistance(source, destination):
    # Instantiate Tables
    costTable = [[0 for x in range(1+ len(source))] for y in range(1+len(destination))]
    costTable[0][0] = 0
    
    # Fill in first row and column
    for i in range(1, 1 + len(source)):
        costTable[0][i] = 1 + costTable[0][i-1]
    for i in range(1, 1 + len(destination)):
        costTable[i][0] = costTable[i-1][0] + 1
 
    
    # Iterate over source and destination and fill in tables    
    for i in range(1, 1 + len(destination)):
        for j in range(1,1 +  len(source)):
            # If transformation is a copy
            if destination[i-1] == source[j-1]:
                costTable[i][j] = costTable[i-1][j-1]
            else:
                # Create Costs
                deleteCost = costTable[i][j-1] + 1
                insertCost = costTable[i-1][j] + 1
                replaceCost = costTable[i-1][j-1] + 1.5
                # Find minimum cost
                minCost = min(deleteCost, insertCost, replaceCost) 
                # Place in cost table
                costTable[i][j] = minCost

    # Create the string of transformations
    i = len(destination)
    j = len(source)
    transformationString = ""
    while i > 0 or j > 0:
        left = costTable[i][j - 1]
        top = costTable[i - 1][j]
        diag = costTable[i -1][j -1]
        minCost = min(left, top, diag)

        if minCost == diag:
            transformationString = 'C' + transformationString
            i = i - 1
            j = j - 1
        elif minCost == left:
            transformationString = 'D' + transformationString
            j = j - 1
        elif minCost == top:
            transformationString = 'I' +  transformationString
            i = i - 1
        else:
            transformationString =  'R' +  transformationString
            i = i - 1
            j = j - 1

    # Print Statements
    if transformationString[0] == 'I':
            source = '_' + source
            
    if transformationString[len(transformationString) -1] == 'I':
        source = source +'_'
            
    print('='*len(transformationString))
    print(source)
        
    for i in range(len(transformationString)):
        if transformationString[i] == 'D':
            destination = destination[:i] + ' ' + destination[i:]
        if transformationString[i] == 'I':
            source = source[:i] + '_' + source[i:]
            
    print(destination)
    print('='*len(transformationString))
    print(transformationString)
    print("Total cost:", costTable[-1][-1])
    

# Wrapper function
def main():
    source = "GATTACA"
    destination = "ATACAB"
    dynamicEditDistance(source, destination)


if __name__ == '__main__':
    main()
