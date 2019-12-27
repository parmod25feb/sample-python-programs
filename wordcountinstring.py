# Lint as: python3
"""This program will show how to count words in the string"""


original = "Hello there, hello buddy Hello Python python is cool"
print("Your stirng is : ", original.lower())
dic = {}
original = original.lower()
lst = original.split(' ')

for item in lst:
  if item in dic.keys():
    dic[item]=dic[item] + 1
  else: 
    dic[item] = 1


for value in dic.keys():
  if dic[value] > 1:
    print("Word - ",value, " is occurring : ", dic[value]," -times")

