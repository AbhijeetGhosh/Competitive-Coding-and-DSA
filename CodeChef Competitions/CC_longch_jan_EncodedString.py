# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 14:25:51 2021

@author: Abhijeet
"""
def fun(S, alphabets):
    if(S[0]==0):
        alphabets = alphabets[:8]
    else:
        alphabets = alphabets[8:]
    
    if(S[1]==0):
        alphabets = alphabets[:4]
    else:
        alphabets = alphabets[4:]
    
    if(S[2]==0):
        alphabets = alphabets[:2]
    else:
        alphabets = alphabets[2:]
    
    if(S[3]==0):
        alphabets = alphabets[0]
    else:
        alphabets = alphabets[1]
        
    return alphabets

for T in range(int(input())):
    N = int(input())
    S = list(map(int, input()))
    
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
    
    a=0
    b=4
    size = len(S)
    answer = ''
    for i in range(int(size/4)):
        answer = answer+fun(S[a:b], alphabets)
        a = a+4
        b = b+4
    
    print(answer)