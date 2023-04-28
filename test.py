from random_point import RandomPointGenerator

# create an instance of the RandomPointGenerator class
center = Point(13.812075143604403, 100.50499488728185)
range_km = 20
generator = RandomPointGenerator(center, range_km)

# generate a random point using the class method
lat, lng = generator.generate_random_point()
print('Latitude:', lat)
print('Longitude:', lng)
