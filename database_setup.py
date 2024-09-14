from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Create the SQLite database
engine = create_engine('sqlite:///concerts.db')

# Create all tables based on the models
Base.metadata.create_all(engine)

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()
