results=[]
for i in range(100,999):
    for j in range(100,999):
        result=i*j
        result=(str(result))
        if result[0]==result[-1] and result[1]==result[-2] and result[2]==result[-3]:
                       results.append(int(result))
print(max(results))