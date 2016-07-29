import random


class Car:
    def __init__(self, position):
        self.car_length = 5
        self.max_speed = 33
        self.acceleration = 2
        self.position = position
        self.speed = 0
        self.distance_between = 27.4

    def accelerate(self):
        if self.speed < self.max_speed - 2:
            self.speed += self.acceleration
        else:
            self.speed == self.max_speed

    def decelerate(self):
        if self.speed <= 2:
            self.speed = 0
        else:
            self.speed -= self.acceleration

    def randomly_slow(self):
        if random.randint(1, 10) == 1:
            Car.decelerate(self)
            return True

    def change_position(self):
        self.position += self.speed

    def find_distance_between(self, other):
        self.distance_between = (self.position - 5) - other.position


class Traffic:
    def __init__(self):
        pass

    def get_starting_positions():
        start = []
        car = 1
        while car <= 30:
            back = (car * 27.4) + ((car) * 5)
            start.append(round(back, 1))
            car += 1
        return start

    def set_up_cars(start):
        cars = []
        for num in range(30):
            car = Car(start[num])
            cars.append(car)
        return cars

    def too_close(self, other):
        if self.distance_between < self.speed:
            self.speed = other.speed
            return True
        if self.distance_between == 0:
            self.speed = 0
            return False

def main():
    cars = Traffic.set_up_cars(Traffic.get_starting_positions())
    for num in range(60):
        for car in range(len(cars)):
            if not Car.randomly_slow(cars[car]):
                Car.accelerate(cars[car])
                Car.find_distance_between(cars[car], cars[car - 1])
                if Traffic.too_close(cars[car], cars[car - 1]):
                    Car.change_position(cars[car])
                    print(cars[car].position)
            else:
                Car.change_position(cars[car])
                print(cars[car].position)




main()
