class Vehicle:

    def __init__(self, make="None", model="None", year="None", weight="None", needs_maintenance=False, trips_since_maintenance=0):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.maintenance = needs_maintenance
        self.trips = trips_since_maintenance

    def setMake(self, make):
        self.make = make

    def setModel(self, model):
        self.model = model

    def setYear(self, year):
        self.year = year

    def setWeight(self, weight):
        self.weight = weight

    def setTrips(self, trips_since_maintenance):
        self.trips = trips_since_maintenance

    def setMaintenance(self):
        if self.trips < 100:
            self.maintenance = False
            return "Maintenance is up to date."
        else:
            self.maintenance = True
            return "Time to go to the garage for a check up!"

    def getTrips(self):
        if self.trips == 0:
            return "No trips since maintenance yet."
        else:
            return self.trips


class Car(Vehicle):

    def __init__(self, make, model, year, weight, needs_maintenance, trips_since_maintenance, isDriving, repair=False):
        Vehicle.__init__(self, make, model, year, weight, needs_maintenance, trips_since_maintenance)
        self.isDriving = isDriving
        self.repair = repair

    def setDriveStop(self):
        if not self.isDriving:
            self.stop = True
            return "The car is stopped."
        else:
            self.stop = False
            self.trips += 1
            return "The car is moving. " + str(self.trips)

    def setRepair(self):
        if self.repair:
            self.trips = 0
            self.maintenance = False
            return self.maintenance


car1 = Car("Ford", "Fusion", 2017, 2000, False, 0, True)

print(car1.make)
print(car1.model)
print(car1.year)
print(str(car1.weight) + "Kg")
print(car1.setMaintenance())
print(car1.getTrips())
print(car1.setDriveStop())
print(car1.maintenance)
print("===============")

car2 = Car("Ford", "Focus", 2019, 2000, False, 100, True, True)

print(car2.make)
print(car2.model)
print(car2.year)
print(str(car2.weight) + "Kg")
print(car2.setMaintenance())
print(car2.getTrips())
print(car2.setDriveStop())
print(car2.setRepair())
print("===============")

car3 = Car("VW", "Golf", 2020, 2000, False, 7, False)

print(car3.make)
print(car3.model)
print(car3.year)
print(str(car3.weight) + "Kg")
print(car3.setMaintenance())
print(car3.getTrips())
print(car3.setDriveStop())
print(car3.maintenance)
print("===============")
