from flask import Flask, request, render_template_string
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
        <h1>Command Injection Test</h1>
        <form action="/execute" method="POST">
            Command: <input type="text" name="command" required><br>
            <input type="submit" value="Execute">
        </form>
    ''')

@app.route('/execute', methods=['POST'])
def execute():
    user_command = request.form['command']
   
    # Debugging: Print the command to the console
    print("Executing command:", user_command)
   
    # Vulnerable code: directly using user input in a system command
    try:
        result = subprocess.check_output(user_command, shell=True, text=True)
    except subprocess.CalledProcessError as e:
        result = f"Error: {e.output}"
   
    return f"Command executed: {user_command}<br>Output:<br>{result}"

if __name__ == '__main__':
    app.run(debug=True)

