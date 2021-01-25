for T in range(int(input())):
    N,K = map(int, input().split())
    
    e_flag = 0
    o_flag = 0
    answer = []
    if((K%2)!=0):
        for i in range(1,K+1):
            if(e_flag==0):
                answer.append(i)
                e_flag=1
            else:
                answer.append(-i)
                e_flag=0
        for i in range(K+1,N+1):
            answer.append(-i)
    if((K%2)==0):
        for i in range(1,K+1):
            if(e_flag==0):
                answer.append(-i)
                e_flag=1
            else:
                answer.append(i)
                e_flag=0
        for i in range(K+1,N+1):
            answer.append(-i)
                
    if(len(answer)!=1):
        an = ""
        for i in answer:
            an = an + str(i) + " "
        an.strip()
        print(an)
    else:
        print(answer[0])