# from string import punctuation


# def longest_word_in_file(file_name: str) -> str:
#     my_file = open(file_name, encoding="utf-8")
#     s = max([i.strip((punctuation)) for i in my_file.read().split()][::-1], key=len)
#     my_file.close()
#     return s


# my_file = open("numbers.txt", encoding="utf-8")
# # n2 = [int(i) for i in my_file.read().split() if len(i) == 2]
# n3 = [int(i) for i in my_file.read().split() if len(i) == 3]
# my_file.close()
# print(len(n3))

words = set()
with open("words.txt", encoding="utf-8") as my_file:
    for i in my_file.read().split():
        if i.upper()[-2:] == "ЕЯ":
            words.add(i.upper())

print(*sorted(words, key=lambda x: (len(x), x)), sep="\n")
