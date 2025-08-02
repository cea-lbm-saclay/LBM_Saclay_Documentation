.. _Math-Models:

PART II: Mathematical models in LBM_Saclay
==========================================

In this Section you will find details on mathematical models which are implemented in LBM_Saclay. They are separated into two main Sections for **Two-phase models** and **Multi-phase models**.
   
Two-phase models
^^^^^^^^^^^^^^^^

Fluid-Fluid interface
"""""""""""""""""""""

Two formulations of Fluid-Fluid interface models differ from the hypotheses of Navier-Stokes (NS) equations. In the first one, the two fluids are supposed to be incompressible. The interface is captured with a levelset-type equation called the *Conservative Allen-Cahn* (CAC) equation. In the second one, the two fluid phases are modelled by a low-Mach formulation of the NS equations with an Equation of State (EoS). Such a model is called *Navier-Stokes/Korteweg* model.

**NS/Conservative Allen-Cahn based models**

.. toctree::
   :maxdepth: 1

   ./01_Fluid_Fluid/Model_NSAC_Comp.rst
   ./01_Fluid_Fluid/Model_NSAC_Surfactant.rst
   ./01_Fluid_Fluid/Model_NSAC_Comp_PhaseChange.rst

**NS/Korteweg based models**

.. toctree::
   :maxdepth: 1

   ./01_Fluid_Fluid/Model_NSK.rst
   ./01_Fluid_Fluid/Model_NSK_Surfactant.rst

Fluid-Solid interface
"""""""""""""""""""""

In this section, the interface is a separation between one liquid phase with one solid phase. fluid flows are not taken into account (no NS equations) in the fluid phase. The interface moves only because of thermodynamic imbalance due to phase change. The models are derived from the phase-field theory. In the first model (*dissolution*), the solid phase disappears whereas in the second one (*crystal growth*) the solid phase expands. For both models, only two components are considered (binary systems). In the third model (*gel maturation*), three components are considered (ternary systems).

.. toctree::
   :maxdepth: 1
   
   ./02_Fluid_Solid/Model_Dissolution.rst
   ./02_Fluid_Solid/Model_CrystalGrowth.rst
   ./02_Fluid_Solid/Model_Maturation_Gel.rst


Multi-phase models
^^^^^^^^^^^^^^^^^^

Fluid-Fluid-Solid interfaces
""""""""""""""""""""""""""""

.. toctree::
   :maxdepth: 1

   ./03_Fluid_Fluid_Solid/Model_NSAC_Comp_Solid.rst

Fluid-Fluid-Fluid interfaces
""""""""""""""""""""""""""""
.. toctree::
   :maxdepth: 1

   ./04_Fluid_Fluid_Fluid/NS_2AC_Comp.rst
   