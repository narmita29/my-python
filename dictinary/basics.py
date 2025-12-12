dic={
     'name':'arya',
     'class':'B.C.A',
     'Roll no.':7640,
     'subjects':['python = 99','java = 88','SAD =90' ],
     'topics' : ('dictinary')
     }

print(dic["subjects"])        #only print subjects
dic['name'] = 'kalpi'         #changes in name
print(dic)
#methods of dictinary:
print(dic.keys())
print(dic.values())
print(dic.items())             #return all pairs
print(dic.get('city.'))      #OR same but it give none other give error
print(dic['name'])        
dic.update({'no':8788})
print(dic)                     #updated dictinary


