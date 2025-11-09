from flask import Flask, jsonify, request

dollar_to_INR = Flask(__name__)

@dollar_to_INR.route("/exchange", methods=["GET", "POST"])
def price_exchange():
    try:
        data = request.get_json()
        dollar = data['amount']  # Extract the dollar amount from JSON
        INR = dollar * 88.64
        return jsonify({"dollar": dollar, "INR": INR})
    except (KeyError, TypeError):
        return jsonify({"error": "Please provide valid JSON with 'amount' field"}), 400

if __name__ == "__main__":
    dollar_to_INR.run(host='0.0.0.0', port=5001, debug=True)
