person_1 = {
    'first_name': 'harry',
    'last_name': 'styles',
    'age': 29,
    'city': 'redditch'
}

person_2 = {
    'first_name': 'louis',
    'last_name': 'tomlinson',
    'age': 31,
    'city': 'doncaster'
}

person_3 = {
    'first_name': 'dua',
    'last_name': 'lipa',
    'age': 28,
    'city': 'london'
}

people = [person_1, person_2, person_3]

for person in people:
    print(f'Full Name: {person["first_name"].title()} {person["last_name"].title()}')
    print(f'Age: {person["age"]}')
    print(f'City: {person["city"].title()}\n')
