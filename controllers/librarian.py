from controllers.router import router
from services import user_service
from fastapi import Depends
from controllers.authentication import SECRET_KEY,ALGORITHM
from fastapi import Depends, HTTPException, status
import jwt
from controllers.router import router
from controllers.authentication import authenticate_user, create_access_token, get_password_hash,security
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials




@router.get("/api/v1/get_user",tags=["LMS"])
def get_user(auth: HTTPAuthorizationCredentials = Depends(security)):
    try:
        payload = jwt.decode(auth.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        user_s = user_service.get_user_data()
        return {"data":user_s}
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

