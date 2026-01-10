#make a tuple with cities name and ask user input and search name in tuple:
tuple_cities=('Patiala','Chandigarh','Khanna','Amritsar','Ludhiana','Ambala')
print('first letter must be capital:')
city=input('please enter city name for search:')
if(city in tuple_cities):
    print("found at index",tuple_cities.index(city))
else:
    print('opps not in tuple try again....')