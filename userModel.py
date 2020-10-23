from userProfileModel import UserProfile


class User:
    def __init__(self, email_id, user_id, name, last_login, user_profile, connection):
        self.email_id = email_id
        self.user_id = user_id
        self.name = name
        self.last_login = last_login
        self.login_status = False
        self.user_profile = user_profile
        self.connection = connection
