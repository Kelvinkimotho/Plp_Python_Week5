class Vehicle:
    """
    Base class representing a generic vehicle.
    """
    def move(self):
        pass  # This method is overridden by subclasses

class Car(Vehicle):
    """
    Represents a Car, which moves by driving.
    """
    def move(self):
        print("Driving ...")

class Boat(Vehicle):
    """
    Represents a Boat, which moves by sailing.
    """
    def move(self):
        print("Sailing ...")

class Plane(Vehicle):
    """
    Represents a Plane, which moves by flying.
    """
    def move(self):
        print("Flying ..")

# Testing implementation one by one

# Test Car
print("A car moves by:")
car = Car()
car.move()

print("A boat moves by:")
# Test Boat
boat = Boat()
boat.move()

print("A plane moves by:")
# Test Plane
plane = Plane()
plane.move()
