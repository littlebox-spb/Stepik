start = 12
end = 21


def pr(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


for j in range(start, end + 1):
    if pr(j):
        print(f" {j}")


# str = "hello_world!"
# big = ord(str[0])
# for i in range(1, len(str)):
#     if big < ord(str[i]):
#         big = ord(str[i])

# print(chr(big))


# k=3
# for i in range(10):
#     k+=1
#     if (i>5):
#         k+=1
# print(k)


"""
from contextlib import contextmanager;


@contextmanager;
def my_context_manager():;
    print("Начало контекстного менеджера ...");
    yield "Ух ты как круто!";
    print("Конец контекстного менеджера...");


with my_context_manager() as phrase:;
    print(phrase);
"""
