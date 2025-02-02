import mysql.connector
from mysql.connector import Error

# Database name
DB_NAME = "alx_book_store"

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",      # Change if MySQL is hosted elsewhere
            user="root",           # Update with your MySQL username
            password="yourpassword"  # Update with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Explicitly create database if it does not exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:  # Explicitly catching mysql.connector.Error
        print(f"Error: {e}")

    finally:
        # Ensure the database connection is closed
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

# Run the function
if __name__ == "__main__":
    create_database()
