


def singleton(_class):
    def inner(*args):
        if not hasattr(_class, "instance"):
            setattr(_class, "instance", _class(*args))
        return getattr(_class, "instance")
    return inner




@singleton
class ConnectionExample:
    def __init__(self, credentials):
        self.credentials = credentials


first_connection = ConnectionExample('first_creds')
second_connection = ConnectionExample('second_credentials')
print(second_connection.credentials)
print()