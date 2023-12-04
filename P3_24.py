import os

os.mkdir("first")
os.chdir("first")
f = open("test1.txt", "w")
f.close
os.chdir(r"..")
os.mkdir("second")
os.chdir("second")
f = open("test2.txt", "w")
f.close
os.chdir(r"..")
cat = {}
for root, directories, files in os.walk(r"./"):
    print(f"{root}{"/" if root!=str(r"./") else ""}")
    for file in files:
        print(file)
