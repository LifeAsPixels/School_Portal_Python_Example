# app.py

# 1. Import the Flask class from the flask module
from flask import Flask

# 2. Create a Flask app instance
app = Flask(__name__)

# 3. Define the homepage route
@app.route('/')
def home():
    return "Welcome to the Student Portal"

# 4. Define a second route for grades
@app.route('/grades')
def grades():
    return "Alice: 95, Bob: 87, Charlie: 78"


# 5. Run the Flask web server in debug mode
if __name__ == '__main__':
    app.run(debug=True)
