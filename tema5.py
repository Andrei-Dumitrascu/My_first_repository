# sa facem o fct care ia un nr infinit de keyword arguments (**kwargs)
# sa documentam ce face fct si parametrii(= docstringul)
# fiecare param il adaugam intr-o lista, facem un return la acea lista
# evidentiam ca fct returneaza type - list (hint: type hint)
# facem un assert inainte de return sa ne asiguram ca len(list) > 0
# sau assert la apelarea fct, o variabila si assert la acea variabila
# cand avem acces la git
# sa explicam ce inseamna smoke, sanity si regration cu cuvintele noastre

# from typing import List

#
# def infinit_keyword_arguments(**kwargs):
#     print(type(kwargs))
#     new_list = []
#     for keyword in kwargs:
#         print(keyword)
#         new_list.append(keyword)
#     assert len(new_list) > 0
#     print(type(new_list))
#     return new_list
#
#
# print(infinit_keyword_arguments(colour='red', eyes='brown', legs=2))

# def sum_of_two_numbers(a, b):
#     suma = a+b
#     return suma
#
#
# print(sum_of_two_numbers(20, 30))

# def check_even_odd_number(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
#
#
# print(check_even_odd_number(32))

# def nr_of_name_characters(name):
#     length = len(name)
#     return length
#
#
# print(nr_of_name_characters('Dumitrascu Andrei-Gabriel'))

# def rectangle_area(length, width):
#     area = length * width
#     return area
#
#
# print(rectangle_area(10, 5))
# import math
#
#
# def circle_area(radius):
#     area = math.pi*radius**2
#     return area
#
#
# print(circle_area(radius=2))

# def find_character_in_string(my_string, character):
#     if character in my_string:
#         return True
#     else:
#         return False
#
#
# print(find_character_in_string(my_string='Andrei', character='A'))

# def number_of_lower_and_upper_case_characters(my_string):
#     lower_count = 0
#     upper_count = 0
#     for i in my_string:
#         if i.islower():
#             lower_count += 1
#         elif i.isupper():
#             upper_count += 1
#     print(f'Number of lower_case characters is: {lower_count}')
#     print(f'Number of upper_case characters is: {upper_count}')
#
#
# number_of_lower_and_upper_case_characters(my_string='Dumitrascu Andrei Gabriel')

# def list_of_positive_numbers(numbers_list: list):
#     new_list = []
#     print(type(numbers_list))
#     for i in numbers_list:
#         if i > 0:
#             new_list.append(i)
#     return new_list
#
#
# print(list_of_positive_numbers(numbers_list=[1, 2, -3, -4, 0, 9]))


# def compare_two_numbers(x, y):
#     if x > y:
#         print(f'Primul nr {x} este mai mare decat al doilea numar {y}')
#     elif x < y:
#         print(f'Al doilea numar {y} este mai mare ca primul nr {x}')
#     else:
#         print('Numerele sunt egale')
#
#
# compare_two_numbers(x=8, y=5)

# def check_if_number_is_in_set(new_number, my_set: set):
#     if new_number in my_set:
#         print(f'Nu am adaugat nr {new_number} in set. Acesta exista deja.')
#         return False
#     else:
#         my_set.add(new_number)
#         print(f'Am adaugat nr nou in set')
#         return True
#
#
# print(check_if_number_is_in_set(new_number=2, my_set={-2, 3, 5, 7}))

# from calendar import monthrange
#
#
# def days_number_of_the_month(year, month):
#     number_of_days = monthrange(year, month)[1]
#     return number_of_days
#
#
# print(days_number_of_the_month(year=2020, month=2))

# def calculator(x, y):
#     addition = x + y
#     subtraction = x - y
#     multiplication = x * y
#     division = x / y
#     return addition, subtraction, multiplication, division
#
#
# a, b, c, d = calculator(x=2, y=3)
# print(f'Suma este: {a}')
# print(f'Diferenta este: {b}')
# print(f'Inmultirea este: {c}')
# print(f'Impartirea este: {d}')

# def list_of_numbers_return_dict(my_list: list):
#     my_dict = dict()
#     for x in range(0, 10):
#         my_dict[x] = my_list.count(x)
#     return my_dict
#
#
# number_list = [0, 2, 3, 4, 3, 6, 7, 9, 8, 3, 4, 5, 2, 6]
# print(list_of_numbers_return_dict(my_list=number_list))
# def maximum(no1, no2, no3):
#     maxim = 0
#     my_list = [no1, no2, no3]
#     for number in my_list:
#         if number > maxim:
#             maxim = number
#     return maxim
#     # maxim = max(no1, no2, no3)
#     # return maxim
#
#
# print(maximum(no1=10, no2=8, no3=30))

# def sum_of_numbers_from_0_to_number(number):
#     suma = 0
#     for i in range(0, number+1):
#         suma += i
#     return suma
#
#
# print(sum_of_numbers_from_0_to_number(number=4))

# def comun_numbers_of_2_lists(list1: list, list2: list):
#     new_set = set()
#     for number in list1:
#         if number in list2:
#             new_set.add(number)
#     return new_set
#
#
# my_list1 = [1, 1, 2, 3, 3]
# my_list2 = [2, 2, 3, 4]
# print(comun_numbers_of_2_lists(list1=my_list1, list2=my_list2))

# def discount_price(price: float, discount: float):
#     # product_price = price
#     # discount_percentage = discount
#     if discount <= 100:
#         price_after_discount = price - (discount/100)*price
#         print(f'Pretul dupa discount este: {price_after_discount}')
#     else:
#         print('Reducerea este invalida')
#
#
# discount_price(price=100, discount=45.5)


# from datetime import datetime
#
#
# def show_date_time_ro():
#     now = datetime.now()
#     return now
#
#
# print(show_date_time_ro())


# from datetime import datetime
# import pytz
#
#
# def show_china_date_time():
#     country_time_zone = pytz.timezone('Asia/Shanghai')
#     country_time = datetime.now(country_time_zone)
#     print(country_time.strftime("Date is %d-%m-%y and time is %H:%M:%S"))
#
#
# show_china_date_time()

# import datetime
# from datetime import date
#
#
# def get_days_until_birthday(year, month, day):
#     today = date.today()
#     birthday = datetime.date(year, month, day)
#     days_to_go = birthday - today
#     return days_to_go.days
#
#
# print(get_days_until_birthday(year=2022, month=8, day=30))
# Smoke Testing is a software testing process that determines whether the deployed software build is stable or not.
# Smoke testing is a confirmation for QA team to proceed with further software testing.
# It consists of a minimal set of tests run on each build to test software functionalities.
# Smoke tests means verifying the important features are working
# and there are no showstoppers in the build that is under testing.
# It is a mini and rapid regression test of major functionality.
# It is a simple test that shows the product is ready for testing.
# This helps determine if the build is flawed as to make any further testing a waste of time and resources.

# Sanity testing is a subset of regression testing.After receiving the software build,
# sanity testing is performed to ensure that the code changes introduced are working as expected .
# This testing is a checkpoint to determine if testing for the build can proceed or not.

# Regression Testing is defined as a type of software testing to confirm that a recent program or code change
# has not adversely affected existing features.
# Regression Testing is nothing but a full or partial selection of already executed test cases
# which are re-executed to ensure existing functionalities work fine.
# This testing is done to make sure that new code changes should not have side effects on the existing functionalities.
# It ensures that the old code still works once the latest code changes are done.

def my_function():
    '''Demonstrates triple double quotes
    docstrings and does nothing really.'''

    return None


print("Using __doc__:")
print(my_function.__doc__)

print("Using help:")
help(my_function)

# Python documentation strings (or docstrings) provide a convenient way of associating documentation with
# Python modules, functions, classes, and methods.

# It’s specified in source code that is used, like a comment, to document a specific segment of code.
# Unlike conventional source code comments, the docstring should describe what the function does, not how.

# What should a docstring look like?

# The doc string line should begin with a capital letter and end with a period.
# The first line should be a short description.
# If there are more lines in the documentation string, the second line should be blank,
# visually separating the summary from the rest of the description.
# The following lines should be one or more paragraphs describing
# the object’s calling conventions, its side effects, etc.
# Declaring Docstrings: The docstrings are declared using ”’triple single quotes”’ or “””triple double quotes”””
# just below the class, method or function declaration. All functions should have a docstring.

# Accessing Docstrings:
# The docstrings can be accessed using the __doc__ method of the object or using the help function.
