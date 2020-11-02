# CONDITIONAL STATEMENTS (IF) AND LOGICAL OPERATORS
a = input("insert a: ")
b = input("insert b: ")
if a == b:
    print("a = b")
elif a > b:
    print("a > b")
else:
    print("a < b")

# we can also use three-argument if statement, where the value is equal to A if the condition is satisfied and
# B if condition is not satisfied
# x = A if condition else B
x = True if a == b else False
print(x)
