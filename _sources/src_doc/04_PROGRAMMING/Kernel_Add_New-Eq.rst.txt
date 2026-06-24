.. _Tuto-New-Equation:

Add a new equation inside the new kernel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In LBM_Saclay 5 equations and distribution functions are already available. If ``fcount`` > 5 then modify file ``src/kernels/LBMSchemeBase.h``. Here, we present a case with 4 equations.

**File Problem_MPwSLphC.h**

1. Modify the number of Equations in ``Problem``

   .. code-block:: ruby
      :emphasize-lines: 2
      :linenos:

      Base::nbEqs = 3;
      Base::nbEqs = 4;

2. For functions ``init_f`` and ``update_f``, add a new block. For example copy-paste the block of Equation1 and modify ``EquationTag1`` --> ``EquationTag4`` and ``collisionType1`` --> ``collisionType4``

   .. code-block:: ruby
      :emphasize-lines: 1,2,3
      :linenos:

      if (params.collisionType1 == BGK) {
         update1eq<EquationTag4, BGKCollider<dim, npop>>();
      }

3. In ``make_boundaries`` add a new line for periodic BC 

   .. code-block:: ruby
      :emphasize-lines: 1
      :linenos:

      this->bcPerMgr.make_boundaries(scheme.f4, BOUNDARY_EQUATION_4);

**File LBMScheme_MPwSLphC.h**

1. In file ``LBMScheme`` add  tag ``EquationTag4 tag``.

   .. code-block:: ruby
      :emphasize-lines: 4
      :linenos:

      EquationTag1 tagPHI;
      EquationTag2 tagNS;
      EquationTag3 tagCOMP;
      EquationTag4 tagPSI;

   Add new setup collider for new Eq with

   .. code-block:: ruby
      :emphasize-lines: 1,2,3,4,5
      :linenos:

      KOKKOS_INLINE_FUNCTION
      void setup_collider(EquationTag4 tag, const IVect<dim> &IJK,
                           BGK_Collider &collider) const {
      
      }

