from flask import Flask
import animal_dictionary

app = Flask(__name__)


@app.route("/getAnimalList", methods=["GET"])
def getAnimalList():
    _dictionary = animal_dictionary.AnimalDictionary()

    return _dictionary.get_html()

def start_routing():
    app.run(debug=False, port=3380)
