# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE

class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

new = LatLon(23, 29)
print(new.lat, new.lon)

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE

class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        self.name = name
        super().__init__(lat, lon)

    def __str__(self):
        return f'Waypoint {self.name} at {self.lat} latitude and {self.lon} longitude'

new2 = Waypoint('this', 23, 28)
print(new2.lon)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE

class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lon, lat):
        self.difficulty = difficulty
        self.size = size
        super().__init__(name, lat, lon)

    def __str__(self):
        return f'{self.name} \n difficulty: {self.difficulty}\n size: {self.size}\n'

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE

new3 = Waypoint("Catacombs", 41.70505, -121.51521)
print(new3)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
# print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

new4 = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)
print(new4)

# Print it--also make this print more nicely
# print(geocache)
