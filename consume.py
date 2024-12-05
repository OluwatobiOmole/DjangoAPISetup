import requests

#Test script for API call
response = requests.get('http://127.0.0.1:8000/drinks')
print(response.json())


