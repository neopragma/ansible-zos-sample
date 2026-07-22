from .helpers import option, options


def render_tso(operation, strategy):

    text = options(
        option("ACCTNUM", operation.account_number),
        option("PROC", operation.procedure),
        option("COMMAND", operation.command),
        option("DEST", operation.destination),
        option("HOLDCLASS", operation.hold_class),
        option("JOBCLASS", operation.job_class),
        option("MSGCLASS", operation.message_class),
    )

    if not text:
        return []

    return [
        strategy.altuser(
            operation.userid,
            f"TSO({text})"
        )
    ]
