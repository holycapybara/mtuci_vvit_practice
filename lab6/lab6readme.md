# Лабораторная работа 6 - Работа с классами ч. 2
## Задание 1 - Защита данных пользователя
> 1.	Создайте класс UserAccount, который представляет аккаунт пользователя с атрибутами: имя пользователя (username), электронная почта (email) и приватный атрибут пароль (password).
>2.	Используйте конструктор `__init__` для инициализации этих атрибутов.
>3.	Реализуйте метод set_password(new_password), который позволяет безопасно изменить пароль аккаунта.
>4.	Реализуйте метод check_password(password), который проверяет, соответствует ли введённый пароль текущему паролю аккаунта и возвращает True или False.
>5.	Создайте объект класса UserAccount, попробуйте изменить пароль и проверить его с помощью методов set_password и check_password.
```python
class UserAccount:
    username : str
    email : str
    __password : str

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_password):
        self.__password = new_password

    def check_password(self, password):
        return self.__password == password


admin = UserAccount("admin", "pussydestroyer666@mail.ru", "ilovedota2")
admin.set_password("ilovecs2")
print(admin.check_password("ilovedota2"))
print(admin.check_password("ilovecs2"))
```
Для аттрибута содержащего пароль добавляем перед именем два нижних подчеркивания, чтобы ограничить к нему доступ извне. Изменить его во внешней 
программе будет невозможно без использование "сеттера". 
## Задание 2 - Полиморфизм и наследование
> 1.	Определите базовый класс Vehicle с атрибутами: make (марка) и model (модель),
> а также методом get_info(), который возвращает информацию о транспортном средстве.
> 2. Создайте класс Car, наследующий от Vehicle, и добавьте в него атрибут fuel_type (тип топлива).
> Переопределите метод get_info() таким образом, чтобы он включал информацию о типе топлива.
```python
class Vehicle:
    make : str
    model : str

    def __init__(self, make, model):
        self.model = model
        self.make = make

    def get_info(self):
        return f'make: {self.make}, model: {self.model}'


class Car(Vehicle):
    fuel_type : str

    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type


    def get_info(self):
        return f'make: {self.make}, model: {self.model}, fuel type: {self.fuel_type}'


plane1 = Vehicle("Boeing", "747")
car1 = Vehicle("Mazda", "CX7")
car2 = Car("Mercedes", "S800", "oil")
car3 = Car("Tesla", "Cybertruck", "electric")
[print(v.get_info()) for v in [plane1, car1, car2, car3]]

```
В конструкторе дочернего класса вызываем конструктор родительского класса. Сделать это можно с помощью метода `super()`. Для переопределения метода
создаем в дочернем классе метод с таким же названием, но другими инструкциями, в данном случае - выводим дополнительную информацию о машине. 

Демонстрацией полиморфизма в данном случае будет то, что несмотря на то что вызов метода `get_info()` как объектов двух разных классов будет идентичен, 
фактически будет вызван метод класса, соответсвущего конкретному объекту, т.е. для `plane` и `car1` вызывается метод класса `Vehicle`, а для
`car2` и `car3` - метод класса `Car`. 
