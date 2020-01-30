# In this program will see the functionality of PYthon Zip function

employee = ("Parmod","Anu","Deepa","Ram")
empid = (101,120,103,104)
salary = (10000,20000,15000,17000)

zipobj = zip(employee,empid,salary)

print(set(zipobj))
