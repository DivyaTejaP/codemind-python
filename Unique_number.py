a=input()
for i in a:
    b=i
    c=0
    for j in a:
        if(b==j):
            c=c+1
    if(c==2):
        break
if(c>1):
    print("Not Unique Number")
else:
    print("Unique Number")