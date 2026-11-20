from flask import Flask, send_from_directory
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
app = Flask(__name__, static_folder="static")

@app.route("/")
def home():
    return send_from_directory(app.static_folder, "index.html")

if __name__ == "__main__":
    print("Website đang chạy tại http://127.0.0.1:5000")
    app.run(debug=True, host="127.0.0.1", port=5000)
