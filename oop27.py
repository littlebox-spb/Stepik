class Money:
    def __init__(self, dollars, cents):
        self.total_cents = dollars * 100 + cents

    @property
    def dollars(self):
        return self.total_cents // 100

    @dollars.setter
    def dollars(self, dollars):
        if isinstance(dollars, int) and dollars >= 0:
            self.total_cents = dollars * 100 + self.cents
        else:
            print("Error dollars")

    @property
    def cents(self):
        return self.total_cents % 100

    @cents.setter
    def cents(self, cents):
        if isinstance(cents, int) and 100 > cents >= 0:
            self.total_cents = self.dollars * 100 + cents
        else:
            print("Error cents")

    def __str__(self) -> str:
        return f"Ваше состояние составляет {self.dollars} долларов {self.cents} центов"


Bill = Money(101, 99)
print(Bill)  # Ваше состояние составляет 101 долларов 99 центов
print(Bill.dollars, Bill.cents)  # 101 99
print(Bill.total_cents)  # 10199
Bill.dollars = 666
print(Bill)  # Ваше состояние составляет 666 долларов 99 центов
Bill.cents = 12
print(Bill)  # Ваше состояние составляет 666 долларов 12 центов

# class Notebook:
#     def __init__(self, listn: list):
#         self._notes = listn

#     @property
#     def notes_list(self):
#         j = 1
#         for i in self._notes:
#             print(f"{j}. {i}")
#             j += 1


# note = Notebook(["Buy Potato", "Buy Carrot", "Wash car"])
# note.notes_list


# # Напишите определение класса File
# class File:
#     def __init__(self, size):
#         self._size_in_bytes = size

#     @property
#     def size(self):
#         if self._size_in_bytes < 1024:
#             return f"{self._size_in_bytes} B"
#         elif 1024 <= self._size_in_bytes < 1048576:
#             return f"{round(self._size_in_bytes/1024,2):.2f} KB"
#         elif 1048576 <= self._size_in_bytes < 1073741824:
#             return f"{round(self._size_in_bytes/1048576,2):.2f} MB"
#         else:
#             return f"{round(self._size_in_bytes/1073741824,2):.2f} GB"

#     @size.setter
#     def size(self, size):
#         self._size_in_bytes = size


# # Ниже код для проверки методов класса File

# file = File(5)
# assert file.size == "5 B"
# file.size = 1023
# assert file.size == "1023 B"
# file.size = 1024
# assert file.size == "1.00 KB"

# file_1 = File(1500000)
# assert file_1._size_in_bytes == 1500000
# assert file_1.size == "1.43 MB"

# file_2 = File(1500)
# assert file_2.size == "1.46 KB"


# file_3 = File(2789326322)
# assert file_3.size == "2.60 GB"
# file_3.size = 1073741824
# assert file_3.size == "1.00 GB"

# print("Good")
