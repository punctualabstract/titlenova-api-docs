Roles
=====

Roles are defined and associated to users which allows the ACL feature of the API to evaluate
whether or not the user has permission to access or modify the requested resource. Users can
be assigned multiple roles. Also, a role can have a parent role, in which case they inherit the
permissions of their parent role.

List Roles
----------

To list a single role in the system, use the following ``GET`` request:

**Endpoint** ``https://auth.titlenova.com/roles/<id>``

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        https://auth.titlenova.com/roles/1

The ``JSON`` response returned will look like:

.. code-block:: json

    {
        "id": 1,
        "parent_id": null,
        "role": "Admin"
    }

To list all of the roles currently in the system, use the following ``GET`` request:

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        https://auth.titlenova.com/roles

The ``JSON`` response returned will look like:

.. code-block:: json

    {
        "page": null,
        "limit": null,
        "sort": null,
        "filter": null,
        "roles": [
            {
                "id": "1",
                "parent_id": null,
                "parent_role": null,
                "role": "Admin"
            }
        ],
        "role_count": 1,
        "role_fields": [
            "id",
            "parent_id",
            "parent_role",
            "role"
        ]
    }

The returned response not only gives you an array of ``roles``, but also returns other pertinent
information regarding the request. In addition to the above request, you can pass some parameters
to fine-tune your request:

+-------------+---------------------------------------------------------------------------------------+
| **page**    | a page number from which to start the result set                                      |
+-------------+---------------------------------------------------------------------------------------+
| **limit**   | a value by which to limit the result set                                              |
+-------------+---------------------------------------------------------------------------------------+
| **sort**    | a flag to sort by a particular field. For example, ``role`` or ``-role`` to sort DESC |
+-------------+---------------------------------------------------------------------------------------+
| **filter**  | a SQL-like filter string. For example, ``role LIKE ad%``                              |
+-------------+---------------------------------------------------------------------------------------+
| **fields**  | a comma-separated list of fields to limit which fields are selected                   |
+-------------+---------------------------------------------------------------------------------------+

*(The "page" value is meant to be utilized in conjunction with the "limit" value, and the length of the
page is calculated by the limit value.)*

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        "https://auth.titlenova.com/roles?filter[]=role%20LIKE%20ad%"

The returned response would be:

.. code-block:: json

    {
        "page": 1,
        "limit": 25,
        "sort": "-id",
        "filter": null,
        "roles": [
            {
                "id": "1",
                "parent_id": null,
                "parent_role": null,
                "role": "Admin"
            }
        ],
        "role_count": 1,
        "role_fields": [
            "id",
            "parent_id",
            "parent_role",
            "role"
        ]
    }

There is also a method to return the number of roles in the system:

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        https://auth.titlenova.com/roles/count

.. code-block:: json

    {
        "filter": null,
        "role_count": 1
    }

That method also supports the above request ``filter`` parameter:

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        "https://auth.titlenova.com/roles/count?filter[]=role%20LIKE%20ad%"

.. code-block:: json

    {
        "filter": [
            "role LIKE ad%"
        ],
        "role_count": 1
    }

And to determine what fields are available for the ``roles`` resource, use the following request:

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        https://auth.titlenova.com/roles/fields

.. code-block:: json

    {
        "role_fields": [
            "id",
            "parent_id",
            "parent_role",
            "role"
        ]
    }

Create a Role
-------------

Create a role with the following ``POST`` request:

.. code-block:: bash

    curl -i -X POST --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        -d"role=Editor" https://auth.titlenova.com/roles

.. code-block:: json

    {
        "id": 2,
        "parent_id": null,
        "role": "Editor"
    }

Accepted role fields include:

+---------------+-----------------------------------------------+
| **parent_id** | the ID of a role's parent role (not required) |
+---------------+-----------------------------------------------+
| **role**      | the name of the role                          |
+---------------+-----------------------------------------------+

Update an Existing Role
-----------------------

To update an existing role, send a ``PATCH`` request with the following payload to the roles endpoint:

**Endpoint** ``https://auth.titlenova.com/roles/<id>``

.. code-block:: bash

    curl -i -X PATCH --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        -d"role=Editor2" https://auth.titlenova.com/roles/2

Upon a successful update, the response will return a ``JSON`` payload with the role's updated data:

.. code-block:: json

    {
        "id": 2,
        "parent_id": null,
        "role": "Editor2"
    }

Deleting Roles
--------------

**Deleting a single role**

**Endpoint** ``https://auth.titlenova.com/roles/<id>``

.. code-block:: bash

    curl -i -X DELETE --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        https://auth.titlenova.com/roles/2

**Deleting multiple roles**

.. code-block:: bash

    curl -i -X DELETE --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        -d"rm_roles[]=3&rm_roles[]=4" https://auth.titlenova.com/roles/
