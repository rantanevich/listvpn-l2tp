import unittest
from pathlib import Path

import signup


BASEDIR = Path(__file__).parent
RESPONSE = BASEDIR / 'fixtures' / 'pptp' / 'response.html'
REGISTRATION = BASEDIR / 'fixtures' / 'pptp' / 'registration.html'


class TestSignUp(unittest.TestCase):
    def test_generate_payload(self):
        page = REGISTRATION.read_text()
        username = 'example'
        password = 'example'

        payload = signup.generate_payload(page, username, password)

        self.assertEqual(payload, {
            'username': username,
            'password': password,
            'id_server': '9',
            'Tanggal': '2020-12-02',
            'idsession': '92422fef84d3496d21539031c1d5ef0f',
            'TanggalEnd': '2020-12-07',
            'Waktu': '15:34:14',
            'id_servernegara': 'america',
            'human-verifier': 16,
            'submit': ''
        })

    def test_extract_auth_data(self):
        page = RESPONSE.read_text()

        auth_data = signup.extract_auth_data(page)

        self.assertEqual(auth_data, [
            'listvpn.net-example',             # username
            'secret',                          # password
            'pptpvpn-us.server-listvpn.net'    # server
        ])


if __name__ == '__main__':
    unittest.main()
