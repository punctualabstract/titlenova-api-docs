Scope
=====

Under the authentication API, scope is the relationship between users, roles and the permissions
of what actions they are allowed to perform on certain resources. With this API, you can manage
scope on a broader role-level or on a more granular user-level.

**Please note:** *By default, all users and roles are denied everything unless there is an explicit scope rule added.*

Get a Role Scope
----------------

To obtain a role's scope, send the following ``GET`` request:

**Endpoint:** ``https://auth.titlenova.com/scope/role/<id>``.

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        https://auth.titlenova.com/scope/role/1

and the ``JSON`` payload below will be returned:

.. code-block:: json

    {
        "scope": {
            "users": {
                "index": true,
                "count": true,
                "fields": true,
                "create": true,
                "update": true,
                "delete": true,
                "history": true,
                "exists": true,
                "validate": true,
                "revoke": true
            },
            "roles": {
                "index": true,
                "count": true,
                "fields": true,
                "create": true,
                "update": true,
                "delete": true,
                "history": true
            },
            "resources": {
                "index": true,
                "count": true,
                "fields": true,
                "create": true,
                "update": true,
                "delete": true,
                "history": true
            }
        }
    }

You can view the scope as a more "flat" model by passing the ``flat=1`` query parameter:

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        https://auth.titlenova.com/scope/role/1?flat=1

and the ``JSON`` response will look like:

.. code-block:: json

    {
        "scope": {
            "1": {
                "id": 1,
                "role_id": 1,
                "role": "Admin",
                "resource_id": 1,
                "resource": "users",
                "action": "index",
                "permission": 1
            },
            "2": {
                "id": 2,
                "role_id": 1,
                "role": "Admin",
                "resource_id": 1,
                "resource": "users",
                "action": "count",
                "permission": 1
            },
            "3": {
                "id": 3,
                "role_id": 1,
                "role": "Admin",
                "resource_id": 1,
                "resource": "users",
                "action": "fields",
                "permission": 1
            }
        }
    }

Get a User Scope
----------------

To obtain the current user's scope (based on the current valid auth token), send the following
``GET`` request:

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        https://auth.titlenova.com/scope

and the ``JSON`` payload below will be returned:

.. code-block:: json

    {
        "scope": {
            "users": {
                "index": true,
                "count": true,
                "fields": true,
                "create": true,
                "update": true,
                "delete": true,
                "history": true,
                "exists": true,
                "validate": true,
                "revoke": true
            }
        }
    }

You can view the scope as a more "flat" model by passing the ``flat=1`` query parameter:

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        https://auth.titlenova.com/scope?flat=1

and the ``JSON`` response will look like:

.. code-block:: json

    {
        "scope": {
            "1": {
                "id": 1,
                "role_id": 1,
                "role": "Admin",
                "resource_id": 1,
                "resource": "users",
                "action": "index",
                "permission": 1
            },
            "2": {
                "id": 2,
                "role_id": 1,
                "role": "Admin",
                "resource_id": 1,
                "resource": "users",
                "action": "count",
                "permission": 1
            },
            "3": {
                "id": 3,
                "role_id": 1,
                "role": "Admin",
                "resource_id": 1,
                "resource": "users",
                "action": "fields",
                "permission": 1
            }
        }
    }

Users can have specific scope settings that override the scope settings of their roles. If you want to
list any user-specific scope settings only, send the following ``GET`` request:

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        https://auth.titlenova.com/scope?all=0

By the default the ``all`` parameter is set to 1 to return both the role- and user-specific scope.
Setting that to 0 will only return any user-specific scope:

.. code-block:: json

    {
        "scope": {
            "contacts": {
                "index": false
            }
        }
    }

The ``all`` parameter also works in conjunction with the ``flat`` parameter:

.. code-block:: json

    {
        "scope": {
            "176": {
                "id": 176,
                "role_id": null,
                "user_id": 1,
                "resource_id": 18,
                "action": "index",
                "permission": 0,
                "resource": "contacts"
            }
        }
    }

To obtain another user's scope based on user ID, the same ``GET`` requests and parameters are available
at this end point:

**Endpoint:** ``https://auth.titlenova.com/scope/user/<id>``.

Create Role Scope
-----------------

To create a new scope for a role, use the following ``PUT`` request below:

**Endpoint:** ``https://auth.titlenova.com/scope/role/<id>``

The layout of the data is such that there is a list of ``resource_id_<i>``, ``action_<i>`` and ``permission_<i>``, where
``<i>`` is an incremental integer to keep the data grouped together correctly.

.. code-block:: text

    resource_id_1 = 1
    action_1 = index
    permission_1 = 1

    resource_id_2 = 1
    action_2 = create
    permission_2 = 1

    resource_id_3 = 1
    action_3 = update
    permission_3 = 0

    resource_id_4 = 1
    action_4 = delete
    permission_4 = 0

.. code-block:: bash

    curl -i -X PUT --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        -d"resource_id_1=1&action_1=index&permission_1=1&resource_id_2=1&action_2=create&permission_2=1&resource_id_3=1&action_3=update&permission_3=0&resource_id_4=1&action_4=delete&permission_4=0" \
        https://auth.titlenova.com/scope/role/3

Assuming the users resource ID of 1, the above request will allow the role of ID 3 to index and create users, but
not allow it to update or delete users.

Upon success, the ``JSON`` payload returned will look like this:

.. code-block:: json

    {
        "users": {
            "index": true,
            "create": true
        }
    }

Create User Scope
-----------------

User scope can be created in the same method as outlined above using a ``PUT`` request to the following endpoint:

**Endpoint:** ``https://auth.titlenova.com/scope/user/<id>``

The creates a specific overriding scope for a user. For example, if a role allows users to delete pages,
but there is only one user under that role that should not be allowed to delete pages, you can add a user-specific
scope rule to deny only that user from deleting pages. That rule will supersede the scope rule on the role level.

Adding to Scope
---------------

To add to a role or user scope, use a ``PATCH`` request to the following endpoints, respectively:

| **Endpoints:**
| ``https://auth.titlenova.com/scope/role/<id>``
| ``https://auth.titlenova.com/scope/user/<id>``

A single request can only add one scope rule per request:

.. code-block:: bash

    curl -i -X PATCH --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        -d"resource_id=18&action=create&permission=0" https://auth.titlenova.com/scope/role/2

On success, the returned ``JSON`` response will look like this:

.. code-block:: json

    {
        "role_id": "2",
        "user_id": null,
        "resource_id": "18",
        "action": "create",
        "permission": 0,
        "id": 180
    }

Deleting Scope Rules
--------------------

You can delete individual scope rules to remove certain rules and permissions from a role or user's scope.

**Deleting a single scope rule**

**Endpoint:** ``https://auth.titlenova.com/scope/permissions/<id>``

.. code-block:: bash

    curl -i -X DELETE --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        https://auth.titlenova.com/scope/permissions/180

**Deleting multiple scope rules**

.. code-block:: bash

    curl -i -X DELETE --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        -d"rm_permissions[]=180&rm_permissions[]=181" https://auth.titlenova.com/scope/permissions/

Clearing Scope
--------------

You can clear all scope rules for a role or user by submitting a ``DELETE`` request to these end points,
respectively:

| **Endpoints:**
| ``https://auth.titlenova.com/scope/user/<id>``
| ``https://auth.titlenova.com/scope/role/<id>``

.. code-block:: bash

    curl -i -X DELETE --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        https://auth.titlenova.com/scope/role/1
.. code-block:: bash

    curl -i -X DELETE --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        https://auth.titlenova.com/scope/user/1
