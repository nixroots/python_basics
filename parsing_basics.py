# 1. opening file with built-in exceptions
===========================================

try:
    with open('file.log') as file:
        read_data = file.read()
except:
    print('Could not open file.log')
    
#If file.log does not exist, this block of code will output the following: > Could not open file.log

# 2. Iterating Over Each Line in the File
==========================================
A common thing to do while reading a file is to iterate over each line. 
Here’s an example of how to use the Python .readline() method to perform that iteration:

method1: 
with open('dog_breeds.txt', 'r') as reader:
     line = reader.readline()  # Read and print the entire file line by line
     while line != '':  # The EOF char is an empty string
         print(line, end='')
        line = reader.readline()
method2:
with open('dog_breeds.txt', 'r') as reader:
     for line in reader.readlines():    ## or -> for line in reader:
         print(line, end='')
         
# 3. Working With Two Files at the Same Time
=============================================
d_path = 'dog_breeds.txt'
d_r_path = 'dog_breeds_reversed.txt'
with open(d_path, 'r') as reader, open(d_r_path, 'w') as writer:
    dog_breeds = reader.readlines()
    writer.writelines(reversed(dog_breeds))
    
The read method will read in all the data into one text string. This is useful for smaller files 
readline which is one useful way to only read in individual line incremental amounts at a time and return them as strings. 
readlines, will read all the lines of a file and return them as a list of strings.

