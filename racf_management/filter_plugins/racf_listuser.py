# filter_plugins/racf_listuser.py
import re

def racf_listuser_content_to_obj(lines):
    if not lines:
        return {"user": {}, "connects": []}

    # Normalize: ensure strings, strip right side only
    lines = [str(x).rstrip("\n") for x in lines]

    def m(pattern, text, group=1, default=None):
        mm = re.search(pattern, text)
        return mm.group(group) if mm else default

    user = {
        "userid": m(r"\bUSER=([^\s]+)", " ".join(lines)),
        "name": m(r"\bNAME=([^\s]+)", " ".join(lines)),
        "owner": m(r"\bOWNER=([^\s]+)", " ".join(lines)),
        "created": m(r"\bCREATED=([0-9.]+)", " ".join(lines)),
        "default_group": m(r"\bDEFAULT-GROUP=([^\s]+)", " ".join(lines)),
        "security_level": m(r"\bSECURITY-LEVEL=([^\s]+)\s+SPECIFIED", "\n".join(lines)),
        "security_label": m(r"\bSECURITY-LABEL=([^\s]+)\s+SPECIFIED", "\n".join(lines)),
        "category_authorization": None,
    }

    # Collect all "ATTRIBUTES=..." lines
    attributes = []
    for ln in lines:
        if "ATTRIBUTES=" in ln:
            # could be: ATTRIBUTES=SPECIAL OPERATIONS
            val = ln.split("ATTRIBUTES=", 1)[1].strip()
            if val:
                attributes.append(val)
    if attributes:
        user["attributes"] = attributes

    # Capture some logon/revoke/resume/last-access-ish fields when present
    user["revoke_date"] = None
    user["resume_date"] = None
    for ln in lines:
        if "REVOKE DATE=" in ln:
            user["revoke_date"] = m(r"REVOKE DATE=([^\s]+)", ln) or user["revoke_date"]
        if "RESUME DATE=" in ln:
            user["resume_date"] = m(r"RESUME DATE=([^\s]+)", ln) or user["resume_date"]
        if "LAST-ACCESS=" in ln:
            user["last_access"] = m(r"LAST-ACCESS=([0-9./]+/[0-9:]+)", ln) or m(r"LAST-ACCESS=([^\s]+)", ln)
        if "LOGON ALLOWED" in ln:
            user["logon_allowed_header"] = ln.strip()
        if re.search(r"\bGROUP=\S+\s+AUTH=\S+.*CONNECT-OWNER=\S+\s+CONNECT-DATE=\S+", ln):
            # connections handled below
            pass

    connects = []

    # Parse connection blocks:
    # Example block header line:
    #   "  GROUP=SYS1      AUTH=JOIN     CONNECT-OWNER=IBMUSER   CONNECT-DATE=21.243"
    #
    # Next indented line:
    #   "    CONNECTS=30,321  UACC=READ     LAST-CONNECT=26.196/05:32:11"
    #
    conn_header_re = re.compile(
        r"\bGROUP=([^\s]+)\s+AUTH=([^\s]+).*?CONNECT-OWNER=([^\s]+)\s+CONNECT-DATE=([0-9.]+)",
        re.IGNORECASE
    )
    conn_counts_re = re.compile(
        r"\bCONNECTS=([^\s]+)\s+UACC=([^\s]+).*?LAST-CONNECT=([^\s]+)",
        re.IGNORECASE
    )

    pending = None
    for ln in lines:
        ln_stripped = ln.strip()

        mh = conn_header_re.search(ln_stripped)
        if mh:
            # start a new connection entry
            pending = {
                "group": mh.group(1),
                "auth": mh.group(2),
                "connect_owner": mh.group(3),
                "connect_date": mh.group(4),
                "connects": None,
                "uacc": None,
                "last_connect": None,
            }
            connects.append(pending)
            continue

        if pending is not None:
            mc = conn_counts_re.search(ln_stripped)
            if mc:
                pending["connects"] = mc.group(1)
                pending["uacc"] = mc.group(2)
                pending["last_connect"] = mc.group(3)
                # keep pending but it’s fine; next header will overwrite pending
                continue

    # Optional: if you want, attach any unknown/unparsed footer as raw lines
    return {"user": user, "connects": connects}

class FilterModule(object):
    def filters(self):
        return {
            "racf_listuser_content_to_obj": racf_listuser_content_to_obj
        }

