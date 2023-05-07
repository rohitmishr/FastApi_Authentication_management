from utils import db_utils
from utils.db_utils import engine
from models.users_model import User
from sqlalchemy.orm import Session

session = Session(engine)

def user_db():
    usr = session.query(User).all()
    return usr


def get_user(username:str):
    get_usr = session.query(User).filter(User.username==username).first()
    return get_usr
    
def reg_user(username, hashed_password, role):
    new_usr = User(
        id = None,
        username=username,
        password=hashed_password,
        role=role
    )
    session.add(new_usr)
    session.commit()
    return "Successfully regiistered user....."