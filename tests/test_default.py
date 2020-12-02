import unittest

import signup


class TestDefault(unittest.TestCase):
    def test_cli_parser(self):
        args = signup.parse_args([
            '--username', 'example',
            '--password', 'secret'
        ])
        self.assertEqual(args.region, 'unitedstates')
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
