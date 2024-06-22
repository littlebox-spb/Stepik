import os

mask = input("Введите маску - ")

for file in os.listdir("."):
    if file.startswith(mask):
        os.rename(file, file[len(mask) :])
