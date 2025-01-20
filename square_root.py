a=int(input("Enter a number:"))
z=1
if a < 0:
     print("Square root of a negative number is not a real number.")
else:
    for num in range(a):
        if a==(z*z):
            break
        z=z+1
    z= (z+a/z)/2
    err=abs(a-z**2)
    if err==0:
        print("The Square root of ",a ,"is",z)





