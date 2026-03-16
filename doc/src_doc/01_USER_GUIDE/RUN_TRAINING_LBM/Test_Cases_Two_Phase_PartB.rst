.. _TwoP-Training-LBM-PARTB:

Run "Two-phase with fluid flows" PART B: Simulations
====================================================

The first three test cases for two-phase with fluid flows compare the numerical solutions with classical solutions: the first one is the comparison with  of double-Poiseuille analytical solution, the second one is the Rayleigh-Taylor instability and the last one is the comparison with analytical solution of Prosperetti. 

Rising bubble
-------------

.. dropdown:: Rising bubble
   :icon: comment
   :open:

   Folder ``TestCase11_Rising-Bubble2D`` contains two test cases for simulations of rising bubble with different Bond and Morton numbers: ``CASE-A2`` and ``CASE-A5``. The choice of dimensionless numbers is inspired from reference :footcite:p:`Kumar_etal_PoF2019`. For ``CASE-A2`` :math:`\text{Bo}=32.2` and :math:`\text{Mo}=8.2\times10^{-4}` and for ``CASE-A5`` :math:`\text{Bo}=339` and :math:`\text{Mo}=43.1`.

   .. admonition:: For LBM training session: pre-processing with python scripts
      :class: hint

      The dimensionless parameters are derived from python scripts contained in folder ``PYTHON_Scripts``

       .. code-block:: shell

          $ cd TestCase11_Rising-Bubble2D/PYTHON_Scripts
          $ python Pre-Pro_InputParam_Rising-Bubble_Water-Air.py

      The derivation of :math:`\sigma^{\star}` and :math:`g^{\star}` for target Bo and Mo numbers are done in ``Pre-Pro_Bo-Mo_2_AdimParam_Rising-Bubble.py``. For test case ``CASE-A2``:
   
       .. code-block:: shell

          $ python Pre-Pro_Bo-Mo_2_AdimParam_Rising-Bubble.py
    
      Finally you can check that parameters of LBM_Saclay match with your dimensionless numbers. For ``CASE-A2``

       .. code-block:: shell

          $ python Ini_2_AdimNb_Rising-Bubble_CASE-A2.py


   .. admonition:: For LBM training session: run LBM_Saclay on Orcus
      :class: error

      Go to folder ``TestCase11_Rising-Bubble2D/CASE-A2`` and run LBM_Saclay.

       .. code-block:: shell

          $ cd TestCase11_Rising-Bubble2D/CASE-A2
          $ sbatch /tmpformation/LBM_Saclay/Slurm-Orcus/JOB_H100_GPU.slurm TestCase11_Rising-Bubble_BoMo-A2.ini

      The simulation ran 263.901 seconds (~4min24sec) on partition gpuq_h100 of Orcus to achieve 320.001 time-steps. Simulation of ``CASE-A5`` took 802.215 seconds (~13min37sec) on same partition to achieve 1.000.001 time-steps.

   .. admonition:: For LBM training session: post-processing with paraview 5.11
      :class: error

      Post-process with paraview11

       .. code-block:: shell

          $ paraview11&
      
      In paraview:
   
       1. open ``TestCase11_Rising-Bubble_CaseA2.xmf``, select ``XDMF Reader`` and clic on green button ``Apply``.
       2. Select field ``phi`` and visualize it for several times.

   .. admonition:: For training session: Exercise
      :class: important

      Derive parameters for simulating with LBM_Saclay
   
       - ``CASE-A3``: :math:`\text{Bo}=243` and :math:`\text{Mo}=266`
       - ``CASE-A4``: :math:`\text{Bo}=115` and :math:`\text{Mo}=4.63\times10^{-3}`


   .. div:: sd-text-center

      .. raw:: html

         <video controls src="../../../_static/Vid_Rising-Bubble_A2.webm" width="500" height="400"> </video>

Falling droplet
---------------

.. dropdown:: Falling droplet
   :icon: comment
   :open:

   The folder ``TestCase10_Falling-Droplet2D`` contains four test cases for simulations of surface tension sensitivity :math:`\sigma`.

   .. admonition:: For LBM training session: run LBM_Saclay on Orcus
      :class: error

      Go to folder ``TestCase10_Falling-Droplet2D/Sigma1`` for :math:`\sigma_1=10^{-5}` and run

       .. code-block:: shell

          $ cd TestCase10_Falling-Droplet2D/Sigma1
          $ sbatch /tmpformation/LBM_Saclay/Slurm-Orcus/JOB_H100_GPU.slurm TestCase10_Rayleigh-Plateau_Sigma1.ini

      The simulation ran 277.977 seconds (~4min38sec) on partition gpuq_h100 of Orcus to achieve 500.001 time-steps.

   .. admonition:: For LBM training session: post-processing with paraview 5.11
      :class: error

      Post-process with paraview11

       .. code-block:: shell

          $ paraview11&

      In paraview:
   
       1. open ``TestCase10_Rayleigh-Plateau_Sigma1.xmf``, select ``XDMF Reader`` and clic on green button ``Apply``.
       2. Select field ``phi`` and visualize it for several times.

   .. admonition:: For training session: Exercise
      :class: important

      Run three simulations with :math:`\sigma=3\times10^{-5}`, :math:`\sigma=5\times10^{-5}` and :math:`\sigma=6\times10^{-5}` to study the influence of surface tension on falling droplet. You should obtain results presented in video below.

   .. div:: sd-text-center

      .. raw:: html

         <video controls src="../../../_static/Vid_Falling-Droplet_256x512_Compare-Sigma.webm" width="700" height="420"> </video>  

2D Taylor bubble
----------------

.. dropdown:: Taylor bubble
   :icon: comment
   :open:

   The 2D test case simulates a bubble water inside a rectangle filled with olive oil. 

   .. admonition:: For LBM training session: pre-processing with python scripts
      :class: hint

      The dimensionless parameters are derived from python script ``Pre-Pro_InputParam_Taylor-Bubble_OliveOil-Air.py``

       .. code-block:: shell

          $ cd TestCase12_Taylor-Bubble2D
          $ python Pre-Pro_InputParam_Taylor-Bubble_OliveOil-Air.py

      The derivation of :math:`\sigma` and :math:`\eta_l` for target Bo and Mo numbers are done in ``Pre-Pro_BoMo_2_AdimNb_Taylor-Bubble.py``.
   
       .. code-block:: shell

          $ python Pre-Pro_BoMo_2_AdimNb_Taylor-Bubble.py
    
      Finally you can check that parameters of LBM_Saclay match with your dimensionless numbers with

       .. code-block:: shell

          $ python Ini_2_AdimNb_Taylor-Bubble.py

   .. admonition:: For LBM training session: run LBM_Saclay on Orcus
      :class: error

      Go to folder and run

       .. code-block:: shell

          $ cd TestCase12_Taylor-Bubble2D/Bo-Mo_Case5
          $ sbatch /tmpformation/LBM_Saclay/Slurm-Orcus/JOB_H100_GPU.slurm TestCase11_Taylor-Bubble_BoMo-Cas5.ini

      The simulation ran 597.596 seconds (~10 min) on partition gpuq_h100 of Orcus to achieve 800.001 time-steps.

   .. admonition:: For LBM training session: post-processing with paraview 5.11
      :class: error

      Post-process with paraview11

       .. code-block:: shell

          $ paraview11&

      In paraview: Clic on ``File`` --> ``Load State``, select ``State_Vid_Taylor-Bubble_Case5_PV511.pvsm``, select ``Choose File Names``, select ``.xmf`` file and ``OK``.

   .. admonition:: For LBM training session: Exercise
      :class: important

      Keep Bo=100 and run three other simulations with :math:`Mo=10^{-2},Mo=10^{-4},Mo=10^{-5}`, and :math:`Mo=10^{-6}`. After post-processing with paraview11 (load ``State_Vid_Taylor-Bubble_Compare_5Mo_PV511.pvsm`` file) you should obtain the video below.

   .. div:: sd-text-center

      .. raw:: html

         <video controls src="../../../_static/Vid_Taylor-Bubble2D_Compare_5Mo.webm" width="800" height="600"> </video>   

Splashing droplet
-----------------

.. dropdown:: Splashing droplet
   :icon: comment
   :open:

   Folder ``TestCase13_Splashing-Droplet2D`` contains one test cases for simulations of splashing droplet. This is an example of using Re and We dimensionless numbers.

   .. admonition:: For LBM training session: run LBM_Saclay on Orcus
      :class: error

      Go to folder and run

       .. code-block:: shell

          $ cd TestCase13_Splashing-Droplet2D/Splash_Re2000-We8000
          $ sbatch /tmpformation/LBM_Saclay/Slurm-Orcus/JOB_H100_GPU.slurm TestCase13_SplashingDroplet_Re2000-We8000_H15_1024x220.ini

      The simulation ran 70.609 seconds on partition gpuq_h100 of Orcus to achieve 100.001 time-steps.

   .. admonition:: For LBM training session: post-processing with paraview 5.11
      :class: error

      Post-process with paraview11

       .. code-block:: shell

          $ paraview11&

      In paraview:
   
       1. open ``TestCase13_Splash_Re2000-We8000.xmf``, select ``XDMF Reader`` and clic on green button ``Apply``.
       2. Select field ``phi`` and visualize it for several times.

   .. div:: sd-text-center

      .. raw:: html

         <video controls src="../../../_static/Vid_Splash_Re876-We2662.webm" width="700" height="350"> </video>

   .. admonition:: For LBM training session: Exercise
      :class: important

      Perform simulations with other Reynolds and Weber numbers. Python scripts in folder ``PYTHON_Scripts`` will help you to set dimensionless parameters in your ``.ini`` file.

Dam break
---------

.. dropdown:: Dam break
   :icon: comment
   :open:

   Folder ``TestCase14_Dam-Break2D`` contains four test cases for simulations of surface tension sensitivity :math:`\sigma`.

   .. admonition:: For LBM training session: run LBM_Saclay on Orcus
      :class: error

      Go to folder and run

       .. code-block:: shell

          $ cd TestCase14_Dam-Break2D
          $ sbatch /tmpformation/LBM_Saclay/Slurm-Orcus/JOB_H100_GPU.slurm TestCase14_Dam-Break.ini

      The simulation ran 385.795 seconds (~6min26sec) on partition gpuq_h100 of Orcus to achieve 500.001 time-steps.

   .. admonition:: For LBM training session: post-processing with paraview 5.11
      :class: error

      Post-process with paraview11

       .. code-block:: shell

          $ paraview11&

   .. admonition:: For LBM training session: Exercise
      :class: important

      Make a video of your simulation with paraview.

3D Taylor bubble
----------------

.. dropdown:: 3D Taylor bubble
   :icon: comment
   :open:

   The mesh is composed of 128x128x1536 cells (i.e. ~ 25.166 Mcells). Go to folder and run

    .. code-block:: shell

       $ cd TestCase22_Taylor-Bubble3D
       $ sbatch /tmpformation/LBM_Saclay/Slurm-Orcus/JOB_H100_4MPI.slurm Taylor-Bubble3D_4MPI.ini


   .. list-table:: Benchmark on several computers
      :stub-columns: 1
      :header-rows: 1

      * - Computer
        - Architecture
        - Model
        - Nb MPI
        - Time of simulation
        - MCUPS
        - Bandwidth (Gb/s)
      * - Orcus
        - GPU nvidia
        - H100
        - 2
        - 41319 s (~11h28min39s)
        - 447.89
        - 505.22
      * - Orcus
        - GPU nvidia
        - H100
        - 4
        - 23021 s (~6h23min41s)
        - 820.26
        - 925.26


References
----------

.. footbibliography::

.. sectionauthor:: Alain Cartalade
   