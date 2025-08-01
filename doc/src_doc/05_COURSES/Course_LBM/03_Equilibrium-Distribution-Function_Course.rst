.. _Equilibrium_Func:


Equilibrium distribution functions
==================================

**For Navier-Stokes equations**

The Equilibrium Distribution Functions (EDF) depend on the physical problem and the mathematical model to be simulated. For example a fluid flow problem will require to simulate the Navier-Stokes (NS) equations. For low-Mach NS version, the EDF is the standard one defined in :ref:`Basic-LBM` by Eq. :eq:`Feq_NS-Overview-LBM`. For incompressible NS version different EDF are implemented. They are summarized in :ref:`Feq-Alt`. For single-phase with unique constant density Eq. :eq:`Feq_Incompr_V0` is sufficient. Two-phase flows with two bulk densities, the EDF is either Eq. :eq:`Feq_Incompr_V1` or Eq. :eq:`Feq_Incompr_V2` with a dimensionless pressure. The choice of one of them implies two different corrections. For the first one a source term is added Eq. :eq:`Source_Pressure`. For the second one, two force terms are added Eq. :eq:`Force_Pressure` and Eq. :eq:`Force_Viscos`.

**For transport equations**

For scalar EDP, such as transport or heat equation or phase-field equation, the equilibrium distribution functions are different. One method to derive them has been presented in :ref:`EdF-For-Transport-Equation`.


.. admonition:: Summary: equilibrium distribution functions are defined in each ``Kernels``
   
   Because the EDF depends on the mathematical model (number of EDP, scalar or vector, etc.) we must refer to the description of each ``Kernels``. If the documentation is not updated, you must see the ``LBMScheme.h`` file. For example for ``NSAC_Comp`` model, the EDF are implemented in file ``LBMScheme_NS_AC_Comp.h`` (folder ``src/kernels/NSAC_Comp``).

