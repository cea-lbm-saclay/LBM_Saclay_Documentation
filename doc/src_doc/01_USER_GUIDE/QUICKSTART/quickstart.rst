.. _Quick-Start:

Quick Start with LBM_Saclay
===========================

1. LBM_Saclay's environment & documentation
-------------------------------------------

.. tab-set::

   .. tab-item:: For DM2S/STMF users

      .. only:: titania

         .. admonition:: Shared directories for DM2S/STMF users
            :class: important

            TITANIA: two main LBM directories exist
   
            - ``/tmp_formation/LBM_Saclay``: free access. You will find the ``html`` version of that documentation; the folder ``run_training_lbm`` which contains several test cases to start running LBM_Saclay; two versions of paraview and several presentations of LBM and phase-field models.

            - ``/home/lbm-saclay``: shared directory for R&D contributors of LBM_Saclay. Send an email to ``alain.cartalade at cea.fr`` or ``teo.boutin at cea.fr`` to get access.

            ORCUS: one shared directory exists

            - ``/tmp_formation/LBM_Saclay``: free access. Several versions of LBM_Saclay are already compiled on GPU partitions of ORCUS. You can go directly to :ref:`Simulations-GPU`.

      .. admonition:: For training session: LBM_Saclay's documentation
         :class: error

         1. Open a terminal, and execute the command below for LBM_Saclay's environment:

            .. code-block:: shell

               $ source /tmp_formation/LBM_Saclay/lbm-env.sh

          The shell script ``lbm-env.sh`` copies in your ``home`` a ``.bashrc`` and ``.profile`` for necessary paths and connexions. The script also copies the source files of LBM_Saclay and the folder of test cases ``run_training_lbm`` inside your ``/home/train``.

         2. Open the LBM_Saclay's documentation

            .. code-block:: shell

               $ lbm-doc.sh &

          ``lbm-doc.sh`` is an alias of command ``google-chrome https://cea-lbm-saclay.github.io/LBM_Saclay_Documentation/index.html``

         3. Either a. or b./c.

          a. For SMEMaG LBM training go to the red box of :ref:`Compilation-CPU-SMEMaG`
          b. For Sorbonne University students go to :ref:`Simulations-GPU`
          c. For INSTN "Two-phase" training go to :ref:`Simulations-GPU`
   
   .. tab-item:: For other users

      To be completed


2. Get the source files of LBM_Saclay
-------------------------------------

.. tab-set::

   .. tab-item:: From folder ``tmp_formation`` for training session

      .. admonition:: For training session
         :class: important

         Copy file ``LBM_Saclay_Rech-Dev.tar``

          .. code-block:: shell

             $ cp /tmp_formation/LBM_Saclay/LBM_Saclay_Rech-Dev.tar .

         untar your file

          .. code-block:: shell

             $ tar -xvf LBM_Saclay_Rech-Dev.tar

         


   .. tab-item:: From git repository (recommended)

      **Get access to the git repository on** ``codev-tuleap.cea.fr``

      .. dropdown::
         :icon: comment

         .. admonition:: Get access to the git repository
   
            LBM_Saclay is on the git repository [1]_. To get an access to codev-tuleap, open an **AD EXTRA** account by sending a message on [2]_. For scientists of other institutes (CNRS, INRIA, University, etc.) open an **AD partner** account by sending an email to ``alain.cartalade at cea.fr`` or ``teo.boutin at cea.fr``. Once you got the account, change your password on [3]_.

               .. [1] https://codev-tuleap.cea.fr/plugins/git/lbmsaclay
               .. [2] https://post.intra.cea.fr/sp
               .. [3] https://gestion-ad.intra.cea.fr:9443/

      **Download LBM_Saclay**

      .. admonition:: Download LBM_Saclay

         To download either the **Training** version or the **Rech-Dev** version, open a terminal (or Konsole) and copy-paste one of two commands below:

         e.g. for ``LBM_Saclay_Rech-Dev`` version:

            .. code-block:: shell

               $ git clone --recursive https://codev-tuleap.cea.fr/plugins/git/lbmsaclay/LBM_Saclay_Rech-Dev.git

         e.g. for ``LBM_Saclay_Training`` version

            .. code-block:: shell

               $ git clone --recursive https://codev-tuleap.cea.fr/plugins/git/lbmsaclay/LBM_Saclay_Training.git

.. _Compilation-CPU-SMEMaG:

3. Compilation
--------------

You can run your first simulations on CPUs of your personal desktop. However, it is highly recommended to run LBM_Saclay on one (or better on several) graphic cards (GPUs). You will find the procedure for compiling on single-CPU, single-GPU, and multi-GPU.

.. admonition:: Makefile on CPU of local computer
   :class: error

   - For openmp  (``omp``) on CPU

    Go to ``LBM_Saclay`` folder

    .. code-block:: shell

       $ cd LBM_Saclay_Rech-Dev

    and execute the ``configure_build.sh`` script to create the ``makefile``

    .. code-block:: shell

       $ ./compilation/local/omp/configure_build.sh

will return:

.. code-block:: shell

   The following problems are currently implemented:
   0  AC
   1  Advection-Diffusion
   2  Crystal_growth_Younsi
   3  GPMixt
   4  GPMixtNS
   5  GPMixtTernary
   6  GPMuTernary
   7  MPwSLphC
   8  NS
   9  NS_3phases_1comp_phase_change
   10 NSAC_Comp
   11 NSAC_Comp_3phases
   12 NSAC_Comp_3phases3D
   13 NSAC_coupling
   14 NSAC_Fakhari
   15 NSAC_Surfactant
   Choose which problems to include by indicating a list of space or comma separated numbers, eg '0 1' or '0,1'.
   Write 'all' to include all problems.
   Problem numbers:

.. admonition:: Compilation
   :class: error

   Write ``10`` for ``NSAC_Comp`` kernel

    .. code-block:: shell

       Problem numbers: 10

   Go to the directory that is indicated by the green link, e.g., if number ``10`` has been set for GPU:

    .. code-block:: shell

       $ cd LBM_Saclay_Rech-Dev/build_omp/build_NSAC_Comp

   Compile:

    .. code-block:: shell

       $ make -j 22

.. dropdown::
   :icon: comment
   
   .. tab-set::

      .. tab-item:: With script ``configure_build.sh``

         .. admonition:: Makefile on GPU
         
            - For cuda on GPU H100 of ORCUS

             .. code-block:: shell

                ./compilation/orcus/cuda_h100/configure_build.sh

             For GPU A100 and V100, modify only ``cuda_h100`` by ``cuda_a100`` (A100) or ``cuda_v100`` (V100)

            - For cuda on A6000 of MANWE

             .. code-block:: shell

                ./compilation/manwe/cuda_a6000/configure_build.sh


         .. admonition:: Compilation errors
            :class: important

            For compilation errors, it is useful to write the exits inside an output file e.g. ``compil.log``:

             .. code-block:: shell

                $ make -j 22 2>&1 | tee compil.log

            or alternatively ``compil2.log``

             .. code-block:: shell

                $ make VERBOSE=1 2>&1 | tee compil2.log

      .. tab-item:: Sections for detailed procedure

         .. toctree::
            :maxdepth: 1

            ./Compil_MonoGPU.rst
            ./Compil_GPU_MPI_Orcus.rst
            ./Compil_Multi_GPU.rst
            ./Compil_GetInfo_GPU.rst

4. Run your first test case on your local CPU
---------------------------------------------

It is recommended to start with a test case of folder ``run_training_lbm`` and execute on local disk ``/volatile``. For example:

.. admonition:: For training session: local computer
   :class: error

   Go to one test case of ``run_training_lbm``, e.g. ``TestCase01_Poiseuille_Water``:

      .. code-block:: shell

         $ cd ~/run_training_lbm/TestCase01_Poiseuille_Water

   Run LBM_saclay with the input file ``name.ini``

    .. code-block:: shell

       $ ~/LBM_Saclay_Rech-Dev/build_omp/build_NSAC_Comp/src/LBM_saclay TestCase01_Poiseuille_Water.ini

5. Post-processing with Paraview
--------------------------------

The ``.bashrc`` file contains an alias for paraview versions 5.11 and 5.12 in ``/tmp_formation/LBM_Saclay``. In paraview, open the ``.vti`` files. For post-processing the ``.h5`` (HDF5) files open the ``.xml`` file and clic on ``XDMF Reader``.

.. admonition:: For training session: post-processing with paraview
   :class: important

   For post-processing ``.xmf`` and ``.h5`` files for videos use paraview11

    .. code-block:: shell
    
       $ paraview11&
    
   For comparison with analytical solutions, use paraview12
   
    .. code-block:: shell
    
       $ paraview12&
   
   and follow tutorials presented in :ref:`Run_Training-LBM`.

6. Help and Support
-------------------

On weblink [4]_ open a ``NEW ID_LBM`` and explain your problem.

.. [4] https://codev-tuleap.cea.fr/plugins/tracker/?tracker=1870

.. sectionauthor:: Alain Cartalade