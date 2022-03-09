target1=3
target2=5
multipliesoftarget1=[]
multipliesoftarget2=[]
for i in range(0,334):
    new_member=3*i
    multipliesoftarget1.append(new_member)

for i in range(0,201):
    new_member=5*i
    multipliesoftarget2.append(new_member)

multipliesoftarget1=set(multipliesoftarget1)
multipliesoftarget2=set(multipliesoftarget2)
    
total_multiplies=multipliesoftarget1.union(multipliesoftarget2)

total_multiplies=list(total_multiplies)

sumoflist=sum(total_multiplies)
print(sumoflist)

#True solution
#sum=0
#for i in range(1000):
#    if(i%3==0 or i%5==0):
#        sum+=i
#print('The sum is '+str(sum))
    
    


