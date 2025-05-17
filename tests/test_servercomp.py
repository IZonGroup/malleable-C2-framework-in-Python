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

    def test_command_output_endpoint(self):
        self.client.post('/command_output', json={'output': 'hello'})
        response = self.client.get('/command_output')
        self.assertIn('hello', response.get_data(as_text=True))

    def test_run_command_stores_output(self):
        self.client.post('/run_command', json={'command': 'echo stored'})
        response = self.client.get('/command_output')
        self.assertIn('stored', response.get_data(as_text=True))


if __name__ == '__main__':
    unittest.main()
