class UserNotFoundException(Exception):
    pass


class Users(object):
    def __init__(self, users_list=[]):
        self.users_list = users_list
        self.current_id = 0

    def generate_id(self):
        self.current_id += 1
        return self.current_id

    def create_user(self, username, password, email, birth_date):
        user = {
            'id': self.generate_id(),
            'username': username,
            'password': password,
            'email': email,
            'birth_date': birth_date
        }
        self.users_list.append(user)

    def delete_user(self, user_id):
        for user in self.users_list:
            if user['id'] == user_id:
                self.users_list.remove(user)
                return

    def edit_user(self, user_id, new_username=None, new_password=None, new_email=None, new_birth_date=None):
        for user in self.users_list:
            if user['id'] == user_id:
                if new_username:
                    user['username'] = new_username
                if new_password:
                    user['password'] = new_password
                if new_email:
                    user['email'] = new_email
                if new_birth_date:
                    user['birth_date'] = new_birth_date
                return
        raise UserNotFoundException(f"User with id number {user_id} not found")
