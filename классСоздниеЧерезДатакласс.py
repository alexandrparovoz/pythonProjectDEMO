# как избавиться от всяких  __init__(self)
# и храня экземпляр класса спокойно передавать его в функцию
# импортируем  dataclasses
from dataclasses import dataclass
@dataclass
class User:
    user_id: int
    name: str
    age: int
    email: str
    # def __init__(self, user_id, name, age, email):
    #     self.user_id = user_id
    #     self.name = name
    #     self.age = age
    #     self.email = email

def get_info(user: User):  # обращаем внимание на обратнй слеш для переноса сторки кода
    return f'Возраст юзера{user.name} - {user.age},\
 а email{user.email}'
user1: User = User(42, 'ivan', 34, 'ivan@mail.ru')
print(get_info(user1))



# как увидеть типы переменных
# вызвать метод __annotations__

def func(string: str, number: int):
    return string * number
print(func.__annotations__)
