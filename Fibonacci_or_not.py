n=int(input())
a=0
b=1
k=0
for i in range(1,n+1):
    #print(a,end=' ')
    c=a+b
    a=b
    b=c
    if(c==n):
        k+=1
if(k==1):
    print("True")
else:
    print("False")