.. _Kernel_Description:

Kernel description: example with ``NSAC_Comp``
==============================================

In LBM_Saclay, a mathematical model is a set of several Partial Derivative Equations (PDEs). Those PDEs are programmed inside a **Kernel**. All kernels are gathered inside the folder ``LBM_Saclay/src/kernels``. For example, the mathematical model of kernel ``NSAC_Comp`` is given by Eqs. :eq:`Mass_Balance_CAC-Model` -- :eq:`Composition_Equation` in :ref:`Math-NSAC-Comp`.

List of main kernels
--------------------

The main kernels are 

- ``NSAC_Comp``: :ref:`Math-NSAC-Comp`
- ``NSAC_Surfactant``: :ref:`Math-NSAC-Surfactant`
- ``NSK``: :ref:`Model_NSK`
- ``GPMixtTernary``: :ref:`Model_GPMixtTernary`

Files, structures and functions inside one kernel
-------------------------------------------------

Inside one kernel, e.g. ``NSAC_Comp``, one can find six files:

   .. code-block:: shell

      $ cd NSAC_Comp
      $ ls -l

returns

   .. code-block:: shell

      -rw-rw----+ 1 ac165432 dm2s-user-cat-a  2434 juil. 11 13:14 Index_NS_AC_Comp.h
      -rw-rw----+ 1 ac165432 dm2s-user-cat-a   968 juil. 11 13:15 InitConditionsTypes.h
      -rw-rw----+ 1 ac165432 dm2s-user-cat-a 78015 juil. 11 13:14 LBMScheme_NS_AC_Comp.h
      -rw-rw----+ 1 ac165432 dm2s-user-cat-a 49717 juil. 11 13:15 Models_NS_AC_Comp.h
      -rw-rw----+ 1 ac165432 dm2s-user-cat-a  6071 juil. 11 13:15 Problem_NS_AC_Comp.h
      -rw-rw----+ 1 ac165432 dm2s-user-cat-a  1960 juil. 11 13:14 Setup.h

We present below a summary of what those files do.

File ``Setup.h``
""""""""""""""""

The file ``Setup.h`` registers the problem (e.g. ``NSAC_Comp``) so that it may be created from ``LBMRun``. You must write a new ``Setup.h`` file for new kernel. See :ref:`Kernel-New` for more details.

File ``Problem_NS_AC_Comp.h``
"""""""""""""""""""""""""""""

The file ``Problem_NS_AC_Comp.h`` contains the functions of various stages of LBM algorithm. We present here only ``init_f()``, ``update_f()`` and ``update_m()``.

.. admonition:: Initialization of distribution function :math:`f_i`: ``init_f()``
   :class: important

   Initialize all distribution functions which are necessary for the mathematical model (3 distribution functions for ``NSAC_Comp``) for all collision operators and all equations.

      .. code-block:: ruby

         void init_f() override {
         // init distribution functions
            if (params.collisionType1 == BGK) {
               init1eq<EquationTag1, BGKCollider<dim, npop>>();
            }
            ...
         }

.. admonition:: Update distribution function :math:`f_i`: ``update_f()``
   :class: important

   Update all distribution functions which are necessary for the mathematical model (3 for NSAC_Com)

      .. code-block:: ruby

         void update_f() override {
         // init distribution functions
            if (params.collisionType1 == BGK) {
               update1eq<EquationTag1, BGKCollider<dim, npop>>();
            }
            ...
         }

.. admonition:: Update macroscopic variables ``update_m()``
   :class: important

   Small function that updates the macroscopic variables and their gradients.

      .. code-block:: ruby

         void update_m() override {
         // update macro fields
            MacroKernel::template apply<TagUpdateMacro>(params, scheme);
            MacroKernel::template apply<TagUpdateMacroGrads>(params, scheme);
         }


File ``Models_NS_AC_Comp.h``
""""""""""""""""""""""""""""

This file contains the C++ structure ``ModelParams`` which performs several tasks:

- Read input parameters set in ``.ini`` datafile. For example

   .. code-block:: ruby

      Mphi   = configMap.getFloat("params", "Mphi", 1.0);

 means: read in ``.ini`` a real value ``Mphi`` in section ``params`` and set it in ``Mphi``. If it does not exist, then set the default value ``1.0``.

- Read the keyword of initial condition. For example

   .. Code-block:: ruby

      else if (initTypeStr == "sphere")
         initType = PHASE_FIELD_INIT_SPHERE;

 means: if the keyword is ``sphere`` in the ``.ini`` file, then initialize with ``PHASE_FIELD_INIT_SPHERE``

.. admonition:: Definition of closure functions
   :class: important

   Interpolation functions, source terms, force terms, tanh solution, etc are defined in this file. For example, the classical hyperbolic tangent solution is defined by the function ``phi0``:

      .. code-block:: ruby

         KOKKOS_INLINE_FUNCTION
         real_t phi0(real_t x) const {
            return 0.5 * (1 + tanh(sign * 2.0 * x / W));
         }

   The surface tension force in NS equation writes:

      .. code-block:: ruby

         template <int dim>
         KOKKOS_INLINE_FUNCTION RVect<dim> force_TS(const LBMState &lbmState) const {
            const real_t tension = sigma * 1.5 / W * (g_prime(lbmState[IPHI]) - SQR(W) * lbmState[ILAPLAPHI]);
            RVect<dim> term;
            term[IX] = tension * lbmState[IDPHIDX];
            term[IY] = tension * lbmState[IDPHIDY];
            if (dim == 3) {
               term[IZ] = tension * lbmState[IDPHIDZ];
            }
            return term;
         }
   One interpolation function is :math:`p(\phi)=\phi^2(3-2\phi)` is defined by the function `p`:

      .. code-block:: ruby

         KOKKOS_INLINE_FUNCTION
         real_t p(real_t phi) const {
            return SQR(phi) * (3.0 - 2.0 * phi);
         }

File ``LBMScheme_NS_AC_Comp.h``
"""""""""""""""""""""""""""""""

This file contains the C++ structure ``LBMScheme`` which defines five functions described below.

.. admonition:: ``setup_collider``: definition of collision stage
   :class: important

   Definition of collision stage for each equation and collision type (BGK, TRT, MRT)

   See :ref:`Tuto-Setup-Collider`


.. admonition:: ``make_boundary``: update the boundary conditions
   :class: important

   for every distribution function

.. admonition:: ``init_macro``: initialization of macroscopic fields
   :class: important

   The initial conditions are defined in ``LBMScheme_NS_AC_Comp.h`` in function ``init_macro``:

      .. code-block:: ruby

         KOKKOS_INLINE_FUNCTION
         void init_macro(IVect<dim> IJK, RANDOM_POOL::generator_type rand_gen) const {
            ...
         }

   Each initial condition is associated with a keyword, for example:

      .. code-block:: ruby

         else if (Model.initType == PHASE_FIELD_INIT_SPHERE) {
            ...
         }

   means that the phase-field :math:`\phi(\boldsymbol{x},0)` will be set as a sphere at initial time.

.. admonition:: ``update_macro``: update the macroscopic fields
   :class: important

   Update the macroscopic fields with the distributions functions at new time-step :math:`t+\delta t`

      .. code-block:: ruby

         KOKKOS_INLINE_FUNCTION
         void update_macro(IVect<dim> IJK) const {
            ...
         }

.. admonition:: ``update_macro_grad``: update gradient of new macroscopic fields
   :class: important

   Update all gradients of macroscopic fields computed at :math:`t+\delta t`:

      .. code-block:: ruby

         KOKKOS_INLINE_FUNCTION
         void update_macro_grad(IVect<dim> IJK) const {
            ...
         }

.. admonition:: Call of closure functions defined in ``Models_NS_AC_Comp.h``
   :class: hint

   All closure functions defined in file ``Models_NS_AC_Comp.h`` are called in LBM schemes. In this file, ``Model`` is defined as a structure ``ModelParams``:

      .. code-block:: ruby

         struct LBMScheme : public LBMSchemeBase<dim, npop> {
            ...
            ModelParams Model;
            ...
         }

   Example, the surface tension force is simply called by:

      .. code-block:: ruby

         RVect<dim> ForceTS_2liq = Model.force_TS<dim>(lbmState);

   or for initialization,

      .. code-block:: ruby

         phi = Model.phi0(xphi);

File ``Index_NS_AC_Comp.h``
"""""""""""""""""""""""""""

.. admonition:: List of component indices
   :class: important

   The file ``Index_NS_AC_Comp.h`` contains the enumeration of component indices

      .. code-block:: ruby

         enum ComponentIndex {
            ID,            /*!< ID Density index */
            IP,            /*!< Pressure   index */
            IU,            /*!< X velocity / momentum index */
            IV,            /*!< Y velocity / momentum index */
            IW,            /*!< Z velocity / momentum index */
            IPHI,          /*!< Phase field index */
            ...
         }

.. admonition:: Add a new index
   :class: hint

   If you want to add a new field, for example :math:`\psi`, simply add the new index relative to this field:

      .. code-block:: ruby

         enum ComponentIndex {
            ...
            IPSI,          /*!< Phase field index for solid phase */
            ...
         }

.. admonition:: Mapping index and keywords
   :class: important

   The file ``Index_NS_AC_Comp.h`` also contains the mapping between the component indices and the keywords set in ``.ini`` file for outputs.

      .. code-block:: ruby

         struct index2names {
            static int2str_t get_id2names() {
            int2str_t map;
            // insert some fields
            map[ID]    = "rho";
            map[IU]    = "vx";
            map[IV]    = "vy";
            map[IW]    = "vz";
            map[IPHI]  = "phi";
            ...
            }
         }

.. admonition:: Output for this new field :math:`\psi`
   :class: hint

   If you want to post-process with paraview this new field :math:`\psi`, you must add

      .. code-block:: ruby

         struct index2names {
            static int2str_t get_id2names() {
            int2str_t map;
            // insert some fields
            ...
            map[IPSI]  = "psi";
            ...
         }
   
   Simply write ``psi`` in the list of output variables in the ``.ini`` file.
         
File ``InitConditionsTypes.h``
""""""""""""""""""""""""""""""

All keywords of initial conditions are gathered in an enumeration list which is written in file ``InitConditionsTypes.h``. For example

   .. code-block:: ruby

      enum InitCondition {
         PHASE_FIELD_INIT_UNDEFINED,
         PHASE_FIELD_INIT_VERTICAL,
         PHASE_FIELD_INIT_SPHERE,
         ...
      };

.. sectionauthor:: Alain Cartalade
   