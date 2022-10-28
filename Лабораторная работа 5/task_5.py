import string
from random import sample


def get_random_password(n=8) -> str:
    list_ = string.ascii_letters + string.digits  # TODO написать функцию генерации случайных паролей
    return ''.join(sample(list_, n))


print(get_random_password())
