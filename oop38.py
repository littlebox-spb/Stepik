# Напишите определение класса ShoppingCart
class ShoppingCart:
    def __init__(self) -> None:
        self.items: dict = {}

    def __getitem__(self, name):
        if name in self.items:
            return self.items[name]
        return 0

    def __setitem__(self, name, value):
        self.items[name] = value

    def __delitem__(self, name):
        self.items.pop(name)

    def add_item(self, name, value=1):
        if name in self.items:
            self.items[name] += value
        else:
            self.items[name] = value

    def remove_item(self, name, value=1):
        if name in self.items:
            if self.items[name] <= value:
                self.items.pop(name)
            else:
                self.items[name] -= value


# Ниже код для проверки методов класса ShoppingCart

# Create a new shopping cart
cart = ShoppingCart()

# Add some items to the cart
cart.add_item("Apple", 3)
cart.add_item("Banana", 2)
cart.add_item("Orange")

assert cart["Banana"] == 2
assert cart["Orange"] == 1
assert cart["Kivi"] == 0

cart.add_item("Orange", 9)
assert cart["Orange"] == 10

print("Shopping Cart:")
for item_name in cart.items:
    print(f"{item_name}: {cart[item_name]}")

cart["Apple"] = 5
cart["Banana"] = 7
cart["Kivi"] = 11
assert cart["Apple"] == 5
assert cart["Banana"] == 7
assert cart["Kivi"] == 11

print("Updated Shopping Cart:")
for item_name in cart.items:
    print(f"{item_name}: {cart[item_name]}")

# Remove an item from the cart
cart.remove_item("Banana")
assert cart["Banana"] == 6

cart.remove_item("Apple", 4)
assert cart["Apple"] == 1

cart.remove_item("Apple", 2)
assert cart["Apple"] == 0
assert "Apple" not in cart.items

cart.remove_item("Potato")

del cart["Banana"]
assert cart["Banana"] == 0
assert "Banana" not in cart.items

print("Updated Shopping Cart:")
for item_name in cart.items:
    print(f"{item_name}: {cart[item_name]}")

# # Напишите определение классов Song и Playlist
# class Song:
#     def __init__(self, title, artist) -> None:
#         self.title = title
#         self.artist = artist


# class Playlist:
#     def __init__(self) -> None:
#         self.songs: list = []

#     def __getitem__(self, key):
#         return self.songs[key]

#     def __setitem__(self, key, value):
#         self.songs.insert(key, value)

#     def add_song(self, value):
#         self.songs.append(value)


# # Ниже код для проверки методов классов Song и Playlist

# playlist = Playlist()
# assert len(playlist.songs) == 0
# assert isinstance(playlist, Playlist)
# playlist.add_song(Song("Paradise", "Coldplay"))
# assert playlist[0].title == "Paradise"
# assert playlist[0].artist == "Coldplay"
# assert len(playlist.songs) == 1

# playlist[0] = Song("Resistance", "Muse")
# assert playlist[0].title == "Resistance"
# assert playlist[0].artist == "Muse"
# assert playlist[1].title == "Paradise"
# assert playlist[1].artist == "Coldplay"

# playlist[1] = Song("Helena", "My Chemical Romance")
# assert playlist[1].title == "Helena"
# assert playlist[1].artist == "My Chemical Romance"

# assert playlist[2].title == "Paradise"
# assert playlist[2].artist == "Coldplay"
# print("Good")

# class Building:
#     def __init__(self, n) -> None:
#         self.et = [None for i in range(n)]

#     def __setitem__(self, key, value):
#         if 0 <= key < len(self.et):
#             self.et[key] = value

#     def __getitem__(self, key):
#         if 0 <= key < len(self.et):
#             return self.et[key]

#     def __delitem__(self, key):
#         if 0 <= key < len(self.et):
#             self.et[key] = None


# iron_building = Building(22)  # Создаем здание с 22 этажами
# iron_building[0] = "Reception"
# iron_building[1] = "Oscorp Industries"
# iron_building[2] = "Stark Industries"
# print(iron_building[2])
# del iron_building[2]
# print(iron_building[2])
