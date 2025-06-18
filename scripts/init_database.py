import sqlite3

def init_db(db_file):
    """Initialize the SQLite database with the defined schema."""
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    # Read the schema from the SQL file
    with open('src/database/schema.sql', 'r') as schema_file:
        schema_script = schema_file.read()

    # Execute the schema script
    cursor.executescript(schema_script)

    # Commit changes and close the connection
    connection.commit()
    connection.close()

if __name__ == '__main__':
    import os
    # Create database directory if it doesn't exist
    db_dir = 'database'
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)

    # Initialize the database
    db_path = os.path.join(db_dir, 'products.db')
    print(f"Initializing database at: {db_path}")
    init_db(db_path)
    print("Database initialized successfully!")