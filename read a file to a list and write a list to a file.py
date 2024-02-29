
def file_lines_to_list():
    # SAMPLE1.TXT
    # a
    # b
    # c
    # d
    # e

    file = open("sample1.txt", "r")

    file_lines = file.read()
    list_of_lines = file_lines.split("\n")

    # print(list_of_lines) >>> ['a', 'b', 'c', 'd', 'e']

def list_of_lines_to_file():
    lines = ("lina 1 \n lina 2 \n lina 3")
    list_of_lines = lines.split("\n")
    with open("sample2.txt", "w") as file:
    #Write to `file`
        file_lines = "\n".join(list_of_lines)
        file.write(file_lines)

    # OUTPUT
    # SAMPLE2.TXT
    # a
    # b
    # c
    # d
    # e
