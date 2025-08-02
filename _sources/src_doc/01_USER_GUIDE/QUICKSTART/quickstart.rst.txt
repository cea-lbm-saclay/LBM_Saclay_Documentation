.. _Quick-Start:

Quick Start with LBM_Saclay
===========================

.. only:: titania

   .. admonition:: Shared directories for DM2S/STMF users
      :class: important

      TITANIA: two main LBM directories exist
   
         - ``/tmpformation/LBM_Saclay``: free access. You will find the ``html`` version of that documentation; the folder ``run_training_lbm`` which contains several test cases to start running LBM_Saclay; two versions of paraview and several presentations of LBM and phase-field models.

         - ``/home/lbm-saclay``: shared directory for R&D contributors of LBM_Saclay. Send an email to ``alain.cartalade at cea.fr`` or ``teo.boutin at cea.fr`` to get access.

      ORCUS: one shared directory exists

         - ``/tmpformation/LBM_Saclay``: free access. Several versions of LBM_Saclay are already compiled on GPU partitions of ORCUS. You can go directly to :ref:`Simulations-GPU`.

1. Open LBM_Saclay's documentation
----------------------------------

.. admonition:: For training session: LBM_Saclay's documentation
   :class: error

   Open a terminal, copy the file ``bashrc-lbm`` from directory ``/tmpformation/LBM_Saclay/CONFIG`` in your ``/home`` and source it:

      .. code-block:: shell

         $ cp /tmpformation/LBM_Saclay/CONFIG/bashrc-lbm ~/.bashrc
         $ source ~/.bashrc

   Open the documentation

      .. code-block:: shell

         $ lbm-saclay-doc&

   ``lbm-saclay-doc`` is an alias of command ``google-chrome /tmpformation/LBM_Saclay/LBM_Saclay_Doc/_build/html/index.html``
   

2. Create your ``Training-LBM`` directory
-----------------------------------------

.. admonition:: For training session: create a new directory on ``volatile``
   :class: error

   Go to your local disk ``/volatile/formation/``:

    .. code-block:: shell

       $ cd /volatile/formation/

   Make your own directory ``Training-LBM``:

    .. code-block:: shell

       $ mkdir Training-LBM
       $ cd Training-LBM

3. Get the source files of LBM_Saclay
-------------------------------------

A. From git repository (recommended)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Get access to the git repository**

.. admonition:: Get access to the git repository
   
   LBM_Saclay is on the git repository [1]_. To get an access to codev-tuleap, open an **AD EXTRA** account by sending a message on [2]_. For scientists of other institutes (CNRS, INRIA, University, etc.) open an **AD partner** account by sending an email to ``alain.cartalade at cea.fr`` or ``teo.boutin at cea.fr``. Once you got the account, change your password on [3]_.

      .. [1] https://codev-tuleap.cea.fr/plugins/git/lbmsaclay
      .. [2] https://post.intra.cea.fr/sp
      .. [3] https://gestion-ad.intra.cea.fr:9443/

**Download LBM_Saclay**

.. admonition:: Download LBM_Saclay

   To download either the **Training** version or the **Rech-Dev** version, open a terminal (or Konsole) and copy-paste one of two commands below.

   e.g. for ``LBM_Saclay_Training`` version

      .. code-block:: shell

         $ git clone --recursive https://codev-tuleap.cea.fr/plugins/git/lbmsaclay/LBM_Saclay_Training.git

   e.g. for ``LBM_Saclay_Rech-Dev`` version:

      .. code-block:: shell

         $ git clone --recursive https://codev-tuleap.cea.fr/plugins/git/lbmsaclay/LBM_Saclay_Rech-Dev.git

B. From folder ``tmpformation`` for training session
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: For training session
   :class: important

   Copy file ``LBM_Saclay_Rech-Dev.tar``

    .. code-block:: shell

       $ cp /tmpformation/LBM_Saclay/LBM_Saclay_Rech-Dev.tar .

   untar your file

    .. code-block:: shell

       $ tar -xvf LBM_Saclay_Rech-Dev.tar


4. Compilation
--------------

You can run your first simulations on CPUs of your personal desktop. However, it is highly recommended to run LBM_Saclay on one (or better on several) graphic cards. You will find on the links below tutorials for compiling on single-CPU, single-GPU, and multi-GPU.

.. toctree::
   :maxdepth: 1

   ./Compil_MonoGPU.rst
   ./Compil_GPU_MPI_Orcus.rst
   ./Compil_Multi_GPU.rst
   ./Compil_GetInfo_GPU.rst

5. Run your first test case on your local CPU
---------------------------------------------

It is recommended to start with a test case of folder ``run_training_lbm`` and execute on local disk ``/volatile``. For example:

.. admonition:: For training session: local computer
   :class: error

   Copy folder ``run_training_lbm`` on your local disk:

      .. code-block:: shell

         $ cd /volatile/formation/Training-LBM/
         $ cp -r /tmpformation/LBM_Saclay/run_training_lbm .

   Go to one test case, e.g. ``TestCase02_Poiseuille_Water``

      .. code-block:: shell

         $ cd /volatile/formation/Training-LBM/run_training_lbm/TestCase02_Poiseuille_Water

   Run LBM_saclay with the input file ``name.ini``

    .. code-block:: shell

       $ /volatile/formation/Training-LBM/LBM_Saclay_Rech-Dev/build_openmp/src/LBM_saclay TestCase02_Poiseuille_Water.ini

6. Post-processing with Paraview
--------------------------------

The ``.bashrc`` file contains an alias for paraview versions 5.11 and 5.12 in ``/tmpformation/LBM_Saclay``. In paraview, open the ``.vti`` files. For post-processing the ``.h5`` (HDF5) files open the ``.xml`` file and clic on ``XDMF Reader``.

.. admonition:: For training session: post-processing with paraview
   :class: error

   For post-processing ``.xmf`` and ``.h5`` files for videos use paraview11

    .. code-block:: shell
    
       $ paraview11&
    
   For comparison with analytical solutions, use paraview12
   
    .. code-block:: shell
    
       $ paraview12&
   
   and follow tutorials presented in :ref:`Run_Training-LBM`.

7. Help and Support
-------------------

On weblink [4]_ open a ``NEW ID_LBM`` and explain your problem.

.. [4] https://codev-tuleap.cea.fr/plugins/tracker/?tracker=1870

.. sectionauthor:: Alain Cartalade