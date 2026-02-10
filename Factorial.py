n=int(input("Enter a number: "))
f,i=1,1
while i<=n:
    f*=i
    i+=1
print("Factorial of ",n," is ",f)