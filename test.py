class User:
    def __init__(self, username, password, active=True):
        self.username = username
        self.password = password
        self.active = active

class UserService:
    def __init__(self):
        self.users = []

    def create_user(self, username, password, active=True):
        user = User(username, password, active)
        self.users.append(user)
        return user

    def get_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None

    def update_user(self, username, password=None, active=None):
        user = self.get_user(username)
        if user:
            if password:
                user.password = password
            if active is not None:
                user.active = active
            return user
        return None

    def delete_user(self, username):
        user = self.get_user(username)
        if user:
            self.users.remove(user)
            return True
        return False

    def list_users(self):
        return self.users

# Example usage
service = UserService()

# Create a user
service.create_user("john_doe", "password123")

# Read user
user = service.get_user("john_doe")
print(user.username, user.password, user.active)

# Update user
service.update_user("john_doe", password="new_password")

# List users
for user in service.list_users():
    print(user.username, user.password, user.active)

# Delete user
service.delete_user("john_doe")
