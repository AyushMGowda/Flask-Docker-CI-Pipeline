from flask import Flask, render_template, request, redirect
import socket
from datetime import datetime

app = Flask(__name__)

tasks = [
    {"title": "Setup Docker Container", "status": "Completed"},
    {"title": "Configure Jenkins Pipeline", "status": "Completed"},
    {"title": "Implement GitHub Actions", "status": "Pending"}
]

@app.route('/')
def home():
    hostname = socket.gethostname()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template(
        'index.html',
        tasks=tasks,
        hostname=hostname,
        current_time=current_time
    )

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    
    if task:
        tasks.append({
            "title": task,
            "status": "Pending"
        })

    return redirect('/')

@app.route('/complete/<int:index>')
def complete_task(index):
    tasks[index]["status"] = "Completed"
    return redirect('/')

@app.route('/delete/<int:index>')
def delete_task(index):
    tasks.pop(index)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)