
def pythagorean_triplet():
    for a in range(1, 333):
        for b in range(a+1, 500):
            for c in range(b+1, 1000):
                if  c ** 2 == a ** 2 + b ** 2 and a+b+c==1000:
                    return a* b* c
                if c ** 2 > a ** 2 + b ** 2 :
                    break
                if a+b+c>=1000:
                    break
            if a+b>=1000:
                break



if __name__ == '__main__':
    print(pythagorean_triplet())
