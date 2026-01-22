#convert celsius to fahrenhit:
user_c=float(input('enter temperature in celsius:'))
def convertor(celsius):
    fahrenhit=(user_c*9/5)+32
    return fahrenhit
result=(convertor(user_c))
print(user_c,'temperature in fahrenhit is',result)