from flask import Flask, request, jsonify
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

# Hardcoded user details
USER_ID = "john_doe_17091999"
EMAIL = "john@xyz.com"
ROLL_NUMBER = "ABCD123"

@app.route('/bfhl', methods=['POST'])
def handle_post():
    data = request.get_json()
    print("🚀 Received:", data)
    if not data or "data" not in data:
        return jsonify({"is_success": False, "error": "Invalid request"}), 400

    numbers = [item for item in data["data"] if item.isdigit()]
    alphabets = [item for item in data["data"] if item.isalpha()]
    highest_alphabet = [max(alphabets, key=str.lower)] if alphabets else []

    return jsonify({
        "is_success": True,
        "user_id": "john_doe_17091999",
        "email": "john@xyz.com",
        "roll_number": "ABCD123",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_alphabet": highest_alphabet
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
