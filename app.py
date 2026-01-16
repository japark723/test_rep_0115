from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Docker + Flask!"

@app.route("/about")
def about():
    return jsonify({
        "app_name": "Flask Docker App",
        "version": "1.0.0",
        "description": "A simple Flask application running in Docker",
        "endpoints": {
            "/": "Welcome message",
            "/about": "Application information"
        }
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
