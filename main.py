def greeting(name):
    print("Hello " + name.title() + "!")

def greeting_2(name):
    print('Hello {}!'.format(name.title()))
    print(f'Hello again {name.title()}!')

name = "Erin"
print(greeting(name))

name = "Andy"
print(greeting_2(name))

greeting_2('Sue')


# Solutions below discussed during first day of class (see slides in Google Classroom).

def odd_numbers2():
    for i in range(1,101,2):
        print(i)

odd_numbers2()

print("\n")

def odd_numbers3():
    numbers = list(range(0,101))
    for number in numbers:
        if number % 2 != 0:
            print(number)

odd_numbers3()


# Solution below discussed during first day of class.
def is_consecutive2(a_list):
    i = 0
    status = True
    while i < len(a_list) - 1:
       if a_list[i] + 1 == a_list[i + 1]:
           i += 1
       else:
            status = False
            break
    print(status)

is_consecutive2([1,10,2,3,4,5])


# Solutions below discussed during first day of class.
def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0:
        print(f'{a_year} is a leap year')
    elif a_year % 400 == 0:
        print(f'{a_year} is a leap year')
    else:
        a_year = False
        print(f'{a_year}')


# Question 4 1.b solution

"""
    TRUTH TREE
    AND 
    T & T == T
    T & F == F
    F & F == F

    OR
    T || F == T
    F || T == T
    F || F == F
"""

def is_leap(a_year):
    if a_year % 4 == 0 and (a_year % 400 == 0 or a_year % 100 != 0):
        print(True)
    else:
        print(False)

is_leap_year(2019)


# git practice 
def welcome(marvel_character):
    print(f'Welcome to {marvel_character} Vision')

welcome('Wanda')
