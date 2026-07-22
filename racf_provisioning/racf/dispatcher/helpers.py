def option(keyword, value):

    if value is None:
        return None

    return f"{keyword}({value})"


def options(*values):

    return " ".join(v for v in values if v)
