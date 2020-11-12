# CONDITIONAL STATEMENTS (IF) AND LOGICAL OPERATORS
"""
a = input("insert a: ")
b = input("insert b: ")
if a == b:
    print("a = b")
elif a > b:
    print("a > b")
else:
    print("a < b")
"""
# we can also use three-argument if statement, where the value is equal to A if the condition is satisfied and
# B if condition is not satisfied
# x = A if condition else B
# x = True if a == b else False
# print(x)

# DICTIONARIES
d = {'a': 1, 'b': 0}
print(d['a'])
# print(d['x']) this is going to return an error, because there is no such key in our dictionary
# if we need to enable an exception, that there is going to be a possibility, we will search for a key that is not
# in our dictionary, we can use the get() method, which is going to return None or some default set value, without
# crashing the programme
print(d.get('x'))
# setting a default value if key is not found:
print(d.get('x', 0))
# we can add new variables into our pre-existing dictionary or redefine keys by doing as follows:
d['c'] = 3
d['d'] = 4
print(d['c'], d['d'])
# if we have two dictionaries and we want to include one of them in the other, we need to use the update() method:
d1 = {'e': 1, 'f': 0, 'g': 4, 'h': 7}
d.update(d1)
print(d)
# we can delete variables from our dictionary by using the del instruction
del d['b']
print(d)
# we can also delete variables from our dictionary by using the pop() method, which is also going to return the value
# the element we are removing
print(d.pop('a'))
print(d)
# also we can individually look through keys and values in a given dict by using the keys() and values() methods
print(d.keys())
print(d.values())
print(list(d.keys()))

# FUNCTIONS
# important thing about functions is to always set the arguments with default value AFTER the arguments with the ones
# with unknown for ex. this is wrong: def fun(a=None, b) ...

# if we want our function to return a value in a chosen type we need to use the "-> 'type'" instruction, its called
# casting, and we can do the same with the arguments using "'argument': 'type'"
# we


def foo(x: int, y: int) -> int:
    return x + y


z = foo(1, 2)
print(z, type(z))

# here is an example of a function, where the default value of the second argument is set to the value of the first one\


def fun(a, b=None):
    if b is None:
        b = a
    return a*b


print(fun(4))

# there is also a thing called variable argument function, where a function takes as many arguments as there is in a
# given object, suppose we have a list of elements
#               l = [a, b, c]
# and want those elements to be arguments of a function without inserting them individually
#               def function(l):
#                   ...
# counterintuitively, this above is not going to work in a same way as this:
#               def function(a, b, c):
#                   ...
# because there is only one argument. To make this work we need to use a unpack operator:


def suma(*ls):
    return sum(ls)


print(suma(1, 2, 3))
print(suma(1, 3))
print(suma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# we can insert as many arguments as we want and the function is going to work just fine
# it's useful to use this operator when we want to have one function to perform multiple tasks
# depending on the number of arguments


def pole(*sides):
    """this function returns the area of a figure based on given arguments 1:square, 2:rectangle, 3:trapezoid"""
    if len(sides) == 1:
        return sides[0]**2
    if len(sides) == 2:
        return sides[0]*sides[1]
    if len(sides) == 3:
        return sides[0]*(sides[1]+sides[2])/2


print(pole(2))
print(pole(2, 4))
print(pole(12, 9, 4))

# there is a similar operation with dictionaries:
#            def f(*args, **kwargs):
#                 ...


def f(*args, **kwargs):
    print(args)
    print(kwargs)


f(1, 2, 3, a=1, b=2)
# returns:
# (1, 2, 3)
# {'a': 1, 'b': 2}

# FUNCTION DOC:
# if we want a function to have a description that can be visible for people who might review or use your code
# we can put a comment in the first line after defining a function as follows:


def hello():
    """this function takes no arguments and prints "hello world" """
    print("hello world")


# we can access this description by getting the "__doc__" parameter from the function
print(hello.__doc__)
# we can do the same with built in functions, like:
print(abs.__doc__)
print(len.__doc__)
print(print.__doc__)
# and build in methods
arr = [1, 2, 3]
print(arr.append.__doc__)
a = "abc"
print(a.split.__doc__)

# GL0BAL VARIABLES IN FUNCTIONS
# we can modify the values of variables outside the function by specifying the global variable before changing
# it's value inside the function


def f1(y):
    global x
    y += 1
    x = y
    return y


# output:
# x = 1
# f2(x) = 2 (changed)
# x = 2
# otherwise it's just going to create a local variable, and the value of global variable is not going to change


def f2(y):
    y += 1
    return y


# output:
# x = 1
# f2(x) = 2
# x = 1

x = 1
print(x)
print(f1(x))
print(x)

# example
napis = "abcdef"


def reverse1(n):
    """this function permanently reverses a global sting using a loop and a variable "juggle" """
    global napis
    hel = list(n)
    for i in range(len(n)//2):
        temp = hel[i]
        hel[i] = n[-1-i]
        hel[-1 - i] = temp
    n = ''.join(hel)
    napis = n


def reverse2(n):
    """this function permanently reverses a global sting using string slicing """
    global napis
    n = n[::-1]
    napis = n


print(napis)
reverse2(napis)
print(napis)

# PYTHON LAMBDA (ANONYMOUS FUNCTIONS)
# if we have simple, one-line functions, we can use the python lambda construction

# def kwadrat(x):         ->            kwadrat = lambda x: x**2
#     return x**2


silnia = lambda x: x*silnia(x-1) if x-1 >= 1 else x
print(silnia(5))
print(1*2*3*4*5)

# lambda functions are especially useful when we need to use a particular function only once
# BUILT IN FUNCTION "map"
l2 = [2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(lambda x: x**2, l2)))
print(list(filter(lambda y: y % 2 == 0, l2)))

print(list(map(lambda w: w*2 if w % 2 == 0 else w, list(filter(lambda z: z % 3 == 0, l2)))))



