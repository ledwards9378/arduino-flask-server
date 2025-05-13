from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return 'Arduino Control Server is live!'

@app.route('/trigger', methods=['POST'])
def trigger():
    print(f"[{datetime.datetime.now()}] Button pressed!")
    # Placeholder: This is where you'd forward the command to Arduino
    return {'status': 'ok', 'message': 'Command received'}

if __name__ == '__main__':
    app.run(host='0.0.0.0')
