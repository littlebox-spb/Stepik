import datetime

  
def candy_wrapper(fun):
    s=fun()
    print('------------------------')
    print(s)
    print('------------------------')


@candy_wrapper    
def ask(input):
    return input('Введите фразу: ')


ask(input)
