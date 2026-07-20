from ..operations import (
    EnsureOMVS,
    EnsureUser,
)


def plan(model):

    userid = model["content"]["base"]["userid"]

    operations = [
        EnsureUser(userid=userid),
    ]

    if "omvs" in model["content"]:
        omvs = model["content"]["omvs"]

        operations.append(
            EnsureOMVS(
                userid=userid,
                uid=omvs["uid"],
                home=omvs["home"],
                program=omvs["program"],
            )
        )

    return operations
