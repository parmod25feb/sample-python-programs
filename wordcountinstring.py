# Lint as: python3
"""This program will show words and their occurrences when >2"""


original = "Hello there, hello buddy Hello Python python is cool"
print("Your stirng is : ", original.lower())
dic = {}
original = original.lower()   # Converting string to lowercase
lst = original.split(' ')     # Splitting the string with spaces and adding into the list

for item in lst:              # Iterating through the list and checking the words
  if item in dic.keys():
    dic[item]=dic[item] + 1
  else: 
    dic[item] = 1


for value in dic.keys():     
  if dic[value] > 1:
    print("Word - ",value, " is occurring : ", dic[value]," -times")

