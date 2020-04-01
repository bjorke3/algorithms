# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 15:36:24 2020

@author: magbjork
"""

def mid(L, R):
    return L + (R - L) // 2 # avoids overflow


def simple_search(a, target):
    if len(a) == 0:
        return -1
    
    L, R = 0, len(a) - 1
    while L <= R:
        m = mid(L, R) 
        if a[m] == target:
            return m
        if a[m] < target:
            
            L = m + 1
        else:
            R = m - 1
    return -1


def first_greater(a, target):
    if len(a) == 0:
        return -1
    
    L, R = 0, len(a) - 1
    ans = -1
    while L <= R:
        m = mid(L, R)
        if a[m] > target:
            ans = m
            R = m - 1
        else:
            L = m + 1
    return ans


def first_greater_equal(a, target):
    return first_greater(a, target-1)


def max_in_shifted(a):
    # a is sorted, but shifted
    if len(a) == 0:
        return -1
    
    L, R = 0, len(a) - 1
    while L <= R:
        m = mid(L, R)
        if a[m] > a[m - 1]:
            ans = m
            L = m + 1
        else:
            R = m - 1
    return ans


def find_sqrt(n):
    L, R = 0, n
    while L <= R:
        m = mid(L, R)
        if m*m <= n:
            ans = m
            L = m + 1
        else:
            R = m - 1
    return ans
