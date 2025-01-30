from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow requests from all origins

submissions = []

@app.route('/submit', methods=['POST'])
def handle_submit():
    data = request.json
    submissions.append(data)
    print("New submission:", data)
    return jsonify({"message": "Data received successfully!"})

@app.route('/submissions', methods=['GET'])
def get_submissions():
    return jsonify({"submissions": submissions})

if __name__ == '__main__':
    app.run(debug=True)