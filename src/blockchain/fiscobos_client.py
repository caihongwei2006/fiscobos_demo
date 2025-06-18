from web3 import Web3
import json

class FiscobosClient:
    def __init__(self, node_url, contract_addresses):
        self.web3 = Web3(Web3.HTTPProvider(node_url))
        self.contracts = {}
        self.load_contracts(contract_addresses)

    def load_contracts(self, contract_addresses):
        for name, address in contract_addresses.items():
            with open(f'src/blockchain/contracts/{name}.json') as f:
                contract_abi = json.load(f)['abi']
                self.contracts[name] = self.web3.eth.contract(address=address, abi=contract_abi)

    def deploy_contract(self, contract_name, deployer_account):
        # Logic for deploying a contract
        pass

    def send_transaction(self, contract_name, function_name, *args):
        contract = self.contracts[contract_name]
        tx = contract.functions[function_name](*args).buildTransaction({
            'from': self.web3.eth.defaultAccount,
            'nonce': self.web3.eth.getTransactionCount(self.web3.eth.defaultAccount),
            'gas': 2000000,
            'gasPrice': self.web3.toWei('50', 'gwei')
        })
        signed_tx = self.web3.eth.account.signTransaction(tx, private_key='YOUR_PRIVATE_KEY')
        tx_hash = self.web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        return tx_hash

    def get_event_logs(self, contract_name, event_name, from_block=0, to_block='latest'):
        contract = self.contracts[contract_name]
        event_filter = contract.events[event_name].createFilter(fromBlock=from_block, toBlock=to_block)
        return event_filter.get_all_entries()