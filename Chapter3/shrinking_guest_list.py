guests = ['Harry Styles', 'David Bowie', 'Chris Nolan']

guests.insert(0, 'Lady Gaga')
guests.insert(1, 'Rihanna')
guests.append('Taylor Swift')

print("Unfortunately I will only be able to invite two people to the dinner. I'm sorry.")

popped_guest = guests.pop()
print(f"You can't come to my house. I am very sorry, {popped_guest}. Maybe next time.")

popped_guest = guests.pop()
print(f"You can't come to my house. I am very sorry, {popped_guest}. Maybe next time.")

popped_guest = guests.pop()
print(f"You can't come to my house. I am very sorry, {popped_guest}. Maybe next time.")

popped_guest = guests.pop()
print(f"You can't come to my house. I am very sorry, {popped_guest}. Maybe next time.")

print(f"Hi! You are still invited, {guests[0]}. I'm looking forward to seeing you.")
print(f"Hi! You are still invited, {guests[1]}. I'm looking forward to seeing you.")

del guests[0]
del guests[0]

print(guests)