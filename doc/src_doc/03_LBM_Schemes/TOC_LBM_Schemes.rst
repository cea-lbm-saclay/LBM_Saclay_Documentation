.. include:: ../Substitutions.rst

.. _LBM-Saclay-Schemes:

PART III: Lattice Boltzmann schemes in LBM_Saclay
=================================================

This section focuses on the description of Lattice Boltzmann schemes in LBM_Saclay. It is seprated into four main subsections: 1) Streaming and collision operators, 2) Equilibrium distribution functions, 3) LBM for Navier-Stokes/Korteweg model and 4) Forces and other schemes.

Streaming and collision operators
---------------------------------

.. admonition:: :mediumbold:`Streaming and collision operators`

   We start with the :ref:`Def-Lattices` and we give precisions on the streaming stage. Next section :ref:`Collision_Op` focuses on four most popular collision operators :math:`\Omega_i^{\iota}(f_{i},f_{i}^{eq})` with :math:`\iota=BGK, TRT, MRT, CM`.

   .. toctree::
      :maxdepth: 2
   
      ./A_Basic-LBM/01_Lattices-Streaming_LBMSaclay.rst
      ./A_Basic-LBM/02_Collision-Operators_LBMSaclay.rst

Equilibrium distribution functions
----------------------------------

.. admonition:: :mediumbold:`Equilibrium distribution functions`

   In this sections, the equilibrium distribution functions :math:`f_i^{eq}` will be described for incompressible Navier-Stokes equations and for transport equations.

   .. toctree::
      :maxdepth: 2

      ./A_Basic-LBM/03_Equilibrium-Functions_Navier-Stokes.rst
      ./A_Basic-LBM/04_Equilibrium-Functions_Transport-Equations.rst
      
LBM for Navier-Stokes/Korteweg model
------------------------------------

.. admonition:: :mediumbold:`LBM for Navier-Stokes/Korteweg model`

   The Navier-Stokes/Korteweg model (NSK) is a popular alternative model for simulating two-phase flows without introducing a phase-field :math:`\phi`. That model is a low Mach formulation of the Navier-Stokes equations, where :math:`\rho` plays the role of phase index. The two-phase behavior is obtained by an appropriate choice of the Equation of State (EoS).

   .. toctree::
      :maxdepth: 3
   
      ./B_Specific-Schemes/LBM_for_NSK.rst

Forces and Other schemes
-------------------------

.. admonition:: :mediumbold:`Forces and other schemes`

   Finally the last term :math:`\mathcal{F}_i` is detailed with discretization of other differential operators (gradients and Laplacian).

   .. toctree::
      :maxdepth: 2
   
      ./A_Basic-LBM/05_Forces-LBMSaclay.rst
      ./C_Other/Additional_Gradients.rst
      ./C_Other/Boundary_Conditions.rst
   
 
