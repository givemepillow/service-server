import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey


class Cryptographer:
    private_key: RSAPrivateKey

    @classmethod
    def generate_key(cls):
        cls.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048 * 2,
            backend=default_backend()
        )

    @classmethod
    def decrypt(cls, data):
        return cls.private_key.decrypt(
            base64.b64encode(data),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

    @classmethod
    def get_public_key(cls):
        public_key = cls.private_key.public_key()
        return base64.b64encode(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))
