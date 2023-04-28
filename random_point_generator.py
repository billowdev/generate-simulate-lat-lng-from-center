from geopy import Point
from geopy.distance import distance
import random

class RandomPointGenerator:
    """
    A class for generating random points within a given range (in km) of a center point.
    """
    def __init__(self, center, range_km):
        self.center = center
        self.range_km = range_km
        self.range_degrees = distance(kilometers=self.range_km).kilometers / 111

    def generate_random_point(self):
        """
        Generate a random point within the given range of the center point.
        Returns a tuple of latitude and longitude.
        """
        while True:
            lat = random.uniform(self.center.latitude - self.range_degrees, self.center.latitude + self.range_degrees)
            lng = random.uniform(self.center.longitude - self.range_degrees, self.center.longitude + self.range_degrees)
            point = Point(lat, lng)
            dist = distance(self.center, point).km
            if dist <= self.range_km:
                break
        return lat, lng

# create an instance of the RandomPointGenerator class
center = Point(13.812075143604403, 100.50499488728185)
range_km = 20
generator = RandomPointGenerator(center, range_km)

# generate a random point using the class method
lat, lng = generator.generate_random_point()
print('Latitude:', lat)
print('Longitude:', lng)
