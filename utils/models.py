from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean, DateTime, BigInteger

Base = declarative_base()

class Member(Base):
    __tablename__ = "members"

    id = Column(BigInteger, primary_key=True)
    last_message_date = Column(DateTime)
    xp = Column(Integer)

    def __repr__(self) -> str:
        return f"<Member id: {self.id}, last_message_date: {self.last_message_date}, xp: {self.xp}"
    
