# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 15:09:35 2021

@author: Abhijeet

"""



for T in range(int(input())):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    ir = 0
    if(len(A)<=len(B)):
        ir = len(A)
    else:
        ir = len(B)
    
    A.sort()
    B.sort(reverse = True)
    
    if(sum(A)>sum(B)):
        print(0)
    else:
        count = 0
        i1 = 0
        while(sum(A)<=sum(B) and i1<ir):
            if(A[i1]<B[i1]):
                temp = A[i1]
                A[i1] = B[i1]
                B[i1] = temp
                
                count = count+1
            i1 = i1+1
            
        if(sum(A)<=sum(B)):
            print(-1)
        else:
            print(count)
    
    
    