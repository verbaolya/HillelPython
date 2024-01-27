import json
import csv
import random

# Read data from the JSON file
with open('data.json', 'r') as json_file:
    data_dict = json.load(json_file)

# Prepare data for writing to CSV
csv_data = [['ID', 'Name', 'Age', 'Phone']]

# List of possible first three digits (operators)
possible_operators = ['095', '066', '098', '096', '050', '097']

for key, value in data_dict.items():
    id_number = key
    name = value[0]
    age = value[1]

    # Determine if the person has a phone number with 75% probability
    has_phone = random.random() < 0.75

    if has_phone:
        # Choose a random operator
        operator = random.choice(possible_operators)

        # Generate the remaining 7 digits of the phone number
        remaining_digits = ''.join([str(random.randint(0, 9)) for _ in range(7)])

        # Combine the operator and remaining digits
        phone_number = f"+{operator}-{remaining_digits}"
    else:
        phone_number = None

    csv_data.append([id_number, name, age, phone_number])

# Write data to the CSV file
with open('data.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(csv_data)

print('Data has been written to data.csv.')
