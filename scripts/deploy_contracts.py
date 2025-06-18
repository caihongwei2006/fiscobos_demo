import json
from web3 import Web3
from solcx import compile_standard, install_solc
import os

# Install the Solidity compiler
install_solc('0.8.0')

# Connect to local Ethereum node
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

# Check if connected to the blockchain
if not w3.isConnected():
    raise Exception("Failed to connect to the blockchain")

# Load the smart contracts
def load_contracts():
    contracts = {}
    contract_files = ['ProductTrace.sol', 'SupplyChain.sol', 'AgriToken.sol']
    
    for contract_file in contract_files:
        with open(os.path.join('src', 'blockchain', 'contracts', contract_file), 'r') as file:
            contracts[contract_file] = file.read()
    
    return contracts

# Compile the smart contracts
def compile_contracts(contracts):
    compiled_contracts = {}
    
    for name, source in contracts.items():
        compiled = compile_standard({
            "language": "Solidity",
            "sources": {name: {"content": source}},
            "settings": {
                "outputSelection": {
                    "*": {
                        "*": ["*"]
                    }
                }
            }
        })
        compiled_contracts[name] = compiled['contracts'][name]
    
    return compiled_contracts

# Deploy the smart contracts
def deploy_contracts(compiled_contracts):
    contract_addresses = {}
    
    for name, contract in compiled_contracts.items():
        contract_interface = contract[list(contract.keys())[0]]
        bytecode = contract_interface['evm']['bytecode']['object']
        abi = contract_interface['abi']
        
        # Create contract instance
        contract_instance = w3.eth.contract(abi=abi, bytecode=bytecode)
        
        # Get the first account to deploy the contract
        account = w3.eth.accounts[0]
        
        # Build the transaction
        tx = contract_instance.constructor().buildTransaction({
            'from': account,
            'nonce': w3.eth.getTransactionCount(account),
            'gas': 2000000,
            'gasPrice': w3.toWei('50', 'gwei')
        })
        
        # Sign the transaction
        signed_tx = w3.eth.account.signTransaction(tx, private_key=os.getenv('PRIVATE_KEY'))
        
        # Send the transaction
        tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        
        # Wait for the transaction to be mined
        tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
        
        # Store the contract address
        contract_addresses[name] = tx_receipt.contractAddress
    
    return contract_addresses

if __name__ == "__main__":
    contracts = load_contracts()
    compiled_contracts = compile_contracts(contracts)
    addresses = deploy_contracts(compiled_contracts)
    
    # Save the deployed contract addresses to a JSON file
    with open('deployed_contracts.json', 'w') as f:
        json.dump(addresses, f, indent=4)
    
    print("Contracts deployed successfully. Addresses saved to deployed_contracts.json")