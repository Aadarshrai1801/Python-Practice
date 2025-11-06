# Nesting Lists & Dictionaries

capitals = {
    "France" : "Paris",
    "Germany" : "Berlin"
}

# Nesting a list in a dictionary

travel_log = {
    "France" : {"cities_visited" : ["Paris", "Lille", "Dijon"], "total_visits" : 12},
    "Germany" : {"cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], "total_visits" : 9}
}

# Nesting Dictionary in a List

travel_log = {
    {
        "Country" : "France",
        "cities_visited" : ["Paris", "Lille", "Dijon"],
        "total_visits" : 12
    },
    {
        "Country" : "Germany",
        "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits" : 9
    }
}


# Day 9-2-Exercise

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