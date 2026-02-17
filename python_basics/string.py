my_str_1= "Hello"
my_str_2= "World!"

my_str_3= """multiline string
yeah
it's multiline"""

my_str_4= '''another
multiline 
string'''

msg= "it's crazy"
quote= 'she said, "you are crazy!"'

msg_1= 'It\'s a crazy day'
quote_1= "She said, \"hello!!!\""
#print(quote_1)

check_str= "Hello"
print('Hello'in check_str)
print('hello'in check_str)
print('hey'in check_str)
print('e'in check_str)

print(len(my_str_1)) #length func
print(my_str_1[1])
print(my_str_1[0])
print(my_str_1[-1])


#Strings are immutable data types in Python. This means that you can reassign a different string to a variable:
greeting='hi'
greeting='hello'
print(greeting)