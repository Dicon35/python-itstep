import random
class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 0
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("Game time")
        self.progress += 0.12
        self.gladness -= 3

    def to_sleep(self):
        print(" Time sleep")
        self.gladness += 3

    def to_chill(self):
        print("Eat time")
        self.gladness += 5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print("The cat is lost...")
            self.alive = False




    def day(self):
        print(f"Walks on the street - {self.gladness}")
        print(f"A cat's love for its owner - {round(self.progress, 2)}")

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        self.day()
        self.is_alive()

cat = Student("Cat")

for day in range(1, 366):
    if cat.alive == False:
        break
    cat.live(day)
