from users import Users

if __name__ == "__main__":
    print("Hello, this is a user account and balance management system")
    user = Users()
    user.create_user("joe","2014","2013@email.com","2001-03-10")
    user.edit_user(1,"new joe")
    user.deposit_funds(1,100)
    print("User budget:",user.users_list[0]['deposit'].budget)