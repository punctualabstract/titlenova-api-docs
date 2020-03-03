Auth API
========

The authentication API is a centralized authentication and authorization API with which all TitleNova
applications interact to request and maintain a valid authenticated session. The authentication API
utilizes a custom token-based authentication system that enforces not only authentication
but also authorization and resource access via defined user and role scopes.

You can check the version of the authentication API at any time with the following `GET` request:

.. code-block:: bash

    curl -i -X GET --header "Authorization: Bearer 48f97a0e966ec61324e225a5c2140616e6efa093" \
        https://auth.titlenova.com/version

The above request will return the following response:

.. code-block:: json

    {
        "version": "0.0.3"
    }

.. toctree::
    :maxdepth: 1

    auth
    users
    roles
    resources
    scope
