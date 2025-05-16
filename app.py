from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow requests from your Arduino

# Initial state
state = {"status": "idle"}

@app.route("/")
def home():
    return jsonify({"message": "Backend online", "current_status": state["status"]})

@app.route("/status", methods=["GET"])
def status():
    return jsonify({"status": state["status"]})

@app.route("/activate", methods=["GET"])
def activate():
    state["status"] = "activate"
    return jsonify({"message": "Status set to activate"})

@app.route("/reset", methods=["GET"])
def reset():
    state["status"] = "idle"
    return jsonify({"message": "Status reset to idle"})

if __name__ == "__main__":
    app.run(debug=True)
