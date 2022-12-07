SCM Staging
===========

This project contains helper libraries & tools to automatically create submit
requests and eventually a full staging workflow from pull requests in gitea.


Requirements
------------

- Python 3.10 or later
- `poetry <https://python-poetry.org/>`_

- A machine with a public IP


Setup
-----

1. Clone this repository
2. Export the environment variables ``OSC_USER`` and ``OSC_PASSWORD`` containing
   your OBS credentials.
3. Launch the application via :command:`poetry run uvicorn scm_staging:app --reload --host 0.0.0.0`
4. Go to your dist-git repository on https://gitea.opensuse.org and add a
   webhook with the url `$YOUR_HOST_IP/hook:8000`

Structure
---------
