# class character():
#     def __init__(self, health, speed, magic):
#         self.health = health
#         self.speed = speed
#         self.magic = magic

# ninja = character(12, 30, 100)

# print(ninja.speed)

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def addPassenger(self, name):
        if not self.openSeats():
            return False
        self.passengers.append(name)
        return True

    def openSeats(self):
        return self.capacity - len(self.passengers)
    


flight = Flight(3)

print(flight)

people = ["Hermione", "Guy", "Spencer", "Gustave"]
for person in people:
    success = flight.addPassenger(person)
    if success:
        print(f"Added successfully {person}")
    else:
        print(f"No available seat for {person}")

