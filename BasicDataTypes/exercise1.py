# y = ax^2 + bx + c

a = float(input("Podaj parametr a: "))
b = float(input("Podaj parametr b: "))
c = float(input("Podaj parametr c: "))
print(f"y = {a}x^2+({b})+({c})")
delta = b**2 - 4*a*c

if delta > 0:
    x1 = (-1*b + delta**.5)/2
    x2 = (-1*b - delta**.5)/2
    print(f"delta>0: x1 = {x1:.2}, x2 = {x2:.2}")
elif delta == 0:
    x = -1*b/2*a
    print(f"delta=0: x = {x:.2}")
else:
    print("brak pierwiastków wśród liczb rzeczywistych")
