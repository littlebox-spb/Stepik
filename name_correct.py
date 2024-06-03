import os

mask = '[pirat.biz] '

for file in os.listdir('.'):
    if file.startswith(mask):
        os.rename(file, file[len(mask):])