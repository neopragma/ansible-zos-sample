from .helpers import option, options


def render_omvs(operation, strategy):

    text = options(
        option("UID", operation.uid),
        option("HOME", operation.home),
        option("PROGRAM", operation.program),
        option("CPUTIMEMAX", operation.cpu_time_max),
        option("ASSIZEMAX", operation.assize_max),
        option("FILEPROCMAX", operation.fileproc_max),
    )

    return [
        strategy.altuser(
            operation.userid,
            f"OMVS({text})"
        )
    ]
