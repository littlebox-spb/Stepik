# Напишите определение класса User и классов исключений
class PasswordInvalidError(Exception):
    pass


class PasswordLengthError(PasswordInvalidError):
    pass


class PasswordContainUpperError(PasswordInvalidError):
    pass


class PasswordContainDigitError(PasswordInvalidError):
    pass


class User:
    def __init__(self, username) -> None:
        self.username = username
        self.password = None

    def set_password(self, _value: str):
        if len(_value) < 8:
            raise PasswordLengthError("Пароль должен быть не менее 8 символов")
        dig = False
        for i in set(_value):
            dig = dig or i.isupper()
        if not dig:
            raise PasswordContainUpperError("Пароль должен содержать хотя бы одну заглавную букву")
        dig = False
        for i in set(_value):
            dig = dig or i.isdigit()
        if not dig:
            raise PasswordContainDigitError("Пароль должен содержать хотя бы одну цифру")
        self.password = _value


# Ниже код для проверки

assert issubclass(PasswordInvalidError, Exception)
assert issubclass(PasswordLengthError, PasswordInvalidError)
assert issubclass(PasswordContainUpperError, PasswordInvalidError)
assert issubclass(PasswordContainDigitError, PasswordInvalidError)

user = User("johndoe")

try:
    user.set_password("weakpwd")
except PasswordLengthError as e:
    print(e)

try:
    user.set_password("strongpassword8")
except PasswordContainUpperError as e:
    print(e)

try:
    user.set_password("Safepassword")
except PasswordContainDigitError as e:
    print(e)

user.set_password("SecurePass123")
assert user.password == "SecurePass123"

# # Напишите определение класса BankAccount и исключений
# # NegativeDepositError и InsufficientFundsError


# class NegativeDepositError(Exception):
#     pass


# class InsufficientFundsError(Exception):
#     pass


# class BankAccount:
#     def __init__(self, balance) -> None:
#         self.balance = balance

#     def deposit(self, _value):
#         if _value < 0:
#             raise NegativeDepositError("Нельзя пополнить счет отрицательным значением")
#         self.balance += _value

#     def withdraw(self, _value):
#         if self.balance < _value:
#             raise InsufficientFundsError("Недостаточно средств для снятия")
#         self.balance -= _value


# # Ниже код для проверки

# try:
#     raise InsufficientFundsError("Недостаточно средств")
# except Exception as e:
#     if not isinstance(e, InsufficientFundsError):
#         raise ValueError("Реализуйте исключение InsufficientFundsError")

# try:
#     raise NegativeDepositError("Внесено отрицательное значение")
# except Exception as e:
#     if not isinstance(e, NegativeDepositError):
#         raise ValueError("Реализуйте исключение NegativeDepositError")

# account = BankAccount(100)
# assert account.balance == 100

# account.deposit(50)
# assert account.balance == 150

# account.withdraw(75)
# assert account.balance == 75

# try:
#     account.withdraw(100)
# except InsufficientFundsError as e:
#     print(e)  # "Недостаточно средств"

# assert account.balance == 75

# try:
#     account.deposit(-50)
# except NegativeDepositError as e:
#     print(e)  # "Внесено отрицательное значение"


# users = {
#     "alice": {"name": "Alice Smith", "email": "alice@example.com"},
#     "bob": {"name": "Bob Johnson", "email": "bob@example.com"},
#     "jack": {"name": "Jack Wild", "email": "jack_wild@example.com"}
# }

# class UserNotFoundError(Exception):
#     pass

# def get_user(username):
#     #  напишите реализацию функции
#     try:
#         return users[username]['name']
#     except Exception:
#         raise UserNotFoundError('User not found')

# try:
#     username = get_user(input())
# except UserNotFoundError as e:
#     print(e)
# else:
#     print(username)
