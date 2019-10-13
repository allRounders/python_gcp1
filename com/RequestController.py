from flask import Flask, jsonify, request
from com.spacy_nlp import find_data

app = Flask(__name__)


@app.route("/pythonservice", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        input_value = request.get_json()
        response = find_data(str(input_value))
        return jsonify({"result": response})
    else:
        return jsonify({"result": "Hello Kundan!!"})


if __name__ == '__main__':
    app.run(port='8081', debug="true")
