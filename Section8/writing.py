__author__ = "Michael E Miles"

from functions import print_separator

cities = ["Adelaide", "Alice Springs", "Darwin", "Melbourne", "Sydney"]

with open("cities.txt", 'w') as city_file:
    for city in cities:
        print(city, file=city_file)

cities_again = []

with open("cities.txt", 'r') as cities_file:
    for city in cities_file:
        cities_again.append(city.strip('\n'))

print(cities_again)
for city in cities_again:
    print(city)

imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"),
    (4, "Kentish Town Waltz")
)

with open("imelda3.txt", 'w') as imelda_file:
    print(imelda, file=imelda_file)

with open("imelda3.txt", 'r') as imelda_file:
    print(imelda, file=imelda_file)


print(type(imelda))
