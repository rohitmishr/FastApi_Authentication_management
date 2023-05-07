from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from pydantic import BaseModel
Base = declarative_base()



# User Model
class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True,autoincrement=True,nullable=True)
    username = Column(String, primary_key=True)
    password = Column(String, primary_key=True)
    role = Column(String, primary_key=True)
    
    def __init__(self, id:int ,username: str, password: str, role: str):
        self.id = id
        self.username = username
        self.password = password
        self.role = role
    
    def __repr__(self):
        return (
            "User(id='{self.id}',"   
            "username='{self.username}',"
            "password='{self.password}',"
            "role='{self.role}')".format(self=self)
            )
