#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Homework 2
    Implementation of edit distance problem using recursion.

    @authors: Owen Bezick & Morgan Dunnigan
    Created on Tue Feb 25 12:44:55 2020
"""


def editDistance(x, y, transformations, newX):
    """ Performs transformations on the x string.

    Parameters
    ----------
    x : str
        The original x string to be transformed
    y : str
        The y string for the x string to be transformed into
    transformations : str
        The str of transformations performed on string x
    newX : str
        The str of the transformed x string
    Returns
    -------
    values : list
        a list of the final transformations and the new x string.
    """
    # If y is empty, return transformations
    if len(y) == 0:
        #print(transformations, newX)
        values = []
        values.append(transformations)
        values.append(newX)
        return values
    
    # if x is empty, insert the elements in y
    if len(x) == 0:
        newX = newX + y[0]
        transformations = transformations + 'I'
        #print(transformations, newX)
        values = []
        values.append(transformations)
        values.append(newX)
        return values
        
    # If the two indices are the same 
    if x[0] == y[0]:
        newX = newX + y[0]
        transformations = transformations + 'C'
        return editDistance(x[1:], y[1:], transformations, newX)
        
    else:
        # If next y is the same as current x
        if x[1] == y[0]:
            newX = newX + ' '
            transformations = transformations + 'D'
            return editDistance(x[1:], y, transformations, newX)
        else:
            newX = newX + y[0]
            transformations = transformations + 'R'
            return editDistance(x[1:], y[1:], transformations, newX)
            
            
def calcCost(transformations, costDict):
    """ Calculates the cost of the transformations.

    Parameters
    ----------
    transformations : str
        The str of transformations performed on string x
    costDict : dict
        A dictionary populated with the costs for each transformation
    Returns
    -------
    cost : numeric
        The total cost of the transformations.
    """
    cost = 0
    for i in range(len(transformations)):
        cost = cost + costDict[transformations[i]]
            
    return cost


def printResults(transformations, newX, x, cost):
    """ Neatly prints the results of the editDistance function.

    Parameters
    ----------
    transformations : str
        The str of transformations performed on string x
    newX : str
        The str of the transformed x string
    x : str
        The original x string to be transformed
    cost : numeric
        The total cost of the transformatiopns.

    Returns
    -------
    none
    """
    print('='*len(newX))
    print(x)
    print(newX)
    print('='*len(newX))
    print(transformations)
    print("Total Cost: ", cost)
    
    
def main():
    """ Wrapper function.

    Parameters
    ----------
    none

    Returns
    -------
    none
    """
    x = 'GATTACA'
    y = 'CATACAC'
    costDict = {'I': 1, 'D': 1, 'R':1.5, 'C':0}
    
    values = editDistance(x, y, '', '')
    #print(values)
    transformations = values[0]
    newX = values[1]
    
    cost = calcCost(transformations, costDict)
    
    printResults(transformations, newX, x, cost)