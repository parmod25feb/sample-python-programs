# In this script will see how to read data from a text file

FILE = open("/usr/local/google/home/parmodku/Downloads/pythonprograms/datafile.txt","r")

content = FILE.read()

print("File content is : \n\n",content)
