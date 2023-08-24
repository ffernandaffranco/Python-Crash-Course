current_users = ['FerTPWK', 'enzoCS', 'OLQED', 'tombo', 'kimbO']
current_users_lower = ['fertpwk', 'enzocs', 'olqed', 'tombo', 'kimbo']
new_users = ['Dinas', 'OTTO', 'RedSito', 'EnzoCS', 'Olqed']

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user.lower()} is already taken. Choose another one.")
    else:
        print(f"Welcome {new_user.lower()}!")
