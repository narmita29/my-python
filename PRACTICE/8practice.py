#take two sets with fruit name *print common fruit name *and diff fruits:
fruit1={'banana','grapes','strawberry','blueberry','apple','watermelon','dragon fruit','mango'}
fruit2={'mango','pineapple','peach','banana','gauva','kiwi','blueberry','grapes','orange','apple'}

print('common fruits are',fruit1.intersection(fruit2))
print('uniques are',fruit1.difference(fruit2))