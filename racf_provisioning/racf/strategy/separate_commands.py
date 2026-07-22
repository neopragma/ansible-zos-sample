class SeparateCommandsStrategy:

    def __init__(self):
        self._commands = []

    def adduser(self, userid):
        self._commands.append(f"ADDUSER {userid}")

    def segment(self, userid, name, body):

        if not body:
            return

        self._commands.append(
            f"ALTUSER {userid} {name}(" +
            " ".join(body) +
            ")"
        )

    def commands(self):
        return self._commands
