class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound

    def make_sound(self):
        return f"{self.name} видає звук: {self.sound}"

    def __str__(self):
        return f"{self.name} - це {self.species}"


class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = [] 

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
            print(f"{animal.name} додано до зоопарку {self.name}")
        else:
            print("Цей об'єкт не є твариною!")

    def show_all_animals(self):
        if not self.animals:
            print(f"У зоопарку {self.name} немає тварин.")
        else:
            print(f"У зоопарку {self.name} є такі тварини:")
            for animal in self.animals:
                print(animal)

    def make_all_sounds(self):
        if not self.animals:
            print("Немає тварин, щоб видавати звуки.")
        else:
            print("Усі тварини видають звуки:")
            for animal in self.animals:
                print(animal.make_sound())

lion = Animal("Лев", "хижак", "Рррр!")
elephant = Animal("Слон", "травоїдний", "Тру-у-у!")
monkey = Animal("Мавпа", "примат", "У-у-у!")

zoo = Zoo("Веселий Зоопарк")
zoo.add_animal(lion)
zoo.add_animal(elephant)
zoo.add_animal(monkey)

zoo.show_all_animals()

zoo.make_all_sounds()
