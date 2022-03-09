def sum_square_difference(n):
    sum_of_the_square=0
    for i in range(1,n+1):
        sum_of_the_square+=i*i

    sum=0
    for i in range(1, n + 1):
        sum += i
    square_of_the_sum=sum*sum


    result=square_of_the_sum-sum_of_the_square
    return result


if __name__ == '__main__':
    print(sum_square_difference(100))



