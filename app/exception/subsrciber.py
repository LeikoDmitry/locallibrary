class SubscriberFoundException(Exception):
    def __init__(self, message="Subscriber already exist!"):
        super().__init__(message)
