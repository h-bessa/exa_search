import bcrypt


def hashed_password(password: bytes):
    salt = bcrypt.gensalt(rounds=15)
    h_password = bcrypt.hashpw(password, salt)
    return h_password
