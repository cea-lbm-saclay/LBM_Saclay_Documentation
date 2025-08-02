.. _TwoP-Compos-Training-LBM:

Run "Two-phase with fluid flows with composition effect"
========================================================

Effect on density
-----------------

Marangoni flow
--------------

.. figure:: ../../FIGS/01_FIGS_VALIDATIONS/MaVar.png
      :name: Analy-Marangoni
      :figclass: align-center
      :align: center
      :height: 400
      :width: 500
      :scale: 80 %
      
      Thermocapillary drop migration: effect of Marangoni number

Surfactant
----------

**Coalescence of two bubbles**

.. admonition:: For LBM training session: run LBM_Saclay on Orcus
   :class: error

   Go to folder and run

    .. code-block:: shell

       $ cd TestCase15_Surfactant/Coalescence
       $ sbatch /tmpformation/LBM_Saclay/JOB_H100_GPU.slurm TestCaseCoalescenceWithSurf.ini

   The simulation ran 59.808 seconds on partition gpuq_h100 of Orcus to achieve 70.001 time-steps.

.. admonition:: For LBM training session: post-processing with paraview 5.11
   :class: error

   Post-process with paraview11

    .. code-block:: shell

       $ paraview11&

   In paraview: open all ``.vti`` files.

.. admonition:: For LBM training session: Exercise
   :class: important

   Compare without surfactant ``TestCaseCoalescenceNoSurf.ini``. The simulation ran 40.485 seconds on partition gpuq_h100 of Orcus to achieve 50.001 time-steps. After post-processing with paraview, you should obtain the video below.

.. container:: sphinx-features

   .. raw:: html
   
      <video controls src="../../../_static/Vid_Surfactant_Droplet-Coalescence.webm" width="600" height="450"> </video>

**Falling droplet**



.. admonition:: For LBM training session: run LBM_Saclay on Orcus
   :class: error

   Go to folder and run

    .. code-block:: shell

       $ cd TestCase15_Surfactant/Falling-Droplet
       $ sbatch /tmpformation/LBM_Saclay/JOB_H100_GPU.slurm TestCase_RP_surf.ini

   The simulation ran 281.409 seconds on partition gpuq_h100 of Orcus to achieve 500.001 time-steps.

.. admonition:: For LBM training session: post-processing with paraview 5.11
   :class: error

   Post-process with paraview11

    .. code-block:: shell

       $ paraview11&

   In paraview: open file ``TestCase10_Rayleigh-PlateauSurf.xmf``,  select ``XDMF Reader`` file and ``OK``.

.. container:: sphinx-features

   .. raw:: html
   
      <video controls src="../../../_static/Vid_Surfactant_Falling-Droplet.webm" width="400" height="300"> </video>

**Other examples**

.. container:: sphinx-features

   .. raw:: html
   
      <video controls src="../../../_static/Vid_Surfactant_Rayleigh-Taylor.webm" width="400" height="300"> </video>

   .. raw:: html
   
      <video controls src="../../../_static/Vid_Surfactant_Rising-Bubble.webm" width="400" height="300"> </video>   
