def get_word_indices(strings: list[str]) -> dict:
    d={}
    for i in range(len(strings)):
        for j in strings[i].split():
            if j.lower() in d:
                d[j.lower()].append(i)
            else:
                d[j.lower()]=[i]      
    return d





assert get_word_indices(['This is a string',
                         'test String',
                         'test',
                         'string']) == {'this': [0], 'is': [0], 'a': [0],
                                        'string': [0, 1, 3], 'test': [1, 2]}

assert get_word_indices(['Look at my horse',
                         'my horse',
                         'is amazing']) == {'look': [0], 'at': [0], 'my': [0, 1],
                                            'horse': [0, 1], 'is': [2], 'amazing': [2]}

assert get_word_indices([]) == {}

assert get_word_indices(['Avada Kedavra',
                         'avada kedavra',
                         'AVADA KEDAVRA']) == {'avada': [0, 1, 2],
                                               'kedavra': [0, 1, 2]}

# MIN_DRIVING_AGE = 18

# def allowed_driving(name: str, age: int) -> None:
#     print(f'{name} может водить' if age>=MIN_DRIVING_AGE else f'{name} еще рано садиться за руль')

# MIN_DRIVING_AGE = 18
# allowed_driving('tim', 17) # выведет "tim еще рано садиться за руль"
# allowed_driving('bob', 18) # выведет "bob может водить"