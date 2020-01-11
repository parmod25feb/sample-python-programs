# This is a python program to print a string "cool" equal "co2l" means if the count is > 1 then only it should print the numeric count

st = input("Please enter the string : ") # Ask user to enter the string
dic = {}                                 # Declare and empty dictionary to store data in key value pair

for ch in st:                            # Start iteration through string character by character
  if ch in dic.keys():                   # Check if the key is in Dictionary 
    dic[ch]=dic[ch]+1                    # If yes, then will increase the value by one and will add in dictionary
  else:
    dic[ch]=1                            # Else will store 1 for the key value 

print("Here is the new string : ")
for key in dic.keys():                   # Now will iterate through the dictionary
  if dic[key] > 1:                       # Will check if key value is >1 then only will print numeric value else will print key only
    print("%c%d"%(key,dic[key]),end="")  # end="" will keep printing the value in the same line
  else:
    print(key,end="")

print("\n\n")                            # This is just for newline


#Output: if entered cool then it would be co2l,if entered abbcccdde then it will be ab2c3d2e

