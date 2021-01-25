for T in range(int(input())):
    N,K = map(int, input().split())
    ar = list(map( int, input().split()))
    
    a = sum(ar)
    if(a%K==0):
        print(0)
    else:
        print(1)