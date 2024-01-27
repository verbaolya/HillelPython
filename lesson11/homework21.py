import json

data_dict = {
    123456: ('Alice', 25),
    234567: ('Bob', 30),
    345678: ('Charlie', 22),
    456789: ('David', 28),
    567890: ('Eva', 35),
    678901: ('Frank', 40)
}

with open('data.json', 'w') as json_file:
    json.dump(data_dict, json_file, indent=2)

print('Data has been written to data.json.')

