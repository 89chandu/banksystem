import json 
class Auth:

    FILE_NAME = "users.json"

    @staticmethod
    def login(username,password):

        with open(Auth.FILE_NAME,"r") as file:

            users = json.load(file)

            for user in users:

                if (
                    user["username"] == username
                    and
                    user["password"] == password
                ):
                    return True
        return False            