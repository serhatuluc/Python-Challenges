fibonacci=[]
fibonacci.append(1)
fibonacci.append(2)

for i in range(0,100):
        new=fibonacci[i+1]+fibonacci[i]
        if new<=4000000:
            fibonacci.append(new)
        else:
            break
even_numbers=[i for i in fibonacci if i%2==0]

sum=0
for i in even_numbers:
    sum+=i

print(sum)


#sum = 0     # Variable to hold sum
#num1 = 0;   # First number
#num2 = 1;   # Second number
 
# While the second number is less than 4000000
# This ensures the first number is less after moving
#while num2 < 4e6:
    # Method 1 of incrementing numbers
    #temp = num1
    #num1 = num2
    #num2 = num1 + temp
 
    # Method 2:
    # num1, num2 = num2, num1+num2
 
    # If the number is eve, add to sum
    #if(num1%2 == 0):
        #sum += num1
 
# Print results
#print('The sum is: ' + str(sum))   