.. _Single-Training-LBM:

Run "Single phase test cases"
-----------------------------

Lid driven cavity flow
^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: For LBM training session: example on Orcus
   :class: error

   Run one of the three ``.ini`` file, e.g. for Re=1000:

    .. code-block:: shell

       $ sbatch /tmpformation/LBM_Saclay/JOB_H100_GPU.slurm TestCase01_Lid_driven_cavity_flow_Re1000.ini

   On gpuq_h100 of Orcus, the simulation ran 55.300 seconds to achieve 200.001 time-steps..

Once the simulation is complete, in paraview12

.. admonition:: For training session: commands in paraview
   :class: error

   1. Open ``lid_driven_cavity_flow_1000_FINAL.vti`` file and ``Apply``
   2. ``Ctrl space`` + ``Cell Data to Point Data`` and ``Apply``
   3. ``Ctrl space`` + ``Plot Over Line``
   4. Select ``Sample At Segment Centers`` Clic on ``Y axis`` and ``Apply`` --> new graph with profile
   5. ``File`` --> ``Save Data``, ``file name``: ``profil_lid_driven_cavity_BGK_1000_Ux.csv`` and ``OK``

Next in your terminal

.. admonition:: For training session: python script
   :class: error

    .. code-block:: shell

       $ python Post-Pro_Lid_Driven_Cavity_Flow_Profile_Ux_y_Re1000.py
Benchmark on cavity flow with Ghia et al (1982)

.. container:: sphinx-features

   .. _target-Fig-Profiles-CavityFlow:
   
   .. figure:: ../../../src_doc/FIGS/01_FIGS_VALIDATIONS/res1_ldcf.png
      :height: 400
      :width: 500
      :scale: 70
      :align: left
      
      Profiles :math:`u_x(y)`.
      
   .. figure:: ../../../src_doc/FIGS/01_FIGS_VALIDATIONS/res2_ldcf.png
      :height: 400
      :width: 500
      :scale: 70
      :align: center 
   
      Profiles :math:`u_y(x)`.

The streamlines inside the cavity are presented on :numref:`target-Fig-Stream-CavityFlow`

.. _target-Fig-Stream-CavityFlow:

.. figure:: ../../../src_doc/FIGS/01_FIGS_VALIDATIONS/simu_ldcf.png
   :height: 500
   :width: 500
   :scale: 60
   :align: center
   
   Streamlines
   
Poiseuille flow
^^^^^^^^^^^^^^^

Once the simulation is complete (78.891 seconds on CPU of is154726 for 250.000 time-steps), follow the instructions below

In paraview12

.. admonition:: For training session: commands in paraview
   :class: error

   1. Open ``TestCase02_Poiseuille_Water_FINAL.vti`` file and ``Apply``
   2. ``Ctrl space`` + ``Cell Data to Point Data`` and ``Apply``
   3. ``Ctrl space`` + ``Plot Over Line``
   4. Select ``Sample At Segment Centers`` Clic on ``Y axis`` and ``Apply`` --> new graph with profile
   5. ``File`` --> ``Save Data``, ``file name``: ``Poiseuille_Water.csv`` and ``OK``

Next in your terminal

.. admonition:: For training session: python script
   :class: error

    .. code-block:: shell

       $ python Post-Pro_Poiseuille_CompareAnaly.py

   In input file ``TestCase02_Poiseuille_Water.ini`` test successively ``nStepmax=250000`` and ``nStepmax=500000``. The python script shoult plot :numref:`target-Fig-SinglePoiseuille`.

.. admonition:: For training session: if problem with plot
   :class: important
   
   Check in ``Poiseuille_Water.csv`` file that the column numbers of ``"vx"`` and ``"Points:1"`` match with numbers set in ``Post-Pro_Poiseuille_Water_CompareAnaly.py`` file:

   .. code-block:: ruby

      if row[0]!= 'laplaphi':
            x_star = np.append(x_star, float(row[32]))
            u_star = np.append(u_star, float(row[10]))


.. _target-Fig-SinglePoiseuille:

.. figure:: ../../../src_doc/FIGS/01_FIGS_VALIDATIONS/Poiseuille_Water.png
   :height: 400
   :width: 500
   :scale: 100
   :align: center
   
   Validation with Poiseuille analytical solution.
   
