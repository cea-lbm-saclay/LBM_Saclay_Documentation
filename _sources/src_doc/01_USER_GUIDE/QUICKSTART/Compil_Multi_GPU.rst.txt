.. _Multi-GPU:

Compilation Multi-GPU (supercomputers)
--------------------------------------

Simulations with LBM_Saclay can be run with domain decomposition. Communications between subdomains are done with MPI. Several french supercomputers with multi-CPU and multi-GPU partitions are available for running simulations with LBM_Saclay:

.. toctree::
   :maxdepth: 1

   ./Compil_GPU_MPI_Topaze.rst
   ./Compil_GPU_MPI_JeanZay.rst

- Adastra (CINES) - no test performed

The procedure to compile depend on those architectures because the library names to load change from a supercomputer to another one. On this page, we detail the procedure for Orcus and Topaze. For Jean-Zay procedures of connexion, modules to load and instructions for compilation can be found on

https://codev-tuleap.cea.fr/plugins/document/lbmsaclay/folder/16583

