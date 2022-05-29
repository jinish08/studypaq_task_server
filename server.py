from flask import Flask,request
from flask_cors import CORS 
from utils import striped_data
from utils import verify_user
import _json

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/images",methods=["POST"])
def fetch_data():
    data = request.json
    # print(data)

    user_verfied = verify_user(data)
    # print(user_verfied)

    if user_verfied:
        return striped_data()  

    content = {'message': 'Invalid credentials'}
    return content, 208

if __name__ == "__main__":
    app.run(debug=True)