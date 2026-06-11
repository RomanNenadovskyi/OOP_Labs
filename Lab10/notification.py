class NotificationService:
    def send(self, user, message):
        pass

class UserManager:
    def __init__(self, service):
        self.service = service

    def notify_user(self, user, message):
        self.service.send(user, message)