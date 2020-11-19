# SEQUENCE TYPES
s = "string"
# string sequence
b = b"bytes"
# byte sequence
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list
tp = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# tuple

print(s[0], b[-1], ls[3], tp[7])
# all of the above types can be indexed, or sliced
print(s[0:3:1])
# where the where the x value in "x:y:z" stands for the beginning of the sequence,
# y stands for the end of the sequence, excluding y itself
# and z is the "step" parameter, which gets every z-ond element in the given sequence
print(ls[0:7:2])
# USEFUL HACK: you can go in the reversed order if you put a negative value in the step parameter

# we can also :
# - use the len() method on each object
print(len(ls))

# - multiply the objects by positive integers (which is going to repeat the sequence n-times)
print(2*ls)

# - concatenate

n_s = "new "+s
print(n_s)

# - check if a value exists in a object
print(5 in ls, 11 in ls)

# - search for min and max value using max() and min() methods
# where in string, max is going to return a value that's the furthest from
# the beginning of the alphabet
print(max(s), min(ls))

# - search for first instance index
ss = "ssasagaa"
print(ss.index('a'))

# - count the instances of a particular element
print(ss.count('a'))

# STR METHODS
# we can turn a string into a list by splitting it
sentence = "this is a random sentence"
words_in_sentence = sentence.split(" ")
fruits = "apples or oranges or bananas or pineapples or berries"
param_values = "fire, fire-claw, water, bananas"
print(words_in_sentence)
print(fruits.split(" or "))
print(param_values.split(", "))

# we can join a list of string sequences with a chosen sequence or sign
ex = ' '.join(["Joey", "has", "an", "apple"])
print(ex)


def convert_int_list_to_string_list(ls1):
    ls2 = []
    for i in range(len(ls1)):
        ls2.append(str(ls1[i]))
    return ls2


print('->'.join(convert_int_list_to_string_list(ls)))

# using startswith()/endswith() we can check if a string begins or ends with a substring/character
print(ex.startswith('Joey'))

# isalpha(), isdigit(), isalnum()
print("abc123".isalpha(), "abc123".isdigit(), "abc123".isalnum())

# strip() can strip a string of whitespaces \

# if we want to replace a containing substring with an other substring, we can do that using replace() method
print("ac/dc".replace("ac", "AC").replace("dc", "DC"))
