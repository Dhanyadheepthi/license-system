# generate_cert.py
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization, hashes
from cryptography import x509
from cryptography.x509.oid import NameOID
import datetime
import os

# Generate private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Save private key (LicenseSign.pem)
os.makedirs("certificate", exist_ok=True)
with open("certificate/LicenseSign.pem", "wb") as f:
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(b"demo")  # password protected
    ))

# Create a self-signed public certificate
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"IN"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"Maharashtra"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, u"Pune"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"MyApp"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"MyApp License Certificate"),
])

cert = x509.CertificateBuilder().subject_name(subject).issuer_name(issuer).public_key(
    private_key.public_key()
).serial_number(
    x509.random_serial_number()
).not_valid_before(
    datetime.datetime.utcnow()
).not_valid_after(
    # Valid for 10 years
    datetime.datetime.utcnow() + datetime.timedelta(days=3650)
).sign(private_key, hashes.SHA256())

# Save public certificate (LicenseVerify.pem)
with open("certificate/LicenseVerify.pem", "wb") as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))

print("Certificates generated successfully!")
