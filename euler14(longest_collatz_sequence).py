import time


def longest_collatz_sequence():
    b = 0
    answer = 0
    for j in range(1, 1000000, 2):
        count = 0
        i = j
        while i != 1:
            if i % 2 != 0:
                i = 3 * i + 1
                # print(i)
                count += 1
            if i % 2 == 0:
                i = i // 2
                # print(i)
                count += 1
        if count > b:
            b = count
            answer = j
    print(answer)


if __name__ == "__main__":
    start = time.time()
    longest_collatz_sequence()
    end = time.time()
    print(int(end - start))
