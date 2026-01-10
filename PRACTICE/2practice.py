#ask user for input then check zero,positive,negative,even or odd:
user=int(input("enter your number here:"))
if(user<0):
    print("your number is negative")
    if(user%2==0):
       print('number is even')
    else:
        print("number is odd")
elif(user>0):
    print("your number is positive")
    if(user%2==0):
       print('number is even')
    else:
        print("number is odd")
else:
    print('your number is zero')