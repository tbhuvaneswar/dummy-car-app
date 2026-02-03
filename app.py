from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.get("/")
def root():
    return jsonify({
        "service": "dummy-car",
        "env": os.getenv("APP_ENV", "unknown"),
        "db_host": os.getenv("DB_HOST", "not-set"),
        "db_name": os.getenv("DB_NAME", "not-set"),
    })

@app.get("/health")
def health():
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
