from ..operations import EnsureTSO


def plan(model):

    if "tso" not in model["content"]:
        return []

    userid = model["content"]["base"]["userid"]
    tso = model["content"]["tso"]

    return [
        EnsureTSO(
            userid=userid,
            acct=tso["acct"],
            proc=tso["proc"],
        )
    ]
