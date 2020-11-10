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

