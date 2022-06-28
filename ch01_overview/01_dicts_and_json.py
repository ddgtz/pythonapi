"""

    01_dicts_and_json.py

"""
import json

capitals = {
    'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento',
    'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
    'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
    'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'St. Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City',
    'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
    'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier',
    'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'
}

# To get just the keys:
states = capitals.keys()
print(f'Keys: {states}')

# To get just the values:
capital_cities = capitals.values()
print(f'Values: {capital_cities}')

# To get both (as a list of tuples):
states_and_cities = capitals.items()
print(f'Keys and values: {states_and_cities}')

# To get a single item:
print(f'One item 3 ways: {capitals["Montana"]}, {capitals.get("Montana")}, {capitals.get("Montana", "Not found.")}')

# To convert it to JSON
capitals_json = json.dumps(capitals)
print('To JSON:\n', capitals_json)

# To convert the JSON string to a dict
capitals_dict = json.loads(capitals_json)
print('From JSON:\n', capitals_dict)

