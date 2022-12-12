import requests
from bs4 import BeautifulSoup as soup
from time import sleep



# WIP: this script should get the value sent in the website but it doesnt work yet
get = requests.Session().get(
    'https://glamorously-beautiful-iris-flat.wayscript.cloud/?', 
    cookies={
        '_wayscript_session': '1dd4f305-85bb-4d15-b16c-e9eba4319f33.L9-vO7Fqv1JfyhvmfEqIbKvLldA',
        'AWSALB': 'XyurPRDkn9CW+AX9Yb5mfkFLH9RrNeNleuFiIwwSD9AAv154OLvqzUfhsiO00yAGejI3xITAoJou6rPN/uuMpnWX+1PlsKMkYJni3t8BmCtg4oTaf1VutzIq2Dy3',
        'AWSALBAPP-0': 'AAAAAAAAAACIQ0h0H8DWDjn2WhLRO0wD+UjuMYTjCgQrhnJM2tbNU8+6ZfFt0XGM/7AcbDFUSctWt0Vn9eBqE/Kf46gVeOWu1n+pKJ2JWdQfWxY7zCc+YviJj4XDSTXkdYqHej/BDYJDOpI=',
        'AWSALBAPP-1': '_remove_',
        'AWSALBAPP-2': '_remove_',
        'AWSALBAPP-3': '_remove_',
        'AWSALBCORS': 'XyurPRDkn9CW+AX9Yb5mfkFLH9RrNeNleuFiIwwSD9AAv154OLvqzUfhsiO00yAGejI3xITAoJou6rPN/uuMpnWX+1PlsKMkYJni3t8BmCtg4oTaf1VutzIq2Dy3',
        'ws_workspace_application_key_e912b38b-9e1d-4400-b2bb-d593c9e44c8a': '1f062a90-86ce-4860-826e-cfd456fdfee2'
        })
response = get.status_code
print(response)
if response == 200:

    html = soup(str(get.text), features='html.parser')
    print(html)

