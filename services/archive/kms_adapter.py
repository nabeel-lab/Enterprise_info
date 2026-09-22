
import boto3

def handle_archive(data):
    # Call AWS KMS to get the data key
    kms = boto3.client('kms')
    response = kms.generate_data_key(
        KeyId='alias/carevault-archive',
        KeySpec='AES_256'
    )
    
    # Encrypt explicitly
    enc_response = kms.encrypt(
        KeyId="alias/carevault-archive",
        Plaintext=data
    )
    return "archived"
