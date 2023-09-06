cities = {
    'Rome': {
        'country': 'italy',
        'population': 4342212,
        'famous landmark': 'colosseum'
    },
    'Prague': {
        'country': 'czech republic',
        'population': 1357326,
        'famous landmark': 'prague castle'
    },
    'Buenos Aires': {
        'country': 'argentina',
        'population': 3120612,
        'famous landmark': 'teatro colón'
    }
}

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    landmark = city_info['famous landmark'].title()
    city_name = city.title()

    print(f"{city_name} is in {country}.")
    print(f"\tIt's population is {population}.")
    print(f"\tA famous landmark is the {landmark}.\n")