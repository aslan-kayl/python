from admin import Privileges, Admin

my_admin = Admin(
    'aslan',
    'kayl',
    9,
    'texas',
    'admin'
)
my_admin.describe_user()
my_privileges = Privileges([
            'разрешено добавлять сообщения',
            'разрешено удалять пользователя',
            'разрешено банить пользователя',
])
my_privileges.show_privileges()
