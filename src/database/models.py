from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.db_manager import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'))
    transactions = relationship('Transaction', back_populates='product')

class Supplier(Base):
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact_info = Column(String)
    products = relationship('Product', back_populates='supplier')

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    timestamp = Column(String, nullable=False)
    location = Column(String)
    product = relationship('Product', back_populates='transactions')