import sqlite3
from sqlite3 import Error

class DatabaseManager:
    def __init__(self, db_file):
        """Initialize the database manager with the database file."""
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)
        return conn

    def execute_query(self, query, params=()):
        """Execute a single query."""
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
            return cursor.lastrowid
        except Error as e:
            print(e)

    def fetch_all(self, query, params=()):
        """Fetch all results from a query."""
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()

    def add_trade_record(self, buyer, seller, product, tx_hash=None):
        """Insert a trade record into the database."""
        query = (
            "INSERT INTO trade_records (buyer, seller, product, tx_hash) VALUES (?, ?, ?, ?)"
        )
        return self.execute_query(query, (buyer, seller, product, tx_hash))
