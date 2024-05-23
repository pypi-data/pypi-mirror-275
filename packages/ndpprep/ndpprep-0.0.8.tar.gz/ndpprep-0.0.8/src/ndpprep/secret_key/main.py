def read_secret_key(secret_path):
    with open(secret_path, "rb") as f:
        secret_key = f.read()
    return secret_key