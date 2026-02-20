a=  int(input("Enter your age: "))
print("You age is:",a)
#conditional opeartor
# >,<,>=,<=,==,!=
print(a>18)
print(a<18)
print(a>=18)
print(a<=18)
print(a==18)
print(a!=18)
if a>=18:
    print("You can drive")
else:
    print("You cannot drive")
print("Thank you!")   
# if elseif else
appleprice=190
budget=200
if appleprice<budget:
    print("You can buy apple")
elif appleprice==budget:
    print("You can buy apple but no money for ice-cream")
else:
    print("You cannot buy apple")
print("Thank you!")

num=int(input("Enter a number: "))
if num<0:
    print("The number is negative") 
elif num==0:
    print("The number is zero")
else:
    print("The number is positive")
print("Thank you!")