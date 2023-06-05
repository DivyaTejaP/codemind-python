n,m=map(str,input().split())
f=n[0:int(m)]
l=n[-int(m)::1]
print(abs(int(f)-int(l)))