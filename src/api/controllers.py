from flask import request, jsonify
from ..database.db_manager import get_product, create_product, update_product
from ..api.validators import validate_product_data

def add_product():
    data = request.json
    if not validate_product_data(data):
        return jsonify({"error": "Invalid data"}), 400
    product_id = create_product(data)
    return jsonify({"product_id": product_id}), 201

def get_product_info(product_id):
    product = get_product(product_id)
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product), 200

def update_product_info(product_id):
    data = request.json
    if not validate_product_data(data):
        return jsonify({"error": "Invalid data"}), 400
    updated = update_product(product_id, data)
    if not updated:
        return jsonify({"error": "Product not found"}), 404
    return jsonify({"message": "Product updated successfully"}), 200