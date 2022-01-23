def timeConversion(s):
    if "AM" in s:
        s = s.split(":")
        hours = int(s[0]) % 12
        hours = str(0) + str(hours)
    else:
        s = s.split(":")
        hours = int(s[0]) % 12 + 12
    return str(hours) + ":" + s[1] + ":" + s[2][0:2]

if __name__ == '__main__':
    matrix = [[1, 3, 2], [1, 5, 6], [19, 5, 0]]
    # 1 3 2
    # 1 5 6
    # 19 5 0
    print(timeConversion("06:40:03AM"))