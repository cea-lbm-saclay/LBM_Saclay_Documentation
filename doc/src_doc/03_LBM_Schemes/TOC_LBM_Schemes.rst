.. _LBM-Saclay-Schemes:

PART III: Lattice Boltzmann schemes in LBM_Saclay
=================================================


Basic Lattice Boltzmann Methods
-------------------------------

This section focuses on the description of Lattice Boltzmann schemes in LBM_Saclay. We start with the :ref:`Def-Lattices` and we give precisions on the streaming stage. Next section :ref:`Collision_Op` focuses on four most popular collision operators :math:`\Omega_i^{\iota}(f_{i},f_{i}^{eq})` with :math:`\iota=BGK, TRT, MRT, CM`. Next, the equilibrium distribution functions :math:`f_i^{eq}` will be described for various PDEs. Finally the last term :math:`\mathcal{F}_i` is detailed in the third subsection :ref:`Forces-LBM`. Finally, that part will wrap up with details on boundary conditions and computations of gradients.

.. toctree::
   :maxdepth: 2
   
   ./A_Basic-LBM/01_Lattices-Streaming_LBMSaclay.rst
   ./A_Basic-LBM/02_Collision-Operators_LBMSaclay.rst
   ./A_Basic-LBM/03_Equilibrium-Functions_LBMSaclay.rst
   ./A_Basic-LBM/04_Forces-LBMSaclay.rst

Specific schemes
----------------

.. toctree::
   :maxdepth: 2
   
   ./B_Specific-Schemes/LBM_for_NSK.rst
   ./C_Other/Additional_Gradients.rst
   ./C_Other/Boundary_Conditions.rst
 
