# This is python program to find out the Prime number

num = int(input("Enter your choice : "))
flag = True

for n in range(2,num):
  if (num % n == 0):
    flag =False
    break

if flag:
  print("Yahoo your choice %d is prime number"%num)
else:
  print("Sorry %d is not prime number"%num)

