def is_prime(n):
    if n < 2:
        return "Error: given value cannot be prime"
    else:
        i = 1
        while i*i <= n:
            i += 1
            if n % i == 0:
                return False
        return True


def ids_of_substring(x, s):
    first = x.index(s)
    ls = []
    for i in range(len(s)):
        ls.append(first+i)
    return ls


def nwd(x: int, y: int) -> int:
    r = x % y
    while r != 0:
        x = y
        y = r
        r = x % y
    return y

if __name__ == "__main__":
    print(is_prime(12))

    a = "abrakadabra"
    b = "kada"
    print(ids_of_substring(a, b))

    print(nwd(282, 78))

    # LIST COMPREHENSION
    ls1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    ls2 = [i*2 if i % 2 != 0 else i for i in ls1 if i % 3 != 0]
    print(ls2)

    l3 = ["abc", "1bc", "a2c", "123"]
    l4 = [''.join([i for i in j if i.isalpha()]) for j in l3]
    print(l4)

    l5 = ["abc", "1bc", "a2c", "123"]
    l6 = [int(''.join([i for i in j if i.isdigit()])) for j in l5 if not j.isalpha()]
    print(l6, type(l6[0]))

    l7 = [(), (1,), (2, 3), (), (4, 5, 6), (1, 2, 3, 4)]
    l8 = [tuple(i[:2]) for i in l7 if len(i) > 1]
    print(l8)

    l9 = [(), (2,), (2, 3), (1,), (4, 8, 6), (1, 7, 9, 4)]
    l10 = [i for i in l9 if sum(i) % 2 == 0]
    print(l10)

    l11 = [(3, 1), (3,), (3, 1), (9,), (3, 8, 6), (3, 6, 9, 27)]
    l12 = [i for i in l11 if all(j % 3 == 0 for j in i)]
    print(l12)

    l13 = [(2, 1, 8), (3,), (3, 2), (9,), (2, 8, 6), (3, 6, 9, 27)]
    l14 = [i for i in l11 if any(j % 3 == 0 for j in i)]
    print(l14)

    l15 = ["ala ma kota", "dąb", "chrząszcz brzmi", "alarm"]
    l16 = [i[:i.index(' ')] for i in l15 if i.count(' ') > 0]
    #
    print(l16)

