from database import Base
from sqlalchemy import Column, Integer, ForeignKey, String

class User(Base):
    __tablename__ = "user"
     
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    
    
    