class UserException (Exception):
    def __init__(self , status,message):
        self.status_code = status
        self.message = message
        super().__init__(message)