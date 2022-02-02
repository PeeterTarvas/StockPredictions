import copy
import math


def countTriplets(arr, r):
    count = 0
    dct: dict = {}
    for enum, i in enumerate(arr[:-2]):
        for j in list(range(enum + 1, len(arr) - 1)):
            a = [enum, j, j + 1]
            b = [enum, enum + 1, j + 1]

            print(a)
            a_lst = [round(math.log(arr[a[0]], r)), round(math.log(arr[a[1]], r)), round(math.log(arr[a[2]], r))]
            b_lst = [round(math.log(arr[b[0]], r)), round(math.log(arr[b[1]], r)), round(math.log(arr[b[2]], r))]
            dct[str(f"{a}")] = a_lst
            dct[str(f"{b}")] = b_lst
    for i in dct.values():
        if i[0] + 1 == i[1] and i[1] + 1 == i[2]:
            count += 1
    print(dct)
    return count




if __name__ == '__main__':
    print(countTriplets([1, 5, 5, 25 ,125], 5))
