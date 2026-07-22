"""
Tests for RACF domain models.
"""

from racf.model import (
    RacfUser,
    load_user,
)


def test_load_user():

    data = {

        "racf_user": {

            "meta": {
                "object_type": "user",
                "schema_version": "0.1.0",
                "zos_version": "3.1.0",
            },

            "state": "present",

            "content": {

                "base": {

                    "userid": "USER01",

                }

            },

        }

    }


    user = load_user(data)


    assert isinstance(user, RacfUser)

    assert user.state == "present"

    assert user.meta["object_type"] == "user"

    assert user.content["base"]["userid"] == "USER01"
