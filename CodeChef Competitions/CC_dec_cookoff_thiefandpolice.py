# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 21:49:33 2020

@author: Abhijeet
"""
for T in range(int(input())):
    x,y,K,N = map(int, input().split())
    xl = xr = x
    yl = yr = y
    #t1 = t2 = t3 = t4 = 0
    
    # if(x%K==0):
    #     t1=1
    # if(y%K==0):
    #     t2=1
    # if((N-x)%K==0):
    #     t3=1
    # if((N-y)%K==0):
    #     t4=1
    
    
    # elif(t1==1 and t2==1):
    #     print('Yes')
    # elif(t3==1 and t4==1):
    #     print('Yes')
    # else:
    #     print('No')
    
    police = []
    thief = []
    
    while(1):
        if(xr>N):
            break
        xr+=K
        police.append(xr)
    while(1):
        xl-=K
        if(xl<0):
            break
        police.append(xr)
    while(1):
        yr+=K
        if(yr>N):
            break
        thief.append(yr)
    while(1):
        yl-=K
        if(yl<0):
            break
        thief.append(xr)
        
    if(N==K):
        print('No')
    elif(N==1):
        print('No')
    elif(len(set(police).intersection(set(thief)))>0):
       print("Yes")
    else:
        print("No")
    
    
    