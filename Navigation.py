from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Placeholder for internal state
last_location = {}
destination_location = {}
last_summary = None

@app.route('/receive_location', methods=['POST'])
def receive_location():
    return jsonify({"message": "Navigation processing stub."}), 200

@app.route('/last_summary', methods=['GET'])
def get_summary():
    return jsonify({"summary": last_summary})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
