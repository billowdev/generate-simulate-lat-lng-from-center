# generate-simulate-lat-lng-from-center-point
- main.py
```py
from geopy import Point
from geopy.distance import distance
import random

def generate_random_point(center, range_km):
    """
    Generate a random point within a given range (in km) of a center point.
    Returns a tuple of latitude and longitude.
    """
    # convert the range from km to degrees
    range_degrees = distance(kilometers=range_km).kilometers / 111

    # generate a random point within the range of the center point
    while True:
        # generate a random latitude and longitude within the range of the center point
        lat = random.uniform(center.latitude - range_degrees, center.latitude + range_degrees)
        lng = random.uniform(center.longitude - range_degrees, center.longitude + range_degrees)
        point = Point(lat, lng)

        # calculate the distance between the center point and the generated point
        dist = distance(center, point).km

        # check if the distance is within the range
        if dist <= range_km:
            break

    # return the latitude and longitude as a tuple
    return lat, lng

# จุดกึ่งกลาง
center = Point(13.812075143604403, 100.50499488728185)
# ช่วงระยะระดับกิโลเมตร
range_km = 20
lat, lng = generate_random_point(center, range_km)
print('Latitude:', lat)
print('Longitude:', lng)
```



