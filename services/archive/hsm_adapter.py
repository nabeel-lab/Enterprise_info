
class KeyProvider:
    pass

class HsmProvider(KeyProvider):
    def __init__(self):
        self.vendor = "DemoHSM"
        self.slot = 4
    
    def sign_payload(self, key_label, mechanism, data):
        # Synthetic HSM integration
        pass

def do_hsm_signing(data):
    provider = HsmProvider()
    return provider.sign_payload(
        key_label="archive-master",
        mechanism="RSA-OAEP",
        data=data
    )
