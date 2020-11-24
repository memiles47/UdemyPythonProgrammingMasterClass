__author__ = "Michael E Miles"
from functions import print_separator

cities = ["Adelaide", "Alice Springs", "Darwin", "Melbourne", "Sydney"]

with open("cities.txt", 'w') as city_file:
    for city in cities:
        print(city, file=city_file, flush=True)

        