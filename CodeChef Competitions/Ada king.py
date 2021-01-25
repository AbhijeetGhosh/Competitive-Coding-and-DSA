"""
king at (r,c)
can move to (r',c')
only if (r'-r)^2+(c'-c)^2<=2

count the no. of squares king can be visited in K moves

input: T
        R C K
output: no. of squares the king can visit
"""

for i in range(int(input())):
    r,c,k = map(int, input().split())
    answer = 0

    for a in range(k):
        for i in range(1, 8):
            for j in range(1, 8):
                if ((j - r) ** 2 + (i - c) ** 2 <= 2):
                    answer = answer + 1
        print(answer)

