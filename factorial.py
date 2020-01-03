# This program is to calculate the Factorial of a number

# Asking user to enter the number and converting that to int 
num = int(input("Please enter your number : "))

# Function to calculate Factorial
def factorial(num):
  if num ==0 or num==1:
    return 1
  else:
    return num*factorial(num-1)

fact=factorial(num)  # Calling the factorial function by passing the num argument
print("Factorial of %d is %d"%(num,fact)) # Printing the number and factorial value
