# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 21:45:33 2021

@author: Abhijeet
"""
for T in range(int(input())):
    N = int(input())
    
    primes=[]
    for num in range(1,N):
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
                
    print(primes)
    answer = 0
    