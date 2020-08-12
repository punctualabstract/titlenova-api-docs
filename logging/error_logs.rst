Error Logs
==========

The error logs in the logging API store detailed data on any errors that occur on any
request sent to any TitleNova API application. Each log entry stores:

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
- Class
- Message
- Timestamp

This provides a much more robust snapshot of who the user was, where they came from,
what they were trying to do and what the error was that they received.

List Error Logs
---------------

To list a single error log entry in the system, use the following ``GET`` request:

**Endpoint:** ``https://logs.titlenova.com/error/<id>``

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        https://logs.titlenova.com/error/1

The ``JSON`` response returned will look like:

.. code-block:: json

    {
        "id": 1,
        "user_id": null,
        "username": null,
        "ip": "127.0.0.1",
        "ua": "curl\/7.58.0",
        "protocol": "HTTP\/1.1",
        "code": "500",
        "host": "instant.titlenova",
        "route": "\/search",
        "method": "POST",
        "headers": {
            "Host": "instant.titlenova",
            "User-Agent": "curl\/7.58.0",
            "Accept": "*\/*",
            "Authorization": "*",
            "Content-Length": "68",
            "Content-Type": "application\/x-www-form-urlencoded"
        },
        "data": {
            "state": "LA",
            "county": "Assumption Parish",
            "tax_id": "700006000",
            "search_type": "taxes"
        },
        "class": "Pop\\Http\\Exception",
        "message": "The header code  is not allowed.",
        "timestamp": "2020-06-02 12:15:41"
    }

To list all of the error log entries currently in the system, use the following ``GET`` request:

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        https://logs.titlenova.com/error

The ``JSON`` response returned will look like:

.. code-block:: json

     {
        "page": null,
        "limit": null,
        "sort": null,
        "filter": null,
        "entries": [
            {
                "id": 48,
                "user_id": null,
                "username": null,
                "ip": "127.0.0.1",
                "ua": "pabs-v5\/php 7.3.14",
                "protocol": "HTTP\/1.0",
                "code": "500",
                "host": "workflow.titlenova",
                "route": "\/tasks\/validate?name=Default&transaction_id=10915295",
                "method": "GET",
                "headers": {
                    "Host": "workflow.titlenova",
                    "Connection": "close",
                    "User-Agent": "pabs-v5\/php 7.3.14",
                    "Authorization": "*"
                },
                "data": {
                    "name": "Default",
                    "transaction_id": "10915295"
                },
                "class": "Pop\\Http\\Server\\Exception",
                "message": "The headers have already been sent.",
                "timestamp": "2020-07-21 12:28:54"
            },
            {
                "id": 49,
                "user_id": null,
                "username": null,
                "ip": "127.0.0.1",
                "ua": "curl\/7.58.0",
                "protocol": "HTTP\/1.1",
                "code": "500",
                "host": "workflow.titlenova",
                "route": "\/tasks\/validate?name=Default&transaction_id=10915295",
                "method": "GET",
                "headers": {
                    "Host": "workflow.titlenova",
                    "User-Agent": "curl\/7.58.0",
                    "Accept": "*\/*",
                    "Authorization": "*"
                },
                "data": {
                    "name": "Default",
                    "transaction_id": "10915295"
                },
                "class": "Pop\\Http\\Server\\Exception",
                "message": "The headers have already been sent.",
                "timestamp": "2020-07-21 12:29:52"
            }
        ],
        "entry_count": 50,
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
            "class",
            "message",
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
        "https://logs.titlenova.com/error?filter[]=ip%20LIKE%20127.0.0.%"

The returned response would be:

.. code-block:: json

     {
        "page": null,
        "limit": null,
        "sort": null,
        "filter": null,
        "entries": [
            {
                "id": 48,
                "user_id": null,
                "username": null,
                "ip": "127.0.0.1",
                "ua": "pabs-v5\/php 7.3.14",
                "protocol": "HTTP\/1.0",
                "code": "500",
                "host": "workflow.titlenova",
                "route": "\/tasks\/validate?name=Default&transaction_id=10915295",
                "method": "GET",
                "headers": {
                    "Host": "workflow.titlenova",
                    "Connection": "close",
                    "User-Agent": "pabs-v5\/php 7.3.14",
                    "Authorization": "*"
                },
                "data": {
                    "name": "Default",
                    "transaction_id": "10915295"
                },
                "class": "Pop\\Http\\Server\\Exception",
                "message": "The headers have already been sent.",
                "timestamp": "2020-07-21 12:28:54"
            },
            {
                "id": 49,
                "user_id": null,
                "username": null,
                "ip": "127.0.0.1",
                "ua": "curl\/7.58.0",
                "protocol": "HTTP\/1.1",
                "code": "500",
                "host": "workflow.titlenova",
                "route": "\/tasks\/validate?name=Default&transaction_id=10915295",
                "method": "GET",
                "headers": {
                    "Host": "workflow.titlenova",
                    "User-Agent": "curl\/7.58.0",
                    "Accept": "*\/*",
                    "Authorization": "*"
                },
                "data": {
                    "name": "Default",
                    "transaction_id": "10915295"
                },
                "class": "Pop\\Http\\Server\\Exception",
                "message": "The headers have already been sent.",
                "timestamp": "2020-07-21 12:29:52"
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

There is also a method to return the number of error log entries in the system:

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        https://logs.titlenova.com/error/count

.. code-block:: json

    {
        "filter": null,
        "entry_count": 50
    }

That method also supports the above request ``filter`` parameter:

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        "https://logs.titlenova.com/error/count?filter[]=ip%20LIKE%20127.0.0.%"

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
        https://logs.titlenova.com/error/fields

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
            "class",
            "message",
            "timestamp"
        ]
    }

Deleting Error Logs
-------------------

**Deleting a single error log entry**

**Endpoint:** ``https://logs.titlenova.com/error/<id>``

.. code-block:: bash

    curl -i -X DELETE --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        https://logs.titlenova.com/error/2

**Deleting multiple error log entries**

.. code-block:: bash

    curl -i -X DELETE --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        -d"rm_logs[]=3&rm_logs[]=4" https://logs.titlenova.com/error/

