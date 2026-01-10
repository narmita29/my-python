#ask input a sentence from user and count vowels,constant,digits,space and store them in dictinary:
sentence=input('enter youe sentence here please:')
vowel=0
constant=0
digits=0
space=0
for ch in sentence:
    if ch.lower() in 'aieou':
        vowel+=1
    elif ch.isdigits():
        digits+=1
    elif ch.isspace():
        space+=1
    elif ch.isconstant():
        constant+=1
result={
        'vowel' : vowel,
        'digits': digits,
        'space' : space,
        'constant': constant        }
print(result)