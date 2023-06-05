a=(input())
s=0
for i in range(0,len(a)):
    s=s+int(a[i])**(i+1)
print(int(a)==s)