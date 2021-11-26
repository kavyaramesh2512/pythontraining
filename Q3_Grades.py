'''
to find the grade of the student
'''
markone =int(input("Enter the marks for English :"))
marktwo =int(input("Enter the marks for Scinece:"))
markThree =int(input("Enter the marks for Maths:"))

tot = markone+marktwo+markThree
avg = tot/3
print("avg",avg)
if avg>=90:
    print("Your Grade is A")
elif avg>=80:
    print("Your Grade is B")
elif avg>=35: 
    print("Average")
else:
    print("Fail")
     
