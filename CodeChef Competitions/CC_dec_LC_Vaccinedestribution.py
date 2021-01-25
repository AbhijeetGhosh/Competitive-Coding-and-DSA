for t in range(int(input())):
    N,D = map(int, input().split())
    age = list(map(int, input().split()))
    
    atrisk = 0
    for i in age:
        if(i<=9 or i>=80):
            atrisk += 1
    
    notatrisk = len(age)-atrisk
    
    day = 0
    curr = 0
    while(curr<atrisk):
        curr = curr+D
        day += 1
    curr=0
    while(curr<notatrisk):
        curr = curr+D
        day += 1
    
    print(day)