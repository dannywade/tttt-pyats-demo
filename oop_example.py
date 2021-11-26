class Car():
    # Class-level
    wheels = 4
    
    def __init__(self, manufacturer: str, model: str, color: str, mileage: int):
    # Instance-level
        self.manufacturer = manufacturer
        self.model = model
        self.color = color
        self.mileage = mileage
        
    # Method
    def add_mileage(self, miles: int) -> str:
        self.mileage += miles
        print(f"The car has {miles} miles on it.")

my_car = Car("Audi", "R8", "Blue", 1000)

print(f"I just bought a {my_car.color} {my_car.manufacturer} {my_car.model}")
print(f"My new car's mileage is {my_car.mileage}")
print("Adding 500 miles to my car...")
my_car.add_mileage(500)
print(f"My new car's mileage is {my_car.mileage}")