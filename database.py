#mysql -h database-1.cwfskmiwgl2c.us-east-1.rds.amazonaws.com -u admin -p
!pip install mysql-connector-python

import mysql.connector
import os

# Set environment variables for security (or replace with hardcoded values)
RDS_ENDPOINT = os.getenv("RDS_ENDPOINT", "database-1.cwfskmiwgl2c.us-east-1.rds.amazonaws.com")
RDS_USERNAME = os.getenv("RDS_USERNAME", "admin")
RDS_PASSWORD = os.getenv("RDS_PASSWORD", "7039536303")
RDS_DATABASE_NAME = os.getenv("RDS_DATABASE_NAME", "mydatabase")

try:
    # Connect to RDS
    conn = mysql.connector.connect(
        host=RDS_ENDPOINT,
        user=RDS_USERNAME,
        password=RDS_PASSWORD,
        database=RDS_DATABASE_NAME
    )
    
    print("Connected to RDS successfully!")

    # Create a table (if it doesn't exist)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100) UNIQUE
        )
    """)
    print("Table created successfully!")

    # Insert data
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", ("Alice", "alice@example.com"))
    conn.commit()

    # Fetch data
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    for row in results:
        print(row)

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("Database connection closed.")
