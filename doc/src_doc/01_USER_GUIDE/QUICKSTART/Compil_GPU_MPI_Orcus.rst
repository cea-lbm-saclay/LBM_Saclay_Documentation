.. include:: ../../Substitutions.rst

.. _ORCUS-DM2S:

ORCUS (CEA-ISAS-DM2S): compilation on single- and multi-GPU - doc updated August 28th, 2025
===========================================================================================

On Orcus, several GPU partitions are available. Here we give an example for compiling and running a job on partition ``gpuq_h100`` equipped with 4 GPU H100. For ``cmake`` the flag ``-DKokkos_ARCH_HOPPER90=ON`` will be used for H100. The test is also performed with problem ``NSAC_Comp``.

1. Connexion on Orcus
---------------------

.. admonition:: Connexion on ORCUS
   :class: error

      .. code-block:: shell

         loginname@is247529:~$ ssh -XC orcusloginamd2


2. Create the makefile with a shell script
------------------------------------------

Several scripts are available in the folder ``compilation`` of ``LBM_Saclay`` to create the ``makefile`` for your own desktop (``local``) and supercomputers ``topaze`` and ``orcus``. For supercomputer ``orcus`` one file ``configure_build.sh`` is set inside all subdirectory for each GPU V100, A100 and H100.

.. admonition:: script
   :class: error

   To create the ``makefile`` for GPU H100 with MPI, simply execute the shell script ``configure_build.sh``:

      .. code-block:: shell

         $ cd LBM_Saclay_Rech-Dev
         $ ./compilation/orcus/cuda_h100_multigpu/configure_build.sh

returns

   .. code-block:: shell

      Loading hdf5/nvhpc_25.3_openmpi_5.0.3/1.14.3
      Loading requirement: gcccore/.14.2.0 cuda/12.8.0 nvhpc/25.3 hwloc/2.11.1 ucx/1.18.0 pmix/5.0.3 prrte/3.0.6 ucc/1.3.0 openmpi/nvhpc_25.3/5.0.3 nvompi/253.503 szip/2.1.1
      Currently Loaded Modulefiles:
      1) cmake/3.28.3      3) cuda/12.8.0   5) hwloc/2.11.1   7) pmix/5.0.3    9) ucc/1.3.0                 11) nvompi/253.503  13) hdf5/nvhpc_25.3_openmpi_5.0.3/1.14.3  
      2) gcccore/.14.2.0   4) nvhpc/25.3    6) ucx/1.18.0     8) prrte/3.0.6  10) openmpi/nvhpc_25.3/5.0.3  12) szip/2.1.1      

      Key:
      auto-loaded  
      The following problems are currently implemented:
      0  AC
      1  Advection-Diffusion
      2  Crystal_growth_Younsi
      3  GPMixt
      4  GPMixtNS
      5  GPMixtTernary
      6  GPMuTernary
      7  NS
      8  NS_3phases_1comp_phase_change
      9  NSAC_Comp
      10 NSAC_Comp_3phases
      11 NSAC_Comp_3phases3D
      12 NSAC_coupling
      13 NSAC_Fakhari
      14 NSAC_Surfactant
      Choose which problems to include by indicating a list of space or comma separated numbers, eg '0 1' or '0,1'.
      Write 'all' to include all problems.
      Problem numbers:

.. admonition:: Enter the problem to be compiled
   :class: error

   Write the number of your problem, e.g. ``9`` for ``NSAC_Comp`` problem:

      .. code-block:: ruby

         Problem numbers: 9

returns

   .. code-block:: shell

      Problem n°9  added to compile list (NSAC_Comp)
      //===================================================
      cmake command is : cmake -DKokkos_ENABLE_OPENMP=ON -DKokkos_ENABLE_CUDA=ON -DKokkos_ARCH_HOPPER90=ON -DUSE_HDF5=ON -DCMAKE_SKIP_RPATH=ON -DCMAKE_BUILD_WITH_INSTALL_RPATH=OFF -DCMAKE_INSTALL_RPATH_USE_LINK_PATH=FALSE -DPROBLEM=NSAC_Comp /home/catA/ac165432/CODEV-TULEAP_LBM_Saclay/LBM_Saclay_Rech-Dev

      //===================================================
      LBM_saclay build configuration:
      //===================================================
      C++ Compiler : NVHPC 25.3.0 
         /product/rocky9-x86_64_cluster/apps/NVHPC/25.3/Linux_x86_64/25.3/compilers/bin/nvc++
      MPI not enabled
      Kokkos OpenMP enabled : ON
      Kokkos CUDA   enabled : ON
      Kokkos CUDA   Lambda  : ON
      Kokkos CUDA   flags   : -extended-lambda;-Wext-lambda-captures-this;-arch=sm_90
      Kokkos HWLOC  enabled : Off
      HDF5 found version    : 1.14.3
      HDF5 definitions      : 
      HDF5 parallel         : TRUE
      HDF5 includes dirs    : /product/rocky9-x86_64_cluster/apps/HDF5/1.14.3-nvompi-253.503/include;/product/rocky9-x86_64_cluster/apps/Szip/2.1.1/include
      HDF5 libraries        : /product/rocky9-x86_64_cluster/apps/HDF5/1.14.3-nvompi-253.503/lib/libhdf5.so;/usr/lib64/libpthread.a;/product/rocky9-x86_64_cluster/apps/Szip/2.1.1/lib/libsz.so;/usr/lib64/libz.so;/usr/lib64/libdl.a;/usr/lib64/libm.so

      //===================================================

      build configured in:
      /home/catA/ac165432/CODEV-TULEAP_LBM_Saclay/LBM_Saclay_Rech-Dev/build_cuda_h100/build_NSAC_Comp
      go there and use make to compile

.. admonition:: Go there to compile
   :class: error

      .. code-block:: shell

         $ cd build_cuda_h100/build_NSAC_Comp
         $ make -j 22

After 15min, the binary ``LBM_saclay`` is created in the directory ``build_cuda_h100/build_NSAC_Comp/src``.

3. Details of commands for compiling
------------------------------------

Single GPU: compilation and run (deprecated)
""""""""""""""""""""""""""""""""""""""""""""

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

Multi-GPU: compilation and run on multi-H100 with MPI (updated July 8th, 2025)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. tab-set::

   .. tab-item:: Modules to load

      .. admonition:: Modules to load
         :class: important

            .. code-block:: shell

               $ module load cmake/3.28.3 
               $ module load hdf5/nvhpc_25.3_openmpi_5.0.3/1.14.3

         The ``hdf5`` module loads the following ones: ``gcccore/.14.2.0 cuda/12.8.0 nvhpc/25.3 hwloc/2.11.1 ucx/1.18.0 pmix/5.0.3 prrte/3.0.6 ucc/1.3.0 openmpi/nvhpc_25.3/5.0.3 nvompi/253.503 szip/2.1.1``.

   .. tab-item:: cmake and compilation

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

   .. tab-item:: Run your job on 4 GPU with MPI

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