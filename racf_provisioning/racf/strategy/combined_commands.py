class CombinedCommandsStrategy:

    def __init__(self):
        self._users = {}

    def adduser(self, userid):

        self._users.setdefault(
            userid,
            {
                "segments": []
            }
        )

    def segment(self, userid, name, body):

        if not body:
            return

        self._users.setdefault(
            userid,
            {
                "segments": []
            }
        )

        self._users[userid]["segments"].append(
            f"{name}(" + " ".join(body) + ")"
        )

    def commands(self):

        result = []

        for userid, data in self._users.items():

            command = f"ADDUSER {userid}"

            if data["segments"]:
                command += " " + " ".join(data["segments"])

            result.append(command)

        return result
