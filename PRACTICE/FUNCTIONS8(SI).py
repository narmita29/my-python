#ASK USER FOR INPUT OF PRINCIPAL,RATE,TIME AND CALCULATE PRINCIPAL AMOUNT;
principal=float(input('please enter principle amount:'))
rate=float(input('please enter rate of interest:'))
time=float(input('please enter time in year:'))

def simple_interest(p,r,t):
    
    SI=(principal*rate*time)/100
    
    return SI    

result=simple_interest(principal,rate,time)
print(result)