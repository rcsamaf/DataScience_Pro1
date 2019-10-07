for num in range (1,101): #num is the number between 1 to 100
    if num%15==0:#all numbers divisible by 15 will return the below:
        print ('FizzBuzz')
    elif num%5==0:#all numbers divisible by 5 will return the below:
        print ('Buzz')
    elif num%3==0:#all numbers divisible by 3 will return the below:
        print ('Fizz')
    else:#the rest of the numbers will return the number:
        print (num)


