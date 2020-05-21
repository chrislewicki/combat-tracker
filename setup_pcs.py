import os.path
from os import path

if path.exists("characters.txt"):
    print("PC list already exists, no need to run setup.")
else:
    PC_count = int(input("Enter number of PCs: "))
    PC_list = []
    for i in range(PC_count):
        name = input("Enter PC name: ")
        PC_list.append(name)

    file = open("characters.txt","w")
    file.write(str(PC_list))
    file.close()
