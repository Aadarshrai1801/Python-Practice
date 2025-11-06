travel_log = [
    {
        "Country" : "France",
        "cities" : ["Paris", "Lille", "Dijon"],
        "visits" : 12
    },
    {
        "Country" : "Germany",
        "cities" : ["Berlin", "Hamburg", "Stuttgart"],
        "visits" : 9
    }
]

def add_new_country(country_visited, cities_visited, times_visited) :
    new_coutry = {}
    new_coutry["Country"] = country_visited
    new_coutry["cities"] = cities_visited
    new_coutry["visits"] = times_visited
    travel_log.append(new_coutry)

add_new_country("Russia", ["Moscow", "Saint Peterburg"], 2)

print(travel_log)