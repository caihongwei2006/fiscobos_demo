from flask import Blueprint, request, jsonify
from .controllers import ProductController
from ..blockchain.fiscobos_client import FiscobosClient
from ..database.db_manager import DatabaseManager
import json

# initialize blockchain client and database manager
with open('config/node_config.json') as f:
    node_cfg = json.load(f)

client = FiscobosClient(node_cfg['rpc_endpoint'], node_cfg['contract_addresses'])
db = DatabaseManager('database/products.db')

api = Blueprint('api', __name__)

@api.route('/products', methods=['POST'])
def create_product():
    data = request.json
    product = ProductController.create_product(data)
    return jsonify(product), 201

@api.route('/products/<product_id>', methods=['GET'])
def get_product(product_id):
    product = ProductController.get_product(product_id)
    if product:
        return jsonify(product), 200
    return jsonify({'error': 'Product not found'}), 404

@api.route('/products/<product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.json
    updated_product = ProductController.update_product(product_id, data)
    if updated_product:
        return jsonify(updated_product), 200
    return jsonify({'error': 'Product not found or update failed'}), 404

@api.route('/products/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    success = ProductController.delete_product(product_id)
    if success:
        return jsonify({'message': 'Product deleted successfully'}), 204
    return jsonify({'error': 'Product not found or delete failed'}), 404

@api.route('/products/trace/<product_id>', methods=['GET'])
def trace_product(product_id):
    trace_info = ProductController.trace_product(product_id)
    if trace_info:
        return jsonify(trace_info), 200
    return jsonify({'error': 'Trace information not found'}), 404

@api.route('/transactions', methods=['POST'])
def register_transaction():
    data = request.json or {}
    buyer = data.get('buyer')
    seller = data.get('seller')
    product = data.get('product')

    if not all([buyer, seller, product]):
        return jsonify({'error': 'buyer, seller and product are required'}), 400

    try:
        tx_hash = client.send_transaction('SupplyChain', 'registerTransaction', buyer, seller, product)
    except Exception:
        tx_hash = None

    db.add_trade_record(buyer, seller, product, tx_hash)
    return jsonify({'tx_hash': tx_hash}), 201

