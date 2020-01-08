# In this script will see how to read data from a text file

# First will open the text file by providing the path and will open in read mode
FILE = open("/usr/local/google/home/parmodku/Downloads/pythonprograms/datafile.txt","r")

# Read the content of the file
content = FILE.read()

# Print the content of the file
print("File content is : \n\n",content)
