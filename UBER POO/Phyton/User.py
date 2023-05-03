from Account import Account

class User(Account):
def _init_(self, name, document, email, password):
    super()._init__ (name, document, email, password)
