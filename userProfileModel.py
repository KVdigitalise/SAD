class UserProfile:
    def __init__(self):
        pass

    def setter(self, name, dob, profile_picture, languages, bio, interest):
        self.name = name
        self.dob = dob
        self.profile_picture = profile_picture
        self.languages = languages
        self.bio = bio
        self.interest = interest

    def update_profile():
        user_Profile = UserProfile()
        user_Profile.setter(
            request.json['name'], request.json['dob'], request.json['profile_picture'], request.json['languages'], request.json['bio'], request.json['interest'])
        users = []
        users = database.child("users").get().val()
        for user in users.values():
            if(user['user_id'] == request.json["user_id"]):
                user_login_profile = user.copy()
        database.child("users").child(
            user_login_profile["user_id"]).update({'user_profile': user_Profile.__dict__})
        user_login_profile["user_profile"] = user_Profile.__dict__
        return jsonify(user_login_profile)
