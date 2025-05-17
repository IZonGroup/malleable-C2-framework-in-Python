## Simple command-line user interface for a C2 framework

"""Simple command-line user interface for the C2 framework."""

import os
import requests

SERVER_URL = os.getenv('SERVER_URL', 'http://server_url')

def send_command(command):
    """Send a command to the server."""
    requests.post(f"{SERVER_URL}/run_command", json={'command': command})

def view_output():
    """Retrieve and display the output from the server."""
    response = requests.get(f"{SERVER_URL}/command_output")
    print(response.text)

def main():
    """Run the simple text-based UI loop."""
    while True:
        command = input('Enter a command: ')
        send_command(command)
        view_output()


if __name__ == '__main__':
    main()
