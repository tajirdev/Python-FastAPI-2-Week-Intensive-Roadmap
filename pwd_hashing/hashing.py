import bcrypt

class hash:
    @staticmethod
    def hash_password(password):
        hash_byte = password.encode("utf-8")
        salt= bcrypt.gensalt()
        hashed = bcrypt.hashpw(hash_byte,salt)
        return hashed.decode("utf-8")
        
    @staticmethod
    def verify_passwprd(plain_passwprd,hashed_password):
        plain_byte = plain_passwprd.enciode("utf-8")
        hashed_byte = hashed_password.encode("utf-8")
        return bcrypt.checkpw(plain_byte,hashed_byte)