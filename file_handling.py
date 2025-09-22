# file handling:
# open()
file = open("stedents.txt","w")
for line in file:
    print(line)
print("data is changed")
file.close()
import numpy as np
with open("students.txt","r") as file1:
    for line in file1:
        print(line)
    print("data is changed")


print(file.read)
file.write("hi prasad\n")
file.write("hi prasad\n")
file.write("hi prateek\n")
print("data is changed")
file.close()


print(file.read)

file = open("students.txt","w")
file.write("hi prasad\n")
file.write("hi b\n")

file = open("students.txt","a")
file.write("hi prasad\n")
file.write("hi prateek\n")

print("data is changed")
file.close()
