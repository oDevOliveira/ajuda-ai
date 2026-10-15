import os

BASE_DIR=os.path.dirname(os.path.abspath(__file__))

class Config:
    SECRET_KEY=os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI="sqlite:///ajuda_ai.db"
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    