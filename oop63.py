class CustomButton:
    def __init__(self, text, **kwargs) -> None:
        self.text = text
        self.config(**kwargs)

    def config(self, **kwargs):
        self.__dict__.update(kwargs)

    def click(self):
        try:
            self.command()
        except AttributeError:
            print("Кнопка не настроена")
        except TypeError:
            print("Кнопка сломалась")


def func():
    print("Оно живое")


btn = CustomButton(text="Hello", bd=20, bg="#ffaaaa")
btn.click()  # Кнопка не настроена
btn.config(command=func)
btn.click()  # Оно живое
