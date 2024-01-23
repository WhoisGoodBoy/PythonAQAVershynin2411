from lesson27.connection import session
from lesson27.models.users import UsersCoolFriends


class UserRepository:
    def __init__(self):
        self.sess = session


    def add_one_row(self, user):
        self.sess.add(user)
        self.sess.commit()

    def get_by_user_id(self, user_id):
        return self.sess.get(UsersCoolFriends, {'id':user_id})


users_repository = UserRepository()
user_to_add = UsersCoolFriends(id='CCCCCCCC', first_name='Gustavo', last_name='Frigman', age=52, email='gf@gmail.com')
users_repository.add_one_row(user_to_add)
hello_its_me_gustavo = users_repository.get_by_user_id('CCCCCCCC')
print(hello_its_me_gustavo)
#print(users_repository.sess.query())