import yaml


def load_yaml(filename):
    with open(filename, "r", encoding="utf-8") as infile:
        return yaml.safe_load(infile)


def extract_profile(document):
    """
    Extract the single RACF profile from a YAML document.

    Expected format:

        racf_user:
            ...

    Returns the inner object.
    """

    if not isinstance(document, dict):
        raise ValueError("Profile document must contain a YAML mapping.")

    if len(document) != 1:
        raise ValueError(
            "Profile document must contain exactly one top-level object."
        )

    wrapper_name, payload = next(iter(document.items()))

    if wrapper_name != "racf_user":
        raise ValueError(
            f"Unsupported profile type '{wrapper_name}'."
        )

    return payload
