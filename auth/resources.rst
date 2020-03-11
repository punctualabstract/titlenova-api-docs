Resources
=========

Resources are the objects with which the users will interact. They have actions associated with
them that represent what the user is trying to do with the resource. For example, one resource
**contacts** may have the following actions associated with it:

* `index` - index (or list) contacts
* `create` - create new contacts
* `update` - update an existing contact
* `delete` - delete contacts

List Resources
--------------

To list a single resource in the system, use the following ``GET`` request:

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        http://auth.titlenova/resources/2

The ``JSON`` response returned will look like:

.. code-block:: json

    {
        "id": 2,
        "resource": "roles",
        "actions": [
            "index",
            "create",
            "update",
            "delete"
        ]
    }

To list all of the resources currently in the system, use the following ``GET`` request:

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        http://auth.titlenova/resources

The ``JSON`` response returned will look like (intentionally abbreviated):

.. code-block:: json

    {
        "page": null,
        "limit": null,
        "sort": null,
        "filter": null,
        "resources": [
            {
                "id": 1,
                "resource": "users",
                "actions": [
                    "index",
                    "count",
                    "fields",
                    "create",
                    "update",
                    "delete",
                    "history",
                    "exists",
                    "validate",
                    "revoke"
                ]
            },
            {
                "id": 2,
                "resource": "roles",
                "actions": [
                    "index",
                    "count",
                    "fields",
                    "create",
                    "update",
                    "delete",
                    "history"
                ]
            },
            {
                "id": 26,
                "resource": "services",
                "actions": [
                    "index",
                    "count",
                    "fields",
                    "create",
                    "update",
                    "delete"
                ]
            }
        ],
        "resource_count": 26,
        "resource_fields": [
            "id",
            "resource",
            "actions"
        ]
    }

The returned response not only gives you an array of ``resources``, but also returns other pertinent
information regarding the request. In addition to the above request, you can pass some parameters
to fine-tune your request:

+-------------+-----------------------------------------------------------------------------------------------+
| **page**    | a page number from which to start the result set                                              |
+-------------+-----------------------------------------------------------------------------------------------+
| **limit**   | a value by which to limit the result set                                                      |
+-------------+-----------------------------------------------------------------------------------------------+
| **sort**    | a flag to sort by a particular field. For example, ``resource`` or ``-resource`` to sort DESC |
+-------------+-----------------------------------------------------------------------------------------------+
| **filter**  | a SQL-like filter string. For example, ``resource LIKE user%``                                |
+-------------+-----------------------------------------------------------------------------------------------+
| **fields**  | a comma-separated list of fields to limit which fields are selected                           |
+-------------+-----------------------------------------------------------------------------------------------+

*(The "page" value is meant to be utilized in conjunction with the "limit" value, and the length of the
page is calculated by the limit value.)*

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        "http://auth.titlenova/resources?filter[]=resource%20LIKE%20user%"

The returned response would be:

.. code-block:: json

    {
        "page": null,
        "limit": null,
        "sort": null,
        "filter": [
            "resource LIKE user%"
        ],
        "resources": [
            {
                "id": 17,
                "resource": "user-logins",
                "actions": [
                    "index",
                    "count",
                    "fields",
                    "create",
                    "delete"
                ]
            },
            {
                "id": 1,
                "resource": "users",
                "actions": [
                    "index",
                    "count",
                    "fields",
                    "create",
                    "update",
                    "delete",
                    "history",
                    "exists",
                    "validate",
                    "revoke"
                ]
            }
        ],
        "resource_count": 2,
        "resource_fields": [
            "id",
            "resource",
            "actions"
        ]
    }


There is also a method to return the number of resources in the system:

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        http://auth.titlenova/resources/count

.. code-block:: json

    {
        "filter": null,
        "resource_count": 26
    }

That method also supports the above request ``filter`` parameter:

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        "http://auth.titlenova/resources/count?filter[]=resource%20LIKE%20user%"

.. code-block:: json

    {
        "filter": [
            "resource LIKE user%"
        ],
        "resource_count": 2
    }

And to determine what fields are available for ``resource``, use the following request:

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        http://auth.titlenova/resources/fields

.. code-block:: json

    {
        "resource_fields": [
            "id",
            "resource",
            "actions"
        ]
    }

Create a Resource
-----------------

Create a resource with the following ``POST`` request:

.. code-block:: bash

    curl -i -X POST --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        -d"resource=orders&actions[]=index&actions[]=create" http://auth.titlenova/resources

.. code-block:: json

    {
        "resource": "orders",
        "actions": [
            "index",
            "create"
        ],
        "id": 27
    }

Accepted resource fields include:

+--------------+--------------------------------------------------------------------------------+
| **resource** | the name of the resource                                                       |
+--------------+--------------------------------------------------------------------------------+
| **actions**  | an array of string values that describe the actions to perform on the resource |
+--------------+--------------------------------------------------------------------------------+

Update an Existing Resource
---------------------------

To update an existing resource, send a ``PATCH`` request with the following payload to the resources endpoint:

.. code-block:: bash

    curl -i -X PATCH --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        -d"resource=orders2&actions[]=index&actions[]=create&actions[]=update&actions[]=delete" \
        http://auth.titlenova/resources/27

Upon a successful update, the response will return a ``JSON`` payload with the resource's updated data:

.. code-block:: json

    {
        "id": 27,
        "resource": "orders2",
        "actions": [
            "index",
            "create",
            "update",
            "delete"
        ]
    }

*(Note: Actions are not additive and the entire array of actions needs to be sent with the PATCH request
to maintain them.)*

Deleting Resources
------------------

**Deleting a single resource**

.. code-block:: bash

    curl -i -X DELETE --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        http://auth.titlenova/resources/27

**Deleting multiple resource**

.. code-block:: bash

    curl -i -X DELETE --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        -d"rm_resources[]=28&rm_resources[]=29" http://auth.titlenova/resources/
