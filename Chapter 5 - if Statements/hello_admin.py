users = ['fertpwk', 'enzocs', 'olqed', 'tombo', 'admin']

for user in users:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again.")

if users:
    print("Hello, users!")
else:
    print("We need to find some users!")