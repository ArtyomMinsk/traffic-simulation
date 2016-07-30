import random


class Car:
    def __init__(self, position, distance_between):
        self.car_length = 5
        self.max_speed = 33
        self.acceleration = 2
        self.position = position
        self.speed = 0
        self.distance_between = distance_between

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
        else:
            return False

    def change_position(self):
        self.position = (self.position + self.speed) % 1000

    def find_distance_between(self, other):
        self.distance_between = (other.position - 5) - self.position


class Traffic:
    def __init__(self):
        pass

    def get_starting_positions(num_cars):
        road_distance = 1000
        start = []
        car = 1
        while car <= num_cars:
            front = (car * (road_distance/num_cars)) + 2.5
            start.append(round(front, 3))
            car += 1
        start = [item % 1000 for item in start]
        return start

    def set_up_cars(start, num_cars):
        road_distance = 1000
        distance_between = road_distance / num_cars - 5
        cars = []
        for num in range(num_cars):
            car = Car(start[num], distance_between)
            cars.append(car)
        return cars

    def too_close(self, other):
        if self.distance_between < self.speed:
            self.speed = other.speed
            return True
        elif self.distance_between == 0:
            self.speed = 0
            return True
        else:
            return False

    def location_list(cars):
        locations = []
        for car in range(len(cars)):
            locations.append(cars[car].position)
        return locations


def main():
    num_cars = 30
    seconds = 60

    starting_positions = Traffic.get_starting_positions(num_cars)
    print(starting_positions)

    cars = Traffic.set_up_cars(starting_positions, num_cars)

    for num in range(seconds):
        for car in range(len(cars)):
            # Last car in the circle must be compared to car 0
            if car == num_cars - 1:
                Car.randomly_slow(cars[car])
                Car.find_distance_between(cars[car], cars[0])

                if Traffic.too_close(cars[car], cars[0]):
                    Car.change_position(cars[car])
                else:
                    Car.accelerate(cars[car])
                    Car.change_position(cars[car])

            # All other cars in the circle must be compared to car+1
            else:
                Car.randomly_slow(cars[car])
                Car.find_distance_between(cars[car], cars[car + 1])

                if Traffic.too_close(cars[car], cars[car + 1]):
                    Car.change_position(cars[car])
                else:
                    Car.accelerate(cars[car])
                    Car.change_position(cars[car])

        print(Traffic.location_list(cars))

main()
