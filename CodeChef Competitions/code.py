"""
2 rounds A and B
sorted in descending order of score
logic-
1. first arrange in descending order
simply find the the score of 1500th team,
count the no. of teams having equal or more than that score

Approach:
arrange in descending order
take first element, add the smallest element check, if yes-end
if not, put it back and then check for next element, if yes-end
if not, put it back and repeat.

"""
for i in range(int(input())):
    n,k = map(int, input().split())
    Q = list(map(int, input().split()))

    Q.sort(reverse=True)

   b1=0
   b2=0

   for i in range(n-1):
       b1 = b1 + Q[0]
