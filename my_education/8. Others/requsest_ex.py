import requests
import json
from getpass import getpass

response = requests.get("https://lenta.ru")
print(response)
print(type(response))
print(response.status_code)
print()

urls = ["https://lenta.ru", "https://skihllbox.ru", "https://lenta.ru/city"]

for url in urls:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.HTTPError as http_err:
        print(f'Error: {http_err}')
    except Exception as err:
        print(f'Unknown error: {err}')
    else:
        print('Connected')

response = requests.get("https://lenta.ru/")
data = dict(response.headers)

response = requests.get("https://go.skillbox.ru/auth/sign-in", auth=("hasanaliyeev@gmail.com", getpass()))

print(response)
