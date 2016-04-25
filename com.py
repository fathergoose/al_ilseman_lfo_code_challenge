from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/customer_scoring")
def score_customer():
    params = request.args.items()
    for key, val in params:
        print(key)
        print(val)
    response = {"propensity": "0.26532", "ranking": "C"}
    return jsonify(response)

if __name__ == "__main__":
    app.run(host='not_real.com', port=4567, debug=True)

