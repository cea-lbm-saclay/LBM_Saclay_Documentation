.. include:: ../Substitutions.rst

.. _Git-Commands:

Before programming: create a new branch from master
---------------------------------------------------

:mediumbold:`Download one version of LBM_Saclay`

For example here ``LBM_Saclay_Rech-Dev`` version, the command ``git clone``

   .. code-block:: shell

      $ git clone --recursive https://codev-tuleap.cea.fr/plugins/git/lbmsaclay/LBM_Saclay_Rech-Dev.git


   
:mediumbold:`Check your current branch`

   .. admonition:: Check your current branch
      :class: hint

      Once the download is complete, go to ``LBM_Saclay_Rech-Dev`` directory
         
      .. code-block:: shell

         $ cd LBM_Saclay_Rech-Dev
         $ git status

   returns:

   .. code-block:: ruby

      Sur la branche master
      Votre branche est a jour avec 'origin/master'.

      rien a valider, la copie de travail est propre

   means that you are currently on the ``master``.

:mediumbold:`Create a new branch`

   .. admonition:: Create a new branch
      :class: hint

      1. Create a new branch, example name of the new branch ``dev/alain.cartalade``

         .. code-block:: shell

            $ git branch dev/alain.cartalade

      2. Move on that new branch

         .. code-block:: shell

            $ git checkout dev/alain.cartalade

      3. Check

         .. code-block:: shell

            $ git status

:mediumbold:`Move on one existing branch`

   .. admonition:: Move on one existing branch
      :class: hint

      Example to move on one existing branch ``dev/hoel.keraudren``

         .. code-block:: shell

            $ git checkout dev/hoel.keraudren

:mediumbold:`Copy and rename one existing branch`

   .. admonition:: Copy one existing branch
      :class: hint

      Example to copy and rename one existing branch e.g. ``development``

      1. Basculement sur la branche ``development``

         .. code-block:: shell

            $ git checkout development

      2. New branch ``dev/alain.cartalade`` copied from ``development`` + switch

         .. code-block:: shell

            $ git checkout -b dev/alain.cartalade

      3. Create the new branch on Tuleap + link to the local one

         .. code-block:: shell

            $ git push -u origin dev/alain.cartalade

      4. You can start your developments on your branch.

:mediumbold:`Synchronize your branch with master`

   .. admonition:: Synchronize your branch with master
      :class: hint

         .. code-block:: shell

            $ git fetch
            $ git merge origin/master

.. _Push-Implementation:

After programming: push your developments
-----------------------------------------

Check the modifications on the current branch

   .. code-block:: shell

      $ git status

:mediumbold:`Add your comment and push your developments`

   .. admonition:: Add, comment and push
      :class: hint

         .. code-block:: shell

            $ git add * (or -all)       # add new modifications
            $ git commit -m "comment"   # add new comments related to modifications
            $ git push                  # push modifications on git

      If your new branch ``dev/firstname.name`` does not exist on the git repository, replace ``git push`` by

         .. code-block:: shell

            $ git push -u origin dev/firstname.name

Compilation and run
-------------------

For ORCUS, follow the instructions:

.. toctree::
   :maxdepth: 1

   ../01_USER_GUIDE/QUICKSTART/Compil_GPU_MPI_Orcus.rst

For project admin
-----------------

**Merge branch dev/firstname.name**

   .. admonition:: Merge one branch in master
      :class: hint

      Stay on branch master and merge the branch you want:

         .. code-block:: shell

            $ git merge origin/dev/aurelien.laurens
            $ git add *
            $ git commit -m "Merge branche dev/aurelien.laurens"
            $ git push

**Cancel your last commit**

   .. admonition:: Merge one branch in master
      :class: hint

         .. code-block:: shell

            $ git status
            $ git reset --hard HEAD~1
            $ git push --force

.. sectionauthor:: Alain Cartalade
   