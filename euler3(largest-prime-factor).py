def compute():
    num=600851475143
    list_of_dems=[]
    for i in range(1,num):
        dem=num%i
        if dem==0:
            num=num/i
            list_of_dems.append(i)
        if num==1.0:
            break
    print(list_of_dems)
    print(max(list_of_dems))
    return

compute()



    







    