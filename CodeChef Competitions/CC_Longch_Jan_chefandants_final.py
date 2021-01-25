# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 11:42:45 2021

@author: Abhijeet
"""
for T in range(int(input())):
    N = int(input())
    
    X = []
    M = []
    #forming the M(for containing ant's line) and X(for containing ant's distance)
    for i in range(N):
        a = []
        li = list(map(int, input().split()))
        M.append(li[0])
        li.pop(0)
        X.append(li)