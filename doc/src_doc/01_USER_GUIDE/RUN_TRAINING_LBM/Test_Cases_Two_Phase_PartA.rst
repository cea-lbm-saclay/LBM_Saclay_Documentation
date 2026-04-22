.. _TwoP-Training-LBM-PARTA:

Run "Two-phase with fluid flows" PART A: Verifications
======================================================

The first three test cases for two-phase with fluid flows compare the numerical solutions with classical solutions: the first one is the comparison with  of double-Poiseuille analytical solution, the second one is the Rayleigh-Taylor instability and the last one is the comparison with analytical solution of Prosperetti. 

Double-Poiseuille analytical solution
-------------------------------------

.. dropdown:: Double-Poiseuille: verification of viscosity ratio
   :icon: comment
   :open:

   Comparison of LBM_Saclay with the analytical solution of double-Poiseuille flows Eqs :eq:`Analy-DP` with the coefficient :math:`G` defined by Eq. :eq:`Coeff_G` written in :bdg-ref-primary-line:`Analytical-Solution-Double-Poiseuille`.

   .. admonition:: For LBM training session
      :class: error

       .. code-block:: shell

          $ cd run_training_lbm/TestCase07_Double-Poiseuille

      Run with BGK collision operator

       .. code-block:: shell

          $ ~/LBM_Saclay_Rech-Dev/build_openmp/src/LBM_saclay TestCase07_Double_Poiseuille_BGK.ini

      The simulation ran 583.956 seconds on CPU of is154726 against 100.055 on partition gpuq_h100 of Orcus to achieve 300.001 time-steps.

      Run with MRT collision operator

       .. code-block:: shell

          $ ~/LBM_Saclay_Rech-Dev/build_openmp/src/LBM_saclay TestCase07_Double_Poiseuille_MRT.ini

   Once the simulation is complete, in paraview12:

   .. admonition:: For training session: commands in paraview
      :class: error

      1. Open ``double_poiseuille_100_FINAL.vti`` and select ``vy``
      2. ``Ctrl space`` and ``Cell Data to Point Data`` and ``Apply``
      3. ``Ctrl space`` + ``Plot Over Line``
      4. Select ``Sample At Segment Centers`` Clic on ``X axis`` and ``Apply`` --> new graph with profile
      5. ``File`` --> ``Save Data``, ``file name``: ``Profil_Double-Poiseuille_BGK.csv`` and ``OK``

   Next in your terminal

   .. admonition:: For training session: python script
      :class: error

       .. code-block:: shell

          $ python Post-Pro_Double-Poiseuille_BGK.py

      After running python script, you should obtain :numref:`target-Fig-DP`. If problem with plot, Check in file ``Profil_Double-Poiseuille_BGK.csv`` that the column numbers of ``"vy"`` and ``"Points:0"`` match with numbers set in file ``Post-Pro_Double-Poiseuille_BGK.py``:

       .. code-block:: ruby

          if row[0]!= 'laplaphi':
            x_list = np.append(x_list, float(row[31]))
            u_y = np.append(u_y, float(row[15]))

   .. container:: sphinx-features

      .. _target-Fig-DP:

      .. figure:: ../../../src_doc/FIGS/01_FIGS_VALIDATIONS/Double-Poiseuille.png
         :height: 400
         :width: 500
         :scale: 80
         :align: center
   
         Validation with double-Poiseuille analytical solution.

      .. _target-Fig-DP_BGK_MRT:

      .. figure:: ../../../src_doc/FIGS/01_FIGS_VALIDATIONS/Double-Poiseuille_Compare_BGK-MRT.png
         :height: 400
         :width: 500
         :scale: 80
         :align: center
   
         Comparison between BGK and MRT collision for :math:`\eta_A/\eta_B=100`.

Rayleigh-Taylor instability
---------------------------

.. dropdown:: Rayleigh-Taylor instability: verification of small density ratio (:math:`\rho_H/\rho_{\ell}=500`)
   :icon: comment
   :open:

   The second validation is a comparison with the Rayleigh-Taylor instability of the literature. For that test case, several dimensionless numbers are commonly used. First, the characteristic velocity is defined by :math:`U_c` where :math:`g` is the gravity and :math:`L` is the domain width. Once that characteristic velocity is defined, it is used in dimensionless numbers of fluid flows such as Reynolds and capillary numbers. The Atwood number is also used in simulations and Peclet number for phase-field equation.

   .. grid:: 3
      :gutter: 4
      :margin: 0

      .. grid-item::
         :columns: 3

         .. admonition:: Characteristic velocity
      
            .. math::
         
               U=\sqrt{gL}

      .. grid-item::
         :columns: 3
   
         .. admonition:: Reynolds number 
      
            .. math::

               \text{Re}=\frac{L\sqrt{gL}}{\nu}

      .. grid-item::
         :columns: 3
   
         .. admonition:: Atwood number 
      
            .. math::

               \text{At}=\frac{\rho_{h}-\rho_{l}}{\rho_{h}+\rho_{l}}

   .. grid:: 3
      :gutter: 4
      :margin: 0

      .. grid-item::
         :columns: 3

         .. admonition:: Capilary number 
      
            .. math::

               \text{Ca}=\frac{\eta\sqrt{gL}}{\sigma}

      .. grid-item::
         :columns: 3

         .. admonition:: Peclet number 
      
            .. math::
         
               \text{Pe}=\frac{L\sqrt{gL}}{M_{\phi}}

   Input parameters inside the ``.ini`` file of LBM_Saclay correspond to those calculated in the python script ``Pre-Pro_InputParam_Rayleigh-Taylor.py``.


   .. admonition:: For LBM training session: run
      :class: error

       .. code-block:: shell

          $ cd run_training_lbm/TestCase08_Rayleigh-Taylor2D

      Run with BGK collision operator

       .. code-block:: shell

          $ ~/LBM_Saclay_Rech-Dev/build_openmp/src/LBM_saclay TestCase08_Rayleigh-Taylor_Spike-Bubble.ini

   The simulation ran 587.993 seconds on CPU of is154726 against 28.233 seconds on gpuq_h100 on Orcus to achieve 52.000 time-steps.

         .. list-table:: Benchmark (performed September 3rd, 2025)
            :align: center
            :stub-columns: 1
            :header-rows: 1

            * - Computer
              - Architecture
              - Model
              - Time of simulation
            * - is247529
              - CPU
              - 13th Gen Intel(R) Core(TM) i9-13900K
              - 142.333 s
            * - manwe
              - CPU
              - Intel(R) Xeon(R) Gold 6230R CPU @ 2.10GHz
              - 140.626 s
            * - manwe
              - GPU
              - RTX A6000
              - 66.424 s
            * - Orcus
              - GPU
              - A100
              - 32.744 s
            * - Orcus
              - GPU
              - H100
              - 28.233 s

   .. admonition:: For training session: commands in paraview
      :class: error

      1. Open all ``.vti`` files and select ``phi``
      2. ``Ctrl space`` and ``Cell Data to Point Data`` and ``Apply``
      3. Clic on ``contour`` and select field ``phi`` with value ``0.5`` and ``Apply``
      4. ``File`` --> ``Save Data``, choose ``.cvs`` format and create a new folder ``Contours``. Select it and write the file name: ``data``
      5. Clic on ``Write Time Steps`` and ``Write Time Steps Separately`` and ``OK``

      For every time-step, the value of phase-field :math:`\phi=0.5` will be written in an output file ``data_I`` where ``I`` is an integer.

   Next in your terminal

   .. admonition:: For training session: python script
      :class: error

      Both files ``RT2D_Bubble_Ref_Fakhari_PRE2017.dat`` & ``RT2D_Spike_Ref_Fakhari_PRE2017.dat`` contain :math:`t^{\star}` and :math:`y` positions of bubble point (1st file) and spike (2nd file). They have been digitalized from Fig 6 of reference :footcite:p:`Fakhari_etal_PRE2017`. All files ``data.csv`` must be set in a new folder ``Contours``:

       .. code-block:: shell

          $ python Post-Pro_Rayleigh-Taylor2D_CompareFakhari.py

      After running the python script you should find :numref:`target-Fig-RT2D-Evol`.

   **Results**

   The initial condition is presented on :numref:`target-Fig-RT2D-Init` and the evolution of bubble (green dots) and spikes (blue triangles) is presented on :numref:`target-Fig-RT2D-Evol`. The benchmark is performed with black dots from reference.

   .. container:: sphinx-features

      .. figure:: ../../../src_doc/FIGS/01_FIGS_VALIDATIONS/Init_Rayleigh-Taylor.png
         :name: target-Fig-RT2D-Init
         :height: 600
         :width: 400
         :scale: 60
         :align: center

         Initial condition for Rayleigh-Taylor test case

      .. figure:: ../../../src_doc/FIGS/01_FIGS_VALIDATIONS/Valid_RT2D.png
         :name: target-Fig-RT2D-Evol
         :height: 600
         :width: 800
         :scale: 60
         :align: center
   
         Evolution of spike and bubble point. Benchmark with literature.
   
   .. div:: sd-text-center

      .. raw:: html
   
         <video controls src="../../../_static/Vid_Rayleigh-Taylor_Instability.webm" width="400" height="550"> </video>

.. admonition:: Exercise
   :class: important

   In LBM_Saclay input file, modify :math:`\nu^{\star}`, and :math:`M_{\phi}` such as Re=1000 and Pe=100. We will simulate two cases. The first one with a surface tension :math:`\sigma^{\star}` set such as Ca=0.01 and the second one such as Ca=0.1. Run both simulations, make the video and discuss consistency of results with the capillary length :math:`l_c`.

   Method:

   1) use the pre-processing python script to set the parameters

    .. code-block:: shell

       $ python InputParam_Exercise.py

   2) Set the parameters in LBM_Saclay input file and run the simulation

   3) Once the simulations is performed, use ``pvpython`` command (paraview python) with ``Rayleigh-Taylor-Make-Video.pvpy`` (which uses the pvstate file ``State_Vid_Rayleigh-Taylor2D_PV513.pvsm``) to make the video. 

    .. code-block:: shell

       $ /tmp_formation/LBM_Saclay/ParaView/ParaView-5.13.0-MPI-Linux-Python3.10-x86_64/bin/pvpython Rayleigh-Taylor-Make-Video.pvpy


Capillary wave: analytical solution of Prosperetti
--------------------------------------------------

.. dropdown:: Capillary wave: verification of high density ratio (:math:`\rho_H/\rho_{\ell}=500`)
   :icon: comment
   :open:

   The *Capillary wave* is a test case with an analytical solution of Prosperetti :bdg-ref-primary-line:`Analytical-Solution-Capillary-Wave-Prosperetti`.

   .. admonition:: For LBM training session: mesh 256x512
      :class: error

      Run LBM_Saclay with one value specific value of kinematic viscosity :math:`\nu`:

       .. code-block:: shell

          $ cd run_training_lbm/TestCase09_Capillary-Wave2D/Mesh_256x512_nu0
          $ ~/LBM_Saclay_Rech-Dev/build_openmp/src/LBM_saclay TestCase09_Capillary-Wave_Prosperetti_Cas1_nu0.ini

      The simulation ran 46 min on GPU A6000 of MANWE to achieve 1.600.001 time-steps. The same simulation ran 797.855 seconds (~ 13min18s) on partition gpuq_h100 of Orcus.

   For comparison with analytical solution in paraview12:

   .. admonition:: For training session: commands in paraview
      :class: error

      1. Open all ``.vti`` files and select ``phi``
      2. ``Ctrl space`` and ``Cell Data to Point Data`` and ``Apply``
      3. Clic on ``contour`` and select field ``phi`` with value ``0.5`` and ``Apply``
      4. ``File`` --> ``Save Data``, ``file name``: ``data``
      5. Clic on ``Write Time Steps`` and ``Write Time Steps Separately`` and ``OK``

      For every time-step, the value of phase-field :math:`\phi=0.5` will be written in an output file ``data_I`` where ``I`` is an integer.

   A python script implements the Prosperreti's analytical solution and plots that solution with LBM_Saclay results post-processed with paraview. To run that script:

   .. admonition:: For training session: python script
      :class: error 

      File ``Solution-Prosperetti.dat`` contains :math:`t^{\star}` and :math:`y` computed by the analytical solution of Prosperetti. That solution was obtained for the following input parameters set inside each python script

       .. code-block:: shell

          $ python Post-Pro_Capillary-Wave_CompareProsperetti_Cas1_nu0.py

   Running python script should plot :numref:`target-Fig-Capillary1_nu0`.

   .. figure:: ../../../src_doc/FIGS/01_FIGS_VALIDATIONS/Init_Capillary-Wave.png
      :height: 400
      :width: 300
      :scale: 80
      :align: center
   
      Initial condition for capillary wave.

   **Results**

   Mesh 256x512

   .. container:: sphinx-features

      .. _target-Fig-Capillary1_nu0:

      .. figure:: ../../../src_doc/FIGS/01_FIGS_VALIDATIONS/Compare_Prosperetti_Mesh256x512_nu0.png
         :height: 400
         :width: 500
         :scale: 80
         :align: center
   
         Validation for :math:`\nu_0` on mesh size 256x512.

      .. _target-Fig-Capillary2_nu1:

      .. figure:: ../../../src_doc/FIGS/01_FIGS_VALIDATIONS/Compare_Prosperetti_Mesh256x512_nu1.png
         :height: 400
         :width: 500
         :scale: 80
         :align: center
   
         Validation for :math:`\nu_1` on mesh size 256x512.

   Mesh 400x800

   .. container:: sphinx-features

      .. _target-Fig-Capillary3_nu0:

      .. figure:: ../../../src_doc/FIGS/01_FIGS_VALIDATIONS/Compare-Prosperetti_Mesh_400x800_nu0.png
         :height: 400
         :width: 500
         :scale: 80
         :align: center
   
         Validation for :math:`\nu_0` on mesh size 400x800.

      .. _target-Fig-Capillary4_nu1:

      .. figure:: ../../../src_doc/FIGS/01_FIGS_VALIDATIONS/Compare-Prosperetti_Mesh_400x800_nu1.png
         :height: 400
         :width: 500
         :scale: 80
         :align: center
   
         Validation for :math:`\nu_1` on mesh size 400x800.


References
----------

.. footbibliography::

.. sectionauthor:: Alain Cartalade
   