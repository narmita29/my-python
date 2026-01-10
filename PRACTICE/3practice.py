#print 1 to 100 numbers divisible by 3 and 5  both 
#for i in range (1,101):
 #   if(i%3==0 and i%5==0):
  #      print(i)
 

x=int(input('enter your number'))


if(x>101):
    print("Enter number lesser than this")
elif(x%3==0 and x%5==0):
    print("yss its divisible by both numbers")
else:
    print("oppps try other number")

   