#TASK_1
def favorite_movie(name, actor, role):
    print("my favorite movie is " + name + ' with a ' + actor + ' in a role' + role)

favorite_movie('Full metal jacket', 'Ronald Lee Ermey', ' sergeant Hartmmann')

#Task_2

def country(name, capital, population):
    print('Name of a country is: ' + name + ', the capital is: ' + capital + ', actualy population is: ' + population + ' people ')

country('Ukraine', 'Kyiv', '35000000')

#TASK_3 variant1
def operation1(*args):
    return_value = 0
    for num in args:
        return_value += num
    return return_value

def operation2(*args):
    return_value = 1
    for num in args:
        return_value *= num
    return return_value

def operation3(*args):
    return_value = 0
    for num in args:
        return_value -= num
    return return_value

print(operation1(7,7,2))
print(operation2(7,6))
print(operation3(5, 5, -10, -20))

#variant2
def make_operation1(x,y,a):
    return_value = x+y+a
    return return_value
def make_operation2(x,y):
    return_value = x*y
    return return_value
def make_operation3(x,y,a,b):
    return_value = x-y-a-b
    return return_value
print(make_operation1(7,7,2))
print(make_operation2(7,6))
print(make_operation3(5, 5, -10, -20))

# variant3 of a calculator with a functions
def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    return x / y
print(add(1,5))
print(sub(10, 6))
print(mul(10, 10))
print(div(6, 2))






#the call make_operation(‘+’, 7, 7, 2) should return 16
#the call make_operation(‘-’, 5, 5, -10, -20) should return 30
#the call make_operation(‘*’, 7, 6) should return 42