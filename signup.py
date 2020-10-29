import re
import string
import random
import argparse
import logging

import requests


URL = 'https://www.listvpn.net/create-account-vpn-l2tp-{}'
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] (%(filename)s:%(lineno)d) %(levelname)s: %(message)s'
)


def main():
    args = get_args()
    url = URL.format(args.region)

    session = requests.session()
    response = session.get(url)

    payload = generate_payload(response.text, args.username, args.password)

    response = session.post(url, data=payload)
    try:
        pattern = 'value=[\'"](.+?)[\'"] id=[\'"]myInput'
        username, password, server = re.findall(pattern, response.text)
    except ValueError:
        logging.error('account has not been created')
        exit(1)

    print(
        f'server    : {server}',
        f'username  : {username}',
        f'password  : {password}',
        f'shared key: listvpn',
        f'port      : 1701',
        sep='\n'
    )


def generate_payload(page, username, password):
    pattern = 'name=[\'"]{}[\'"] value=[\'"](.+?)[\'"]'
    payload = {
        'id_server': '',
        'Tanggal': '',
        'idsession': '',
        'TanggalEnd': '',
        'Waktu': '',
        'id_servernegara': ''
    }
    for option in payload:
        data = re.findall(pattern.format(option), page)[0]
        if not data:
            logging.error(f'{option} has not been found')
            exit(1)
        payload[option] = data

    captcha = re.findall('What is (\d+ . \d+)', page)[0]
    payload['human-verifier'] = eval(captcha)
    payload['username'] = username
    payload['password'] = password
    payload['submit'] = ''

    return payload


def get_args():
    parser = argparse.ArgumentParser(
        description='Creates L2TP VPN account https://www.listvpn.net'
    )
    parser.add_argument('-r', '--region',
                        type=str,
                        default='unitedstates',
                        help='region of vpn server (default: unitedstates)')
    parser.add_argument('-u', '--username',
                        type=str,
                        default=get_random_string(8),
                        help='username (from 5 to 10 characters)')
    parser.add_argument('-p', '--password',
                        type=str,
                        default=get_random_string(8),
                        help='password (from 5 to 10 characters)')
    return parser.parse_args()


def get_random_string(size=6):
    alphabet = string.ascii_letters + string.digits
    return ''.join([random.choice(alphabet) for _ in range(size)])


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        logging.exception(err, exc_info=True)
