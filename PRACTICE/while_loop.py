#lec5 (while loops)
# qns1.print('hello ' *5)
#while loop
#while True:
  #  print('hello')

#qns 2 i=1                #print number from 1 to 100
#while i<=100:
#   print("hello",i )
 #qns 3   i+=1
#i= 100               #print 100 -1
#while i>=1:
 #   print(i)
  #  i-=1
#qns 4 i=1                #multiplicatiion of 7
#while i<=10:
 #   print(78*i)
 #   i+=1
#qns 5nums=[1,4,9,16,25,36,49,56,81,100]         #print list with l
#index=0
#while index<len(nums):
   #  print(nums[index])
    # index+=1
#qns6.find n number 
#nums=(1,4,9,16,25,36,49,56,81,100)        
#x = 49

#i = 0
#while i < len(nums):
 #   if(nums[i]==x):
  #     print("found your value at index",i)
   # i+=1


#use of break statement
#nums=(1,4,9,16,25,36,49,56,81,100,36)        
#x = 36

#i = 0
#while i < len(nums):
 #   if(nums[i]==x):
  #     print("found your value at index",i)
   #    break;      #when found first then we out from loop
    #i+=1


#use of continue statement
i=0
while i <= 6:
    if(i% 2== 0):
       i +=1
       continue;
    print(i)
    i += 1

