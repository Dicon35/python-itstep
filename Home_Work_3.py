import random
class Fish:
    def __init__(self, size, color, age):
        self.size = size
        self.color = color
        self.age = age
        self.alive = True

    def change_size(self):
        self.size = random.randint(1, 10)

    def generate_color(self):
        colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']
        self.color = random.choice(colors)

    def die(self):
        self.alive = False

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hungry = True
        self.alive = True

    def feed(self):
        self.hungry = False

    def play(self):
        self.hungry = True

    def sleep(self):
        self.hungry = True

    def eat(self, fish):
        if isinstance(fish, Fish) and fish.alive:
            self.hungry = False
            fish.die()
        else:
            print("I can't eat that!")


fish1 = Fish(5, 'red', 2)
fish2 = Fish(3, 'green', 1)
cat1 = Cat('Whiskers', 3)


print(fish1.size, fish1.color, fish1.age, fish1.alive)
fish1.change_size()
