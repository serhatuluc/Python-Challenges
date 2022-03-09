def divisor(n):
    for i in range(1, 21):
        if n % i != 0:
            return False
    return True


def smallest_multiple():
    n = 20
    while True:
        if divisor(n):
            break
        n += 20


    print(n)

if __name__ == '__main__':
    smallest_multiple()
