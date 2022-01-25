import copy

def sherlockAndAnagrams(s):
    count = 0
    d: dict = {i: [] for i in list(range(len(s)))}
    for i in list(range(len(s))):
        for j in list(range(len(s))):
            ans = s[i:j]
            d[len(ans)].append(ans)
    d.pop(0)
    for items in d.values():
        for enum, i in enumerate(items):
            if i[::-1] in items[enum:]:
                count += 1
    return count



if __name__ == '__main__':
    print(sherlockAndAnagrams("ansans"))
