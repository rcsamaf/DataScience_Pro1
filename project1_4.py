string1 = input("enter your string: ")#asking for the string to be evaluated
#string1 = string1.lower() we can add this line to make it case insensitive
string2= ""#defining a string where we will add our characters
l = len(string1)#to reduce the typing
i = 1#position of characters
cont = 1#initiating our counter
while i < l:
  if string1[i] == string1[i - 1]: # check it is the characters match 
    cont += 1#if above is true we count one more
  else:
    string2= string2 + string1[i - 1] + str(cont) # if not, we store the previous data
    cont = 1 #set the counter to 1 again
  i += 1#incrementing the position to evaluate the next one
string2 = string2 + string1[i - 1] + str(cont) #concatenating the strings
if l < len(string2):#we need to check if the length will smaller than the first one
    print(string1)
else:
    print (string2)


