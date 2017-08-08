class vehicle:

    def __init__(self, name):
        self.name = name
        self.wheels = 0
        self.ingnition = False
        self.passengers = []
        self.windows = 0

    def add_passenger(self,passenger):
        self.passengers.append(passenger)
    def set_color(self,color):
        self.color = color



def main():
    car = vehicle("prius")
    print (car.name)
    car.windows = 7
    print (car.windows)
    car.add_passenger("gabby")
    car.add_passenger("devki")
    car.set_color("blue")
    print(car.color)


    for seat in car.passengers:
        print("{} is great!".format(seat))


main()
