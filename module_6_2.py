class Vehicle:   # зададим класс
    __COLOR_VARIANTS = ['Violet', 'seashell', 'BlAcK ', 'pink', 'carmine'] # атриб. класса - допуст. цвета

    def __init__(self, owner, model, color, engine_power): # зададим метод для базовых парам.
        self.owner = owner    # владелец транспорта
        self.__model = model  # модель (марка)
        self.__engine_power = engine_power # мощность двигателя
        self.__color = color  # название цвета

    def get_model(self):  # метод возвращ-т назв. модели
        return f"Модель: {self.__model}"

    def get_horsepower(self):  # метод возвращ-т мощность двигателя
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):  # метод возвращ-т цвет авто
        return f"Цвет: {self.__color}"

    def print_info(self): # для вывода результатов методов
        print(self.get_model()) # модель (марка)
        print(self.get_horsepower())  # мощность двигателя
        print(self.get_color()) # название цвета
        print(f"Владелец: {self.owner}") # инф-ция о владельце

    def set_color(self, new_color):  # метод для замены цвета
        # есть ли нов. цвет среди допустимых невзирая на регистр
        if new_color.lower() in [color.lower() for color in self.__COLOR_VARIANTS]:
            self.__color = new_color
        else: # иначе вывод надписи
            print(f"Нельзя сменить цвет на {new_color}")

class Sedan(Vehicle):  # зададим класс
    __PASSENGERS_LIMIT = 5 # атриб. класса: в седан может поместиться только 5 пассажиров
    # остальные параметры наследуются от Vehicle

# пример
vehicle1 = Sedan('Lana', 'Nissan Silvia S13', 'CarmIne', 135)

vehicle1.print_info() # вывод заданной информации

# изменим свойства (в т.ч. вызывая методы)
vehicle1.set_color('Violet')
vehicle1.owner = 'Svetlana'

vehicle1.print_info() # вывод изм-ой информации