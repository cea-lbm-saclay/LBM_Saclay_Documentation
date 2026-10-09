.. include:: ../../Substitutions.rst

.. _Test-Dissolution-Ternary:

Ternary dissolution
===================

Compilation of kernel ``GPMixtTernary``
---------------------------------------

.. dropdown:: Compilation on A6000

   .. admonition:: :mediumbold:`Makefile for GPU of manwe server`
      :class: important

      - For ``cuda`` on GPU A6000 of manwe Go to folder ``LBM_Saclay_Rech-Dev``

       .. code-block:: shell

          $ cd LBM_Saclay_Rech-Dev

      and execute the ``configure_build.sh`` script to create the ``makefile``

       .. code-block:: shell

          $ ./compilation/manwe/cuda_a6000/configure_build.sh

      will return:

       .. code-block:: shell

          The following problems are currently implemented:
          0  AC
          1  Advection-Diffusion
          2  Crystal_growth_Younsi
          3  GPMixt
          4  GPMixtNS
          5  GPMixtTernary
          6  GPMuTernary
          7  MPwSLphC
          8  NS
          9  NS_3phases_1comp_phase_change
          10 NSAC_Comp
          11 NSAC_Comp_3phases
          12 NSAC_Comp_3phases3D
          13 NSAC_coupling
          14 NSAC_Fakhari
          15 NSAC_Surfactant
          Choose which problems to include by indicating a list of space or comma separated numbers, eg '0 1' or '0,1'.
          Write 'all' to include all problems.
          Problem numbers:

   .. admonition:: :mediumbold:`Compilation`
      :class: error

      Write ``5`` for ``GPMixtTernary`` kernel

       .. code-block:: shell

          Problem numbers: 5

      Go to the directory that is indicated by the green link, e.g., if number ``5`` has been set for GPU:

       .. code-block:: shell

          $ cd LBM_Saclay_Rech-Dev/build_cuda_a6000/build_GPMixtTernary

      Compile:

       .. code-block:: shell

          $ make -j 22

Run test cases
--------------

