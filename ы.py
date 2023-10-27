class Car:
    # Атрибути рівня класу
    car_types = ['Седан', 'Спорткар', 'SUV', 'Мінівен']
    fuel_type = 'Бензин'

    def __init__(self, brand, car_type, color, year, speed):
        # Атрибути рівня об'єкту
        self.brand = brand
        self.car_type = car_type
        self.color = color
        self.year = year
        self.speed = speed

    def start(self):
        print(f"{self.color} {self.brand} поїхав")

    def stop(self):
        print(f"{self.color} {self.brand} зупинився")

    def accelerate(self):
        print(f"{self.color} {self.brand} розганяється")

    def brake(self):
        print(f"{self.color} {self.brand} гальмує")

    def honk(self):
        print(f"{self.color} {self.brand} сигналить")

# Створення об'єктів класу Car
sedan = Car('Toyota', 'Седан', 'Червоний', 2020, 120)
sportscar = Car('Ferrari', 'Спорткар', 'Жовтий', 2022, 250)
suv = Car('Jeep', 'SUV', 'Синій', 2021, 180)
minivan = Car('Honda', 'Мінівен', 'Сірий', 2019, 100)

# Виклик методів для об'єктів
sedan.start()
sportscar.accelerate()
minivan.brake()
suv.honk()
