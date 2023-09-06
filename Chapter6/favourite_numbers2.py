favourite_numbers = {
    'enzo': [2, 4, 6],
    'pablo': [29, 30, 31],
    'fernanda': [11, 2],
    'agustín': [7, 1238545],
    'belén': [1298732, 15]
}

for name, numbers in favourite_numbers.items():
    print(f"\n{name.title()}'s favourite numbers are:")
    for number in numbers:
        print(f"\t{number}")

