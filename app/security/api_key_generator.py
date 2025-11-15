import secrets
import base64


def generate_api_key() -> str:
    raw = secrets.token_bytes(32)
    return base64.urlsafe_b64encode(raw).decode("utf-8")
