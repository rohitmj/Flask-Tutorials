from flask import Flask

app = Flask(__name__)

# Home Route: Returns a simple "Hello, World!" message.

@app.route("/")
def home():
    return "Hello, World!"

# Greeting route: returns a personalized greeting.
# For example, accessing/ greet/ Alice will return "Hello, Alice!"

@app.route("/greet/<name>")
def greet(name):
    return f"Hello, {name.capitalize()}!"

if __name__ == "__main__":
    app.run(debug=True)
