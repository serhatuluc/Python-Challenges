def ten_thousand_first_prime():
    i = 3
    n = 1
    while True:
        for k in range(3, i//2, 2):
            if i % k == 0:
                break
        else:
            n+=1

        if n == 10001:
            return i

        i += 2


if __name__ == '__main__':
    print(ten_thousand_first_prime())
