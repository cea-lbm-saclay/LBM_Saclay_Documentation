.. _TwoP-Solid-Training-LBM:

Run "Two-phase fluid flows interacting with a solid phase"
==========================================================

The mathematical model is described in :ref:`Math-NSAC-Comp-Solid`.

Hydrophobic surface
-------------------

Folder ``TestCase17_Hydrophobic-Solid`` contains four test cases for simulations of surface tension sensitivity :math:`\sigma`.

.. admonition:: For LBM training session: run LBM_Saclay on Orcus
   :class: error

   Go to folder ``TestCase17_Hydrophobic-Solid/Sensib_Sigma1s_val1`` for :math:`\sigma_1=10^{-5}` and run

    .. code-block:: shell

       $ cd TestCase17_Hydrophobic-Solid/Sensib_Sigma1s_val1
       $ sbatch /tmpformation/LBM_Saclay/JOB_H100_GPU.slurm TestCase_Hydrophobic-Surface_val1.ini

   The simulation ran 394.865 seconds (~6min35sec) on partition gpuq_h100 of Orcus to achieve 200.001 time-steps.

.. admonition:: For LBM training session: post-processing with paraview 5.11
   :class: error

   Post-process with paraview11

    .. code-block:: shell

       $ paraview11&

   In paraview:
   
    1. open ``TestCase_HyPhob-Surf_val1.xmf``, select ``XDMF Reader`` and clic on green button ``Apply``.
    2. Select field ``rho`` and visualize it for several times.

.. admonition:: For training session: Exercise
   :class: important

   Run three simulations with ``.ini`` file of folders ``Sensib_Sigma2s_val1`` and ``Sensib_Sigma2s_val2`` and ``Sensib_Sigma2s_val3`` to study the influence of :math:`\sigma_{2s}` on wetting. You should obtain results presented in video below.

.. container:: sphinx-features

   .. raw:: html
   
      <video controls src="../../../_static/Vid_Contact-Angle_Wetting_Surface.webm" width="700" height="450"> </video>

Vertical walls
--------------

Same test case than previous one but with vertical walls.

.. container:: sphinx-features

   .. raw:: html
   
      <video controls src="../../../_static/Vid_Contact-Angle_Vertical-Walls.webm" width="700" height="450"> </video>

Container with splashing droplet
--------------------------------

.. admonition:: For LBM training session: run LBM_Saclay on Orcus
   :class: error

   Go to folder  ``TestCase18_Container-Splash`` and run LBM_Saclay on Orcus.

    .. code-block:: shell

       $ cd TestCase18_Container-Splash
       $ sbatch /tmpformation/LBM_Saclay/JOB_H100_GPU.slurm TestCase18_Container-Splash.ini

   The simulation ran 966.784 seconds (~16min07sec) on partition gpuq_h100 of Orcus to achieve 300.001 time-steps.

.. admonition:: For LBM training session: post-processing with paraview 5.11
   :class: error

   Post-process with paraview11

    .. code-block:: shell

       $ paraview11&

   In paraview:
   
    1. open ``TestCase18_Container-Splash.xmf``, select ``XDMF Reader`` and clic on green button ``Apply``.
    2. Select field ``rho`` and visualize it for several times.

.. container:: sphinx-features

   .. raw:: html
   
      <video controls src="../../../_static/Vid_Container-with-Splash.webm" width="650" height="350"> </video>


Static container with hole
--------------------------

.. admonition:: For LBM training session: run LBM_Saclay on Orcus
   :class: error

   Go to either folder  ``TestCase19_Static-Container-Hole`` or ``TestCase20_Moving-Container-Hole`` and run LBM_Saclay on Orcus.

    .. code-block:: shell

       $ cd TestCase19_Static-Container-Hole
       $ sbatch /tmpformation/LBM_Saclay/JOB_H100_GPU.slurm TestCase19_Static-Container-Hole.ini

   The simulation ran 489.607 seconds (~8min10sec) on partition gpuq_h100 of Orcus to achieve 260.001 time-steps.

.. admonition:: For LBM training session: post-processing with paraview 5.11
   :class: error

   Post-process with paraview11

    .. code-block:: shell

       $ paraview11&

   In paraview:
   
    1. open ``TestCase19_Static-Container-Hole.xmf``, select ``XDMF Reader`` and clic on green button ``Apply``.
    2. Select field ``rho`` and visualize it for several times.

Moving container with hole
--------------------------

.. admonition:: For LBM training session: run LBM_Saclay on Orcus
   :class: error

   Go to either folder  ``TestCase19_Static-Container-Hole`` or ``TestCase20_Moving-Container-Hole`` and run LBM_Saclay on Orcus.

    .. code-block:: shell

       $ cd TestCase20_Moving-Container-Hole
       $ sbatch /tmpformation/LBM_Saclay/JOB_H100_GPU.slurm TestCase20_Moving-Container-Hole.ini

   The simulation ran 1956.470 seconds (~32min36sec) on partition gpuq_h100 of Orcus to achieve 1.000.001 time-steps.

.. admonition:: For LBM training session: post-processing with paraview 5.11
   :class: error

   Post-process with paraview11

    .. code-block:: shell

       $ paraview11&

   In paraview:
   
    1. open ``TestCase20_Moving-Container-Hole.xmf``, select ``XDMF Reader`` and clic on green button ``Apply``.
    2. Select field ``rho`` and visualize it for several times.

.. container:: sphinx-features

   .. raw:: html
   
      <video controls src="../../../_static/Vid_Container-Hole_Move-noMove.webm" width="650" height="420"> </video>
