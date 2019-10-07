pal_max = 0#initiating the largest palindrome number
for num1 in range (100, 1000):
  for num2 in range (100, 1000):
    num = num1 * num2#we will get all the possible numbers obtained by the multiplication of two numbers with three digits
    if str(num)==str(num)[::-1] and num > pal_max:#checking if is is palindrome and if it is not the maximum
      pal_max = num
print (pal_max)#printing the maximum number


