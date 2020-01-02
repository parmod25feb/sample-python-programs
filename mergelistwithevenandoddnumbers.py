# This program is to merge two lists with even number from 1st list and odd number from 2nd list and create 3rd list

listone = [10,20,30,1,3,30,5]
listtwo = [11,2,21,4,31,51]

finallist =[]

for odd in listone:
    if (odd % 2 != 0):
        finallist.append(odd)

for even in listtwo:
    if (even %2 == 0):
        finallist.append(even)

print("\n\n Final list is : ",finallist)
print("\n\n")
print(set(finallist))
