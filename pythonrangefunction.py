# In this program will see how Python Range function works

# 1. Range function with stop parameter
for num in range(5):
  print(num)        #It will print numbers from 0 to 4, if there is no start parameter then bydefault it will start from 0

print("\n")

# 2. Range function with start and stop parameter
for num in range(10,16):
  print(num)        #It will print the number from 10 to 15

print("\n")

# 3. Range function wiht start, stop and step parameter, where step parameter will
# increment the loop value by it's vale

for num in range(0,11,2):
  print(num)

print("\n")

# 4. Printing in reverse order

for num in range(10,1,-2):
  print(num)
