def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return number * 3 + 1


inp = int(input("input a number for the collatz sequence to begin"))
if inp == 1:
    inp = input("input a different number")
else:
    while inp != 1:
        res = collatz(inp)
        inp = res
        print(res)
        if res == 1:
            break
