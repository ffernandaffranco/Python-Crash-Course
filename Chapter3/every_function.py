languages = ['Spanish', 'English', 'Portuguese', 'Guaraní', 'Dutch']

languages.append('Italian') # Adds Italian at the end

languages.insert(2, 'Japanese') # Adds Japanese to position 2

del languages[1] # Removes language in position 1

popped_language = languages.pop() # Removes last language

print(f"{popped_language} has been removed.")

languages.sort() # Changes the order of the list permanently in alphabetical order.
print(languages)

languages.sort(reverse = True) # Changes the order of the list permanently in reverse-alphabetical order.
print(languages)

print(sorted(languages)) # Displays the list in alphabetical order, but doesn't affect the actual order of the list.

print(sorted(languages, reverse = True)) # Displays the list in reverse-alphabetical order, but doesn't affect the actual order of the list.

languages.reverse() # Reverses the list permanently.
print(languages)

print(len(languages)) # Prints the number of items in the list







