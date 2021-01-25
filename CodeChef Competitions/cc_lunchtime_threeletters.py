def Convert(string): 
	list1=[] 
	list1[:0]=string 
	return list1 

            
for T in range(int(input())):
    S = input()

        
    S = Convert(S)
    answer = 0
    # for i in range(len(S)-1):
    #     if(S.count(S[i])>=2):
    #         S.pop(i)
    #         S.remove(S[i])
            
    #         j = i
    #         while(S[j+1]):
    #             if(S.count(S[j+1])<2):
    #                 S.pop(j+1)
    #                 answer = answer + 1
    #                 break
    #             else:
    #                 j=j+1
                    
    # print(answer)         
                  
    c = 0
    for i in S:
        if(S.count(i)>=2):
            S.remove(i) #removing curr
            S.remove(i) #removing duplecate
            while(len(S)>0):
                if(S.count(S[c])==1):
                    S.pop(c)
                    answer = answer+1
                    break
                else:
                    c=c+1
    print(answer)