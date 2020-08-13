Audit Logs
==========

The audit logs in the logging API store detailed data any and all changes to any
resource in the TitleNova API applications. This includes the creation, update
and deletion of a resource or record. Each log entry stores:

- User ID
- Username
- Domain
- Route
- Method
- Model
- Model ID
- Action
- Old
- New
- Metadata
- Timestamp

This provides a much more robust snapshot on everything that's been done to any
resource or record in the system.

List Audit Logs
---------------

To list a single audit log entry in the system, use the following ``GET`` request:

**Endpoint:** ``https://logs.titlenova.com/audit/<id>``

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        https://logs.titlenova.com/audit/1

The ``JSON`` response returned will look like:

.. code-block:: json

    {
        "id": 1,
        "user_id": 1000,
        "username": "admin",
        "domain": "cli",
        "route": ".\/nova-auth role:grant-global 1",
        "method": null,
        "model": "Nova\\Auth\\Model\\Scope",
        "model_id": "1",
        "action": "created",
        "old": [],
        "new": {
            "role_id": "1",
            "resource_id": 1,
            "action": "index",
            "permission": 1,
            "id": 1
        },
        "metadata": [],
        "timestamp": "2020-06-02 10:56:16"
    }

To list all of the audit log entries currently in the system, use the following ``GET`` request:

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        https://logs.titlenova.com/audit

The ``JSON`` response returned will look like:

.. code-block:: json

     {
        "page": null,
        "limit": null,
        "sort": null,
        "filter": null,
        "entries": [
            {
                "id": 890,
                "user_id": 18977,
                "username": "admin",
                "domain": "workflow.titlenova",
                "route": "\/tasks\/validate",
                "method": "POST",
                "model": "Nova\\Workflow\\Model\\TaskResponse",
                "model_id": "13",
                "action": "updated",
                "old": {
                    "comment": "No online access",
                    "timestamp": "2020-07-24 12:19:32"
                },
                "new": {
                    "comment": null,
                    "timestamp": "2020-07-24 12:29:56"
                },
                "metadata": [],
                "timestamp": "2020-07-24 12:29:56"
            },
            {
                "id": 891,
                "user_id": 97,
                "username": "superadmin",
                "domain": "workflow.titlenova",
                "route": "\/tasks\/validate",
                "method": "POST",
                "model": "Nova\\Workflow\\Model\\TaskResponse",
                "model_id": "11",
                "action": "updated",
                "old": {
                    "comment": "Nope!3333",
                    "timestamp": "2020-07-23 16:34:20"
                },
                "new": {
                    "comment": null,
                    "timestamp": "2020-07-27 15:50:12"
                },
                "metadata": [],
                "timestamp": "2020-07-27 15:50:12"
            }
        ],
        "entry_count": 891,
        "entry_fields": [
            "id",
            "user_id",
            "username",
            "domain",
            "route",
            "method",
            "model",
            "model_id",
            "action",
            "old",
            "new",
            "metadata",
            "timestamp"
        ]
    }

The returned response not only gives you an array of ``entries``, but also returns other pertinent
information regarding the request. In addition to the above request, you can pass some parameters
to fine-tune your request:

+-------------+-----------------------------------------------------------------------------------------+
| **page**    | a page number from which to start the result set                                        |
+-------------+-----------------------------------------------------------------------------------------+
| **limit**   | a value by which to limit the result set                                                |
+-------------+-----------------------------------------------------------------------------------------+
| **sort**    | a flag to sort by a particular field. For example, ``model`` or ``-model`` to sort DESC |
+-------------+-----------------------------------------------------------------------------------------+
| **filter**  | a SQL-like filter string. For example, ``route LIKE /users%``                           |
+-------------+-----------------------------------------------------------------------------------------+
| **fields**  | a comma-separated list of fields to limit which fields are selected                     |
+-------------+-----------------------------------------------------------------------------------------+

*(The "page" value is meant to be utilized in conjunction with the "limit" value, and the length of the
page is calculated by the limit value.)*

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        "https://logs.titlenova.com/audit?filter[]=route%20LIKE%20%2Fusers%"

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
                "route": "\/audit\/1",
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
                    "X-Resource": "audit-logs",
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

There is also a method to return the number of audit log entries in the system:

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        https://logs.titlenova.com/audit/count

.. code-block:: json

    {
        "filter": null,
        "entry_count": 891
    }

That method also supports the above request ``filter`` parameter:

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        "https://logs.titlenova.com/audit/count?filter[]=ip%20LIKE%20127.0.0.%"

.. code-block:: json

    {
        "filter": [
            "route LIKE /users%"
        ],
        "entry_count": 2
    }

And to determine what fields are available for the ``entries`` resource, use the following request:

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        https://logs.titlenova.com/audit/fields

.. code-block:: json

    {
        "entry_fields": [
            "id",
            "user_id",
            "username",
            "domain",
            "route",
            "method",
            "model",
            "model_id",
            "action",
            "old",
            "new",
            "metadata",
            "timestamp"
        ]
    }

Creating an Audit Log Entry
----------------------------

You can create an audit log entry either via a request using an API key or a request using a user
auth token. The requests are the same, except for the endpoint URLs are slightly different.

**Using an API key**

**Endpoint:** ``https://logs.titlenova.com/api/audit``

- Example API Key: *e6861fe5b6d0e911a6764d04de26b0ff0c08c1ce*

.. code-block:: bash

    curl -i -X POST --header "Authorization: Bearer e6861fe5b6d0e911a6764d04de26b0ff0c08c1ce" \
        -d"user_id=1&username=admin&host=auth.titlenova&route=/users" https://logs.titlenova.com/api/audit

**Using a User Auth Token**

**Endpoint:** ``https://logs.titlenova.com/audit``

- Example User Auth Token: *48f97a0e966ec61324e225a5c2140616e6efa093*

.. code-block:: bash

    curl -i -X POST --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        -d"user_id=1&username=admin&route=/users&model=Users&model_id=1&action=created" https://logs.titlenova.com/audit

The result of both requests are the same. They will produce a ``201`` response with a JSON payload of the
newly created log entry.

Deleting Audit Logs
--------------------

**Deleting a single audit log entry**

**Endpoint:** ``https://logs.titlenova.com/audit/<id>``

.. code-block:: bash

    curl -i -X DELETE --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        https://logs.titlenova.com/audit/2

**Deleting multiple audit log entries**

.. code-block:: bash

    curl -i -X DELETE --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        -d"rm_logs[]=3&rm_logs[]=4" https://logs.titlenova.com/audit/

