from flask import Flask
import socket
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    hostname = socket.gethostname()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return f"""
    <html>
    <head>
        <title>Docker Flask App</title>
        <style>
            body {{
                font-family: Arial;
                background-color: #f4f4f4;
                text-align: center;
                padding-top: 100px;
            }}
            .container {{
                background: white;
                padding: 30px;
                margin: auto;
                width: 60%;
                border-radius: 10px;
                box-shadow: 0px 0px 10px rgba(0,0,0,0.2);
            }}
            h1 {{
                color: #0078D7;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Docker + Flask CI/CD Project 🚀</h1>
            <p><b>Container Hostname:</b> {hostname}</p>
            <p><b>Current Time:</b> {current_time}</p>
            <p>Application successfully running inside Docker container.</p>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)