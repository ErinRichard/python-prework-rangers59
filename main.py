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