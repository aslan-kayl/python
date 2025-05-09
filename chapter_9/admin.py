from user import User

class Privileges():
    def __init__(self, privileges='admin'):
        self.privileges = privileges

    def show_privileges(self):
        if self.privileges == 'admin':
            print(f"Список привилегий для администратора:\n {self.privileges}")
        else:
            print(f"Вы вошли как пользователь:\n {self.privileges}")


class Admin(User):
    def __init__(self, first_name, last_name, age, location, privileges):
        super().__init__(first_name, last_name, age, location)
        self.privileges = 'admin'
        f"{privileges}"

# my_admin = Admin(
#     'aslan',
#     'kayl',
#     26,
#     'amsterdam',
#     'admin')
# my_admin.describe_user()
# my_admin.greet_user()
# my_admin.increment_login_attempts()
# my_privileges = Privileges([
#             'разрешено добавлять сообщения',
#             'разрешено удалять пользователя',
#             'разрешено банить пользователя'
#         ])
# my_privileges.show_privileges()
