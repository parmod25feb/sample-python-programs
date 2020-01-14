# This program is to convert a list of characters into string

lst =  ['I', 'n', 'd', 'i', 'a ', ' i', 's', ' a ', 'g', 'r', 'e', 'a', 't'] 
print("Original list is : ",lst)
def characterstostring(lst):
  new_str = ""
  for ch in lst:
    new_str = new_str + ch
  return new_str


finalstring = characterstostring(lst) 
print("Your string is : %s"%finalstring)


"""OUTPUT :
Original list is :  ['I', 'n', 'd', 'i', 'a ', ' i', 's', ' a ', 'g', 'r', 'e', 'a', 't']
Your string is : India  is a great"""
