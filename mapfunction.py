# In python we use map() function to apply a given function (custom or inbuilt) on all the elements of specified iterable (list, tuple etc.)

# When we have to run all the elements of iterable like list, tuple to function one by one and store the output in variable for further use, in this case we use map() function.

listone = ["Parmod","Ayansh","Vinay"]
tup = ("Kumar","Sharma","Singh")

def merge(l,t):
  return l +' '+t

result = map(merge,listone,tup)
print(list(result))


#Output : ['Parmod Kumar', 'Ayansh Sharma', 'Vinay Singh']

