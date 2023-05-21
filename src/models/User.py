class User:
    def __init__(self, id, name, password, mail):
        self.id = id
        self.name = name
        self.password = password
        self.mail = mail

    def __str__(self):
        return f"ID: {self.id}\nName: {self.name}\nPassword: {self.password}\nMail: {self.mail}"