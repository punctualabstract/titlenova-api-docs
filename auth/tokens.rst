Tokens
======

Tokens can be generally managed to monitor who currently has access to the system
and revoke the token of any user that should not have access.

List Tokens
-----------

To list information about a single token in the system, use the following ``GET`` request:

**Endpoint:** ``https://auth.titlenova.com/tokens/<token>``

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        https://auth.titlenova.com/tokens/48f97a0e966ec61324e225a5c2140616e6efa093

The ``JSON`` response returned will give you information on the token and the user who owns it:

.. code-block:: json

    {
        "user_id": 1,
        "token": "48f97a0e966ec61324e225a5c2140616e6efa093",
        "refresh": "4968cf04e35decdfd345fb31026e672373bef510",
        "expires": 0,
        "requests": 86,
        "ip": "127.0.0.1",
        "ua": "curl\/7.58.0",
        "created": "2020-03-11 11:46:12",
        "last_request": "2020-03-12 13:28:05",
        "scope_updated": null,
        "username": "admin",
        "active": 1,
        "attempts": 0,
        "roles": [
            {
                "id": 1,
                "role": "Admin"
            }
        ]
    }

To list all of the tokens currently in the system, use the following ``GET`` request:

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        https://auth.titlenova.com/tokens

The ``JSON`` response returned will look like:

.. code-block:: json

    {
        "page": null,
        "limit": null,
        "sort": null,
        "filter": null,
        "tokens": [
            {
                "user_id": "1",
                "username": "admin",
                "token": "48f97a0e966ec61324e225a5c2140616e6efa093",
                "refresh": "4968cf04e35decdfd345fb31026e672373bef510",
                "expires": "0",
                "requests": "90",
                "active": "1",
                "attempts": "0"
            }
        ],
        "token_count": 1,
        "token_fields": [
            "user_id",
            "username",
            "token",
            "refresh",
            "expires",
            "requests",
            "ip",
            "ua",
            "created",
            "last_request",
            "scope_updated"
        ]
    }

The returned response not only gives you an array of ``tokens``, but also returns other pertinent
information regarding the request. In addition to the above request, you can pass some parameters
to fine-tune your request:

+-------------+-----------------------------------------------------------------------------------------------+
| **page**    | a page number from which to start the result set                                              |
+-------------+-----------------------------------------------------------------------------------------------+
| **limit**   | a value by which to limit the result set                                                      |
+-------------+-----------------------------------------------------------------------------------------------+
| **sort**    | a flag to sort by a particular field. For example, ``username`` or ``-username`` to sort DESC |
+-------------+-----------------------------------------------------------------------------------------------+
| **filter**  | a SQL-like filter string. For example, ``username LIKE ad%``                                  |
+-------------+-----------------------------------------------------------------------------------------------+
| **fields**  | a comma-separated list of fields to limit which fields are selected                           |
+-------------+-----------------------------------------------------------------------------------------------+
| **user_id** | a value to filter the result set by a certain user                                            |
+-------------+-----------------------------------------------------------------------------------------------+

*(The "page" value is meant to be utilized in conjunction with the "limit" value, and the length of the
page is calculated by the limit value.)*

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        "https://auth.titlenova.com/tokens?user_id=1&page=1&limit=25&sort=-id"

The returned response would be:

.. code-block:: json

    {
        "page": 1,
        "limit": 25,
        "sort": "-id",
        "filter": null,
        "tokens": [
            {
                "user_id": 1,
                "username": "admin",
                "token": "48f97a0e966ec61324e225a5c2140616e6efa093",
                "refresh": "4968cf04e35decdfd345fb31026e672373bef510",
                "expires": 0,
                "requests": 94,
                "active": 1,
                "attempts": 0
            }
        ],
        "token_count": 1,
        "token_fields": [
            "user_id",
            "username",
            "token",
            "refresh",
            "expires",
            "requests",
            "ip",
            "ua",
            "created",
            "last_request",
            "scope_updated"
        ]
    }


There is also a method to return the number of tokens in the system:

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        https://auth.titlenova.com/tokens/count

.. code-block:: json

    {
        "filter": null,
        "token_count": 1
    }

That method also supports the above request parameters of ``filter`` and ``user_id``:

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        "https://auth.titlenova.com/tokens/count?filter[]=username%20LIKE%20ad%"

.. code-block:: json

    {
        "filter": [
            "username LIKE ad%"
        ],
        "token_count": 1
    }

And to determine what fields are available for the ``token`` resource, use the following request:

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        https://auth.titlenova.com/tokens/fields

.. code-block:: json

    {
        "token_fields": [
            "user_id",
            "username",
            "token",
            "refresh",
            "expires",
            "requests",
            "ip",
            "ua",
            "created",
            "last_request",
            "scope_updated"
        ]
    }

Deleting a Token
----------------

**Deleting a token**

**Endpoint:** ``https://auth.titlenova.com/tokens/<token>``

.. code-block:: bash

    curl -i -X DELETE --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        https://auth.titlenova.com/tokens/7f7cbaa7c2073fc5dc38f14a8f8890038fbff919
