from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

def get_top_output():
    try:
        return subprocess.check_output("top -bn1 | head -20", shell=True).decode()
    except Exception as e:
        return str(e)

@app.route('/htop')
def htop():
    name = "Swati Agrawal"  
    system_username = os.getenv("USER", "Unknown User")  # Will show 'codespaces'
    github_username = os.getenv("CODESPACES_USER", "swati191")  # Get actual GitHub username
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")
    top_output = get_top_output().replace("\n", "<br>")  

    return f"""
    <h1>System Info</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>System Username:</strong> {system_username}</p>
    <p><strong>GitHub Username:</strong> {github_username} </p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)