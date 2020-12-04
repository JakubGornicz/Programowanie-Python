""" Sortowanie rosnące metodą selection

    o niech l będzie listą wejściową (nieposortowaną)
    o pętla for po wszystkich indeksach l, gdzie zmienną iterującą będzie i:
        o min_index = i
        o pętla for w zakresie od i + 1 do długości l - 1:
            o jeżeli l[j] < l[min_index] to ustaw min_index = j
        o zamień miejscami wartości w liście na pozycjach j oraz min_index
"""

# descending
def selection_sort(ls: [], dsc: bool = False) -> []:
    for i in range(len(ls)):
        min_index = i
        for j in range(i+1, len(ls)):
            if ls[j] < ls[min_index]:
                min_index = j
            temp = ls[j]
            ls[j] = ls[min_index]
            ls[min_index] = temp
    return ls


new_ls = [3, 5, 8, 7, 1, 6, 9, 4, 0, 2]
print(selection_sort(new_ls))
