import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class DatabaseManager:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        """Establishes a connection to the database."""
        try:
            if self.connection is None or self.connection.closed:
                self.connection = psycopg2.connect(
                    dbname=os.getenv("DB_NAME"),
                    user=os.getenv("DB_USER"),
                    password=os.getenv("DB_PASSWORD"),
                    host=os.getenv("DB_HOST", "localhost"),
                    port=os.getenv("DB_PORT", "5432")
                )
                self.cursor = self.connection.cursor()
                print("Database connection successful.")
        except psycopg2.OperationalError as e:
            print(f"Connection error: {e}")
        except Exception as e:
            print(f"Unexpected error while connecting: {e}")

    def execute_query(self, query, values=None, fetch=False):
        """Executes a SQL query and optionally fetches results."""
        try:
            # Ensure connection is established
            self.connect()

            self.cursor.execute(query, values)
            self.connection.commit()
            print("Query executed successfully.")

            # Fetch results if required
            if fetch:
                return self.cursor.fetchall()
        except psycopg2.DatabaseError as e:
            print(f"Database error: {e}")
            self.connection.rollback()
        except Exception as e:
            print(f"Error executing query: {e}")
        return []

    def close(self):
        """Closes the database connection."""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print("Database connection closed.")
