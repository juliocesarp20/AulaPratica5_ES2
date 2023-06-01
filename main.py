from users import Users

if __name__ == "__main__":
    print("Hello, this is a user management system")
    user = Users()
    user.create_user("joe","2014","2013@email.com","2014-03-10")
    user.edit_user(1,"new joe")
    print(user.users_list[0])