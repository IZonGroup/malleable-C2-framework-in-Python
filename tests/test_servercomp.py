import unittest

from servercomp import app


class ServerCompTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_run_command_echo(self):
        response = self.client.post('/run_command', json={'command': 'echo test'})
        data = response.get_data(as_text=True)
        self.assertIn('test', data)


if __name__ == '__main__':
    unittest.main()
