class User:
    def __init__(self, id, name, access_level='user'):
        self.__id = id
        self.__name = name
        self.__access_level = access_level

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    def set_access_level(self, access_level):
        self.__access_level = access_level

class Admin(User):
    def __init__(self, id, name):
        super().__init__(id, name, 'admin')
        self.__users = []

    def add_user(self, user):
        if not isinstance(user, User):
            raise ValueError("Can only add instances of User class")
        self.__users.append(user)
        # проверяется, является ли переданный объект user экземпляром класса User. Если это не так,
        # то выбрасывается исключение ValueError с сообщением "Can only add instances of User class".
        # Если же переданный объект является экземпляром класса User, то он добавляется в список __users класса Admin.

    def remove_user(self, user):
        if user in self.__users:
            self.__users.remove(user)
        else:
            raise ValueError("User not found in the system")

    def get_users(self):
        return self.__users


# Создание обычных пользователей
user1 = User(1, 'John Doe')
user2 = User(2, 'Jane Doe')
user3 = User(3, 'Alex Doe')

# Создание администратора
admin = Admin(4, 'Admin User')

# Добавление пользователей в систему
admin.add_user(user1)
admin.add_user(user2)
admin.add_user(user3)

# Удаление пользователя из системы
admin.remove_user(user1)

# Получение списка всех пользователей
print([user.get_name() for user in admin.get_users()])

# Получение уровня доступа пользователя
print(user2.get_access_level())

# Изменение уровня доступа пользователя
user2.set_access_level('admin')
print(user2.get_access_level())
