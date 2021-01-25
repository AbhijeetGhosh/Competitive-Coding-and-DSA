d1,v1,d2,v2,P = map(int, input().split())
ad=av=bd=bv = 0

maxvax = v1+v2
curr = 0


if(d1<d2):
    ad = d1
    av = v1
    bd = d2
    bv = v2
if(d2<d1):
    ad = d2
    av = v2
    bd = d1
    bv = v1

def fun(curr,P):
    cur_day = 0
    if(d1==d2):
        while(curr<P):
            curr += maxvax
            cur_day += 1
        print(cur_day+d1-1)
        return
    c = bd-ad
    
    while(curr<P):
        if(cur_day<c):
            curr += av
            cur_day+=1
        else:
            curr+=maxvax
            cur_day += 1
    print(cur_day+ad-1)
    return

fun(0,P)
