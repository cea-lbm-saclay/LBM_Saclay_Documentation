.. _ORCUS-DM2S:

ORCUS (CEA-ISAS-DM2S): compilation on single- and multi-GPU - doc updated July 8th, 2025
========================================================================================

On Orcus, several GPU partitions are available. Here we give an example for compiling and running a job on partition ``gpuq_h100`` equipped with 4 GPU H100. For ``cmake`` the flag ``-DKokkos_ARCH_HOPPER90=ON`` will be used for H100. The test is also performed with problem ``NSAC_Comp``.

1. Connexion on Orcus
---------------------

.. admonition:: Connexion on ORCUS
   :class: error

      .. code-block:: shell

         loginname@is247529:~$ ssh -XC orcusloginamd2


2. Single GPU: compilation and run (deprecated)
-----------------------------------------------

.. dropdown::
   :icon: comment

   .. admonition:: Single-GPU compilation on ORCUS (deprecated)
      :class: note

      **Modules to load**

         .. code-block:: shell

            $ source /tmpformation/LBM_Saclay/modules_compil_h100_v11fev2025

      where the modules list inside file ``modules_compil_h100_v11fev2025`` is

         .. code-block:: ruby

            module purge
            module load cmake/3.28.3
            module load gcc/13.3.0
            module load cuda/12.4.0
            module load hdf5/gcc_13.3.0_openmpi_4.1.6/1.14.3
            module list

      **cmake and compilation**

         .. code-block:: shell

            $ mkdir build_cuda_h100
            $ cd build_cuda_h100

         Creation of ``makefile``

         .. code-block:: shell

            $ /tmpformation/LBM_Saclay/cmake_h100.scr

         Compilation

         .. code-block:: shell

            $ make -j 22

3. Multi-GPU: compilation and run on multi-H100 with MPI (updated July 8th, 2025)
---------------------------------------------------------------------------------

Modules to load
"""""""""""""""

.. admonition:: Modules to load
   :class: important

      .. code-block:: shell

         $ module load cmake/3.28.3 
         $ module load hdf5/nvhpc_25.3_openmpi_5.0.3/1.14.3

   The ``hdf5`` module loads the following ones: ``gcccore/.14.2.0 cuda/12.8.0 nvhpc/25.3 hwloc/2.11.1 ucx/1.18.0 pmix/5.0.3 prrte/3.0.6 ucc/1.3.0 openmpi/nvhpc_25.3/5.0.3 nvompi/253.503 szip/2.1.1``.

cmake and compilation
"""""""""""""""""""""

.. admonition:: Create a directory

      .. code-block:: shell

         $ mkdir build_cuda_h100_mpi
         $ cd build_cuda_h100_mpi

Next, two methods are possible. In the first one, turn off the ``RPATH``:

.. admonition:: First method: turn off the ``RPATH`` in ``cmake``
   :class: important

   For that purpose you must add the following options after ``-DPROBLEM=NSAC_Comp`` in your ``cmake`` command: ``-DCMAKE_SKIP_RPATH=ON -DCMAKE_BUILD_WITH_INSTALL_RPATH=OFF -DCMAKE_INSTALL_RPATH_USE_LINK_PATH=FALSE``

      .. code-block:: shell

         $ cmake -DKokkos_ENABLE_OPENMP=ON -DKokkos_ENABLE_CUDA=ON -DKokkos_ENABLE_CUDA_LAMBDA=ON -DKokkos_ARCH_HOPPER90=ON -DUSE_MPI=ON -DUSE_MPI_CUDA_AWARE_ENFORCED=ON -DKokkos_ENABLE_HWLOC=ON -DUSE_HDF5=ON -DPROBLEM=NSAC_Comp -DCMAKE_SKIP_RPATH=ON -DCMAKE_BUILD_WITH_INSTALL_RPATH=OFF -DCMAKE_INSTALL_RPATH_USE_LINK_PATH=FALSE ..
         $ make -j 22

In the second one, use command ``make install``

.. admonition:: Second method: ``make install``
   :class: important

   Add an option for ``cmake``: ``-DCMAKE_INSTALL_PREFIX=${LBMSACLAY_TOP_DIR}/install/`` where ``LBMSACLAY_TOP_DIR`` is the LBM directory 

      .. code-block:: shell

         $ cmake -DKokkos_ENABLE_OPENMP=ON -DKokkos_ENABLE_CUDA=ON -DKokkos_ENABLE_CUDA_LAMBDA=ON -DKokkos_ARCH_HOPPER90=ON -DUSE_MPI=ON -DUSE_MPI_CUDA_AWARE_ENFORCED=ON -DKokkos_ENABLE_HWLOC=ON -DUSE_HDF5=ON -DPROBLEM=NSAC_Comp -DCMAKE_INSTALL_PREFIX=${LBMSACLAY_TOP_DIR}/install/ ..
         $ make -j 22
         $ make install

Run your job on 4 GPU with MPI
""""""""""""""""""""""""""""""

Write a script to submit your job, e.g. with name ``GPU_H100_Taylor-Bubble3D.slurm``:

   .. code-block:: ruby

      #!/bin/bash

      # Paramètres du job slurm. Ajuster en particulier le Walltime, le nom du job
      # et fichiers de sortie/erreur, et l'adresse mail.
      # Plus d'infos à la section 5. du manuel utilisateur d'Orcus.

      #SBATCH -N 1                                  # Nombre de nœuds
      #SBATCH -n 4                                  # Nombre de taches
      #SBATCH --gres=gpu:4                          # nb GPU Orcus (commande à rajouter depuis décembre)
      #SBATCH -p gpuq_h100                          # Partitions adaptées au job
      #SBATCH -t 12:00:00                           # Walltime
      #SBATCH -J myjob                              # Nom du job
      #SBATCH -o myjob_%j.o                         # Fichier de sortie
      #SBATCH -e myjob_%j.e                         # Fichier d'erreur
      #SBATCH --mail-user=user@cea.fr               # Adresse email
      #SBATCH --mail-type=begin,end,fail            # Envoi d'email à l'exécution, fin et échec du job

      # Module nécessaires au fonctionnement de LBM_saclay.
      module purge
      module load cmake/3.28.3 
      module load hdf5/nvhpc_25.3_openmpi_5.0.3/1.14.3

      # Lance LBM_saclay. Remplacer les deux chemins comme nécessaire.
      mpirun -np 4 /home/catA/loginname/LBM_Saclay_Rech-Dev/build_cuda_h100_mpi/src/LBM_saclay $1 --kokkos-map-device-id-by=mpi_rank
      exit 0

The job will be run on 4 MPI processes (``#SBATCH -n 4`` and ``mpirun -np 4``) on partition (``#SBATCH -p gpuq_h100``).

.. admonition:: Submit your job
   :class: error

   Submit your job with the following command

      .. code-block:: shell

         $ sbatch GPU_H100_Taylor-Bubble3D.slurm TestCase19_Taylor-Bubble3D_004-GPU.ini

where ``TestCase19_Taylor-Bubble3D_004-GPU.ini`` is the input file for LBM_Saclay with the appropriate domain decomposition. For example in the input file ``TestCase19_Taylor-Bubble3D_004-GPU.ini`` the sections ``[mesh]`` and ``[mpi]`` are set to

   .. code-block:: ruby

      [mesh]
      nx=128
      ny=128
      nz=318
      xmin=-64.0
      xmax=64.0
      ymin=-64.0
      ymax=64.0
      zmin=0.0
      zmax=1272.0

      [mpi]
      mx=1
      my=1
      mz=4

.. sectionauthor:: Alain Cartalade