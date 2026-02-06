my_str_1= "Hello"
my_str_2= 'world'
str_plus_str= my_str_1 +' '+ my_str_2
print(str_plus_str)

"""name="John Doe"
age= 26
name_and_age= name + age
print(name_and_age) """

name="John Doe"
age= 26
#name_and_age= name +" "+ str(age)
name_and_age = name
name_and_age += str(age)
print(name_and_age)

name_and_age2= f'my name is {name} and my age is {age}'
print(name_and_age2)

num_1 = 10
num_2 = 12
print(f'the sum of {num_1} and {num_2} is {num_1 + num_2}')
