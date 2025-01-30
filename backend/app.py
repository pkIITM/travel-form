from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# In-memory storage for form submissions
submissions = []

# Route to handle form submissions
@app.route('/submit', methods=['POST'])
def submit_form():
    # Get JSON data from the request
    data = request.get_json()

    # Log the received data to the console (for debugging)
    print("Received data:", data)

    # Store the data in the submissions list
    submissions.append(data)

    # Send a success response back to the front-end
    return jsonify({
        "message": "Form submitted successfully!",
        "received_data": data  # Optional: Send the received data back
    })

# Route to view all submissions (optional, for debugging)
@app.route('/submissions', methods=['GET'])
def view_submissions():
    return jsonify({
        "submissions": submissions
    })

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)