#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 17:39:50 2020

@author: owenbezick
"""

def fancyMultiplication(x ,y):
    # Convert to strings 
    x = str(x)
    y = str(y)
    
    # Base case
    if len(x) == 1 and len(y) == 1:
        return int(x) * int(y)
    if len(x) < len(y):
        x = '0' * (len(y) - len(x)) + x
    elif len(y) < len(x):
        y = '0' * (len(x) - len(y)) + y
    
    
    n = len(x)
    j = n//2
    
    # Odd digit integers
    if (n % 2) != 0:
        j += 1    
    
    a = int(x[:j])
    b = int(x[j:])
    c = int(y[:j])
    d = int(y[j:])
    
    # Recursive cases
    ac = fancyMultiplication(a, c)
    bd = fancyMultiplication(b, d)
    k = fancyMultiplication(a + b, c + d)
    # Final Calculations
    A = int(str(ac) + '0' * ((n-j) *2))
    B = int(str(k - ac - bd) + ('0' * (n - j)))
    return A + B + bd