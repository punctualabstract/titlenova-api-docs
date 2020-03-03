Overview
========

Introduction
------------

TitleNova is a new generation of title software that represents a distributed system of applications,
each with a specific purpose that all work together to deliver a modern title platform solution.
At the core of TitleNova is a series of REST-based APIs with which application clients can interact
to procure and transmit all the necessary data and files involved in a title transaction.

In this documentation, you will find direction and examples of how to utilize the TitleNova APIs.
All of the APIs require authentication via a bearer token that is obtained from the authentication API.
With a few exceptions, all of the APIs will respond with a JSON payload. The storage API may respond
with actual file data content if the corresponding request is made, and the TitleNova schema standard
utilized within the TitleNova ecosystem supports both JSON and XML requests and responses in an effort
to achieve compatibility with other external application systems for integration purposes.

For the examples given in the documentation below, cURL is used as a simple example, but any basic
client, such as **Postman**, should work to execute the examples as well.

