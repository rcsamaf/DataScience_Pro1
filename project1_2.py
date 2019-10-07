sum_num = 0#initiating our sum
for num in range (2, 2000):#will give us the numbers from 2 to 1999
   count = 2#the first prime number is 2
  true_prim = True#assuming that all the number are primes
  while count < num and true_prim:#loop to check if it is prime
    if num % count == 0:#this will point us all the numbers that are not prime
      true_prim = False
    else:
      count += 1#if the above is not true then we have try the next number
  if true_prim:#the number passed the test and it will be prime
    sum_num += num#adding all the prime numbers
print (sum_num)

