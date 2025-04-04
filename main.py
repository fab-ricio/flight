class character():
    def __init__(self, health, speed, magic):
        self.health = health
        self.speed = speed
        self.magic = magic

ninja = character(12, 30, 100)

print(ninja.speed)