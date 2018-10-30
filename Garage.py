#!/usr/bin/python
class Garage():
        vehicles = []
        isOpen = True

        def add(self, vehicle):
                assert isinstance(vehicle, Vehicle)
                if self.isOpen:
                        self.vehicles.append(vehicle)
                else:
                        print("the garage needs to be open first")
        def empty(self):
                self.vehicles = []
        def open(self):
                self.isOpen = True
        def close(self):
                self.isOpen = False

class Vehicle:
        def __init__(self, wheels):
                self.wheels = wheels

class Car(Vehicle):
        def __init__(self, model):
                Vehicle.__init__(self, 4)
                self.model = model

class Bike(Vehicle):
        def __init__(self, model):
                Vehicle.__init__(self, 2)
                self.model = model

garage = Garage()
garage.add(Car("BMW"))
garage.add(Car("BMW"))
garage.add(Bike("Suzuki"))
garage.add(Bike("Suzuki"))


for vehicle in garage.vehicles:
        print(isinstance(vehicle, Bike))