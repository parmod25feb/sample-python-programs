# Program to reverse the string in various ways

st = input("Pls enter your string : ")
print("Original string is : %s"%st)

# String reverse using string slice method
def streverse(st):
  count = len(st)
  return st[count::-1]

st_reverse1 = streverse(st)
print("String reverse using slice method is : %s"%st_reverse1)


# String reverse using Range function
print("String reverse using range function is : ",end='')
count = len(st)
lst = []
for ch in range(count-1,-1,-1):
  print(st[ch],end='')


# String reverse using another string

st_rev=""
for ch in st:
  st_rev= ch+st_rev

print("\nString reverse using another empty string is  : %s"%st_rev)



"""OUTPUT : Original string is : Hello
String reverse using slice method is : olleH
String reverse using range function is : olleH
String reverse using another empty string is  : olleH
"""
