# Read and print the contents of a file
def read_file(filename):
    with open(filename, 'r', encoding="utf-8") as file:
        content = file.read()
    return content
#file_content = read_file('sample.txt')
#print(file_content)

# Write content to a file
def write_file(filename, content):
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(content)
#write_file('output.txt', 'Hello, world!')



# Count lines in a file
def count_lines(filename):
    with open(filename, 'r', encoding="utf-8") as file:
        line_count = sum(1 for line in file)
    return line_count
#line_count = count_lines('sample.txt')
#print("Number of lines:", line_count)

# Search for a keyword in a file
def search_text(filename, keyword):
    with open(filename, 'r', encoding="utf-8") as file:
        matching_lines = [line.strip() for line in file if keyword in line]
    return matching_lines
#matching_lines = search_text('sample.txt', 'python')
#print("Matching lines:", matching_lines)


