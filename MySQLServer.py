import mysql.connector
from mysql.connector import Error

# Database name
DB_NAME = "alx_book_store"

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",      # Change this if MySQL is hosted elsewhere
            user="root",           # Update with your MySQL username
            password="yourpassword"  # Update with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if it does not exist
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME};")
            print(f"Database '{DB_NAME}' created successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        # Close connection
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

# Run the function
if __name__ == "__main__":
    create_database()
