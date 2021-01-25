for T in range(int(input())):
    N,X,Y = map(int, input().split())
    A = list(map(int, input().split()))

    A.sort(reverse=True)
    remainder = N%X
    answer = 0
    if(remainder==0):
        answer = sum(A)/X
        print(round(answer,6))
    else:
        xD = N-remainder
        answer = sum(A[:xD])/X
        if(remainder<Y):
            print(round(answer,6))
        else:
            answer = answer+sum(A[xD:]/remainder)
            print(round(answer,6))