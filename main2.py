# user.py
class User:
    def __init__(self, email, name, password, profession):
        self.email = email
        self.name = name
        self.password = password
        self.profession = profession

    def get_user_info(self):
        print("Email:", self.email)
        print("Name:", self.name)
        print("Profession:", self.profession)
