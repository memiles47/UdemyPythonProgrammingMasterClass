__author__ = "Michael E Miles"
from functions import print_separator

cities = ["Adelaide", "Alice Springs", "Darwin", "Melbourne", "Sydney"]

with open("cities.txt", 'w') as city_file:
    for city in cities:
        print(city, file=city_file)

cities_again = []

with open("cities.txt", 'r') as cities_file:
    for city in cities_file:
        cities_again.append(city)

print(cities_again)
for city in cities_again:
    print(city, end='')
