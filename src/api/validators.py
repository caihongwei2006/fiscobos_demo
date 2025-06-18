from flask import request, jsonify
from marshmallow import Schema, fields, validate, ValidationError

class ProductSchema(Schema):
    product_id = fields.String(required=True, validate=validate.Length(min=1))
    name = fields.String(required=True, validate=validate.Length(min=1))
    description = fields.String(required=True, validate=validate.Length(min=1))
    supplier_id = fields.String(required=True, validate=validate.Length(min=1))
    location = fields.String(required=True, validate=validate.Length(min=1))
    timestamp = fields.DateTime(required=True)

class SupplierSchema(Schema):
    supplier_id = fields.String(required=True, validate=validate.Length(min=1))
    name = fields.String(required=True, validate=validate.Length(min=1))
    contact_info = fields.String(required=True, validate=validate.Length(min=1))

def validate_product(data):
    schema = ProductSchema()
    try:
        schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400

def validate_supplier(data):
    schema = SupplierSchema()
    try:
        schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400