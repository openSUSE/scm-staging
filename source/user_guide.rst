User Guide
==========

The git packaging workflow is currently an opt-in mechanism for submissions to
openSUSE:Factory via `src.opensuse.org <https://src.opensuse.org>`_ instead of
`OBS <https://build.opensuse.org/>`_. It allows packagers to maintain their
package sources in the `pool <https://src.opensuse.org/pool>`_ organization
instead of on OBS. Submissions are handled via pull requests on
https://src.opensuse.org instead of submit requests on OBS.

A bot has been setup that will automatically forward eligible pull requests as
submitrequests directly to openSUSE:Factory.


Maintainer Guide
----------------

.. hint::
   Consider adjusting the package description to alert contributors that
   ordinary submitrequests are no longer possible and where they should send a
   pull request instead.

To participate in the test drive, modify the development package in the
devel project as follows:

1. Login to https://src.opensuse.org using the openSUSE IDP provider.

2. Checkout your package from the configured devel project from OBS:

.. code-block:: bash

   osc co $(osc develproject openSUSE:Factory $pkgname)

3. Clone your package from https://src.opensuse.org/pool/$pkg_name in a
   temporary location and switch to the ``factory`` branch.

4. Compare your package in git (from step 2) with the package on OBS (from step
   3). If there are differences, fork the package on src.opensuse.org and send a
   pull request to get both in sync.

5. Modify the package meta of the devel package via :command:`osc meta -e pkg
   $develprj $pkgname` by adding the following entry, which will automatically
   synchronize your package from git to OBS. This will also indicate to the
   ``openSUSE:Factory`` team that the package is maintained in git and that
   submitrequests are no longer expected to come from the devel project but via
   the ``scm-staging-bot`` that is mirroring pull requests.

.. code-block:: xml

   <package name="$pkg_name" project="$develprj">
     <!-- snip -->
     <scmsync>https://src.opensuse.org/pool/$pkg_name#factory</scmsync>
   </package>

6. Checkout your package again via (it should now be a git repository):

.. code-block:: bash

   osc co $(osc develproject openSUSE:Factory $pkgname)

7. Pull requests against the ``factory`` branch by a package or project
   maintainer on OBS will automatically get forwarded as submitrequests. Pull
   requests from all other users have to be approved by a maintainer first,
   before a submit request to ``openSUSE:Factory`` is created.

   Note that the ``factory-auto`` bot will decline more than one submission to
   the same package in ``openSUSE:Factory``. You can thus use pull request
   approvals as a selection which pull request to send first.


Contributor Guide
-----------------

1. Install the ``obs-scm-bridge``.

2. Checkout the devel project of the package that you want to contribute to:

.. code-block:: shell-session

   osc co $(osc develproject openSUSE:Factory $pkg_name)

3. Find the package that you want to contribute to on
   https://src.opensuse.org/pool and fork it from the repository
   ``src.opensuse.org/pool/$pkg_name``

4. Add the fork as a git remote to your osc checkout (:command:`osc co` will use
   command:`git` behind the scenes):

.. code-block:: shell-session

   git remote add fork gitea@src.opensuse.org:$username/$pkg_name
   git fetch fork

5. Implement your changes:

.. code-block:: shell-session

   $EDITOR $pkg_name.spec
   osc vc -m "$CLEVER_CHANGELOG_ENTRY" $pkg_name.changes
   git add ... # add the appropriate files
   git commit -m "Insightful message here"

6. Push your changes to your fork:

.. code-block:: shell-session

   git push fork

5. Create a pull request against the ``factory`` branch of the package in
   src.opensuse.org/pool.

6. The user `scm-staging-bot <https://src.opensuse.org/scm-staging-bot>`_ will
   create a submitrequest on OBS for you if your pull request has been approved
   by the package or project maintainer or if you are the package or project
   maintainer.
