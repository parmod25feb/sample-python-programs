# This program is to calculate the Factorial of a number

num = int(input("Please enter your number : "))

def factorial(num):
  if num ==0 or num==1:
    return 1
  else:
    return num*factorial(num-1)

fact=factorial(num)
print("Factorial of %d is %d"%(num,fact))
