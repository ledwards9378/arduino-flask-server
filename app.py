from flask import Flask, request, send_file, jsonify
import threading

app = Flask(__name__)

# Global state: "idle" or "activate"
state = {"action": "idle"}

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/trigger', methods=['POST'])
def trigger():
    # When the button is pressed, set action to activate
    state["action"] = "activate"
    return jsonify(status="ok", action=state["action"])

@app.route('/status', methods=['GET'])
def status():
    # Return current action
    return jsonify(action=state["action"])

@app.route('/reset', methods=['POST'])
def reset():
    # Arduino calls this after it’s run to clear the flag
    state["action"] = "idle"
    return jsonify(status="ok", action=state["action"])

if __name__ == '__main__':
    app.run(host='0.0.0.0')
