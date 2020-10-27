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
    def remove_friend(self):
        users = []
        users = database.child("users").get().val()
        for user in users.values():
            if((user['user_id'] == request.json["user_id_sender"]) or (user['user_id'] == request.json["user_id_receiver"])):
                connection_list = []
                for connection in user['connection']:
                    if((connection['user_id_sender'] == request.json["user_id_sender"]) and (connection['user_id_receiver'] == request.json["user_id_receiver"])):
                        connection['status'] = -1
                        connection_list.append(connection)
                    else:
                        connection_list.append(connection)
                database.child("users").child(user["user_id"]).update(
                    {"connection": connection_list})
        return 'Connection Rejected Successfully'
