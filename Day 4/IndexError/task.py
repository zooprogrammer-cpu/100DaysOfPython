states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america)

num_of_states = len(states_of_america)

print(num_of_states)

# print(states_of_america[num_of_states]) # this creates an IndexError : list index out of range

print(states_of_america[num_of_states-1]) # Prints Hawaii

# Nested List
dirty_dozen = ["Spinach", "Strawberries", "Potatoes", "Kale", "Pears"]

fruits = ["Strawberries", "Pears"]

vegetables = ["Spinach", "Potatoes"]

nested_list = [fruits, vegetables]

print(nested_list) #[['Strawberries', 'Pears'], ['Spinach', 'Potatoes']]

print (nested_list[1][1]) # Potatoes




