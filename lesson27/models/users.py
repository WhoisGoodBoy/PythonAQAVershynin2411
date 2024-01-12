from sqlalchemy.orm import declarative_base
from sqlalchemy import VARCHAR, INTEGER, Column


Base = declarative_base()


class UsersCoolFriends(Base):
    __tablename__ = 'usertablecoolfriends'
    id = Column(VARCHAR(8), primary_key=True)
    first_name = Column(VARCHAR(25))
    last_name = Column(VARCHAR(25))
    age = Column(INTEGER)
    email = Column(VARCHAR(50))

    def __str__(self):
        return f'id:{self.id}, first_name:{self.first_name}, last_name:{self.last_name}, age:{self.age}, email:{self.email}'
