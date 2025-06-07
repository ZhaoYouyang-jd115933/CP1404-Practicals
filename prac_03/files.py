# 1.Write code that asks the user for their name, then opens a file called name.txt and writes that name to it.
# Use open and close for this question.
FILENAME = "name.txt"
name = input("Enter name: ")
out_file = open(FILENAME, "a")
print(name, file=out_file)
out_file.close()
