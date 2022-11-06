import requests


def get_url(url):
    response = None
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.HTTPError as http_err:
        print(f'Error: {http_err}')
    except Exception as err:
        print(f'Unknown error: {err}')
    else:
        print('Connected')
    return response


def image_download(url, image_name):
    response = get_url(url)
    with open(f'{image_name}', 'wb') as file:
        file.write(response.content)
        print('Image download')



