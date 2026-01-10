#waf to print elements of a list in a single line:
fruits=['apple','mango','banana','grapes','dragon fruit','lichi','kiwi','watermelon']
vegetables=['patato','lady finger','tomato','onion','carrot','bottle guad','cucumber','beans','ginger','garlic']

def print_fuc(iteams):
    for elements in iteams:
        print(elements, end=' ')


print_fuc(fruits)
print_fuc(vegetables)