import copy
import math


def countTriplets(arr, r):
    count = 0
    dct: dict = {i: [] for i in list(range(len(arr[:-2])))}
    for enum, i in enumerate(arr[:-2]):
        for j in list(range(enum + 1, len(arr))):
            a = [i] + arr[j: j + 2]
            if len(a) == 3:
                dct[enum].append(a)
    for i in dct.values():
        for j in i:
            lst = []
            for m in j:
                lst.append(round(m / r))
            print(lst)
    print(dct)




if __name__ == '__main__':
    print(countTriplets([1, 5, 5, 25 ,125], 5))
