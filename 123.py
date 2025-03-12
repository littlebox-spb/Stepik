file = open("example.txt", "w")  # Открыть файл для записи ✏️
file.write("Первая строка.")  # Записать текст в файл 📝
file.close()  # Закрыть файл 🔒

file = open("example.txt", "a")  # Открыть файл для добавления данных ➕
file.write("\nВторая строка.")  # Добавить строку в конец файла 📝
file.close()  # Закрыть файл 🔒

file = open("example.txt", "r")  # Открыть файл для чтения 📖
content = file.read()  # Читаем весь файл 📚
print(content)  # Печатаем содержимое файла 🖨️
file.close()  # Закрываем файл 📕
