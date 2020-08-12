Event Logs
==========

The event logs in the logging API store event messaging that is triggered by any
specific or custom events in any TitleNova API application. Each log entry stores:

- User ID
- Username
- IP Address
- User Agent
- Protocol
- Domain
- Route
- Type
- Level
- Name
- Message
- Context
- Timestamp

The format supports and follows the RFC-3164 syslog protocol.

List Event Logs
---------------

To list a single event log entry in the system, use the following ``GET`` request:

**Endpoint:** ``https://logs.titlenova.com/event/<id>``

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        https://logs.titlenova.com/event/1

The ``JSON`` response returned will look like:

.. code-block:: json

    {
        "id": 1,
        "user_id": 1,
        "username": "admin",
        "ip": "127.0.0.1",
        "ua": "Mozilla",
        "domain": "auth.titlenova.com",
        "route": "\/users",
        "type": null,
        "level": 5,
        "name": "NOTICE",
        "message": "Something happened!",
        "context": null,
        "timestamp": "2020-08-12 16:24:56"
    }

To list all of the event log entries currently in the system, use the following ``GET`` request:

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        https://logs.titlenova.com/event

The ``JSON`` response returned will look like:

.. code-block:: json

    {
        "page": null,
        "limit": null,
        "sort": null,
        "filter": null,
        "entries": [
            {
                "id": 1,
                "user_id": 1,
                "username": "admin",
                "ip": "127.0.0.1",
                "ua": "Mozilla",
                "domain": "auth.titlenova.com",
                "route": "\/users",
                "type": null,
                "level": 5,
                "name": "NOTICE",
                "message": "Something happened!",
                "context": null,
                "timestamp": "2020-08-12 16:24:56"
            }
        ],
        "entry_count": 1,
        "entry_fields": [
            "id",
            "user_id",
            "username",
            "ip",
            "ua",
            "domain",
            "route",
            "type",
            "level",
            "name",
            "message",
            "context",
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
| **sort**    | a flag to sort by a particular field. For example, ``ip`` or ``-ip`` to sort DESC     |
+-------------+---------------------------------------------------------------------------------------+
| **filter**  | a SQL-like filter string. For example, ``domain LIKE auth%``                          |
+-------------+---------------------------------------------------------------------------------------+
| **fields**  | a comma-separated list of fields to limit which fields are selected                   |
+-------------+---------------------------------------------------------------------------------------+

*(The "page" value is meant to be utilized in conjunction with the "limit" value, and the length of the
page is calculated by the limit value.)*

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        "https://logs.titlenova.com/event?filter[]=ip%20LIKE%20127.0.0.%"

The returned response would be:

.. code-block:: json

    {
        "page": null,
        "limit": null,
        "sort": null,
        "filter": null,
        "entries": [
            {
                "id": 1,
                "user_id": 1,
                "username": "admin",
                "ip": "127.0.0.1",
                "ua": "Mozilla",
                "domain": "auth.titlenova.com",
                "route": "\/users",
                "type": null,
                "level": 5,
                "name": "NOTICE",
                "message": "Something happened!",
                "context": null,
                "timestamp": "2020-08-12 16:24:56"
            }
        ],
        "entry_count": 1,
        "entry_fields": [
            "id",
            "user_id",
            "username",
            "ip",
            "ua",
            "domain",
            "route",
            "type",
            "level",
            "name",
            "message",
            "context",
            "timestamp"
        ]
    }

There is also a method to return the number of event log entries in the system:

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        https://logs.titlenova.com/event/count

.. code-block:: json

    {
        "filter": null,
        "entry_count": 2
    }

That method also supports the above request ``filter`` parameter:

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        "https://logs.titlenova.com/event/count?filter[]=ip%20LIKE%20127.0.0.%"

.. code-block:: json

    {
        "filter": [
            "ip LIKE 127.0.0.%"
        ],
        "entry_count": 1
    }

And to determine what fields are available for the ``entries`` resource, use the following request:

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        https://logs.titlenova.com/event/fields

.. code-block:: json

    {
        "entry_fields": [
            "id",
            "user_id",
            "username",
            "ip",
            "ua",
            "domain",
            "route",
            "type",
            "level",
            "name",
            "message",
            "context",
            "timestamp"
        ]
    }

Deleting Event Logs
-------------------

**Deleting a single event log entry**

**Endpoint:** ``https://logs.titlenova.com/event/<id>``

.. code-block:: bash

    curl -i -X DELETE --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        https://logs.titlenova.com/event/2

**Deleting multiple event log entries**

.. code-block:: bash

    curl -i -X DELETE --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        -d"rm_logs[]=3&rm_logs[]=4" https://logs.titlenova.com/event/
