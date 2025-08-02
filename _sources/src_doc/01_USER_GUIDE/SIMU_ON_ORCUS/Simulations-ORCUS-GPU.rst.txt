.. _Simulations-GPU:

First simulations on ORCUS: example with GPU partition
======================================================

On Orcus, several GPU partitions are available. Here we present the basic commands to run a job on GPU partitions of ORCUS.

For compilation, a tutorial is given on :ref:`ORCUS-DM2S` for partition ``gpuq_h100`` equipped with 4 GPU H100. For ``cmake`` the flag ``-DKokkos_ARCH_HOPPER90=ON`` will be used for H100. The test is also performed with problem ``NSAC_Comp``.

Connexion and disks on ORCUS
----------------------------

.. admonition:: For training session: connexion on ORCUS
   :class: error

      .. code-block:: shell

         loginname@is247529:~$ ssh -XC orcusloginamd2

returns

   .. code-block:: shell

      Bienvenue sur le cluster

                ____  _____   _____ _    _  _____
               / __ \|  __ \ / ____| |  | |/ ____|
              | |  | | |__) | |    | |  | | (___
              | |  | |  _  /| |    | |  | |\___ \
              | |__| | | \ \| |____| |__| |____) |
               \____/|_|  \_\\_____|\____/|_____/


      Support :      https://codev-tuleap.intra.cea.fr/projects/InfoSc
      Doc :          evince /product/documentations/users/user_manual.pdf
      Guide ACL :    vim +"set syntax=markdown" /product/documentations/users/README_ACL.md

                   Frontale ROCKY Linux 9

      Last login: Wed Nov 27 09:10:54 2024 from 132.166.148.113
      loginname@orcusloginamd2:~$

.. admonition:: Disks on ORCUS

   Several disks are available

   - ``HOME``: configuration files, source files of LBM_Saclay, compilation and binary

      .. code-block:: shell

         $ cd ~

   - ``SCRATCH`` for running and output files (``.vti`` and ``.h5``)

      .. code-block:: shell

         $ cd $SCRATCH

   - ``/tmpformation/LBM_Saclay``: shared directory for compiled versions of LBM_Saclay and slurm scripts

      .. code-block:: shell

         $ cd /tmpformation/LBM_Saclay

Get information about ORCUS
---------------------------

.. admonition:: Check the number of nodes
   :class: hint

   Check the number of nodes (for CPU and GPU partitions):

      .. code-block:: shell

         loginname@orcusloginamd2:~$ sinfo

returns (only GPU partitions)

   .. code-block:: ruby

      PARTITION NODES      STATE CPUS SOCKETS CORES MEMORY NODELIST

      gpuq_v100     2       idle   32       2    16 376000 orcus-n[3001-3002]
      gpuq_a100     1      mixed   32       2    16 485000 orcus-n3201
      gpuq_a100     1       idle   32       2    16 485000 orcus-n3202
      gpuq_h100     1       idle   72       2    36 990000 orcus-n3401

meaning that five GPU partitions are available on Orcus:
 - 2 nodes of one GPU V100 (2 GPUs V100)
 - 2 nodes of one GPU A100 (2 GPUs A100)
 - 1 node of four GPUs H100. The partition ``gpuq_h100`` contains 4 GPUs H100.

.. admonition:: To check the number of graphic cards on that node
   :class: hint

   You can make a reservation in interactive mode with:

      .. code-block:: shell

         loginname@orcusloginamd2:~$ srun -p gpuq_h100 -n 1 --gres=gpu:1 --pty bash -i

   If the node is free, you will be able to connect and open a terminal. The command

      .. code-block:: shell

         loginname@orcus-n3401:~$ nvidia-smi

returns

   .. code-block:: ruby

      Tue Nov 26 10:17:49 2024       
      +-----------------------------------------------------------------------------------------+
      | NVIDIA-SMI 555.42.02              Driver Version: 555.42.02      CUDA Version: 12.5     |
      |-----------------------------------------+------------------------+----------------------+
      | GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
      | Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
      |                                         |                        |               MIG M. |
      |=========================================+========================+======================|
      |   0  NVIDIA H100 80GB HBM3          On  |   00000000:4E:00.0 Off |                    0 |
      | N/A   39C    P0             73W /  700W |       1MiB /  81559MiB |      0%      Default |
      |                                         |                        |             Disabled |
      +-----------------------------------------+------------------------+----------------------+
      |   1  NVIDIA H100 80GB HBM3          On  |   00000000:5F:00.0 Off |                    0 |
      | N/A   37C    P0             70W /  700W |       1MiB /  81559MiB |      0%      Default |
      |                                         |                        |             Disabled |
      +-----------------------------------------+------------------------+----------------------+
      |   2  NVIDIA H100 80GB HBM3          On  |   00000000:CB:00.0 Off |                    0 |
      | N/A   38C    P0             71W /  700W |       1MiB /  81559MiB |      0%      Default |
      |                                         |                        |             Disabled |
      +-----------------------------------------+------------------------+----------------------+
      |   3  NVIDIA H100 80GB HBM3          On  |   00000000:DB:00.0 Off |                    0 |
      | N/A   38C    P0             72W /  700W |       1MiB /  81559MiB |      0%      Default |
      |                                         |                        |             Disabled |
      +-----------------------------------------+------------------------+----------------------+

      +-----------------------------------------------------------------------------------------+
      | Processes:                                                                              |
      |  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
      |        ID   ID                                                               Usage      |
      |=========================================================================================|
      |  No running processes found                                                             |
      +-----------------------------------------------------------------------------------------+

We can check that four ``NVIDIA H100 80GB HBM3`` are available.

Submit your job with slurm script
---------------------------------

.. admonition:: For LBM training session
   :class: important

   Three slurm scripts are available in folder ``/tmpformation/LBM_Saclay/`` to submit one job on Orcus.

      - ``JOB_H100_GPU.slurm`` to submit one job on gpuq_h100
      - ``JOB_A100_GPU.slurm`` to submit one job on gpuq_a100
      - ``JOB_V100_GPU.slurm`` to submit one job on gpuq_v100

.. admonition:: For training session: run on ORCUS
   :class: error

   **Submit a job and run**

   Copy folder ``run_training_lbm`` in your directory (content on :ref:`Run_Training-LBM`):

      .. code-block:: shell

         $ cp -r /tmpformation/LBM_Saclay/LBM_Saclay_Rech-Dev/run_training_lbm .

   Go to one test case folder (e.g. ``TestCase05_Spinodal-Decomposition2D``):

      .. code-block:: shell

         $ cd run_training_lbm/TestCase05_Spinodal-Decomposition2D

   Submit your test case on one partition: gpuq_h100, gpuq_a100 or gpuq_v100. For example for gpuq_h100:

      .. code-block:: shell

         $ sbatch /tmpformation/LBM_Saclay/JOB_H100_GPU.slurm TestCase05_Spinodal-Decomposition_CH.ini

.. admonition:: For training session: check your submission
   :class: hint

   Check that your job is running: the following command

      .. code-block:: shell

         $ squeue -u S-SAC-DM2S-train1

   returns

      .. code-block:: ruby

         JOBID   PARTITION       QOS PRIORITY         NAME     USER ST       TIME          START_TIME   TIME_LIMIT CPUS    NODES NODELIST(REASON)
         533013   gpuq_h100     1jour 0.000000        myjob ac165432  R       0:01 2025-02-16T11:32:25     12:00:00 18          1 orcus-n3401

   To stop your job

      .. code-block:: shell

         $ scancel 533013
   
   where 533013 corresponds to your JOBID 


Transfer your output files on your local computer
-------------------------------------------------

.. admonition:: For training session: from your local desktop
   :class: error

   Once the job is complete, transfer the output files on your local computer:

      .. code-block:: shell

         $ scp -r S-SAC-DM2S-train1@orcusloginamd2:~/run_training_lbm/TestCase05_Spinodal-Decomposition2D .

   Post-process with paraview

      .. code-block:: shell

         $ paraview11&

.. sectionauthor:: Alain Cartalade
   