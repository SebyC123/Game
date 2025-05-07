import random

def Q():
    l = 1
    s = 0
    while True:
        i = l
        d = 10**(i - 1)
        u = (10**i) - 1

        if i == 1:
            d = 0

        a = random.randint(d, u)
        b = random.randint(d, u)

        c = a + b
        try:
            p = int(input(f"{a} + {b} = ? "))
            if p == c:
                print("V")
                s += 1
                print(s)
                l += 1
            else:
                print("X")
                s = 0
                print(s)
                l = 1
        except ValueError:
            print("X")
            s = 0
            print(s)
            l = 1

if __name__ == "__main__":
    Q()