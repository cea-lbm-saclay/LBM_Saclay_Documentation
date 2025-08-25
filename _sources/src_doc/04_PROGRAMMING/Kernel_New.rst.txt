.. _Kernel-New:

Add a new kernel
----------------

Here we present how to add a new kernel in the ``LBM_Saclay_Rech-Dev`` version. For example, we want to add a new kernel based on ``NSAC_Comp`` and named ``MPwSLphC`` for *Multi-Phase with Solid-Liquid phase Change*. The mathematical model of ``NSAC_Comp`` detailed in :ref:`Math-NSAC-Comp`, is extended here to add a new phase-field equation for simulating crystal growth.

.. toctree::
   :maxdepth: 1

   ./Kernel_Add_New-Kernel.rst
   ./Kernel_Add_New-Eq.rst
   ./Kernel_Add_Setup-Collider.rst
