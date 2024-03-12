from datetime import datetime

import pyotp

from lib.otp.config import OTPConfig


class OTP:

    @classmethod
    def otp_verify(cls, secret_key: str) -> any:
        try:
            otp = pyotp.TOTP(secret_key, interval=OTPConfig.timeout)
            otp.verify(secret_key)
            return otp, False
        except Exception as e:
            return e, True

    @classmethod
    def get_code(cls, opt: any) -> str:
        return opt.now()

    @classmethod
    def get_expire(cls, otp: any) -> int:
        return int(otp.interval - datetime.now().timestamp() % otp.interval)
