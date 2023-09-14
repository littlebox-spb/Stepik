cc = enumerate(input()[-1::-1], start=1)
cs = 0
for i in cc:
    if i[0] % 2 == 0:
        cs += int(i[1]) * 2 if int(i[1]) * 2 < 10 else int(i[1]) * 2 - 9
    else:
        cs += int(i[1])
print(cs % 10 == 0)

# english_words = (
#     "attack",
#     "bless",
#     "look",
#     "reckless",
#     "short",
#     "monster",
#     "trolley",
#     "sound",
#     "ambiguity",
#     "researcher",
#     "trunk",
#     "coat",
#     "quantity",
#     "question",
#     "tenant",
#     "miner",
#     "definite",
#     "kit",
#     "spectrum",
#     "satisfied",
#     "selection",
#     "carve",
#     "ask",
#     "go",
#     "suggest",
# )

# for index, value in enumerate(english_words, start=1):
#     print(f"Word № {index} = {value}")


# words = [
#     "feel",
#     "graduate",
#     "movie",
#     "fashionable",
#     "bacon",
#     "drop",
#     "produce",
#     "acquisition",
#     "cheap",
#     "strength",
#     "master",
#     "perception",
#     "noise",
#     "strange",
#     "am",
# ]

# # words_with_position

# words_with_position = []
# for index, value in enumerate(words,start=1):
#     c = (value, index)
#     words_with_position.append(c)

# print(words_with_position)
