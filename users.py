import datetime
import re

from deposit import Deposit


class UserNotFoundException(Exception):
    pass


class MailInvalidException(Exception):
    pass


class AgeInvalidException(Exception):
    pass


class Users(object):
    def __init__(self, users_list=None):
        self.users_list = users_list if users_list is not None else []
        self.current_id = 0

    def generate_id(self):
        self.current_id += 1
        return self.current_id

    def is_adult(self, birth_date):
        today = datetime.date.today()
        birth_date = datetime.datetime.strptime(birth_date, "%Y-%m-%d").date()
        age = today.year - birth_date.year - (
                (today.month, today.day) < (birth_date.month, birth_date.day))
        return age >= 18

    def is_valid_email(self, email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email)

    def create_user(self, username, password, email, birth_date):
        if not self.is_valid_email(email):
            raise MailInvalidException("Invalid email format")
        if not self.is_adult(birth_date):
            raise AgeInvalidException("Age requirement of 18 years old not met")

        user = {
            'id': self.generate_id(),
            'username': username,
            'password': password,
            'email': email,
            'birth_date': birth_date,
            'deposit': Deposit()
        }
        self.users_list.append(user)

    def delete_user(self, user_id):
        for user in self.users_list:
            if user['id'] == user_id:
                self.users_list.remove(user)
                return

    def edit_user(self, user_id, new_username=None, new_password=None,
                  new_email=None, new_birth_date=None):
        for user in self.users_list:
            if user['id'] == user_id:
                if new_username:
                    user['username'] = new_username
                if new_password:
                    user['password'] = new_password
                if new_email:
                    if not self.is_valid_email(new_email):
                        raise MailInvalidException("Invalid email format")
                    user['email'] = new_email
                if new_birth_date:
                    if not self.is_adult(new_birth_date):
                        raise AgeInvalidException("Age requirement of 18"
                                                  " years old not met")
                    user['birth_date'] = new_birth_date
                return
        raise UserNotFoundException(f"User with id number {user_id} not found")

    def deposit_funds(self, user_id, amount):
        for user in self.users_list:
            if user['id'] == user_id:
                user['deposit'].deposit(amount)
                break
        else:
            raise UserNotFoundException(f"User with ID {user_id} not found")

    def withdraw_funds(self, user_id, amount):
        for user in self.users_list:
            if user['id'] == user_id:
                user['deposit'].withdraw_funds(amount)
                break
        else:
            raise UserNotFoundException(f"User with ID {user_id} not found")
