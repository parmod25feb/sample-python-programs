# In this program will understand how to concatenate 2 strings in Python

# 1. Here will do concatenation with + operator

st1 = input("Please enter your first name : ")
st2 = input("Please enter your second name : ")
full_name= st1 +' '+ st2

print("Concatenated string is : ",full_name)

"""Output is : Please enter your first name : Google
               Please enter your second name : Alphabet
               Concatenated string is :  Google Alphabet"""

# 2. Concatenation using Join function

st3 = ' '
concatenated_string = ''.join([st1,st3,st2])
print("\nConcatenated string is : ",concatenated_string)


"""Output is : Concatenated string is :  Google Alphabet"""

