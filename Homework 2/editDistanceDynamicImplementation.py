#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Homework 2
    Implementation of edit distance problem using Dynamic Programming.

    @authors: Owen Bezick & Morgan Dunnigan


- Overall, the algorithm is correct in structure
- I couldn't run the tests GATTACA->BUATTAA and GATTACA->ATACAB 

- If you try strings of different length, you have a problem on line 27. 
You invert the indexes of source/dest in the for loop 
- In your reconstruction of the alignment, you should have three indexes,
 one for the source, another for the destination, and one for the operation 
 that you are currently examining.
 
"""


def dynamicEditDistance(source, destination):
    # Instantiate Tables
    costTable = [[0 for x in range(1+ len(destination))] for y in range(1+len(source))]
    costTable[0][0] = 0
    transformationTable = [[0 for x in range(1+ len(destination))] for y in range(1+len(source))]
    
    # Fill in first row and column
    for i in range(1, 1 + len(destination)):
        costTable[0][i] = 1 + costTable[0][i-1]
        transformationTable[0][i] = 'D'
    for i in range(1, 1 + len(source)):
        costTable[i][0] = costTable[i-1][0] + 1
        transformationTable[i][0] = 'I'
    
    # Iterate over source and destination and fill in tables
    for i in range(1, 1 + len(destination)):
        for j in range(1,1 +  len(source)):
            # If transformation is a copy
            if destination[j-1] == source[i-1]:
                costTable[j][i] = costTable[j-1][i-1]
                transformationTable[j][i] = 'C'
            else:
                # Create Costs
                deleteCost = costTable[j][i-1] + 1
                insertCost = costTable[j-1][i] + 1
                replaceCost = costTable[j-1][i-1] + 1.5
                # Find minimum cost
                minCost = min(deleteCost, insertCost, replaceCost) 
                # Place in cost table
                costTable[j][i] = minCost
                # Fill transformation table
                if minCost == replaceCost:
                    transformationTable[j][i] = 'R'
                elif minCost == deleteCost:
                    transformationTable[j][i] = 'D'
                else:
                    transformationTable[j][i] = 'I'

    
    # Create the string of transformations
    i = len(source)
    j = len(destination)
    transformationString =  transformationTable[i][j]
    while i != 0 and j != 0:
        left = costTable[i][j - 1]
        top = costTable[i - 1][j]
        diag = costTable[i -1][j -1]
        minCost = min(left, top, diag)

        if diag == costTable[i][j]:
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

    # Trace back through transition table to get the new string
    # Reconstruction of alignment?
    newString = ''
    i = 0
    c = 0
    while i < len(transformationString):
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

    # Print out results
    print('Transformations:', transformationString)
    print('New String:', newString)
    print('Cost:', costTable[len(source)][len(destination)])


# Wrapper function
def main():
    source = "GATTACA"
    destination = "ATACAB"
    dynamicEditDistance(source, destination)


if __name__ == '__main__':
    main()
