import unittest
from src.api.routes import app

class ApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_product_trace(self):
        response = self.app.get('/api/product/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Product Trace', response.data)

    def test_create_product(self):
        response = self.app.post('/api/product', json={
            'name': 'Tomato',
            'supplier_id': 1,
            'location': 'Farm A',
            'timestamp': '2023-10-01T12:00:00Z'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Product created', response.data)

    def test_update_product(self):
        response = self.app.put('/api/product/1', json={
            'location': 'Warehouse B'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Product updated', response.data)

    def test_delete_product(self):
        response = self.app.delete('/api/product/1')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()