import os

mask = input("Введите маску - ")
#mask = mask if mask else "[InfoVolna.com] "
#mask = mask if mask else "[Boominfo.ORG] "
#mask = mask if mask else "[SuperSliv.biz] "
#mask = mask if mask else "[pirat-zerkalo.com] "
#mask = mask if mask else "[sharewood-zerkalo.pro] "
mask = mask if mask else "[SW.BAND] "

for file in os.listdir("."):
    if file.startswith(mask):
        os.rename(file, file[len(mask) :])
