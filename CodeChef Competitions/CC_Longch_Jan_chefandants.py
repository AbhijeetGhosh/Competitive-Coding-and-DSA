# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 11:48:23 2021

@author: Abhijeet
"""
# import time

from itertools import chain

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
    # start = time.time()
    D = []#contains an ant's direction and has the same size as that of X
    P = [] #contains positions of ants and has the same size as that of X
    #I am assuming no ant is spawn at O
    #creating the array of position.. and the array of direction
    for i in range(N):
        
        a = []
        b = []
        for p in X[i]:
            if(p<0):
                a.append(-1)
                b.append(1)
            else:
                a.append(1)
                b.append(-1)
            
        P.append(a)
        D.append(b)


    # #direction of any ant = -1 * position
    # for i in range(N):
    #     a=[]
    #     for j in range(len(X[i])):
    #         a[j]=(-1)*P[i][j]
    #     D.append(a)
    
    iterations = 0
    collisions = 0
    
    # start = time.time()
    while(1): #the ultimate loop
    
        #collided ants
        col = []
    
        #condition 1 : check if there's any collision in the same line
        for i in range(len(X)):#for every row in a
            temp = [] #will store the value of element which has a duplecate for a particular row
            for j in range(len(X[i])): #for every element in the given row that we're gonna check
                for k in range(j+1,len(X[i])): #for every element after the current element that we will compare the current element with
                    if(X[i][j]==X[i][k] and X[i][j]!=0): #comparing to check if it's same and not equal to 0
                        if(X[i][j] not in temp): #checking if that element has already been counted
                            collisions = collisions+1 #adding collision
                            # temp.append(X[i][j]) #appending to the temp list
                            # coor = [i,j]
                            # col.append(coor)
                            # coor = [i,k]
                            # col.append(coor)
                        
        #condition 2 : check if there's any collision 
        temp2 = [] #this will have the coordinates of ants at O
        for i in range(len(X)): #for every row
            for j in range(len(X[i])): #for every column
                if(X[i][j]==0): 
                    coor = [i,j]
                    temp2.append(coor)
            
        if(len(temp2)>1): #if more than one ent is at O
            collisions = collisions+1
            for ants in temp2:
                col.append(ants)
            
        #code to update and change the direction of all ants that collided
        for ant in col:
            i=ant[0]
            j=ant[1]
            D[i][j]=(-1)*D[i][j]
            
        #code to update and increment the appropriate distance of every ant according to it's direction
        for i in range(len(X)):
            for j in range(len(X[i])):
                X[i][j] = X[i][j] + (0.5*D[i][j])
                
        #code to update the position of every ant
        # P=[]
        # for i in range(N):
        #     a = []
        #     for p in X[i]:
        #         if(p<0):
        #             a.append(-1)
        #         else:
        #             a.append(1)
            
        # P.append(a)
        
        it_is_time = False
        
        # check = []
        
        # for i in range(len(P)):
        #     temp3 = []
        #     for j in range(len(P[i])):
        #         tem = P[i][j]*D[i][j]
        #         temp3.append(tem)
        #         print(temp3)
        #     check.append(temp3)
        #     print(check)       
        
        flag = []
        for i in range(len(P)):
            sub = []
            for j in range(len(P[i])):
                if(X[i][j]==0):
                    a=-1
                else:
                    a = int((X[i][j]/abs(X[i][j]))*D[i][j])
                sub.append(a)
            flag.append(sub)
    
        
        
       
        if set(chain.from_iterable(flag)) == {1}:
            it_is_time = True
        # print(collisions)
        if(it_is_time==True):
            break
            
        
        iterations += 1
        # print(flag)
        # print(iterations)
        # print("X = ",X)
        # print("P = ",P)
        # print("D = ",D)
        # print(flag)
        
        #print(collisions)
        #code to check if it's time to break the while loop
        # class breakIt(Exception): pass
        
        # is_it_time=False
        # try:
        #     for i in range(len(X)):
        #         for j in range(len(X[i])):
        #             if(P[i][j]*D[i][j]==-1):
        #                 raise breakIt
        #     is_it_time=True
        # except breakIt:
        #     pass
                        
        # if(is_it_time==True):
        #     break
                
            
        
                
    # print(N)
    # print(M)
    # print(X)
    # print(P)
    # print(D)
    print(collisions)
    # print("iterations = ", iterations)
# end = time.time()
# print("time: ",end-start)