# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 12:50:59 2021

@author: Abhijeet
"""
for T in range(int(input())):
    N,K,D = map(int, input().split())
    A = list(map(int, input().split()))
    
    answer = 0
    summation = sum(A)
    div = summation/K
    if(div>D):
        print(int(D))
    else:
        print(int(div))