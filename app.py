from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask app!"})

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')
    if num1 is None or num2 is None:
        return jsonify({"error": "Please provide num1 and num2"}), 400
    result = num1 + num2
    return jsonify({"result": result})

@app.route('/subtract', methods=['POST'])
def subtract():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')
    if num1 is None or num2 is None:
        return jsonify({"error": "Please provide num1 and num2"}), 400
    result = num1 - num2
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
