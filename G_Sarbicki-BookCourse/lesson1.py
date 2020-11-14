# INTEGERS
a = 2005
print(type(a))
print(f"decimal: {a}\nbinary: {bin(a)}\nhexadecimal: {hex(a)}")

# FLOATING POINT NUMBERS
b = 3.14
c = 4
print(type(b))
d = b/c
e = a/c
print(f"{d}\n{e} {type(e)}")
# division of two integers is going to result with an float number
# python is not going to round up/down the number
f = a//c
# to get a get an integer result from a division we can use the '//' operator,
# which is called integer division
print(f)
# defining variables can also be done in scientific notation which is XeY
# where X stands for a value >0 and <10 and eY stands for 10 to the power of Y
# if we insert negative Y, we are going to get the negative power of the given value

# COMPLEX NUMBERS
a = 2+3j
b = 8+7j
c = a+b
d = a*b
print(a)
print(type(a))
print(c, d)

# STRING
a = "hello world"
print(type(a))

# STRING ESCAPE CHARACTERS (\' , \" , \n , \t...)
b = 'He\tsaid\tto\tme:\n\"I wasn\'t at school today\"'
# if we need to include both single and double quotes, we can place a back slash sign in front of it
# as written above
# there are also
print(b)

# RAW STRINGS
a = "one\ntwo"
print(a)
b = r"one\ntwo"
print(b)

# TRIPLE QUOTE STRINGS
# they are an alternative for using escape characters, because we can include anything inside triple quotes
print("""This is an example: "woah, I can use double quotes as well as single: ' with no effort
I can also                  put holes in my text and the form is going to be kept as it is.
But I need to keep in ming that some characters still need to be written using escape characters like backslash: \\

this is awesome !!!""")
# it's a good practise to use triple quotes to describe in a short way what does a function do


def foo(value):
    """Takes a value and prints it on the screen"""
    print(f"{value}")
    return

# BOOLEANS
