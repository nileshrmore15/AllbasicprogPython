class Vehicle:  # parent class
    def start(self):
        print("Vehicle started")

    def stop(self):
        print("Vehicle stopped")

class Car(Vehicle):    # child class
    def drive(self):
        print("Car driving")

# Create a Car object and call its methods
car = Car()
car.start()
car.drive()
car.stop()