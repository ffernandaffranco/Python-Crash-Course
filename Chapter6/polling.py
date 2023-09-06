favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

people = ['sarah', 'fernanda', 'pablo', 'edward']

for person in people:
    if person in favourite_languages:
        print(f"Thank you for taking the poll, {person.capitalize()}!\n")
    else:
        print(f"Hello, {person.capitalize()}. Would you like to participate in our poll?\n")
