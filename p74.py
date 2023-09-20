def shift_letter(l:str,sh:int)->str:
    "Функция сдвигает символ letter на shift позиций"
    sl:str=[chr(i) for i in range(97,123)]
    ind:int=sl.index(l)+sh
    while ind>26 or ind<=-26:
        ind=ind%26
    return sl[ind]

def caesar_cipher(st:str,sh:int)->str:
    "Шифр цезаря"
    so:str=''
    for ind in range(len(st)):
        so+=shift_letter(st[ind],sh) if st[ind].isalpha() else st[ind]
    return so

    
print(caesar_cipher('one more light',-33)) #hgx fhkx ebzam
# print(caesar_cipher('w',-26)) #w
# print(caesar_cipher('z',5)) #e
# print(caesar_cipher('a',53)) #b



