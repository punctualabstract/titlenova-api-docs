Logging API
===========

The logging API is a robust logging application that handles the following logs:

.. toctree::
    :maxdepth: 1

    access_logs
    error_logs
    audit_logs
    event_logs

Logs are only created at the point where the application resource fires off the
request to create the log entry. Outside of that, logs can only be retrieved for
review or deleted out of the system.