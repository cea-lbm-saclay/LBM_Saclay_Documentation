.. _Kernel_Modif:

Implementing your initial conditions, force terms and closure relationships
===========================================================================

When applied on one specific test case, the PDEs must supplied by **initial conditions**, **force terms** and **closure relationships**. We describe the list of instructions to add in order to implement them inside a kernel. The options of using various initial conditions, force terms or closure relationships are controlled by ``Models_NS_AC_Comp.h``.

.. code-block:: shell

   $ cd LBM_Saclay_Rech-Dev/src/kernels/NSAC_Comp


.. toctree::
   :maxdepth: 1

   ./Kernel_Modif1_Initial-Condition.rst
   ./Kernel_Modif2_Force-Term.rst
   ./Kernel_Modif3_Def-Macro-Functions.rst
      
