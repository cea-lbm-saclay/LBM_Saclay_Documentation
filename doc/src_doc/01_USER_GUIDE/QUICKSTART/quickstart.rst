.. _Quick-Start:

Quick Start with LBM_Saclay 
===========================

1. LBM_Saclay's environment & documentation
-------------------------------------------

.. tab-set::

   .. tab-item:: For LBM Training session

      .. admonition:: For training session: LBM_Saclay's documentation
         :class: error

         1. Open a terminal, and execute the command below for LBM_Saclay's environment:

            .. code-block:: shell

               $ source /tmp_formation/LBM_Saclay/lbm-env.sh

          The shell script ``lbm-env.sh`` copies in your ``/home/train`` a ``.bashrc`` and ``.profile`` for necessary paths and connexions. The script also copies the source files of LBM_Saclay and the folder of test cases ``run_training_lbm`` inside your ``/home/train``. The script will also generate a ``ssh-keygen`` for your future connexion on Orcus (details in dropdown below).

            .. dropdown:: 
               :icon: comment

               For future connexion on Orcus, the script ``lbm-env.sh`` execute two ``ssh`` commands.
            
               1. For the first one

                  .. code-block:: shell

                     ssh-keygen -t rsa -f ~/.ssh/id_rsa

                simply answer with empty responses (``return`` & ``return``).

               2. For the second one

                  .. code-block:: shell

                     ssh-copy-id -i ~/.ssh/id_rsa.pub orcusloginamd2

                write your ``password`` of your login & ``return``.

         2. Open the LBM_Saclay's documentation

            .. code-block:: shell

               $ lbm-doc.sh &

          ``lbm-doc.sh`` is an alias of command ``google-chrome https://cea-lbm-saclay.github.io/LBM_Saclay_Documentation/index.html``

         3. Either a. or b./c.

          a. For SMEMaG LBM training go to the red box of :bdg-ref-primary-line:`Compilation-CPU-SMEMaG`
          b. For Sorbonne University students go to :bdg-ref-primary-line:`Simulations-GPU`
          c. For INSTN "Two-phase" training go to :bdg-ref-primary-line:`Simulations-GPU`
   
   .. tab-item:: For STMF interns
      
      .. admonition:: Shared directories for DM2S/STMF users
         :class: important

         **TITANIA/OBERON**: two main LBM directories exist
   
            - ``/tmp_formation/LBM_Saclay``: free access. You will find the folder ``run_training_lbm`` which contains several test cases to start running LBM_Saclay; two versions of paraview and several presentations of LBM and phase-field models.

            - ``/home/lbm-saclay``: shared directory for R&D contributors of LBM_Saclay. Send an email to ``alain.cartalade at cea.fr`` or ``teo.boutin at cea.fr`` to get access.

         **ORCUS**: one shared directory exists

            - ``/tmpformation/LBM_Saclay``: free access. One version of LBM_Saclay (kernel ``NSAC_Comp``) is compiled for several graphic cards available on ORCUS (V100, A100 and H100). 

            - First simulations on ORCUS: you can go directly to :bdg-ref-primary-line:`Simulations-GPU` and follow the instructions.

      .. admonition:: Configuration
         :class: error

         1. Get access to the directory ``/home/lbm-saclay``

         2. Open a terminal, and execute the command below for LBM_Saclay's environment:

          .. code-block:: shell

             $ source /home/lbm-saclay/INTERN-START/CONFIG/configure.sh

          The shell script ``configure.sh`` copies in your ``home`` a ``.bashrc`` and ``.profile`` for necessary paths and connexions. The script also copies the ``texmf`` and ``layouts`` for Beamer presentations.

         3. Open the LBM_Saclay's documentation

          .. code-block:: shell

             $ lbm-doc.sh &

          ``lbm-doc.sh`` is an alias of command ``google-chrome https://cea-lbm-saclay.github.io/LBM_Saclay_Documentation/index.html``

         
   .. tab-item:: For other users

      To be completed

.. _Get-Access-Repository:

2. Get the source files of LBM_Saclay
-------------------------------------

.. tab-set::

   .. tab-item:: From codev-tuleap repository (recommended)

      

      **Get access to the git repository on** ``codev-tuleap.cea.fr``

      .. admonition:: Get access to the git repository
   
         - The lastest version of LBM_Saclay is available on the git repository :bdg-link-success-line:`codev-tuleap.cea.fr <https://codev-tuleap.cea.fr/plugins/git/lbmsaclay>`.
         
         - To get an access to ``codev-tuleap``, open an **AD partner** account by sending a message on :bdg-link-success-line:`https://post.intra.cea.fr/sp`.
         
         - For scientists of other institutes (CNRS, INRIA, University, etc.) send an email to ``alain.cartalade at cea.fr`` or ``teo.boutin at cea.fr``. Once you got the account, change your password on :bdg-link-success-line:`https://gestion-ad.intra.cea.fr:9443/`.

         - Help and support: on weblink :bdg-link-success-line:`Trackers > Suivi des I.D. LBM <https://codev-tuleap.cea.fr/plugins/tracker/?tracker=1870>` open a ``NEW ID_LBM`` and explain your problem.

      **Download LBM_Saclay**

      .. admonition:: Download LBM_Saclay

         To download either the **Training** version or the **Rech-Dev** version, open a terminal (or Konsole) and copy-paste one of two commands below:

         e.g. for ``LBM_Saclay_Rech-Dev`` version:

            .. code-block:: shell

               $ git clone --recursive https://codev-tuleap.cea.fr/plugins/git/lbmsaclay/LBM_Saclay_Rech-Dev.git

         e.g. for ``LBM_Saclay_Training`` version

            .. code-block:: shell

               $ git clone --recursive https://codev-tuleap.cea.fr/plugins/git/lbmsaclay/LBM_Saclay_Training.git

   .. tab-item:: From folder ``/tmp_formation``

      .. admonition:: For training session
         :class: important

         Copy file ``LBM_Saclay_Rech-Dev.tar``

          .. code-block:: shell

             $ cp /tmp_formation/LBM_Saclay/LBM_Saclay_Rech-Dev.tar .

         untar your file

          .. code-block:: shell

             $ tar -xvf LBM_Saclay_Rech-Dev.tar

         :octicon:`alert-fill;2em;sd-text-info` The tar archive does not contain the latest version of LBM_Saclay.


.. _Compilation-CPU-SMEMaG:

3. Compilation
--------------

You can run your first simulations on CPUs of your personal desktop. However, it is highly recommended to run LBM_Saclay on one (or better on several) graphic cards (GPUs). You will find the procedure for compiling on single-CPU, single-GPU, and multi-GPU.

.. tab-set::

   .. tab-item:: Compilation on CPU with openmp

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

   .. tab-item:: Compilation on GPU
   
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

It is recommended to start with a test case of folder ``run_training_lbm`` (see list of test cases on :bdg-ref-primary-line:`Run_Training-LBM`) and execute on your local computer. For example:

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

.. admonition:: For training session
   :class: error

   For post-processing ``TestCase01_Poiseuille_Water``, open ``paraview12``

    .. code-block:: shell
    
       $ paraview12&
   
   and follow the instructions in :bdg-ref-primary-line:`Single-Training-LBM`

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

.. sectionauthor:: Alain Cartalade