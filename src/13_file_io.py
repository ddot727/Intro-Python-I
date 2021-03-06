"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE

filename = "foo.txt"

with open(filename, 'r') as filehandle:
    for line in filehandle:
        print(line)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

with open("bar.txt", "w") as bar:
    bar.write('Do you know the muffin man?\n')
    bar.write('Nah I dont\n')
    bar.write('Oh..\n')
