Authentication
==============

The authentication API is a centralized authentication and authorization API with which all TitleNova
applications interact to request and maintain a valid authenticated session. The authentication API
utilizes a custom token-based authentication system that enforces not only authentication
but also authorization and resource access via defined user and role scopes.

Obtain Authentication Token
---------------------------

To authenticate a user, a `POST` call can be made with a `username` and `password` value:

.. code-block:: bash

    curl -X POST -d"username=admin&password=password" https://auth.titlenova.com/


That returned response will return the following payload with the token and other necessary information:

.. code-block:: json

    {
        "user_id": 1,
        "username": "admin",
        "token": "48f97a0e966ec61324e225a5c2140616e6efa093",
        "refresh": "93ef615b4b6968802411a96b898af50ef9fa0ec1",
        "expires": 1576875495,
        "scope_updated": null,
        "password_expires": "2020-04-07 15:42:09"
    }

The refresh token is essential to maintaining a valid session. The `expires` value is a UNIX timestamp
that designates when the token will expire. Once the token expires, any requests made with it will result
in a `401 Unauthorized` response.

Refresh the Authentication Token
--------------------------------

When a client application needs to obtain a new authentication token, a request can be made via `POST`
using the expired authentication token and the refresh token that was returned on the initial
authentication request:

.. code-block:: bash

    curl -X POST --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        -d"refresh=93ef615b4b6968802411a96b898af50ef9fa0ec1" \
        https://auth.titlenova.com/token/refresh

The response will be returned with a new authentication token and expiration value:

.. code-block:: json

    {
        "token": "b8baba77fbddadec73ab84e08b81bc779219341e",
        "refresh": "93ef615b4b6968802411a96b898af50ef9fa0ec1",
        "expires": 1580508359
    }

Validate the Authentication Token
---------------------------------

To validate the authentication token and verify if it has expired or not, the following `POST`
request can be made:

.. code-block:: bash

    curl -i -X POST \
        --header "Authorization: Bearer b8baba77fbddadec73ab84e08b81bc779219341e" \
        https://auth.titlenova.com/token

and, if valid, a `200 OK` response will be returned with a JSON payload containing the basic user
and token information:

.. code-block:: json

    HTTP/1.1 200 OK
    Date: Fri, 31 Jan 2020 21:55:16 GMT
    Content-Length: 101
    Content-Type: application/json

    {
        "user_id": 1,
        "username": "admin",
        "expires": 1580509494,
        "scope_updated": null
    }

If the token is not valid, a `401 Unauthorized` will be returned.

Authorize a User
----------------

Once a user’s identity is authenticated, the API provides an end point to allow client applications
to authorize a user’s request for permission to perform an action on a resource. A user may be
authenticated, but may not have permission to, for example, create other users. If that is the case,
a `403 Forbidden` response would be returned.

Authorization of a user is also a way to perform both a token validation and an user authorization at
the same time. For flexibility, there are 3 different ways to authorize a user with the authorization
endpoint via a POST request:

* Form Data
* Query Data
* HTTP Headers

**Using Form Data:**

.. code-block:: bash

    curl -i -X POST \
        --header "Authorization: Bearer b8baba77fbddadec73ab84e08b81bc779219341e" \
        -d"resource=users&permission=create" https://auth.titlenova.com/authorize

**Using Query Data:**

.. code-block:: bash

    curl -i -X POST \
        --header "Authorization: Bearer b8baba77fbddadec73ab84e08b81bc779219341e" \
        "https://auth.titlenova.com/authorize?resource=users&permission=create"

**Using HTTP Headers:**

.. code-block:: bash

    curl -i -X POST \
        --header "Authorization: Bearer b8baba77fbddadec73ab84e08b81bc779219341e" \
        --header "X-Resource: users" --header "X-Permission: create" \
        https://auth.titlenova.com/authorize

All 3 of the above requests will yield the same response. If the token is valid and user is authorized
to create users, the response will be a `200 OK` and include a JSON payload describing the user:

.. code-block:: json

    HTTP/1.1 200 OK
    Date: Fri, 31 Jan 2020 23:19:11 GMT
    Content-Length: 117
    Content-Type: application/json

    {
        "user_id": 1,
        "username": "admin",
        "scope_updated": null,
        "roles": {
            "1": "Admin"
        }
    }

However, the user is not authorized to create users, the response will be a `403 Forbidden`:

.. code-block:: json

    HTTP/1.1 403 Forbidden
    Date: Fri, 31 Jan 2020 23:19:21 GMT
    Content-Length: 49
    Content-Type: application/json

    {
        "code": 403,
        "message": "Forbidden"
    }

And if the token is not valid, the response will be a `401 Unauthorized`:

.. code-block:: json

    HTTP/1.1 401 Unauthorized
    Date: Fri, 31 Jan 2020 23:22:53 GMT
    Content-Length: 52
    Content-Type: application/json

    {
        "code": 401,
        "message": "Unauthorized"
    }

If no resource or permission is provided on the request, then the authorization end point will only
validate the token and return a `200 OK` or a `401 Unauthorized`, depending on whether the token is valid.

Revoke the Authentication Token
-------------------------------

To end a user’s session, or log them out, a revoke request is issued via `POST`:

.. code-block:: bash

    curl -i -X POST \
        --header "Authorization: Bearer b8baba77fbddadec73ab84e08b81bc779219341e" \
        https://auth.titlenova.com/token/revoke

If the token is valid, it would be deleted, rendering it no longer valid for any further requests.
A successful response from revoking the token will be a `204 No Content`.

.. toctree::
    :maxdepth: 1

    users
    roles
    resources
    scope
