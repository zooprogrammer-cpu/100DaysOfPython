def print_letter(person_name):
    with open("./Input/Letters/starting_letter.txt") as file:
        contents = file.read()
        replaced = contents.replace("[name]", person_name)
        print(replaced)
        return replaced

with open("./Input/Names/invited_names.txt") as file:
    name_list =  file.read().splitlines()
    print(name_list)
    for name in name_list:
        replaced_letter = print_letter(name)
        with open(f"Letter -{name}.txt", "w") as individual_letter:
            individual_letter.write(replaced_letter)