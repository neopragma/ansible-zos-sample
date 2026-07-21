from filter_plugins.racf.engine import generate_commands


class FilterModule:
    """
    RACF provisioning Ansible filters.
    """

    def filters(self):

        return {
            "racf_provision": generate_commands,
        }
