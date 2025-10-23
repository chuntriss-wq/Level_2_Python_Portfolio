class Car:
    # 1. Class Attribute (shared by all Car objects)
    wheels = 4

    # 2. Constructor Method (initializes the object's state)
    def __init__(self, make, model, color):
        # 3. Instance Attributes (unique to this specific car)
        self.make = make
        self.model = model
        self.color = color
        self.speed = 0  # Initial speed is 0

    # 4. Instance Method (a behavior/action)
    def accelerate(self, increment):
        """Increases the car's speed."""
        self.speed += increment
        return f"The {self.color} {self.make} is now traveling at {self.speed} mph."

    # 5. Another Instance Method
    def get_description(self):
        """Returns a string describing the car."""
        return f"A {self.color} {self.make} {self.model} with {self.wheels} wheels."

# ------------------------------------------------------------------

# Creating objects (instances) of the Car class
car1 = Car("Toyota", "Camry", "Red")
car2 = Car("Ford", "Focus", "Blue")

# Accessing Attributes
print(car1.get_description())
print(f"Car 2 has {car2.wheels} wheels.")

# Calling Methods (making the objects do something)
print(car1.accelerate(30))
print(car2.accelerate(15))
print(car2.accelerate(10))

