"""
Schema definition for RACF user profiles.

This module defines the structure and validation metadata for:

    racf_user:
        meta:
        state:
        content:
            base:
            omvs:
            tso:

The schema describes desired state only.
It does not generate RACF commands.
"""

from __future__ import annotations

from .common import Field, Section, ValueType


USER_SCHEMA = Section(

    fields={

        "state": Field(
            type=ValueType.ENUM,
            required=True,
            choices=(
                "present",
                "absent",
            ),
            description=(
                "Desired lifecycle state of the RACF user."
            ),
        ),

    },

    sections={

        #
        # ------------------------------------------------------------------
        # Metadata
        # ------------------------------------------------------------------
        #

        "meta": Section(

            fields={

                "object_type": Field(
                    type=ValueType.STRING,
                    required=True,
                    default="user",
                    description=(
                        "RACF object type."
                    ),
                ),

                "schema_version": Field(
                    type=ValueType.STRING,
                    required=True,
                    description=(
                        "Version of this YAML schema."
                    ),
                ),

                "zos_version": Field(
                    type=ValueType.STRING,
                    required=True,
                    description=(
                        "Target z/OS version."
                    ),
                ),

            }

        ),


        #
        # ------------------------------------------------------------------
        # User content
        # ------------------------------------------------------------------
        #

        "content": Section(

            sections={


                #
                # ----------------------------------------------------------
                # Base segment
                # ----------------------------------------------------------
                #

                "base": Section(

                    fields={

                        "userid": Field(
                            type=ValueType.STRING,
                            required=True,
                            description=(
                                "RACF user identifier."
                            ),
                        ),

                        "name": Field(
                            type=ValueType.STRING,
                            description=(
                                "User name."
                            ),
                        ),

                        "owner": Field(
                            type=ValueType.STRING,
                            description=(
                                "Owning RACF user or group."
                            ),
                        ),

                        "default_group": Field(
                            type=ValueType.STRING,
                            description=(
                                "Default RACF group."
                            ),
                        ),

                    },

                    sections={


                        #
                        # User attributes
                        #

                        "attributes": Section(

                            fields={

                                "special": Field(
                                    type=ValueType.BOOLEAN,
                                    description=(
                                        "User has RACF SPECIAL authority."
                                    ),
                                ),

                                "operations": Field(
                                    type=ValueType.BOOLEAN,
                                    description=(
                                        "User has OPERATIONS authority."
                                    ),
                                ),

                                "auditor": Field(
                                    type=ValueType.BOOLEAN,
                                    description=(
                                        "User has AUDITOR authority."
                                    ),
                                ),

                                "revoker": Field(
                                    type=ValueType.BOOLEAN,
                                    description=(
                                        "User can revoke users."
                                    ),
                                ),

                                "protected": Field(
                                    type=ValueType.BOOLEAN,
                                    description=(
                                        "User is protected."
                                    ),
                                ),

                                "restricted": Field(
                                    type=ValueType.BOOLEAN,
                                    description=(
                                        "User is restricted."
                                    ),
                                ),

                                "trusted": Field(
                                    type=ValueType.BOOLEAN,
                                    description=(
                                        "User is trusted."
                                    ),
                                ),

                                "privileged": Field(
                                    type=ValueType.BOOLEAN,
                                    description=(
                                        "User is privileged."
                                    ),
                                ),

                            }

                        ),


                        #
                        # Password policy
                        #

                        "password": Section(

                            fields={

                                "source": Field(
                                    type=ValueType.ENUM,
                                    choices=(
                                        "generated",
                                        "vault",
                                        "external",
                                    ),
                                    description=(
                                        "Where password material originates."
                                    ),
                                ),

                                "expired": Field(
                                    type=ValueType.BOOLEAN,
                                    description=(
                                        "Password should be expired."
                                    ),
                                ),

                                "no_password": Field(
                                    type=ValueType.BOOLEAN,
                                    description=(
                                        "User should not have a password."
                                    ),
                                ),

                            }

                        ),


                        #
                        # Revocation
                        #

                        "revoke": Section(

                            fields={

                                "revoked": Field(
                                    type=ValueType.BOOLEAN,
                                    description=(
                                        "User should be revoked."
                                    ),
                                ),

                                "resume_date": Field(
                                    type=ValueType.STRING,
                                    description=(
                                        "Date when revoked user resumes."
                                    ),
                                ),

                            }

                        ),

                    }

                ),


                #
                # ----------------------------------------------------------
                # OMVS segment
                # ----------------------------------------------------------
                #

                "omvs": Section(

                    fields={

                        "uid": Field(
                            type=ValueType.INTEGER,
                            minimum=1,
                            description=(
                                "UNIX user identifier."
                            ),
                        ),

                        "home": Field(
                            type=ValueType.STRING,
                            description=(
                                "UNIX home directory."
                            ),
                        ),

                        "program": Field(
                            type=ValueType.STRING,
                            description=(
                                "Initial UNIX program."
                            ),
                        ),

                        "cpu_time_max": Field(
                            type=ValueType.INTEGER,
                        ),

                        "assize_max": Field(
                            type=ValueType.INTEGER,
                        ),

                        "fileproc_max": Field(
                            type=ValueType.INTEGER,
                        ),

                        "threads_max": Field(
                            type=ValueType.INTEGER,
                        ),

                        "region_size_max": Field(
                            type=ValueType.INTEGER,
                        ),

                        "auto_uid": Field(
                            type=ValueType.BOOLEAN,
                            description=(
                                "Allow RACF to assign UID."
                            ),
                        ),

                        "auto_home": Field(
                            type=ValueType.BOOLEAN,
                            description=(
                                "Allow RACF to assign home directory."
                            ),
                        ),

                    }

                ),


                #
                # ----------------------------------------------------------
                # TSO segment
                # ----------------------------------------------------------
                #

                "tso": Section(

                    fields={

                        "account_number": Field(
                            type=ValueType.STRING,
                        ),

                        "procedure": Field(
                            type=ValueType.STRING,
                        ),

                        "command": Field(
                            type=ValueType.STRING,
                        ),

                        "destination": Field(
                            type=ValueType.STRING,
                        ),

                        "hold_class": Field(
                            type=ValueType.STRING,
                        ),

                        "job_class": Field(
                            type=ValueType.STRING,
                        ),

                        "message_class": Field(
                            type=ValueType.STRING,
                        ),

                        "size_max": Field(
                            type=ValueType.INTEGER,
                        ),

                        "region_size": Field(
                            type=ValueType.INTEGER,
                        ),

                        "unit": Field(
                            type=ValueType.STRING,
                        ),

                        "user_data": Field(
                            type=ValueType.STRING,
                        ),

                    },

                    sections={

                        "logon": Section(

                            fields={

                                "reconnect": Field(
                                    type=ValueType.BOOLEAN,
                                ),

                                "logon_allowed": Field(
                                    type=ValueType.BOOLEAN,
                                ),

                            }

                        ),

                        "performance": Section(

                            fields={

                                "priority": Field(
                                    type=ValueType.INTEGER,
                                ),

                                "max_region_size": Field(
                                    type=ValueType.INTEGER,
                                ),

                            }

                        ),

                    }

                ),

            }

        ),

    },

)
