#write a Recursive function to cakculate sum of n numbers;
def sum_n(numbers):
    if(numbers==0):
        return 0

    return sum_n(numbers-1)+numbers
sum=sum_n(6)
print(sum)