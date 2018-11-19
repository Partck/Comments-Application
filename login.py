
from register import data


class Login(object):
    def __init__(self):
        self.db = data
    def login(self, username, password):
        for user in self.db:
            if user["username"] != username:
                    return False
            if user["password"] != password:
                    return False
        return True
        




