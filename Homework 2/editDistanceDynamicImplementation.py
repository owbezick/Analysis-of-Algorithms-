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
 
    
    # Iterate over source and destination and fill in cost table    
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
                minCost = min(deleteCost, insertCost, replaceCost)
                if i > 2 and j >  2:
                    exchangeCost = costTable[i-2][j-2] + 1.8
                    minCost = min(minCost, exchangeCost)                     
                if i == len(destination) and j >= len(destination):
                    killCost = costTable[i][j-4] + 3
                    minCost = min(minCost, killCost)
                    if minCost == killCost:
                        for k in range(j, len(source) + 1):
                            costTable[i][k] = minCost
                        break
                # Place in cost table
                costTable[i][j] = minCost
    
    #for i in range(len(costTable)):
     #   print(costTable[i])
        
    # Create the string of transformations
    # edge cases for copy and exchange 
    i = len(destination)
    j = len(source)
    transformationString = ""
    while i > 0 or j > 0:
        #print("i:", i, " j:", j, " cost:", costTable[i][j])
        delete = costTable[i][j - 1]
        #print("deleteCost: ", delete)
        insert = costTable[i - 1][j]
        #print("insert: ", insert)
        replace = costTable[i -1][j -1]
        #print("replace: ", replace)
        minCost = min(delete, replace, insert)
        if i == len(destination) and j > len(destination):
             killCost = costTable[i][len(destination)+1]
             minCost = min(minCost, killCost)
        if i > 2 and j > 2 and source[j-2] == destination[i-1] and destination[i-2] == source[j-1]:
             exchange = costTable[i-2][j-2]
             print("exchange: ", exchange)
             minCost = min(minCost, exchange)
             if minCost == exchange:
                 transformationString = 'EE' + transformationString
                 i = i - 2
                 j = j - 2
        #print("minCost: ", minCost)
        if minCost == delete:
            transformationString = 'D' + transformationString
            j = j - 1
        elif minCost == insert:
            transformationString = 'I' +  transformationString
            i = i - 1
        elif minCost == killCost:
            transformationString = 'K' + transformationString
            j = len(destination) +1
            
        if source[j-1] == destination[i-1]:
            transformationString = 'C' + transformationString
            i = i - 1
            j = j - 1
        else:
            transformationString =  'R' +  transformationString
            i = i - 1
            j = j - 1
        
            
    # Print Statements
    if transformationString[0] == 'I':
            source = '_' + source
            
    if transformationString[len(transformationString) -1] == 'I':
        source = source +'_'
            
    print('='* len(transformationString))
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
    source = "this_is_too_longgggg"
    destination = "this_is_cool"
    dynamicEditDistance(source, destination)


if __name__ == '__main__':
    main()
