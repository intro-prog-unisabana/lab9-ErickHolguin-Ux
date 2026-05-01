# Write your class definition here!
class Car:
    def __init__(self, car_id, brand, year, color, mileage):
        self.car_id = car_id
        self.brand = brand
        self.year = year
        self.color = color
        self.mileage = mileage

    def drive(self, miles):
        self.mileage += miles

    def change_color(self, new_color):
        self.color = new_color

    def __str__(self):
        return f"{self.car_id} - {self.year} {self.color} {self.brand} with {self.mileage} miles"