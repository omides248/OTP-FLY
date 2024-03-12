import base64

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class Secret:
    password = b"u_RYaWoKYrw6O9dKfMusoIef7BoQRGqw0ukgOIWQob4="
    salt = b'\xde\xd9{\x96\xaa\x88\x01\xc4\xe6N7{\x16\x96\xfc\t'
    fernet = None

    @classmethod
    def get_fernet(cls):
        if cls.fernet is None:
            # kdf = PBKDF2HMAC(
            #     algorithm=hashes.SHA256(),
            #     length=32,
            #     salt=cls.salt,
            #     iterations=480000,
            # )
            # key = base64.urlsafe_b64encode(kdf.derive(cls.password))
            # print("key", key)
            key = b'Xs1VSRbPFjc1jkNknBfLpYP21leRXoXeGcZ_flE-NtQ='
            cls.fernet = Fernet(key)
        return cls.fernet
