from sqlalchemy import Column, BigInteger, UnicodeText
from database.postgresql import BASE, SESSION


class Users(BASE):
    __tablename__ = "users"
    username = Column(UnicodeText)
    user_id = Column(BigInteger, primary_key=True)

    def __init__(self, user_id, username=None):
        self.user_id = user_id
        self.username = username

    def __repr__(self):
        return "<User {} ({})>".format(self.username, self.user_id)
    
Users.__table__.create(checkfirst=True)


def create(user_id, username):
    user = Users(user_id, username)
    SESSION.add(user)
    SESSION.commit()
    
def get_user(user_id: int) -> Users or None:
    try:
        return SESSION.query(Users).get(Users.user_id == int(user_id)).first()
    finally:
        SESSION.close()

def del_user(user_id):
    curr = SESSION.query(Users).get(user_id)
    if curr:
        SESSION.delete(curr)
        SESSION.commit()
        return True
    return False
