a=int(input())
if(a>=3 and a<=100):
    for i in range(1,a+1):
        for j in range(1,i+1):
            print("*",end='')
        print(end='
')
    for x in range(a-1,0,-1):
        for y in range(1,x+1):
            print("*",end='')
        print(end='
')
else:
    print("The pattern is not possible")
    
    
    
    
    