# Python has functions for creating, reading, updating, and deleting files.


#  WRITE :  w
#  APPEND : a
#  READ : r+

# Open a file
myFile = open('myfile.txt', 'w')

# Get some info
print('Name: ', myFile.name)
print('Is Closed : ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Write to file
myFile.write('I love Python')
myFile.write(' and JavaScript')
myFile.close()

# Append to file
myFile = open('myfile.txt', 'a')
myFile.write(' I also like PHP, and PHP also supports OOPs .')
myFile.close()

# Read from file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)

#   read( to read number of characters )
#  read(10 )  ,or  read(200)
print(text)
