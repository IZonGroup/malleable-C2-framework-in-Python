## client component that can receive commands from the server and execute them.

from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/run_command', methods=['POST'])
def run_command():
    # Extract the command from the JSON payload
    command = request.json['command']

    # Execute the command using subprocess
    try:
        output = subprocess.check_output(command, shell=True)
    except subprocess.CalledProcessError as err:
        return err.output

    # Send the output back to the server using an HTTP POST request
    requests.post('http://server_url/command_output', json={'output': output})

    return 'Command executed successfully'
