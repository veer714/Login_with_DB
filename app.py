from flask import Flask, render_template, request, jsonify
try:
    from db_config import get_db_connection
except ImportError:
    print("Database configuration not found or mysql-connector-python is missing.")
    get_db_connection = None
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

@app.route("/")
def login_page():
    return render_template("login.html")

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    username = data["username"]
    password = generate_password_hash(data["password"])

    db = get_db_connection()
    cursor = db.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            (username, password)
        )
        db.commit()
        return jsonify({"message": "User registered successfully"})
    except:
        return jsonify({"message": "Username already exists"})
    finally:
        cursor.close()
        db.close()

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data["username"]
    password = data["password"]

    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
    user = cursor.fetchone()

    cursor.close()
    db.close()

    if user and check_password_hash(user["password"], password):
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"message": "Invalid username or password"})

if __name__ == "__main__":
    app.run(debug=True)
