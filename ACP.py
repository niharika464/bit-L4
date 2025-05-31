def computepower(a,b):
    result=1
    while(a>0):
        if(a%2==0):
            b=b*b
            a>>=1
        else:
            result=result*b
            a=a-1
            return result
        a=int(input("Enter a for a^b:"))
        b=int(input("Enter b for a^b:"))
        print("Total:",computepower(a,b))