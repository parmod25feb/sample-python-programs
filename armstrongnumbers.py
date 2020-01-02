# This program will check and print all the armstrong numbers <1000

print("Here is the list of all the Armstrong numbers less then < 1000")

for num in range(0,1000):
  rem =0
  rev =0 
  num1 =0
  num1=num
  while num1 != 0:
    rem = num1 % 10
    rev = rev + rem**3
    num1 = num1//10

  if num == rev:
    print(" ",rev)
