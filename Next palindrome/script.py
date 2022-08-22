def smallPal(n):
    while n > 0:
        char = str(n)
        if char == char[::-1]:
            return n

        n += 1


n = int(input())
print(smallPal(n))
