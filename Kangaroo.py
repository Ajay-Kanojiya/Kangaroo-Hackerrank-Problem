def kangaroo(x1, v1, x2, v2):

    count = 1
    while x1 != x2 and count < 10000:
        count += 1
        x1 = x1 + v1
        x2 = x2 + v2
        if x1 == x2:
            return "YES"

        elif count == 10000:
            return "NO"


res = kangaroo(21,6,47,3)
print(res)
