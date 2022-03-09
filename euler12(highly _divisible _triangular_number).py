import time
def highly_divisible_triangular_number():
    i = 0
    sum = 0
    while True:
        sum += i
        count = 0
        for k in range(1,int(sum**0.5)):
            if sum%k==0:
                count+=1
        if count>250:
            print(sum)
            return
        i += 1


if __name__ == '__main__':
    start = time.time()
    highly_divisible_triangular_number()
    end=time.time()
    print(int(end-start))