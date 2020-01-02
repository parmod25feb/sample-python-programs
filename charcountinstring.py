# This program is to count the occurrence of the characters in the string

original = input("Please enter your string : ")

print("Your original strin is : ", original)
dic = {}
for ch in original:
        if ch in dic:
            dic[ch]= dic[ch]+1
        else:
            dic[ch]=1

for key in dic.keys():
    print("Char %c occurres %d times"%(key, dic[key]))
