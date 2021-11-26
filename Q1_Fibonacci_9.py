'''
To Print first 9 fibonacci numbers
'''

a=1
b=1

count=0
print(a)
while count<8 :
    print(b)
    a=b
    b=a+b
    count+=1
