n=input()
c=0
k=0
for i in n:
    if(int(i)%2==0):
        c=c+1
    else:
        k=k+1
if c==0 and k>0:
    print("Odd")
elif k==0 and c>0:
    print("Even")
elif c>0 and k>0:
    print("Mixed")