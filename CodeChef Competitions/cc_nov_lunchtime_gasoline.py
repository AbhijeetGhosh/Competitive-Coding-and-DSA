def checkP(petrol,F,N):
    flag = 0
    while(petrol!=0):
        if(flag==N):
            return sum(F)
        if(petrol<N-1):
            for i in range(petrol-1):
                petrol += F[i]
                petrol-=1
                flag = flag+1
        else:
            petrol = sum(F)
            return petrol
    return petrol
for T in range(int(input())):
    N = int(input())
    F = list(map(int, input().split()))


    answer = 0
    petrol = F[0]
    if(petrol<N-1):
        answer = checkP(petrol, F, N)
    else:
        answer = sum(F)
    print(answer)