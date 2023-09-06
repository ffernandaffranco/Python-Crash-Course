favourite_places = {
    'fernanda': ['jardín japonés', 'plaza mayor', 'civita di bagnoregio'],
    'enzo': ['central park', 'venice beach'],
    'pablo': ['observatoire de paris', 'tour eiffel']
}

for person, places in favourite_places.items():
    print(f"{person.title()}'s favourite places are:")
    for place in places:
        print(f"\t{place.title()}")
