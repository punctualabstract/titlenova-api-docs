Access Logs
===========

The access logs in the logging API store detailed data on anyone who has accessed any
TitleNova API application. Each log entry stores:

- User ID
- Username
- IP Address
- User Agent
- Protocol
- HTTP Code
- Host
- Route
- Method
- Headers
- Data
- Timestamp

This provides a much more robust snapshot of who the user is, where they came from,
what they were trying to do and what response they received.

List Access Logs
----------------

To list a single access log entry in the system, use the following ``GET`` request:

**Endpoint:** ``https://logs.titlenova.com/access/<id>``

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        https://logs.titlenova.com/access/1

The ``JSON`` response returned will look like:

.. code-block:: json

    {
        "id": 1,
        "user_id": null,
        "username": null,
        "ip": "127.0.0.1",
        "ua": "curl\/7.58.0",
        "protocol": "HTTP\/1.1",
        "code": "401",
        "host": "auth.titlenova",
        "route": "\/",
        "method": "POST",
        "headers": {
            "Host": "auth.titlenova",
            "User-Agent": "curl\/7.58.0",
            "Accept": "*\/*"
        },
        "data": null,
        "timestamp": "2020-06-02 10:41:50"
    }


To list all of the access log entries currently in the system, use the following ``GET`` request:

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        https://logs.titlenova.com/access

The ``JSON`` response returned will look like:

.. code-block:: json

     {
        "page": null,
        "limit": null,
        "sort": null,
        "filter": null,
        "entries": [
            {
                "id": 3110,
                "user_id": 1,
                "username": "admin",
                "ip": "127.0.0.1",
                "ua": "curl\/7.58.0",
                "protocol": "HTTP\/1.1",
                "code": "200",
                "host": "logs.titlenova",
                "route": "\/access\/1",
                "method": "GET",
                "headers": {
                    "Host": "logs.titlenova",
                    "User-Agent": "curl\/7.58.0",
                    "Accept": "*\/*",
                    "Authorization": "*"
                },
                "data": null,
                "timestamp": "2020-08-12 15:18:33"
            },
            {
                "id": 3111,
                "user_id": 1,
                "username": "admin",
                "ip": "127.0.0.1",
                "ua": "nova-logs\/php 7.3.14",
                "protocol": "HTTP\/1.1",
                "code": "200",
                "host": "auth.titlenova",
                "route": "\/authorize",
                "method": "POST",
                "headers": {
                    "Host": "auth.titlenova",
                    "Connection": "close",
                    "User-Agent": "nova-logs\/php 7.3.14",
                    "X-Resource": "access-logs",
                    "X-Permission": "index",
                    "Authorization": "*"
                },
                "data": null,
                "timestamp": "2020-08-12 15:19:00"
            }
        ],
        "entry_count": 3111,
        "entry_fields": [
            "id",
            "user_id",
            "username",
            "ip",
            "ua",
            "protocol",
            "code",
            "host",
            "route",
            "method",
            "headers",
            "data",
            "timestamp"
        ]
    }


The returned response not only gives you an array of ``entries``, but also returns other pertinent
information regarding the request. In addition to the above request, you can pass some parameters
to fine-tune your request:

+-------------+---------------------------------------------------------------------------------------+
| **page**    | a page number from which to start the result set                                      |
+-------------+---------------------------------------------------------------------------------------+
| **limit**   | a value by which to limit the result set                                              |
+-------------+---------------------------------------------------------------------------------------+
| **sort**    | a flag to sort by a particular field. For example, ``code`` or ``-code`` to sort DESC |
+-------------+---------------------------------------------------------------------------------------+
| **filter**  | a SQL-like filter string. For example, ``code LIKE 40%``                              |
+-------------+---------------------------------------------------------------------------------------+
| **fields**  | a comma-separated list of fields to limit which fields are selected                   |
+-------------+---------------------------------------------------------------------------------------+

*(The "page" value is meant to be utilized in conjunction with the "limit" value, and the length of the
page is calculated by the limit value.)*

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        "https://logs.titlenova.com/access?filter[]=19%20LIKE%20127.0.0.%"

The returned response would be:

.. code-block:: json

     {
        "page": null,
        "limit": null,
        "sort": null,
        "filter": null,
        "entries": [
            {
                "id": 3110,
                "user_id": 1,
                "username": "admin",
                "ip": "127.0.0.1",
                "ua": "curl\/7.58.0",
                "protocol": "HTTP\/1.1",
                "code": "200",
                "host": "logs.titlenova",
                "route": "\/access\/1",
                "method": "GET",
                "headers": {
                    "Host": "logs.titlenova",
                    "User-Agent": "curl\/7.58.0",
                    "Accept": "*\/*",
                    "Authorization": "*"
                },
                "data": null,
                "timestamp": "2020-08-12 15:18:33"
            },
            {
                "id": 3111,
                "user_id": 1,
                "username": "admin",
                "ip": "127.0.0.1",
                "ua": "nova-logs\/php 7.3.14",
                "protocol": "HTTP\/1.1",
                "code": "200",
                "host": "auth.titlenova",
                "route": "\/authorize",
                "method": "POST",
                "headers": {
                    "Host": "auth.titlenova",
                    "Connection": "close",
                    "User-Agent": "nova-logs\/php 7.3.14",
                    "X-Resource": "access-logs",
                    "X-Permission": "index",
                    "Authorization": "*"
                },
                "data": null,
                "timestamp": "2020-08-12 15:19:00"
            }
        ],
        "entry_count": 2,
        "entry_fields": [
            "id",
            "user_id",
            "username",
            "ip",
            "ua",
            "protocol",
            "code",
            "host",
            "route",
            "method",
            "headers",
            "data",
            "timestamp"
        ]
    }

There is also a method to return the number of access log entries in the system:

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        https://logs.titlenova.com/access/count

.. code-block:: json

    {
        "filter": null,
        "entry_count": 3111
    }

That method also supports the above request ``filter`` parameter:

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        "https://logs.titlenova.com/access/count?filter[]=19%20LIKE%20127.0.0.%"

.. code-block:: json

    {
        "filter": [
            "ip LIKE 127.0.0.%"
        ],
        "entry_count": 2
    }

And to determine what fields are available for the ``entries`` resource, use the following request:

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        https://logs.titlenova.com/access/fields

.. code-block:: json

    {
        "entry_fields": [
            "id",
            "user_id",
            "username",
            "ip",
            "ua",
            "protocol",
            "code",
            "host",
            "route",
            "method",
            "headers",
            "data",
            "timestamp"
        ]
    }

Deleting Access Logs
--------------------

**Deleting a single access log entry**

**Endpoint:** ``https://logs.titlenova.com/access/<id>``

.. code-block:: bash

    curl -i -X DELETE --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        https://logs.titlenova.com/access/2

**Deleting multiple access log entries**

.. code-block:: bash

    curl -i -X DELETE --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        -d"rm_logs[]=3&rm_logs[]=4" https://logs.titlenova.com/access/

