import mysql.connector
from db_config import get_db_connection

def setup_database():
    # Connect without database first to create it if it doesn't exist
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="veerpratap714"
        )
        cursor = conn.cursor()
        
        # Create database
        cursor.execute("CREATE DATABASE IF NOT EXISTS login_db")
        print("Database 'login_db' checked/created.")
        
        conn.close()
        
        # Now connect to the database to create table
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Create users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) NOT NULL UNIQUE,
                password VARCHAR(255) NOT NULL
            )
        """)
        print("Table 'users' checked/created.")
        
        conn.close()
        print("Database setup complete.")
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    setup_database()
