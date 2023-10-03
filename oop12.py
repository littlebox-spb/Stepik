class Person:
    name = "John Smith"
    age = 30
    gender = "male"
    address = "123 Main St"
    phone_number = "555-555-5555"
    email = "johnsmith@example.com"
    is_employed = True


for i in list(input().split()):
    print(f'{i} - {"YES" if hasattr(Person,i) else "NO"}')
