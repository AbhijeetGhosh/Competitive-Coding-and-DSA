for T in range(int(input())):
   A,B = map(int, input().split())
    
   if( a==1 and b==1):
       print(1)
       continue
   if((A%2)!=0 and (B%2)!=0):
       count = (A*B)/2+1
   else:
       count = (A*B)/2
   print(int(count))