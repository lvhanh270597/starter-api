import pickle, configparser
from flask import Flask
from flask import request, jsonify

configFile = "./config/config.ini"
config = configparser.ConfigParser()
config.read(configFile)
    
class Servicer:

    def __init__(self):
        self.load_data()
    
    def load_data(self):
        self.corrector = pickle.load(
            open(config["MODELS"]["correctModel"], "rb")
        )

    def process(self, text):
        testcase = [text]
        sentences = self.corrector.predict(testcase)[0]
        return {
            "raw_text" : text,
            "output" : sentences
        }

servicer = Servicer()
app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def process():
    if request.method == "POST":
        text = request.form.get('text')
        data = servicer.process(text)
        print(data)
        return jsonify(isError=False, message="Success", statusCode=200, data=data), 200

if __name__ == '__main__':
    app.run(host=config["SERVICE"]["server"], port=int(config["SERVICE"]["port"]))