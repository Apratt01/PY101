flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones1 = flintstones

flintstones += ['Dino', 'Hoppy']

print(flintstones)

#or

flintstones1.extend(['Dino', 'Hoppy'])

# extend modifies a list in place and returns None

print(flintstones1)

