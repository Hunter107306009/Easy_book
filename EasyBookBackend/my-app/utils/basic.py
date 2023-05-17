def sha_256(pwd: str) -> str:
    """
    雜湊演算法.
    """
    import hashlib

    sha256 = hashlib.sha256()
    sha256.update(pwd.encode("utf-8"))
    return sha256.hexdigest()
