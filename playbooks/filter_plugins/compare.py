def compare_group(desired, current):

    result = {
        "attributes_changed": {},
        "connections_to_add": [],
        "connections_to_remove": [],
        "connections_to_update": []
    }


    #
    # Compare group attributes
    #

    desired_attributes = desired.get(
        "attributes",
        {}
    )

    current_attributes = current.get(
        "attributes",
        {}
    )


    for attribute, desired_value in desired_attributes.items():

        current_value = current_attributes.get(attribute)

        if desired_value != current_value:

            result["attributes_changed"][attribute] = {
                "current": current_value,
                "desired": desired_value
            }


    #
    # Compare connections
    #

    desired_connections = {
        c["userid"]: c
        for c in desired.get("connections", [])
    }

    current_connections = {
        c["userid"]: c
        for c in current.get("connections", [])
    }


    #
    # New CONNECTs
    #

    for userid, desired_conn in desired_connections.items():

        if userid not in current_connections:

            result["connections_to_add"].append(
                desired_conn
            )


    #
    # Removed CONNECTs
    #

    for userid, current_conn in current_connections.items():

        if userid not in desired_connections:

            result["connections_to_remove"].append(
                current_conn
            )


    #
    # Changed authorities
    #

    for userid in desired_connections.keys():

        if userid in current_connections:

            desired_auth = (
                desired_connections[userid]
                .get("authority")
            )

            current_auth = (
                current_connections[userid]
                .get("authority")
            )

            if desired_auth != current_auth:

                result["connections_to_update"].append(
                    {
                        "userid": userid,
                        "current_authority": current_auth,
                        "desired_authority": desired_auth
                    }
                )


    return result



class FilterModule(object):

    def filters(self):
        return {
            "compare_group": compare_group
        }
