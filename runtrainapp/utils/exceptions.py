# Authorization Exception
class AuthException(Exception):
    def __init__(self, user, message="User: %s not authorized"):
        self.user = user
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message % self.user.username


# Http Exception
class HttpException(Exception):
    def __init__(self, status_code, message="Http Exception - Status Code: %s"):
        self.status_code = status_code
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message % self.status_code
