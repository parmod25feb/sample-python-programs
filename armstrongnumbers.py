# This program will check and print all the armstrong numbers <1000

print("Here is the list of all the Armstrong numbers less then < 1000")

#Iterating through the numbers from 0 to 1000
for num in range(0,1000):
  rem =0           #declaring local variables
  rev =0 
  num1 =0
  num1=num
  while num1 != 0:               # logic for Armstrong number
    rem = num1 % 10
    rev = rev + rem**3
    num1 = num1//10

  if num == rev:                 # checking and pritning if the number is armstrong number
    print(" ",rev)



# Output is  : 0, 1, 153, 370, 371, 407
