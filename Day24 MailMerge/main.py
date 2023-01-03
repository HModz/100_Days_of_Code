names = []

with open("Input/Names/invited_names.txt") as file:
    for i in file:
        print(i)
        names.append(i[:-1])

print(names)

for name in names:
    print(name)
    with open("Input/Letters/starting_letter.txt") as file:
        letter = file.read()
        new_letter = letter.replace("[name]", name)
        with open(f"Output/ReadyToSend/{name}_letter", mode="w") as new_file:
            new_file.write(new_letter)
