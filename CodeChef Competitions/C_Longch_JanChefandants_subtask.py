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
        
    pos = 0
    neg = 0
    
    for i in range(len(X)):
        for j in range(len(X[i])):
            if(X[i][j]<0):
                neg+=1
            else:
                pos+=1
                
    print(pos*neg)
    
    