from ..operations import EnsureUser


def plan(model):

    userid = model["content"]["base"]["userid"]

    return [
        EnsureUser(
            userid=userid,
        ),
    ]
