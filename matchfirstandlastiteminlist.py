# This program is to check whether first and last item of the list are equal or
# not

# Let's make a list first
lst = []           # Declare an empty list

# Ask user to add some element in the list, let's add 5 items
for i in range(5):
  item = int(input("Please enter your choice for list items : "))
  lst.append(item)

# Here is your list 
print(lst)

def checkfirstandlast(lst):   # Function definition to check First and Last number of the list
  if lst[0]==lst[-1]:
    flg= True
  else:
    flg = False
  return flg

flag = checkfirstandlast(lst)  # Calling the function and getting return value in the flag

# Showing output based on the retrun of the function
if flag:
  print("Congratualtion! First and Last items of list are equal. ")
else:
  print("Sorry! First and Last items are not equal.")


"""
Output: Please enter your choice for list items : 2
Please enter your choice for list items : 3
Please enter your choice for list items : 4
Please enter your choice for list items : 5
Please enter your choice for list items : 2
[2, 3, 4, 5, 2]
Congratualtion! First and Last items of list are equal. 
"""
