"""

    21_testing_flask_sqlalchemy_patch.py

"""
import requests

base_url = 'http://localhost:8051'
path = '/api/celebrities/'



print('posting:')
celeb_name = 'George Costanza'
results = requests.post(f'{base_url}{path}',
                        data={'name': celeb_name, 'pay': 1.1, 'year': 1993,
                              'category': 'Sales Rep in Charge of the Penske File'})
print(results.text)

print('getting:')
new_celeb_id = results.json().get('id')
results = requests.get(f'{base_url}{path}{new_celeb_id}')
print(results.text)

print('patching (only category):')
results = requests.patch(f'{base_url}{path}{new_celeb_id}', data={'category': 'Hand Model'})
print(results.text)

print('putting (only category, this would be incorrect behavior):')
results = requests.put(f'{base_url}{path}{new_celeb_id}', data={'category': 'Hand Model'})
print(results.text)

print('deleting:')
results = requests.delete(f'{base_url}{path}{new_celeb_id}')
print(results.text)
