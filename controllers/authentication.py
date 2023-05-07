from controllers.router import router
import jwt
import datetime
import hashlib
from passlib.context import CryptContext
from databases import ms
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
security = HTTPBearer()

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def generate_token(data: dict, expires_delta: datetime.timedelta):
    to_encode = data.copy()
    expire = datetime.datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_password_hash(password):
    hash_object = hashlib.sha256(password.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig

def verify_password(plain_password, hashed_password):
    # Hash the plain password using the same algorithm and salt
    plain_password_hash = get_password_hash(plain_password)
    # Compare the hashes
    return plain_password_hash == hashed_password




def authenticate_user(username: str, password: str):
    user = ms.get_user(username)
    if not user:
        return False 
    if not verify_password(password, user.password):
        return False
    return user

def create_access_token(data: dict):
    expires_delta = datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    return generate_token(data, expires_delta)
