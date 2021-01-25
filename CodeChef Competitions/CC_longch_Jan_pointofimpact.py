for T in range(int(input())):
    N,K,x,y = map(int, input().split())
    if(x==y):
        print(N,N)
    else:
        li = []
        if(x<y):
            li=[[x+N-y, N],[N,N-y+x],[y-x,0],[0,y-x]]
        else:
            li=[[N,y+N-x],[y+N-x,N],[0,x-y],[x-y,0]]
        
        potato = li[(K-1)%4]
        print(potato[0],potato[1])