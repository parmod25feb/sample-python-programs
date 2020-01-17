# This program is to reverse a list in 3 chunks
# E.g. we have a list like [1,2,3,4,5,6,7,8,9]
# now we want [3,2,1,6,5,4,9,8,7]

# Here is the list items
lst = [1,2,3,4,5,6,7,8,9]
print("Here is your original list : ",lst)
length = int(len(lst)/3)                    # Calculating chunk size

# Declaring some variables and empty list
start = end = 0
lstrev = lstrev1 = lstrev2 = []
finallist= []

for i in range(3):           # Running the loop up 3 times
  if i == 0:                 # When loop will run firsttime
    start=0
    end=length-1
    for i in range(end,start-1,-1):
      lstrev.append(lst[i])
    finallist.extend(lstrev)
  if i == 1:                  # When loop will run 2nd time
    start = end
    end = end + length
    lstrev1 = lst[end:start:-1]
    finallist.extend(lstrev1)
  if i == 2:                  # When loop will run 3rd time
    start =end
    end = end + length
    lstrev2 = lst[end:start:-1]
    finallist.extend(lstrev2)

print("Here is the expected list : ",finallist)


"""
OUTPUT : Here is your original list :  [1, 2, 3, 4, 5, 6, 7, 8, 9]
         Here is the expected list :  [3, 2, 1, 6, 5, 4, 9, 8, 7]

"""
