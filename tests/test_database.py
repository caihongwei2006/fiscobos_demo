import unittest
import sqlite3
from src.database.db_manager import connect_db, execute_query
from src.database.models import create_tables

class TestDatabase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.connection = connect_db(':memory:')  # Use in-memory database for testing
        create_tables(cls.connection)

    @classmethod
    def tearDownClass(cls):
        cls.connection.close()

    def test_insert_product(self):
        query = "INSERT INTO products (name, description, supplier_id) VALUES (?, ?, ?)"
        execute_query(self.connection, query, ('Tomato', 'Fresh tomatoes', 1))
        
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM products WHERE name = ?", ('Tomato',))
        product = cursor.fetchone()
        
        self.assertIsNotNone(product)
        self.assertEqual(product[1], 'Tomato')

    def test_retrieve_product(self):
        query = "INSERT INTO products (name, description, supplier_id) VALUES (?, ?, ?)"
        execute_query(self.connection, query, ('Cucumber', 'Organic cucumbers', 2))
        
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM products WHERE name = ?", ('Cucumber',))
        product = cursor.fetchone()
        
        self.assertIsNotNone(product)
        self.assertEqual(product[1], 'Cucumber')

    def test_update_product(self):
        query = "INSERT INTO products (name, description, supplier_id) VALUES (?, ?, ?)"
        execute_query(self.connection, query, ('Carrot', 'Crunchy carrots', 3))
        
        update_query = "UPDATE products SET description = ? WHERE name = ?"
        execute_query(self.connection, update_query, ('Fresh crunchy carrots', 'Carrot'))
        
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM products WHERE name = ?", ('Carrot',))
        product = cursor.fetchone()
        
        self.assertEqual(product[2], 'Fresh crunchy carrots')

    def test_delete_product(self):
        query = "INSERT INTO products (name, description, supplier_id) VALUES (?, ?, ?)"
        execute_query(self.connection, query, ('Lettuce', 'Crispy lettuce', 4))
        
        delete_query = "DELETE FROM products WHERE name = ?"
        execute_query(self.connection, delete_query, ('Lettuce',))
        
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM products WHERE name = ?", ('Lettuce',))
        product = cursor.fetchone()
        
        self.assertIsNone(product)

if __name__ == '__main__':
    unittest.main()