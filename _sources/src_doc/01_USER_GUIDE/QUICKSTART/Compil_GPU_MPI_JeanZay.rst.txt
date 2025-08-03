Jean-Zay (CNRS-IDRIS) - doc updated November 28th, 2024
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. admonition:: Documentation
   :class: important

   The documentation of supercomputer is available on http://www.idris.fr/jean-zay/

On Jean-Zay, several GPU partitions are available: the first one is equipped with V100, the second one is equipped with A100 and the third one with H100 (see http://www.idris.fr/jean-zay/gpu/jean-zay-gpu-exec_partition_slurm.html).

Here we give an example for compiling and running a job on partition ``v100`` equipped with 4 GPU V100 per node. For ``cmake`` the flag ``-DKokkos_ARCH_VOLTA70=ON`` will be used for V100. The test is also performed with the problem ``NSAC_Comp_3phases3D``.

Connexion on Jean-Zay
"""""""""""""""""""""

.. code-block:: shell

   ac165432@is247529:~$ ssh -XC loginname@jean-zay.idris.fr

returns after password

.. code-block:: shell

   ***********************************************************************
   * Ceci est un serveur de calcul de l IDRIS. Tout acces au systeme     *
   * doit etre specifiquement autorise par l IDRIS. Si vous tentez de    *
   * de continuer a acceder cette machine alors que vous n y etes pas    *
   * autorise, vous vous exposez a des poursuites judiciaires.           *
   *                               ---                                   *
   * This is an IDRIS compute node.  Each access to this system must be  *
   * properly authorized by IDRIS. If you go on accessing this machine   *
   * without authorization, then you are liable to prosecution.          *
   ***********************************************************************
   *                                                                     *
   * Orsay      CNRS / IDRIS - Frontale  -  jean-zay.idris.fr   France   *
   *                                                                     *
   ***********************************************************************
   loginname@jean-zay1:~$

Available disks
"""""""""""""""

- ``HOME`` only for configuration files

.. code-block:: shell

   loginname@jean-zay1:~$ pwd
   /linkhome/rech/genpuc01/loginname

- ``WORK`` for source files of LBM_Saclay, compilation and binary

.. code-block:: shell

   loginname@jean-zay1:~$ cd $WORK
   loginname@jean-zay1:/lustre/fswork/projects/rech/aih/loginname$

- ``SCRATCH`` for running and output files (``.vti`` and ``.h5``)

.. code-block:: shell

   loginname@jean-zay1:~$ cd $SCRATCH
   ubt36ea@jean-zay1:/lustre/fsn1/projects/rech/aih/loginname$

- ``STORE`` for saving output files
        
.. code-block:: shell

   loginname@jean-zay1:~$ cd $STORE
   loginname@jean-zay1:/lustre/fsstor/projects/rech/aih/loginname
        

Modules to load (last test August 2023)
""""""""""""""""""""""""""""""""""""""""

It can be useful to put those lines inside a file ``modules_compil_v100_mpi``:

.. code-block:: ruby

   module purge
   module load cmake/3.18.0
   module load gcc/8.5.0
   module load cuda/12.1.0
   #module load intel-compilers/19.1.3
   #module load nvidia-compilers/23.1
   module load openmpi/4.1.5-cuda
   module load hdf5/1.12.0-mpi-cuda

Next, load all modules with the command

.. code-block:: shell

   $ source modules_compil_v100_mpi

cmake and compilation
"""""""""""""""""""""

Write inside a new file (e.g. ``cmake_v100_mpi.scr``) the following commands

.. code-block:: ruby

   #!/bin/bash
   #build_cuda_mpi
   export OMPI_CXX=/gpfswork/rech/aih/loginname/PATH_TO_LBM_Saclay/external/kokkos/bin/nvcc_wrapper
   export CXX=/gpfslocalsup/spack_soft/openmpi/4.1.5/gcc-8.5.0-hjw556pajrrm3khundk6jqtvfwviedeu/bin/mpicxx
   cmake -DKokkos_ENABLE_OPENMP=ON -DKokkos_ENABLE_CUDA=ON -DKokkos_ENABLE_CUDA_LAMBDA=ON -DKokkos_ARCH_VOLTA70=ON -DKokkos_ENABLE_HWLOC=ON -DUSE_HDF5=ON -DUSE_MPI=ON -DUSE_MPI_CUDA_AWARE_ENFORCED=ON -DPROBLEM=NSAC_Comp_3phases3D ..

Remark: in 2023, it was necessary to put the two ``export`` commands before ``cmake``. Maybe those two lines are not any more necessary (see Tests on Topaze).

Here the options ``-DUSE_MPI=ON``, ``-DUSE_MPI_CUDA_AWARE_ENFORCED=ON`` are used for ``MPI``. For outputs with ``HDF5`` format the option ``-DUSE_HDF5=ON`` is turned on. After a ``chmod u+x cmake_v100_mpi.scr`` command, you can run the script to create the ``makefile``:

.. code-block:: shell

   $ mkdir build_cuda_mpi
   $ cd build_cuda_mpi
   $ cmake_v100_mpi.scr

Finally compile

.. code-block:: shell

   $ make -j 22

Submit a job and run (last test 2023)
""""""""""""""""""""""""""""""""""""

Examples of script slurm can be found on http://www.idris.fr/jean-zay/gpu/jean-zay-gpu-exec_multi_mpi_batch.html. The example of script below is for parition v100 with 16 MPI processes.

Write a script to submit your job, e.g. with name ``016-GPU.slurm``:

.. code-block:: ruby

   #!/bin/bash
   #SBATCH --job-name=RT3P_vD    # nom du job
   ##SBATCH --partition=gpu_p2          # de-commente pour la partition gpu_p2
   #SBATCH --account=aih@v100
   #SBATCH -C v100-16g
   #SBATCH --qos=qos_gpu-t3
   #SBATCH --ntasks=16                  # nombre total de tache MPI
   #SBATCH --ntasks-per-node=4          # nombre de tache MPI par noeud (= nombre de GPU par noeud)
   #SBATCH --gres=gpu:4                 # nombre de GPU par noeud (max 8 avec gpu_p2)
   #SBATCH --cpus-per-task=10           # nombre de coeurs CPU par tache (un quart du noeud ici)
   ##SBATCH --cpus-per-task=3           # nombre de coeurs CPU par tache (pour gpu_p2 : 1/8 du noeud)
   # /!\ Attention, "multithread" fait reference a l'hyperthreading dans la terminologie Slurm
   #SBATCH --hint=nomultithread         # hyperthreading desactive
   #SBATCH --time=20:00:00               # temps d'execution maximum demande (HH:MM:SS)
   #SBATCH --output=Job_cuda_mpi_%j.o # nom du fichier de sortie
   #SBATCH --error=Job_cuda_mpi_%j.e  # nom du fichier d'erreur (ici commun avec la sortie)

   # nettoyage des modules charges en interactif et herites par defaut
   module purge

   # chargement des modules
   module load cuda/10.2
   module load gcc/8.5.0
   module load openmpi/4.0.5-cuda
   ###module load hdf5/1.12.0-mpi-cuda
   module list

   # echo des commandes lancees
   set -x

   # execution du code
   srun /gpfswork/rech/aih/loginname/PATH_TO_LBM_saclay/build_cuda_mpi_3D/src/LBM_saclay $@ --kokkos-num-devices=16

The job will run on 16 MPI processes (``#SBATCH --ntasks=16``) on GPU partition V100 (``#SBATCH -C v100-16g``). To run the job write the following command

.. code-block:: shell

   $ sbatch 016-GPU.slurm parameter.ini

where ``parameter.ini`` is the input file for LBM_Saclay with the appropriate domain decomposition.

Visualization with Jean-Zay
"""""""""""""""""""""""""""

See

http://www.idris.fr/jean-zay/pre-post/jean-zay-outils-visu-noeuds.html
