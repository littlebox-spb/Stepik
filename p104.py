# days = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve"]
# print(*sorted(list(filter(lambda s: len(s) == 4 or s[0] == "S", days))), sep="\n")


employees = [
    "Pankratiy",
    "Innokentiy",
    "Anfisa",
    "Yaroslava",
    "Veniamin",
    "Leonti",
    "Daniil",
    "Mishka",
    "Lidochka",
    "Terenti",
    "Vladik",
    "Svetka",
    "Maks",
    "Yura",
    "Sergei",
]

identifiers = [77, 48, 88, 85, 76, 81, 62, 43, 5, 56, 17, 20, 37, 32, 96]
employees_data = {}
employees_data.update(zip(sorted(identifiers), sorted(employees)))
print(employees_data)
