def validUtf8(data):
    n = 0
    for x in data:
        if n > 0:
            if x & 0b11000000 != 0b10000000:
                return False
            else:
                n -= 1
        else:
            flag = False
            if x & 0b11111000 == 0b11110000:
                n = 3
                flag = True
            if x & 0b11110000 == 0b11100000:
                n = 2
                flag = True
            if x & 0b11100000 == 0b11000000:
                n = 1
                flag = True
            if x & 0b10000000 == 0b00000000:
                n = 0
                flag = True
            if x & 0b11000000 == 0b10000000:
                return False
            if not flag:
                return False
    return n == 0

print validUtf8([235, 140, 4])