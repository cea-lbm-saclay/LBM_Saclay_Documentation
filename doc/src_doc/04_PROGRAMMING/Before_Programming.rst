Before programming: create a new branch from master
---------------------------------------------------

**Download one version of LBM_Saclay**

For example here ``LBM_Saclay_Rech-Dev`` version, the command ``git clone``

   .. code-block:: shell

      $ git clone --recursive https://codev-tuleap.cea.fr/plugins/git/lbmsaclay/LBM_Saclay_Rech-Dev.git


   
**Check your current branch**

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

**Create a new branch**

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

**Move on one existing branch**

   .. admonition:: Move on one existing branch
      :class: hint

      Example to move on one existing branch ``dev/hoel.keraudren``

         .. code-block:: shell

            $ git checkout dev/hoel.keraudren

**Copy and rename one existing branch**

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

After programming: push your developments
-----------------------------------------

Check the modifications on the current branch

   .. code-block:: shell

      $ git status

**Add your comment and push your developments**

   .. admonition:: Add, comment and push
      :class: hint

         .. code-block:: shell

            $ git add * (or -all)       # add new modifications
            $ git commit -m "comment"   # add new comments related to modifications
            $ git push                  # push modifications on git

Compilation and run
-------------------

For ORCUS, follow the instructions:

.. toctree::
   :maxdepth: 1

   ../01_USER_GUIDE/QUICKSTART/Compil_GPU_MPI_Orcus.rst

.. sectionauthor:: Alain Cartalade
   