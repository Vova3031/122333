class Zoo:
    # Атрибути рівня класу
    animal_types = ['Тигр', 'Пташка', 'Слон', 'Крокодил']
    habitat = 'Джунглі'

    def __init__(self, name, animal_type, can_fly=False, can_swim=False):
        # Атрибути рівня об'єкту
        self.name = name
        self.animal_type = animal_type
        self.can_fly = can_fly
        self.can_swim = can_swim

    def make_sound(self):
        if self.animal_type == 'Пташка':
            print(f"{self.name} співає")
        else:
            print(f"{self.name} ричить")

    def perform_action(self):
        if self.can_fly:
            print(f"{self.name} взлетів у небо")
        elif self.can_swim:
            print(f"{self.name} плаває в воді")
        else:
            print(f"{self.name} не вміє літати або плавати")

# Створення об'єктів класу Zoo
tiger = Zoo('Тигр', 'Тигр', can_fly=False, can_swim=False)
bird = Zoo('Пташка', 'Пташка', can_fly=True, can_swim=False)
elephant = Zoo('Слон', 'Слон', can_fly=False, can_swim=False)
crocodile = Zoo('Крокодил', 'Крокодил', can_fly=False, can_swim=True)

# Виклик методів для об'єктів
tiger.make_sound()
bird.perform_action()

