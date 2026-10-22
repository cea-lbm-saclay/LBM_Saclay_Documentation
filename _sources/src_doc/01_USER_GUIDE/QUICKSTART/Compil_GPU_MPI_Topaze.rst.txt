First simulations on Topaze (CEA-CCRT) - doc updated Nov 27th, 2024
-------------------------------------------------------------------

On Topaze, one GPU partition of GPUs A100 is available. 

.. admonition:: Documentation
   :class: important

   The documentation of supercomputer is available on

   https://www-ccrt.ccc.cea.fr/docs/topaze/fr/html/toc/fulldoc/Introduction.html

Here we give an example for compiling and running a job on partition ``a100`` equipped with 4 GPU A100 per node. For ``cmake`` the flag ``-DKokkos_ARCH_AMPERE80=ON`` will be used for A100. The test is also performed with the problem ``NSAC_Comp``.

Connexion and available disks on Topaze
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Connexion on Topaze
   :class: hint

      .. code-block:: shell

         ac165432@is247529:~$ ssh -XY loginname@topaze.ccc.cea.fr

returns after password

   .. code-block:: shell

      ┌─────────────────┐
      │▀▛▘              │
      │ ▌▞▀▖▛▀▖▝▀▖▀▜▘▞▀▖│
      │ ▌▌ ▌▙▄▘▞▀▌▗▘ ▛▀ │
      │ ▘▝▀ ▌  ▝▀▘▀▀▘▝▀▘│
      └─────────────────┘

      Hotline: hotline.tgcc@cea.fr
                +33 17757 4242

      Help: $ machine.info

      Web site: https://www-ccrt.ccc.cea.fr/
   
      loginname@topaze171:/ccc/cont002/dsku/lautrec/home/user/den/loginname$

.. admonition:: Available disks

   Several disks are available

   - ``HOME`` only for configuration files

      .. code-block:: shell

         $ cd /ccc/cont002/home/den/loginname

   - ``WORK`` for source files of LBM_Saclay, compilation and binary

      .. code-block:: shell

         $ cd /ccc/work/cont002/den/loginname

   - ``SCRATCH`` for running and output files (``.vti`` and ``.h5``)

      .. code-block:: shell

         $ cd /ccc/scratch/cont002/den/loginname

   - ``STORE`` for saving output files
        
      .. code-block:: shell

         $ cd /ccc/store/cont002/den/loginname
        
   - SHARE LBM_Saclay

      .. code-block:: shell

         $ cd /ccc/work/cont002/den/den/LBM_Saclay

Compilation
^^^^^^^^^^^

.. admonition:: Modules to load (last test October 2024)
   :class: hint

   It can be useful to put those lines inside a file ``modules_compil_a100_mpi``:

      .. code-block:: ruby

         module purge
         module load cmake/3.26.4
         module load gnu/11.2.0
         module load ucx/1.14
         module load flavor/cuda/standard
         module load cuda/12
         module load mpi/openmpi/4.1.4.6
         module load flavor/hdf5/parallel
         module load hdf5/1.12.0
         module list

   Next, load all modules with the command

      .. code-block:: shell

         $ source modules_compil_a100_mpi

.. admonition:: cmake and compilation
   :class: hint

   Write inside a new file (e.g. ``cmake_a100_mpi.scr``) the following commands

      .. code-block:: ruby

         #!/bin/bash
         cmake -DKokkos_ENABLE_OPENMP=ON -DKokkos_ENABLE_CUDA=ON -DKokkos_ENABLE_CUDA_LAMBDA=ON -DKokkos_ARCH_AMPERE80=ON -DUSE_MPI=ON -DUSE_MPI_CUDA_AWARE_ENFORCED=ON -DKokkos_ENABLE_HWLOC=ON -DUSE_HDF5=ON -DPROBLEM=NSAC_Comp ..

   Here the options ``-DUSE_MPI=ON``, ``-DUSE_MPI_CUDA_AWARE_ENFORCED=ON`` are used for ``MPI``. For outputs with ``HDF5`` format the option ``-DUSE_HDF5=ON`` is turned on. After a ``chmod u+x cmake_a100_mpi.scr`` command, you can run the script to create the ``makefile``:

      .. code-block:: shell

         $ mkdir build_cuda_mpi
         $ cd build_cuda_mpi
         $ cmake_a100_mpi.scr

   Finally compile

      .. code-block:: shell

         $ make -j 22

Submit a job and run
^^^^^^^^^^^^^^^^^^^^

Write a script to submit your job, e.g. with name ``GPU_H100_Taylor-Bubble3D.slurm``:

.. code-block:: ruby

   #!/bin/bash
   #MSUB -r Cyl16GPU # nom du job
   #MSUB -q a100
   #MSUB -Q normal
   #MSUB -n 16 # nombre total de tache MPI
   #MSUB -N 4  # nombre de nœuds
   #MSUB -m work,scratch
   #MSUB -c 32 # nombre de cœurs par tache
   #MSUB -o Cyl16G_%j.o # nom du fichier de sortie
   #MSUB -e Cyl16G_%j.e # nom du fichier d erreur (ici commun avec la sortie)
   #MSUB -T 86400 # temps limite à modifier en secondes

   # nettoyage des modules charges en interactif et herites par defaut
   module purge
   # chargement des modules
   module load gnu/11.2.0
   module load ucx/1.14
   module load flavor/cuda/standard
   module load cuda/12
   module load mpi/openmpi/4.1.4.6
   module load flavor/hdf5/parallel
   module load hdf5/1.12.0

   # echo des commandes lancees
   set -x
   # execution du code
   ccc_mprun /ccc/work/cont002/den/loginname/LBM_saclay/build_cuda_mpi/src/LBM_saclay ./TestCase_016GPU.ini --kokkos-map-device-id-by=mpi_rank

The job will run on 16 MPI processes (``#MSUB -n 16``) on GPU partition A100 (``#MSUB -q a100``). To run the job write the following command

.. code-block:: shell

   $ ccc_msub 016-GPU.slurm

where ``TestCase19_Taylor-Bubble3D_004-GPU.ini`` is the input file for LBM_Saclay with the appropriate domain decomposition.

Visualization with Topaze
^^^^^^^^^^^^^^^^^^^^^^^^^

1. Allocate one node for visualization with command

.. code-block:: shell

   $ ccc_visu console -T 43200 -p a100

2. Returns

.. code-block:: shell

     _______________   
  / ___/ ___/ ___/  A compute node is going to be allocated and a
 / /__/ /__/ /__    Nice DCV visualisation session as well as an
 \___/\___/\___/    interactive shell session launched on it.

            Waiting for free ressources... (Hit CTL-C to abort)

 Visualisation session is now available and accessible at :
 https://visu-ccrt.ccc.cea.fr/visu-ccrt/?choice&node=topaze7003&sid=slurm-u40114-j6603652-ftJbvMwxBc45KbXu-console

    Hit CTL-D or enter "exit 0" to close the interactive
    and visualisation sessions and release the allocation.

    /!\  Warning: performing the exit action will kill any
    /!\  task still active in the visualisation session.
    /!\  You should close the visualisation session first.

3. Copy the weblink https://visu-ccrt.ccc.cea.fr (link above) returned in Firefox and next

   - Write your username and password
   - Click on "Web connexion"
   - Write your username and password (again)
   - Click on "Activities" (top left) and open a terminal

4. Inside the new terminal, write the following commands

.. code-block:: shell

   $ module load gnu/8 mpi/openmpi/4 flavor/paraview/opengl paraview/5.11.0 python3/3.10.6
   $ cd /ccc/scratch/cont002/den/loginname/RUN_TRAINING_LBM3D
   $ paraview&

Useful commands on Topaze
"""""""""""""""""""""""""

1. Follow the job submission (useful to make an alias in ``.bashrc``)

.. code-block:: shell

   $ squeue -u loginname # jobs of loginname
   $ squeue -p a100     # all jobs for partition a100 of Topaze

2. Remaining hours

.. code-block:: shell

   $ ccc_myproject

.. sectionauthor:: Alain Cartalade