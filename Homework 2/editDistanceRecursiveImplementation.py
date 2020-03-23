#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Homework 2
    Implementation of edit distance problem using recursion.

    @authors: Owen Bezick & Morgan Dunnigan
    
"""

def getTransformations(source, destination, transformations, cost):
    # If source is empty, the only option is to
    # insert all characters of second string into first
    if len(source) == 0 and len(destination) == 0:
        return [transformations, cost]

    if len(source) == 0 and len(destination) != 0:
        return getTransformations(source, destination[1:], transformations + 'I', cost + 1) # Insert operation
    elif len(source) != 0 and len(destination) == 0:
        return getTransformations(source[1:], destination, transformations + 'D', cost + 1) # Delete operation
    # If first characters of two strings are same, copy
    # the letter in question over to the new string
    # and pass the rest of the values of both strings
    elif source[0] == destination[0]:
        return getTransformations(source[1:], destination[1:], transformations + 'C', cost) # Copy operation
    # If first characters are not same, consider all three
    # operations on first character of source string, recursively
    # compute minimum cost for all three operations and return those values
    else:
        replace = getTransformations(source[1:], destination[1:], transformations + 'R', cost + 1.5) # Replace operation

        insert = getTransformations(source, destination[1:], transformations + 'I', cost + 1) # Insert operation

        delete = getTransformations(source[1:], destination, transformations + 'D', cost + 1) # Delete operation

        replaceCost = replace[1]
        insertCost = insert[1]
        deleteCost = delete[1]

        minCost = min(replaceCost, insertCost, deleteCost)

        # return transformations
        if minCost == replaceCost:
            return replace
        elif minCost == deleteCost:
            return delete
        else:
           return insert

# Wrapper function
def main():
    source = "GATTACA"
    destination = "CATACAC"
    cost = 0
    print (getTransformations(source, destination, '', cost))

if __name__ == '__main__':
    main()
