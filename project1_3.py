sum_num = 0#initiating the sum
for num in range (1, 1000):#we will get all the numbers from 1 to 999
  if num%15 == 0:#it will give us the numbers that are both multiples of 3 and 5
    sum_num +=num#if it pass the test, then we add it to the sum
print (sum_num)

