from flask import Flask
from flask_cors import CORS 
from utils import striped_data

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/images")
def fetch_data():
    return striped_data()

if __name__ == "__main__":
    app.run(debug=True)