"""
#include <stdio.h>
//#define mod 1000000007


int main(void) {
	// your code goes here
	// return 0;
	int test_case;
	unsigned long int a,b,res;
	scanf("%d",&test_case);
	while(test_case--){
	     scanf("%lu %lu",&a,&b);
	     if(a == 1 && b == 1){
	          printf("%lu\n",a);
	     } else {
	          res = (a*b)/2;
	          if(a%2 != 0 && b%2 != 0){
	               res = res + 1;
	          }
	         printf("%lu\n",res);
	     }
	}
"""
for T in range(int(input())):
   A,B = map(int, input().split())
    
   if(A==1 and B==1):
       print(A)
   else:
       res = (A*B)/2
       if(A%2!=0 and B%2!=0):
           res = res+1
       print(int(res))  