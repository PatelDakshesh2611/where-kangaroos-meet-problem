def kangaroo(x1, v1, x2, v2):
    kangaroo1=v1
    kangaroo2=v2
    kangl1=x1
    kangl2=x2
    flag=0
    if kangl1>kangl2:
        
        while(kangl2<=kangl1):
            kangl2=kangl2+kangaroo2
            kangl1=kangl1+kangaroo1
            if(kangl1==kangl2):
                flag=1
                return "YES"
    else:
        while(kangl1<=kangl2):
            kangl2=kangl2+kangaroo2
            kangl1=kangl1+kangaroo1
            if(kangl1==kangl2):
                flag=1
                return "YES"
                
    if flag==0:
        return "NO"        
print(kangaroo(0,2,5,3))