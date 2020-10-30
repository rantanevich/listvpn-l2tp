import unittest
from pathlib import Path

import signup


BASEDIR = Path(__file__).parent
RESPONSE = BASEDIR / 'response.html'
REGISTRATION = BASEDIR / 'registration.html'


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

    def test_cli_parser(self):
        args = signup.parse_args([
            '--username', 'example',
            '--password', 'secret'
        ])
        self.assertEquals(args.region, 'unitedstates')
        self.assertEqual(args.username, 'example')
        self.assertEqual(args.password, 'secret')

        args = signup.parse_args([
            '-r', 'russia2'
        ])
        self.assertEqual(args.region, 'russia2')
        self.assertTrue(args.username)
        self.assertTrue(args.password)

    def test_get_random_string(self):
        for size in range(5, 11):
            text = signup.get_random_string(size)

            self.assertIsInstance(text, str)
            self.assertEqual(len(text), size)


if __name__ == '__main__':
    unittest.main()
