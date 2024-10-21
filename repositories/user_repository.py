class UserRepository:
    def __init__(self):
        self.user_dict = {}

    def create_user(self, name, age):
        if name in self.user_dict:
            return False  # user already exists
        self.user_dict[name] = age
        return True
    
    def get_all_users(self):
        return self.user_dict
    
    def delete_user(self, name):
        if name in self.user_dict:
            del self.user_dict[name]
            return True
        else:
            return False