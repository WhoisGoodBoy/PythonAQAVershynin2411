from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("postgresql://postgres:postgres@localhost:9999/postgres")
__session = sessionmaker(engine)
session = __session()