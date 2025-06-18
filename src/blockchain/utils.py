def encode_data(data):
    # Function to encode data for blockchain transactions
    return data.encode('utf-8')

def decode_data(encoded_data):
    # Function to decode data from blockchain transactions
    return encoded_data.decode('utf-8')

def generate_hash(data):
    # Function to generate a hash for the given data
    import hashlib
    return hashlib.sha256(data.encode()).hexdigest()

def verify_signature(signature, data, public_key):
    # Function to verify a signature against the data and public key
    from cryptography.hazmat.primitives.asymmetric import rsa, padding
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.backends import default_backend

    try:
        public_key.verify(
            signature,
            data.encode(),
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        return True
    except Exception:
        return False

def sign_data(data, private_key):
    # Function to sign data with a private key
    from cryptography.hazmat.primitives.asymmetric import rsa, padding
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.backends import default_backend

    return private_key.sign(
        data.encode(),
        padding.PKCS1v15(),
        hashes.SHA256()
    )