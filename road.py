class Road:
    def __init__(self):
        self.length = 1000




def make_road():
    counter = 29
    road = [0, 5]
    for num in range(counter):
        road.append(road[-1] + 28)
        road.append(road[-1] + 5)

    return road


print(make_road())
