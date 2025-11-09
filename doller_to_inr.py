from flask import Flask,jsonify,request
dollor_to_INR = Flask(__name__)

@doller_to_INR.route("/exchange", methods=["GET","POST"])
def price_exchange():
dollor = request.get_json()
INR = dollor * 88.64
return INR


if __name__ == "__main__":
    dollor_to_INR.run(debug=True)
