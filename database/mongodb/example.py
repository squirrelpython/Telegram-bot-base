from pymodm import MongoModel
from pymodm.fields import CharField, BigIntegerField



class Users(MongoModel):
    username = CharField()
    user_id = BigIntegerField()
    
    class Meta:
        collection_name = 'users'
        final = True
        
    def __repr__(self):
        return "<User {} ({})>".format(self.username, self.user_id)
    
def create_user(username: str, user_id: int) -> Users:
    return Users(username, user_id).save()

def get_user(user_id: int)-> Users or None:
    return Users.objects.get({'user_id': user_id})

def delete_user(user_id: int) -> bool:
    prev = get_user(user_id)
    if prev:
        prev.delete()
        return True
    return False

