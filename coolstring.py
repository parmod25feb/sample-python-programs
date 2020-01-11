# This is a python program to print a string "cool" equal "co2l" means if the count is > 1 then only it should print the numeric count

st = input("Please enter the string : ")
dic = {}

for ch in st:
  if ch in dic.keys():
    dic[ch]=dic[ch]+1
  else:
    dic[ch]=1

print("Here is the new string : ")
for key in dic.keys():
  if dic[key] > 1:
    print("%c%d"%(key,dic[key]),end="")
  else:
    print(key,end="")

print("\n\n")


#Output: if entered cool then it would be co2l,if entered abbcccdde then it will be ab2c3d2e

