class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

mode1X = Vehicle(240, 18)
print("Model Max Speed:",mode1X.max_speed)
print("Model Mileage", mode1X.mileage)