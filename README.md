# Flask Login Application with Database

This project is a simple Flask application that demonstrates how to implement user authentication using a database.

## Features
- User registration
- User login
- Password hashing
- Session management
- Database integration with SQLite

## Requirements
- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Werkzeug

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/veer714/Login_with_DB.git
   cd Login_with_DB
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Set up the database:
   ```bash
   python create_db.py
   ```
2. Run the Flask application:
   ```bash
   python app.py
   ```
3. Open your web browser and visit `http://127.0.0.1:5000`.

## API Endpoints
- **POST /register**: Register a new user.
- **POST /login**: Log in an existing user.
- **GET /logout**: Log out the current user.

## Database Schema
- **users** table:
  - id (integer, primary key)
  - username (string, unique)
  - password_hash (string)

## Contributing
Contributions are welcome! Please submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License.