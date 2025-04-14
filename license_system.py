# license_system.py
import json
from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

class License:
    def __init__(self, feature1=False, feature2=False, feature3=False):
        self.feature1 = feature1
        self.feature2 = feature2
        self.feature3 = feature3

    def to_json(self):
        return json.dumps(self.__dict__)

    @staticmethod
    def from_json(data):
        return License(**json.loads(data))


def sign_license(license_data, private_key_path, password):
    with open(private_key_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(), password=password.encode()
        )
    signature = private_key.sign(
        license_data.encode(),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature.hex()


def verify_license(license_data, signature, public_key_path):
    with open(public_key_path, "rb") as key_file:
        public_key = x509.load_pem_x509_certificate(key_file.read()).public_key()
    try:
        public_key.verify(
            bytes.fromhex(signature),
            license_data.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except:
        return False


def save_license_file(license_obj, signature, path="license.json"):
    data = {
        "license": license_obj.to_json(),
        "signature": signature
    }
    with open(path, "w") as f:
        json.dump(data, f)


def load_and_verify_license(public_key_path="certificate/LicenseVerify.pem"):
    try:
        with open("license.json", "r") as f:
            data = json.load(f)
            license_data = data["license"]
            signature = data["signature"]
            if verify_license(license_data, signature, public_key_path):
                return License.from_json(license_data)
    except:
        return None
    return None
