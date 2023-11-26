import simplecrypt as cr

with open("encrypted.bin", "rb") as fileE:
    enc = fileE.read()
with open("passwords.txt", "r") as file:
    for pas in file:
        try:
            pas = pas.strip()
            print(cr.decrypt(pas, enc).decode("utf-8"))
            break
        except:
            print(f"{pas} - неверный пароль")
