class Wallet:
    def __init__(self, currency, balance) -> None:
        if not isinstance(currency, str):
            raise TypeError("Неверный тип валюты")
        elif len(currency) != 3:
            raise NameError("Неверная длина названия валюты")
        elif not currency.isupper():
            raise ValueError("Название должно состоять только из заглавных букв")
        self.currency = currency
        self.balance = balance

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Wallet):
            raise TypeError(f"Wallet не поддерживает сравнение с {__value}")
        elif self.currency != __value.currency:
            raise ValueError("Нельзя сравнить разные валюты")
        return self.balance == __value.balance

    def __add__(self, __value: object):
        if not isinstance(__value, Wallet) or self.currency != __value.currency:
            raise ValueError("Данная операция запрещена")
        return Wallet(self.currency, self.balance + __value.balance)

    def __sub__(self, __value: object):
        if not isinstance(__value, Wallet) or self.currency != __value.currency:
            raise ValueError("Данная операция запрещена")
        return Wallet(self.currency, self.balance - __value.balance)


wallet1 = Wallet("USD", 50)
wallet2 = Wallet("RUB", 100)
wallet3 = Wallet("RUB", 150)
# wallet4 = Wallet(12, 150)  # исключение TypeError('Неверный тип валюты')
# wallet5 = Wallet("qwerty", 150)  # исключение NameError('Неверная длина названия валюты')
wallet6 = Wallet("abc", 150)  # исключение ValueError('Название должно состоять только из заглавных букв')
print(wallet2 == wallet3)  # False
# print(wallet2 == 100)  # TypeError('Wallet не поддерживает сравнение с 100')
# print(wallet2 == wallet1)  # ValueError('Нельзя сравнить разные валюты')
wallet7 = wallet2 + wallet3
print(wallet7.currency, wallet7.balance)  # печатает 'RUB 250'
wallet2 + 45  # ValueError('Данная операция запрещена')
