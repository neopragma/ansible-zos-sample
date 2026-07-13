import re


def parse_listgrp(lines):
    """
    Convert RACF LISTGRP output into a dictionary.

    Input:
        list of LISTGRP output lines

    Output:
        {
          name: DEV01,
          attributes: {...},
          connections: [...]
        }
    """

    result = {
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

    for line in lines:

        line = line.rstrip()

        # Group name
        match = re.search(
            r"INFORMATION FOR GROUP\s+(\S+)",
            line
        )
        if match:
            result["name"] = match.group(1)
            continue


        # Owner / superior
        match = re.search(
            r"SUPERIOR GROUP=(\S+).*OWNER=(\S+)",
            line
        )
        if match:
            result["attributes"]["superior"] = match.group(1)
            result["attributes"]["owner"] = match.group(2)
            continue


        # Installation data
        match = re.search(
            r"INSTALLATION DATA=(.*)",
            line
        )
        if match:
            result["attributes"]["installation_data"] = (
                match.group(1).strip()
            )
            continue


        # Model dataset
        match = re.search(
            r"MODEL DATA SET=(.*)",
            line
        )
        if match:
            result["attributes"]["model_dataset"] = (
                match.group(1).strip()
            )
            continue


        if "NO MODEL DATA SET" in line:
            result["attributes"]["model_dataset"] = None

        # TERMUACC
        if line.strip() == "TERMUACC":
            result["attributes"]["termuacc"] = True

        elif line.strip() == "NO TERMUACC":
            result["attributes"]["termuacc"] = False

        if line.strip() == "NO USERS":
            result["connections"] = []
            continue

        # Users
        #
        # Example:
        #       PLAT01        USE           000000
        #
        match = re.match(
            r"\s+([A-Z0-9@$#]+)\s+(USE|CREATE|CONNECT|JOIN|GROUP-SPECIAL|AUDITOR|OPERATIONS)",
            line
        )

        if match:
            result["connections"].append(
                {
                    "userid": match.group(1),
                    "authority": match.group(2)
                }
            )


    return result



class FilterModule(object):

    def filters(self):
        return {
            "parse_listgrp": parse_listgrp
        }
