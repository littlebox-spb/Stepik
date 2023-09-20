

# def count_AGTC(dna: list):
#     return dna.count("A"), dna.count("G"), dna.count("T"), dna.count("C")


# # код ниже не стоит удалять, он нужен для проверки
# assert count_AGTC("AGGTC") == (1, 2, 1, 1)
# assert count_AGTC("AAAATTT") == (4, 0, 3, 0)
# assert count_AGTC("AGTTTTT") == (1, 1, 5, 0)
# assert count_AGTC("CCT") == (0, 0, 1, 2)
# print("Проверки пройдены")

# def factorial(n):
#     fact = 1
#     for num in range(2, n + 1):
#         fact *= num
#     return fact


# def trailing_zeros(n):
#     cnt = 0
#     f = factorial(n)
#     while True:
#         if f % 10 != 0:
#             return cnt
#         else:
#             f //= 10
#             cnt += 1
#     return cnt


# код ниже не стоит удалять, он нужен для проверки
# assert trailing_zeros(0) == 0
# assert trailing_zeros(6) == 1
# assert trailing_zeros(30) == 7
# assert trailing_zeros(12) == 2
# print("Проверки пройдены")


# def get_domain_name(url):
#     s = []
#     if url.startswith("http://"):
#         s = url.replace("http://", "").split(".")
#     if url.startswith("www."):
#         s = url.replace("www.", "").split(".")
#     if url.startswith("https://"):
#         s = url.replace("https://", "").split(".")
#     if url.startswith("http://www."):
#         s = url.replace("http://www.", "").split(".")
#     if url.startswith("https://www."):
#         s = url.replace("https://www.", "").split(".")
#     return s[0]


# # код ниже не стоит удалять, он нужен для проверки
# assert get_domain_name("http://google.com") == "google"
# assert get_domain_name("http://google.co.jp") == "google"
# assert get_domain_name("www.xakep.ru") == "xakep"
# assert get_domain_name("https://youtube.com") == "youtube"

# assert get_domain_name("http://github.com/carbonfive/raygun") == "github"
# assert get_domain_name("http://www.zombie-bites.com") == "zombie-bites"
# assert get_domain_name("https://www.siemens.com") == "siemens"
# assert get_domain_name("https://www.whatsapp.com") == "whatsapp"
# assert get_domain_name("https://www.mywww.com") == "mywww"
# print("Проверки пройдены")


# def format_name_list(names: list):
#     out = ""
#     i = 0
#     while i < len(names):
#         if i == 0:
#             out += names[i]["name"]
#         elif i < len(names) - 1:
#             out = out + ", " + names[i]["name"]
#         else:
#             out = out + " и " + names[i]["name"]
#         i += 1

#     return out


# # код ниже не стоит удалять, он нужен для проверки
# assert (
#     format_name_list([{"name": "Bart"}, {"name": "Lisa"}, {"name": "Maggie"}, {"name": "Homer"}, {"name": "Marge"}])
#     == "Bart, Lisa, Maggie, Homer и Marge"
# )

# assert format_name_list([{"name": "Bart"}, {"name": "Lisa"}, {"name": "Maggie"}]) == "Bart, Lisa и Maggie"

# assert format_name_list([{"name": "Bart"}, {"name": "Lisa"}]) == "Bart и Lisa"

# assert format_name_list([{"name": "Bart"}]) == "Bart"

# assert format_name_list([]) == ""

# assert (
#     format_name_list(
#         [{"name": "Maggie"}, {"name": "Lisa"}, {"name": "Barney"}, {"name": "Homer"}, {"name": "Bart"}, {"name": "Moe"}]
#     )
#     == "Maggie, Lisa, Barney, Homer, Bart и Moe"
# )

# assert format_name_list([{"name": "Marge"}, {"name": "Maggie"}, {"name": "Seymour"}]) == "Marge, Maggie и Seymour"

# assert format_name_list([{"name": "Maude"}, {"name": "Bart"}]) == "Maude и Bart"

# print("Проверки пройдены")


# def first_unique_char(s):
#     for i in s:
#         if s.count(i) == 1:
#             return s.index(i)
#     else: return -1

# s = input()
# print(first_unique_char(s))

# def find_duplicate(lst):
#     skan = []
#     sout = []
#     for s in lst:
#         if s not in skan and s not in sout:
#             skan.append(s)
#             sout.append(s)
#             continue
#         else:
#             if s in skan:
#                 skan.remove(s)
#     else:
#         if skan == sout:
#             sout = []
#         elif len(skan) > 0:
#             for j in skan:
#                 sout.remove(j)
#     return sout


# assert find_duplicate([1, 1, 1, 1, 1, 2, 2, 2, 2]) == [1, 2]
# assert find_duplicate([2, 1, 1, 1, 1, 1, 2, 2, 2, 2]) == [2, 1]
# assert find_duplicate([1, 2, 3, 4]) == []
# assert find_duplicate([8, 7, 6, 5, 4, 3, 4, 5, 6, 7, 8]) == [8, 7, 6, 5, 4]
# print("Все успешно")

# def gcd(a, b):
#     while b > 0:
#         a, b = b, a % b
#     return a


# n = []
# a = 0
# nod = 0
# for _ in range(int(input())):
#     n.append(int(input()))
# for i in n:
#     if a == 0:
#         a = i
#         continue
#     b = i
#     nod = gcd(a, b)
#     a = nod
# print(nod)


# def generate_fizz_buzz_list(n):
#     sp=[]
#     for i in range(1,n+1):
#         if i%3==0 and i%5==0: sp.append(['FizzBuzz'])
#         elif i%3==0: sp.append(['Fizz'])
#         elif i%5==0: sp.append(['Buzz'])
#         else: sp.append([i])
#     return sp

# print(generate_fizz_buzz_list(10))
