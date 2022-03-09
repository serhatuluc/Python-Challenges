#This a solution i have come up with but i takes a lot of times. At the end of page
#i give what i found by searching on the internet. It uses an ancient alghoritm but
#works perfectly
def summation_of_primes():
    i=3
    primes=2
    while i<200000:
        for k in range(3, i // 2, 2):
            if i % k == 0:
                break
        else:
            primes+=i
        i+=2
    print(primes)
if __name__ == '__main__':
    summation_of_primes()

# def sumPrimes(n):
#     sum, sieve = 0, [True] * n
#     for p in range(2, n):
#         if sieve[p]:
#             sum += p
#             for i in range(p*p, n, p):
#                 sieve[i] = False
#     return sum
#
# print sumPrimes(2000000)