"""

    03_test_celeb_auth.py
    This client requires 02_celeb_auth.py to be running in order for it to work.

"""
import requests
from requests.auth import HTTPBasicAuth

base_url = 'http://localhost:8051'
path = '/api'
print('Working with our Celeb auth API.  It will require authentication before')
print('accessing any resources, as demonstrated with this client.')

# This should respond with token is missing
print(requests.get(f'{base_url}{path}/celebrities').json())

# This should respond with token is invalid
print(requests.get(f'{base_url}{path}/celebrities', headers={'x-access-token': 'foo'}).json())

# This should give back a token, we'll print the token to the screen
# We can use GET here since no HTTP body is needed, credentials are supplied as an HTTP header.
credentials = HTTPBasicAuth('admin', 'admin')                                           # these should be stored externally and retrieved via os.environ.get("MYAPP_PASSWORD")
print(f'Logging in as: ', credentials.username)
login_response = requests.get(f'{base_url}{path}/login', auth=credentials).json()
print(login_response)
token = login_response.get('token')

# this should enable access to the earlier URL above with the token now supplied
print('Making a request to get 1 page from GET ALL Celebrities:')
print(requests.get(f'{base_url}{path}/celebrities', headers={'x-access-token': token}).json())

# next we'll create a user with a name of Sally and a password of password, she is not an administrator and
# therefore should not be allowed to create or delete a user...we'll attempt to delete the John user
new_user_info = {
    'name': 'Sally',
    'password': 'password',
    'admin': False
}
new_user_req = requests.post(f'{base_url}{path}/user',
                             headers={'x-access-token': token},
                             data=new_user_info)
print(new_user_req.text)
sallys_public_id = new_user_req.json().get('public_id')

# log in with new user creds (Sally, password, not an admin)
credentials = HTTPBasicAuth('Sally', 'password')
print(f'Logging in as: ', credentials.username)
login_response = requests.get(f'{base_url}{path}/login', auth=credentials).json()
print(login_response)
token = login_response.get('token')

# access get one celebrity with new creds
celeb_id = 1  # (Oprah Winfrey)
print('Making request to retrieve 1 celebrity')
print(requests.get(f'{base_url}{path}/celebrities/{celeb_id}', headers={'x-access-token': token}).json())

# try to delete the John user without proper creds
print('Attempting to delete a user with Sally\'s credentials')
print(requests.delete(f'{base_url}{path}/user/ba0db74c-5844-44bc-bd9a-2c8b35d48c28',
                      headers={'x-access-token': token}).text)

# log in as admin, delete Sally
credentials = HTTPBasicAuth('admin', 'admin')
print(f'Logging in as: ', credentials.username)
login_response = requests.get(f'{base_url}{path}/login', auth=credentials).json()
token = login_response.get('token')

print('Deleting Sally...')
print(requests.delete(f'{base_url}{path}/user/{sallys_public_id}', headers={'x-access-token': token}).text)
