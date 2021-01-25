def Convert(string): 
	list1=[] 
	list1[:0]=string 
	return list1 
    
for T in range(int(input())):
    N = int(input())
    S = input()
    P = input()
    
    s_one = S.count('0')
    s_zero = S.count('1')
    
    p_one = P.count('0')
    p_zero = P.count('1')
    
    if(s_one==p_one and s_zero==p_zero):
        print("Yes")
    else:
        print("No")
    