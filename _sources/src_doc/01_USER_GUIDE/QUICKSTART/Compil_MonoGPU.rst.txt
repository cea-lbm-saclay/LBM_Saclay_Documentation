Compilation mono-CPU (desktop): training session
================================================

Test performed on computer with ubuntu 22 (4th October, 2024) for kernel ``NSAC_Comp``

.. admonition:: For training session
    :class: error

    Go to ``LBM_Saclay_Rech-Dev`` and make a directory for compilation

     .. code-block:: ruby

        $ cd LBM_Saclay_Rech-Dev
        $ mkdir build_openmp
        $ cd build_openmp

    Create your ``makefile``

     .. code-block:: ruby

        $ cmake -DKokkos_ENABLE_OPENMP=ON -DUSE_HDF5=ON -DPROBLEM=NSAC_Comp ..

    Compilation

     .. code-block:: ruby

        $ make -j 22

    The binary ``LBM_saclay`` is created in folder ``build_openmp/src``

.. admonition:: If problem with HDF5 library (on ubuntu 22)
   :class: important

   In file bashrc the following modules are loaded

    .. code-block:: ruby

        $ module avail HDF5
        $ module unload hdf5/intel-compilers_2023.2.1_openmpi_4.1.6/1.14.3
        $ module load hdf5/gcc_13.2.0_openmpi_4.1.6/1.14.3


Compilation mono-GPU (desktop)
==============================

Test performed on "manwe" (server) and "is247845" (desktop) both on ubuntu 22.04 (September 2024). In what follows, the procedure is presented only on manwe because it is identical for is247845. For yor own desktop

1. Check that cuda-toolkit is installed on the computer

    - Check file ``/proc/driver/nvidia/version`` exists
    - Check folder ``/usr/local/cuda`` exists
    - Check compiler ``nvcc`` (``> which nvcc``)
    - Put in ``.bashrc``: ``export PATH=/usr/local/cuda-12.6/bin${PATH:+:${PATH}}``

2. If not

    Ask installation https://codev-tuleap.intra.cea.fr/plugins/tracker/?tracker=3602
    If root: can be downloaded from https://developer.nvidia.com/cuda-downloads

Connexion on manwe
""""""""""""""""""

.. code-block:: shell

    ac165432@is247529:~$ ssh -XY manwe

returns after password

.. code-block:: shell

    ac165432@manwe:~$

To get information on graphic card, the command

.. code-block:: shell

    $ nvidia-smi

returns

.. code-block:: ruby

    Wed Nov 27 16:16:26 2024       
    +-----------------------------------------------------------------------------------------+
    | NVIDIA-SMI 560.35.03              Driver Version: 560.35.03      CUDA Version: 12.6     |
    |-----------------------------------------+------------------------+----------------------+
    | GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
    | Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
    |                                         |                        |               MIG M. |
    |=========================================+========================+======================|
    |   0  NVIDIA RTX A6000               On  |   00000000:3B:00.0 Off |                  Off |
    | 30%   31C    P8             17W /  300W |      11MiB /  49140MiB |      0%      Default |
    |                                         |                        |                  N/A |
    +-----------------------------------------+------------------------+----------------------+
                                                                                         
    +-----------------------------------------------------------------------------------------+
    | Processes:                                                                              |
    |  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
    |        ID   ID                                                               Usage      |
    |=========================================================================================|
    |    0   N/A  N/A      2757      G   /usr/lib/xorg/Xorg                              4MiB |
    +-----------------------------------------------------------------------------------------+

meaning that one GPU ``NVIDIA RTX A6000`` is available on the server. The memory available is 49.14Go.

``cmake`` and compilation of LBM_Saclay
""""""""""""""""""""""""""""""""""""""""

The ``makefile`` is created with command ``cmake`` with flags ``openmp``, ``cuda`` and ``HDF5``. First create a folder ``build_cuda``

.. code-block:: shell

    $ cd LBM_saclay
    $ mkdir build_cuda
    $ cd build_cuda

Set environment variables (set the appropriate path)

.. code-block:: shell

    $ export CC=gcc
    $ LBMSACLAY_TOP_DIR=PATH_to/LBM_saclay
    $ export CXX=${LBMSACLAY_TOP_DIR}/external/kokkos/bin/nvcc_wrapper

Create the ``makefile``

.. code-block:: shell

    $ cmake -DKokkos_ENABLE_OPENMP=ON -DKokkos_ENABLE_CUDA=ON -DKokkos_ENABLE_CUDA_LAMBDA=ON -DUSE_HDF5=ON -DPROBLEM=NSAC_Comp ..

Compilation:

.. code-block:: shell

    $ make -j 22

.. sectionauthor:: Alain Cartalade