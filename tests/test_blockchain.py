import unittest
from src.blockchain.fiscobos_client import FiscobosClient
from src.database.db_manager import DBManager

class TestBlockchain(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = FiscobosClient()
        cls.db_manager = DBManager()
        cls.db_manager.connect()

    @classmethod
    def tearDownClass(cls):
        cls.db_manager.close()

    def test_deploy_product_trace_contract(self):
        contract_address = self.client.deploy_product_trace_contract()
        self.assertIsNotNone(contract_address, "Contract address should not be None")

    def test_add_product_trace(self):
        product_id = "12345"
        trace_info = {"location": "Farm A", "timestamp": "2023-10-01"}
        result = self.client.add_product_trace(product_id, trace_info)
        self.assertTrue(result, "Failed to add product trace")

    def test_get_product_trace(self):
        product_id = "12345"
        trace = self.client.get_product_trace(product_id)
        self.assertIsNotNone(trace, "Trace should not be None")
        self.assertEqual(trace['location'], "Farm A", "Location should match")

    def test_supply_chain_management(self):
        supplier_id = "supplier_1"
        result = self.client.add_supplier(supplier_id)
        self.assertTrue(result, "Failed to add supplier")

        product_id = "12345"
        result = self.client.track_product_movement(product_id, supplier_id)
        self.assertTrue(result, "Failed to track product movement")

if __name__ == '__main__':
    unittest.main()