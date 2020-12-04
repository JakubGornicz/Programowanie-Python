"""Sortowanie rosnące metodą bąbelkową

    o niech l będzie listą wejściową (nieposortowaną)
    o pętla for po wszystkich indeksach l, gdzie zmienną iterującą będzie i:
        o pętla for po wszystkich indeksach l, gdzie zmienną iterującą będzie j:
            o jeżeli l[i] < l[j], to zamień te wartości miejscami w liście"""


def bubble_sort(ls: [], dsc: bool = False) -> []:
    for i in range(len(ls)):
        for j in range(len(ls)):
            if dsc is True:
                if ls[i] > ls[j]:
                    temp = ls[i]
                    ls[i] = ls[j]
                    ls[j] = temp
            else:
                if ls[i] < ls[j]:
                    temp = ls[i]
                    ls[i] = ls[j]
                    ls[j] = temp
    return ls


new_ls = [3, 5, 8, 7, 1, 6, 9, 4, 0, 2]
print(bubble_sort(new_ls))
