# Blockchain-Based Agricultural Product Traceability System

This project implements a blockchain-based agricultural product traceability system using the Fiscobos framework and a local SQLite relational database. The system allows users to trace agricultural products from farm to table, ensuring transparency and authenticity in the supply chain.

## Project Structure

```
fiscobos_demo
├── src
│   ├── blockchain
│   │   ├── contracts
│   │   │   ├── ProductTrace.sol
│   │   │   ├── SupplyChain.sol
│   │   │   └── AgriToken.sol
│   │   ├── fiscobos_client.py
│   │   └── utils.py
│   ├── database
│   │   ├── models.py
│   │   ├── schema.sql
│   │   └── db_manager.py
│   ├── api
│   │   ├── routes.py
│   │   ├── controllers.py
│   │   └── validators.py
│   ├── frontend
│   │   ├── static
│   │   │   ├── css
│   │   │   │   └── main.css
│   │   │   └── js
│   │   │       └── app.js
│   │   └── templates
│   │       ├── index.html
│   │       ├── trace.html
│   │       └── product.html
│   └── main.py
├── config
│   ├── fiscobos_config.toml
│   ├── node_config.json
│   └── app_config.py
├── tests
│   ├── test_blockchain.py
│   ├── test_database.py
│   └── test_api.py
├── scripts
│   ├── deploy_contracts.py
│   └── init_database.py
├── requirements.txt
└── README.md
```

## Features

- **Product Traceability**: Users can track the journey of agricultural products through the supply chain.
- **Smart Contracts**: Utilizes Ethereum-based smart contracts for secure and transparent transactions.
- **SQLite Database**: A local SQLite database is used to store product, supplier, and transaction information.
- **API Integration**: RESTful API endpoints for interacting with the system.
- **Frontend Interface**: A user-friendly web interface for displaying product information and traceability.

## Setup Instructions

1. **Clone the Repository**:
   ```
   git clone <repository-url>
   cd fiscobos_demo
   ```

2. **Install Dependencies**:
   Ensure you have Python and pip installed, then run:
   ```
   pip install -r requirements.txt
   ```

3. **Initialize the Database**:
   Run the following script to set up the SQLite database:
   ```
   python scripts/init_database.py
   ```

4. **Deploy Smart Contracts**:
   Deploy the smart contracts to the blockchain using:
   ```
   python scripts/deploy_contracts.py
   ```

5. **Run the Application**:
   Start the Flask application:
   ```
   python src/main.py
   ```

6. **Access the Application**:
   Open your web browser and go to `http://localhost:5000` to access the application.

## Usage

- Use the web interface to add new products, view traceability information, and manage suppliers.
- The API can be accessed for programmatic interactions with the system.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.