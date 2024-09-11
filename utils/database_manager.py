from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from utils.models import *

class SessionManager:
    _default_url = "sqlite:///.database.db"
    _engine = None
    _Session = None

    @classmethod
    def create_engine(cls, url=_default_url):
        """Create and configure the SQLAlchemy engine and session."""
        cls._engine = create_engine(url)
        Base.metadata.create_all(cls._engine)
        cls._Session = sessionmaker(bind=cls._engine)
        print(f"Engine created with URL: {url}")

    @classmethod
    def get_session(cls):
        """Get a new SQLAlchemy session"""
        if cls._Session is None:
            raise RuntimeError("Engine is not created. Call `create_engine` first.")
        return cls._Session()
    
    @classmethod
    def close_engine(cls):
        """Dispose of the SQLAlchemy engine."""
        if cls._engine:
            cls._engine.dispose()
            cls._engine = None
            cls._Session = None
            print("Engine disposed.")

SessionManager.create_engine()