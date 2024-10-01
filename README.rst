SCM Staging
===========

This project contains helper libraries & tools to automatically create submit
requests and eventually a full staging workflow from pull requests in gitea.


Requirements
------------

for development:

- Python 3.11 or later
- `poetry <https://python-poetry.org/>`_

for deployment:

- A machine with a public IP
- A container runtime of your choice


Setup
-----

1. Clone this repository

.. code-block::

   git clone https://github.com/openSUSE/scm-staging

2. Build the container:

.. code-block::

   buildah bud --layers -t webhook -f Dockerfile.webhook .

3. Create the json configuration file. It contains a single list of objects,
   where each object configures the behavior of the bot for one organization on
   gitea. Each of these objects has the following contents (the keys
   ``require_approval``, ``submission_style``, ``merge_pr`` and
   ``project_prefix`` are optional), the keys are defined in the class
   :py:class:`~scm_staging.config.BranchConfig`:

.. code-block::

   {
     "target_branch_name": "factory",
     "organization": "rpm",
     "destination_project": "openSUSE:Factory",
     "merge_pr": false,
     "submission_style": "factory_devel",
     "require_approval": true,
     "project_prefix": "devel:scm"
   }

4. Launch the container:

.. code-block::

   podman run -d -e "GITEA_API_KEY=$YOUR_API_KEY"      \
                 -e "OSC_USER=$YOUR_OBS_ACCOUNT"       \
                 -e "OSC_PASSWORD=$YOUR_OBS_PASSWORD"  \
                 -p 8000:8000                          \
                 --name webhook                        \
                 -v /path/to/config/scm_staging:/src:z \
                 localhost/webhook:latest


5. Go to your dist-git repository on https://src.opensuse.org and add a
   webhook with the url ``$YOUR_HOST_IP/hook:8000``. Or add it for a whole
   organization or the full gitea instance.
