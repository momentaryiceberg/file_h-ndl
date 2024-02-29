def lesaLinur():
    """gerir lista sem inniheldur hverja línu úr textafæl sem streng"""
    mylines = []
    with open ('islenska.txt', 'r', encoding='utf8') as myfile:
        for myline in myfile:
            mylines.append(myline.rstrip('\n'))
    for element in mylines:
        print(element)

def skrifaLinur2():
    """Glósar hverja LÍNU sem línu í txt fæl"""
    with open("aaa.txt", 'w', encoding='utf8') as f3:
        lines = """tekur 
        bara línur"""
        f3.writelines(lines)

def skrifarStrLinur():
    """Glósar streng og línur"""
    person_data = ['Name: Emma', '\nAddress: 221 Baker Street', '\nCity: London']
    fp = open("write.txt", "w")
    fp.writelines(person_data)
    fp.close()

def WordCount():
	"""Counts number of words"""
	file = open("C:\data.txt", "rt")
	data = file.read()
	words = data.split()
	print('Number of words in text file :', len(words))
def count_words_in_text_file(file_path):
    """This function will read words count in a text file"""
    ret = -1
    try:
        # Open the text file.
        file_object = open(file_path, "r")
        # Get all file content in a string.
        file_content = file_object.read()
        # Split the file content into an array.
        words_array = file_content.split()
        # Get words array length.
        words_array_len = len(words_array)
        ret = words_array_len
        print(file_path + " contains " + str(words_array_len) + " words.")
    except FileNotFoundError:
        print(file_path + " do not exist. ")
    except PermissionError:
        print("You do not have permission to read file " + file_path)
    except IOError:
        print("IOError.")    
    return ret

def readWordbyWord():
	"""read file word by word"""
	with open('GFG.txt','r') as file:
		for line in file:
			for word in line.split():
				print(word)

def readCharByChar():
	"""read file character by character"""
	file = open('file.txt', 'r')
	while 1:
		char = file.read(1)	# read by character
		if not char:
			break
		print(char)
	file.close()

def readCharsbyChars():
	"""Reads more than one charactes at a time."""
	with open('file.txt') as f:
		while True:
			c = f.read(5)
			if not c:
				break
			print(c)

def counter(fname):
	"""counts number of characters, words, spaces and lines in a file"""
	num_words = 0
	num_lines = 0
	num_charc = 0
	num_spaces = 0
	with open(fname, 'r') as f:
		for line in f:
			num_lines += 1
			word = 'Y'
			"""# declaring a variable word and assigning its value as Y
			because every file is supposed to start with a word or a character"""
			for letter in line:
				if (letter != ' ' and word == 'Y'):
					num_words += 1
					word = 'N'
				elif (letter == ' '):
					num_spaces += 1
					word = 'Y'
				for i in letter:
					if(i !=" " and i !="\n"):
						num_charc += 1
	print("Number of words in text file: ", num_words)
	print("Number of lines in text file: ", num_lines)
	print('Number of characters in text file: ', num_charc)
	print('Number of spaces in text file: ', num_spaces)

def counter2(fname):
	import os
	num_words = 0
	num_lines = 0
	num_charc = 0
	num_spaces = 0
	with open(fname, 'r') as f:
		for line in f:
			line = line.strip(os.linesep)
			wordslist = line.split()
			num_lines = num_lines + 1
			num_words = num_words + len(wordslist)
			num_charc = num_charc + sum(1 for c in line
						if c not in (os.linesep, ' '))
			num_spaces = num_spaces + sum(1 for s in line
								if s in (os.linesep, ' '))
	print("Number of words in text file: ", num_words)
	print("Number of lines in text file: ", num_lines)
	print("Number of characters in text file: ", num_charc)
	print("Number of spaces in text file: ", num_spaces)

def findWordChar():
	"""Finding ‘n’ Character Words in a Text File"""
	count = 1
	chrw = ""
	file = open('textfile.txt', 'r')
	while 1:
		sp = file.read(1)
		if count<= 3:
			chrw = chrw + sp
		if count>3:
			if sp ==" ":
				count = 0
				if len(chrw)>0:
					print(chrw)
					chrw =""
			elif sp !=" ":
				chrw =""
		count = count + 1

		if not sp:
			break
	file.close()

def CountLines():
	file = open("gfg.txt","r")
	Counter = 0
	Content = file.read()
	CoList = Content.split("\n")
	for i in CoList:
		if i:
			Counter += 1
	print("This is the number of lines in the file")
	print(Counter)

def removeLinesStartingWith2():
	import re
	file1 = open('GeeksforGeeks.txt','r')
	file2 = open('GeeksforGeeksUpdated.txt','w')
	for line in file1.readlines():
		x = re.findall("^Geeks", line)
		if not x:
			print(line)
			file2.write(line)
	file1.close()
	file2.close()

def eliminateDuplines():
	"""Eliminating repeated lines from a file"""
	outputFile = open('C:/Users/user/Desktop/Lorem_output.txt', "w")
	inputFile = open('C:/Users/user/Desktop/Lorem_input.txt', "r")
	lines_seen_so_far = set()
	for line in inputFile:
		if line not in lines_seen_so_far:
			outputFile.write(line)
			lines_seen_so_far.add(line)
	inputFile.close()
	outputFile.close()

def parse(d):
	"""Read List of Dictionaries from File in Python"""
	dictionary = dict()
	pairs = d.strip('{}').split(', ')
	for i in pairs:
		pair = i.split(': ')
		# Other symbols from the key-value pair should be stripped.
		dictionary[pair[0].strip('\'\'\"\"')] = pair[1].strip('\'\'\"\"')
	return dictionary

def GeekekkiViss():
	try:
		geeky_file = open('geeky_file.txt', 'rt')
		lines = geeky_file.read().split('\n')
		for l in lines:
			if l != '':
				dictionary = parse(l)
				print(dictionary)
		geeky_file.close()
	except:
		print("Something unexpected occurred!")

def appendFromfiletoFile():
	"""Append content of one text file to another"""
	firstfile = input("Enter the name of first file ")
	secondfile = input("Enter the name of second file ")
	f1 = open(firstfile, 'r')
	f2 = open(secondfile, 'r')
	print('content of first file before appending -', f1.read())
	print('content of second file before appending -', f2.read())
	f1.close()
	f2.close()
	f1 = open(firstfile, 'a+')
	f2 = open(secondfile, 'r')
	f1.write(f2.read())
	f1.seek(0)
	f2.seek(0)
	print('content of first file after appending -', f1.read())
	print('content of second file after appending -', f2.read())
	f1.close()
	f2.close()


def write_line_and_lines():
	name = '\nEmma'
	address = ['\nAddress: 221 Baker Street', '\nCity: London', '\nCountry:United Kingdom']
	# append to file
	with open("Write_demo.txt", "a") as f:
		f.write(name)
		f.writelines(address)


def append_and_read():
	# Append and read on the same file
	name = '\nAntony'
	address = ['\nAddress: 221 Baker Street', '\nCity: London', '\nCountry:United Kingdom']
	# append to file
	with open("Write_demo.txt", "a+") as f:
		f.write(name)
		f.writelines(address)
		# move file handle to the start
		f.seek(0)
		print(f.read())

def write_to_binary_file():
	# Writing to a Binary File
	file = open("Writedemo.bin", "wb")
	file.write("This is a sample string stored in binary format")
	file.close()
