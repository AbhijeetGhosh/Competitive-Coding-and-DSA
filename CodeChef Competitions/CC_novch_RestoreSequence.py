"""
Bi is the largest index j such that
Ai divides Aj

"""
for i in range(int(input())):
    N = int(input())
    N = N-1
    B = list(map(int, input().split()))

    result = [2]
    for i in range(0,N):
        result.append(1)
    for i in range(0,N):
        result[B[i]-1] = result[i]*2
    print(B)
