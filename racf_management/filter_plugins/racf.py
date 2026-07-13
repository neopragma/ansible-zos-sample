import re


def parse_listgrp(content, group_name=None):
    """
    Parse the output from RACF LISTGRP.

    Parameters
    ----------
    content : list[str]
        group_info.output[0].content

    group_name : str
        Optional. Used when LISTGRP reports "group not found".

    Returns
    -------
    dict
    """

    group = {
        "exists": True,
        "name": None,
        "attributes": {
            "owner": None,
            "superior": None,
            "installation_data": None,
            "model_dataset": None,
            "termuacc": False
        },
        "connections": []
    }

    #
    # Detect "group not found"
    #
    if any("NAME NOT FOUND IN RACF DATA SET" in line for line in content):
        group["exists"] = False
        group["name"] = group_name
        return group

    #
    # Parse remaining output
    #
    for line in content:

        line = line.rstrip()

        #
        # INFORMATION FOR GROUP DEV01
        #
        m = re.match(
            r"INFORMATION FOR GROUP\s+(\S+)",
            line
        )

        if m:
            group["name"] = m.group(1)
            continue

        #
        # SUPERIOR GROUP=SYS1 OWNER=IBMUSER
        #
        m = re.search(
            r"SUPERIOR GROUP=(\S+).*OWNER=(\S+)",
            line
        )

        if m:
            group["attributes"]["superior"] = m.group(1)
            group["attributes"]["owner"] = m.group(2)
            continue

        #
        # INSTALLATION DATA=...
        #
        m = re.search(
            r"INSTALLATION DATA=(.*)",
            line
        )

        if m:
            group["attributes"]["installation_data"] = (
                m.group(1).strip()
            )
            continue

        #
        # MODEL DATA SET=...
        #
        m = re.search(
            r"MODEL DATA SET=(.*)",
            line
        )

        if m:
            value = m.group(1).strip()

            if value.upper().startswith("NO "):
                value = None

            group["attributes"]["model_dataset"] = value
            continue

        #
        # TERMUACC
        #
        if line.strip() == "TERMUACC":
            group["attributes"]["termuacc"] = True
            continue

        #
        # NO USERS
        #
        if line.strip() == "NO USERS":
            continue

        #
        # Connected users
        #
        m = re.match(
            r"\s+([A-Z0-9@$#]+)\s+"
            r"(USE|CREATE|CONNECT|JOIN|GROUP-SPECIAL|AUDITOR|OPERATIONS)",
            line
        )

        if m:
            group["connections"].append(
                {
                    "userid": m.group(1),
                    "authority": m.group(2)
                }
            )

    return group


class FilterModule(object):

    def filters(self):

        return {
            "parse_listgrp": parse_listgrp
        }
