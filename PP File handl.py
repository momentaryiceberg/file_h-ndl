
"""   Mode	                    Description
r	          Opens a file for reading. (default)
w	          Opens a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
x	          Opens a file for exclusive creation. If the file already exists, the operation fails.
a	          Opens a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
t	          Opens in text mode. (default)
b	          Opens in binary mode.
+	          Opens a file for updating (reading and writing) """

# f = open("test.txt")          # open file in current directory
# f = open("C:/PP/fæll.txt")    # specifying full path
# f = open("test.txt")          # equivalent to 'r' or 'rt'
# f = open("test.txt",'w')      # write in text mode
# f = open("img.bmp",'r+b')     # read and write in binary mode
# f = open("test.txt", mode='r', encoding='utf-8')


# Reading Files;
"""
f = open("test.txt",'r',encoding = 'utf-8')
f.read(4)       # read the first 4 data

f.read(4)       # read the next 4 data
f.read()        # read in the rest till end of file
f.read()        # further reading returns empty sting
f.readline() 
f.readlines()
f.tell()         # get the current file position
f.seek(0)        # bring file cursor to initial position

for line in f:   # read a file line-by-line using a for loop;
    print(line, end = '')
"""

# File Methods;
"""  Method	                       Description
close()	                       Closes an opened file. It has no effect if the file is already closed.
detach()	                   Separates the underlying binary buffer from the TextIOBase and returns it.
fileno()	                   Returns an integer number (file descriptor) of the file.
flush()	                       Flushes the write buffer of the file stream.
isatty()	                   Returns True if the file stream is interactive.
read(n)	                       Reads at most n characters from the file. Reads till end of file if it is negative or None.
readable()	                 Returns True if the file stream can be read from.
readline(n=-1)	             Reads and returns one line from the file. Reads in at most n bytes if specified.
readlines(n=-1)	             Reads and returns a list of lines from the file. Reads in at most n bytes/characters if specified.
seek(offset,from=SEEK_SET)	 Changes the file position to offset bytes, in reference to from (start, current, end).
seekable()	                 Returns True if the file stream supports random access.
tell()	                     Returns an integer that represents the current position of the file's object.
truncate(size=None)	         Resizes the file stream to size bytes. If size is not specified, resizes to current location.
writable()	                 Returns True if the file stream can be written to.
write(s)	                 Writes the string s to the file and returns the number of characters written.
writelines(lines)	         Writes a list of lines to the file.  
"""
