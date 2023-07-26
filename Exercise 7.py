# file_a = open("a.txt", "r")
# print(file_a.read())
#
# file_b = open("b.txt", "r")
# print(file_b.read())
#
# file_c = open("c.txt", "r")
# print(file_c.read())

filenames = ['a.txt', 'b.txt', 'c.txt']

for filename in filenames:
    file = open(filename, 'r')
    content = file.read()
    print(content)