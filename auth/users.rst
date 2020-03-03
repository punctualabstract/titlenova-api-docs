Users
=====

The user data stored under the authentication API is only the pertinent data that is
associated with user authentication. *All other user data (names, profiles, contacts, etc.)
is stored in the user API.*

Create a User
-------------

At a minimum, a new user requires a ``username`` and a ``password``, along with at least
one valid ``role_id``. A user cannot be granted access to any system unless they have a valid
role associated with them to evaluate their level of access. *Users can have more than one role.*

To create a user, send a ``POST`` request with the following payload to the users endpoint:

.. code-block:: bash

    curl -i -X POST --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        -d"username=admin2&password=123456&role_ids[]=1" https://auth.titlenova.com/users

A user's ``username`` and ``password`` must also meet certain criteria. The username must be
at least 6 characters long and not contain a space. The password must meet 3 of the following
4 conditions:

* One uppercase character
* One lowercase character
* One number
* One special character ($ ? ! _ - # % & @)

Also passwords are set to expire every 90 days and must be reset. A previous password cannot
be reused until 4 other passwords have be used.

Accepted user fields include:

+----------------------+-------------------------------------------------------+
| ``username``         | *the user's username*                                 |
+----------------------+-------------------------------------------------------+
| ``password``         | *a string that will be converted into a one-way hash* |
+----------------------+-------------------------------------------------------+
| ``active``           | *a 0 or 1 boolean value*                              |
+----------------------+-------------------------------------------------------+
| ``attempts``         | *number of failed authentication attempts*            |
+----------------------+-------------------------------------------------------+
| ``password_expires`` | *a datetime value*                                    |
+----------------------+-------------------------------------------------------+
| ``metadata``         | *an optional array of additional user data*           |
+----------------------+-------------------------------------------------------+

Validate a User
---------------

Before submitting the request to create (or update) a user, you can validate a user's information.

**Check if a username already exists**

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        https://auth.titlenova.com/users/exists?username=admin

The above request returns the following ``JSON`` response to let you know if the username exists or not:

.. code-block:: json

    {
        "user_exists": true
    }

**Validate attempted user credentials**

To determine if the attempted credentials meant the requirements listed above, the following ``POST``
request can be sent to this endpoint:

.. code-block:: bash

    curl -i -X POST --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        -d"username=admin&password=123456" https://auth.titlenova.com/users/validate

which will return a response outlining any issues with the attempted credentials:

.. code-block:: json

    {
        "username": [
            "The username must be at least 6 characters.",
            "That username is not allowed."
        ],
        "password": [
            "The password must be at least 8 characters.",
            "The password did not meet the required conditions."
        ]
    }

If all requirements are met, then the following response is returned:

.. code-block:: json

    {
        "username": true,
        "password": true
    }

You can validate new credentials for an existing user by added the user's id to the endpoint.
This takes into account the existing user's current username and excludes it from validation
(which would create a false failure.)

.. code-block:: bash

    curl -i -X POST --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        -d"username=admin&password=123456" https://auth.titlenova.com/users/validate/1

Update an Existing User
-----------------------

To update an existing user, send a ``PATCH`` request with the following payload to the users endpoint:

.. code-block:: bash

    curl -i -X PATCH --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        -d"active=1&role_ids[]=2" https://auth.titlenova.com/users/1

Upon a successful update, the response will return a ``JSON`` payload with the user's updated data:

.. code-block:: json

    {
        "id": 1,
        "username": "admin",
        "active": 1,
        "attempts": 0,
        "password_expires": "2020-05-03 13:40:18",
        "metadata": [],
        "roles": [
            {
                "id": 1,
                "role": "Admin"
            }
        ]
    }

Revoking a User
---------------

If a user that should not have access has gained access to any of the systems, you can revoke that user's
token with the following request:

.. code-block:: bash

    curl -i -X DELETE --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        https://auth.titlenova.com/users/revoke/2

Deleting Users
--------------

**Deleting a single user**

.. code-block:: bash

    curl -i -X DELETE --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        https://auth.titlenova.com/users/2

**Deleting multiple users**

.. code-block:: bash

    curl -i -X DELETE --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        -d"rm_users[]=4&rm_users[]=5&rm_users[]=6" https://auth.titlenova.com/users/


