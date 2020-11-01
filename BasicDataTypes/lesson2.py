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


