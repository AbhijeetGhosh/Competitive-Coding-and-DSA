# cook your dish here
for t in range(int(input())):
    a = input()
    b = input()
    la=[]
    lb=[]
    for i in a:
        la.append(i)
    for i in b:
        lb.append(i)
    c = 0
    for i in range(len(la)):
        if(la[i]==lb[i]):
            continue
        p = i
        while(p<len(la) and la[p]!=lb[p]):
            la[p]=lb[p]
            p = p+2
        c = c+1
    print(c)