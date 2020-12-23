import requests

response = requests.get('https://randomuser.me/api/?results=5')

data = response.json()