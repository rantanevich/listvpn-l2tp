import unittest
from pathlib import Path

import signup


BASEDIR = Path(__file__).parent
RESPONSE = BASEDIR / 'fixtures' / 'l2tp' / 'response.html'
REGISTRATION = BASEDIR / 'fixtures' / 'l2tp' / 'registration.html'


class TestSignUp(unittest.TestCase):
    def test_generate_payload(self):
        page = REGISTRATION.read_text()
        username = 'example'
        password = 'example'

        payload = signup.generate_payload(page, username, password)

        self.assertEqual(payload, {
            'username': username,
            'password': password,
            'id_server': '18',
            'Tanggal': '2020-10-30',
            'idsession': '125f9dfe7fe3d7ef176cb801f527e09f',
            'TanggalEnd': '2020-11-04',
            'Waktu': '13:02:39',
            'id_servernegara': 'america',
            'human-verifier': 28,
            'submit': ''
        })

    def test_extract_auth_data(self):
        page = RESPONSE.read_text()

        auth_data = signup.extract_auth_data(page)

        self.assertEqual(auth_data, [
            'listvpn.net-example',             # username
            'secret',                          # password
            'l2tpvpn-us.server-listvpn.net'    # server
        ])


if __name__ == '__main__':
    unittest.main()
