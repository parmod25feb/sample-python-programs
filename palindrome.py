# Program to check if a string is Palindrome or not

st = input("Please enter your string : ")

def palindrome(st):
  rev=""
  for ch in st:
    rev = ch + rev

  if st == rev:
    return True
  else:
    return False

result = palindrome(st)

if result:
  print("It is Palindrom")
else:
  print("No it is not Palindrom")


