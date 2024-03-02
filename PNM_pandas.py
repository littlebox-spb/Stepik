import pandas as pd

# create two series
s1 = pd.Series([1, 2])
s2 = pd.Series([3, 4])

# append s2 to s1
s3 = s1._append(s2)

print(s3)

s = pd.Series([10, 20, 30])

mean_value = s.mean()

print(mean_value)

import numpy as np

# Создаем DataFrame с пропусками
df = pd.DataFrame(
    [
        [np.nan, 2, np.nan, 0],
        [3, 4, np.nan, 1],
        [np.nan, np.nan, np.nan, np.nan],
        [np.nan, 3, np.nan, 4],
    ],
    columns=list("ABCD"),
)

# Выводим исходный DataFrame
print(df)

# Заполняем все пропуски нулями
df1 = df.fillna(0)

print(df1)

# create a series
s = pd.Series([1, 2, 3])

# apply a function to each element in the series
s = s.apply(lambda x: x * 2)

print(s)

s = pd.Series([1, None, 3])


def fillna_mean(x):
    return x.fillna(x.mean())


print(s.transform(fillna_mean))

# создадим фрейм данных
df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})

# отбросим колонку 'B'
df = df.drop(columns=["B"])

print(df)

# создадим серию с дублирующимися значениями
s = pd.Series([1, 2, 2])

# удалим дубликаты
s = s.drop_duplicates()

print(s)

# создадим две серии с одинаковыми значениями
s1 = pd.Series([1, 2])
s2 = pd.Series([1, 2])

# проверим, одинаковы ли они
result = s1.equals(s2)

print(result)

# создадим серию и список значений для проверки
s = pd.Series([1, 2])
values = [1]

# проверим, есть ли каждый элемент в серии в списке значений
result = s.isin(values)

print(result)

# создать серию и словарь для сопоставления с новыми значениями
s = pd.Series(["cat", "dog"])
mapping = {"cat": "feline", "dog": "canine"}

# сопоставить значения в серии с новыми значениями с помощью .map()
s = s.map(mapping)

print(s)

# создайте ряд с некоторыми значениями для замены их другими значениями.
s = pd.Series([1, 2])
to_replace = [1]
value = [3]

# заменим значения в серии на новое значение
s = s.replace(to_replace=to_replace, value=value)

print(s)

# Создаем series
s = pd.Series([2, 1])

# сортировка значений в серии
s = s.sort_values()

print(s)

s = pd.Series([3, 1, 2])

print(s.sort_values())

s1 = pd.Series([10, 20, 30])
n = 5

s_new = s1.div(n)

print(s_new)

s_new = s1.sub(n)

print(s_new)

s1 = pd.Series([1, 2, 3])
s2 = pd.Series([4, 5, 6])

s_new = s1.mul(s2)

print(s_new)

s = pd.Series([1, 2, 3])

s_new = s.pow(2)

print(s_new)
