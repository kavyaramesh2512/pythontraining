'''
to find the whether a given number is fibonacci number or not'''

n=int(input("if the given number is :"))
c=0
a=1
b=1
if n==0 or n==1:
    print("Yes, it is a Fibonacci Number")
else:
    while c<n:
        c=a+b
        b=a
        a=c
    if c==n:
        print("Yes, it is a Fibonacci Number")
    else:
        print("No, it is not a fibonacci Number")
                    
