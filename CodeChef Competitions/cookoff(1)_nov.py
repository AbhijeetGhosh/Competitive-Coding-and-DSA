count = 0
n,m,k = map(int, input().split())
list1 = []
for i in range(0,n):
    list1 = list(map(int, input().split()))
    if((sum(list1)-list1[k])>=m and list1[k]<=10):
        count = count+1
print(count)