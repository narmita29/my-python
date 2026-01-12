#write a Recursive function to cakculate sum of n numbers;
def sum_n(numbers):
    if(numbers==0):
        return 0

    return sum_n(numbers-1)+numbers
print(sum_n(6))