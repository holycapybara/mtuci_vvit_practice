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




def task_1():
    admin = UserAccount("admin", "pussydestroyer666@mail.ru", "ilovedota2")
    admin.set_password("ilovecs2")
    print(admin.check_password("ilovedota2"))
    print(admin.check_password("ilovecs2"))


def task_2():
    plane1 = Vehicle("Boeing", "747")
    car1 = Vehicle("Mazda", "CX7")
    car2 = Car("Mercedes", "S800", "oil")
    car3 = Car("Tesla", "Cybertruck", "electric")
    [print(v.get_info()) for v in [plane1, car1, car2, car3]]


if __name__ == "__main__":
    task_2()