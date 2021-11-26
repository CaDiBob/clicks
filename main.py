import argparse
import os
import requests
from dotenv import load_dotenv
from urllib.parse import urlparse


def is_bitlink(url_parse, token):
    headers = {'Authorization': token}
    link_for_verif = 'https://api-ssl.bitly.com/v4/bitlinks/{}'.format(url_parse)
    response = requests.get(link_for_verif, headers=headers,)
    return response.ok


def shorten_link(url, token):
    link_for_shorten = URL_MAIN
    headers = {'Authorization': token}
    data = {'long_url': url}
    response = requests.post(link_for_shorten, headers=headers, json=data)
    response.raise_for_status()
    return response.json()['link']


def count_clicks(url_parse, token):
    link_for_clicks = 'https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'.format(url_parse)
    headers = {'Authorization': token}
    response = requests.get(link_for_clicks, headers=headers,)
    response.raise_for_status()
    return response.json()['total_clicks']


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('name', help='ссылка для проверки')
    namespace = parser.parse_args()

    url = namespace.name
    url_parse = urlparse(url)[1] + urlparse(url)[2]
    load_dotenv()
    token = os.getenv('BITLY_API_TOKEN')
    if is_bitlink(url, token):
        try:
            clicks = count_clicks(url, token)
            print(f'По вашей ссылке прошли: {clicks} раз(a)')
        except requests.exceptions.HTTPError:
            print('Не корректная ссылка!')
    else:
        try:
            shortened = shorten_link(url, token)
            print(f'Битлинк: {shortened}')
        except requests.exceptions.HTTPError:
            print('Не корректная ссылка!')


if __name__ == '__main__':
    main()
