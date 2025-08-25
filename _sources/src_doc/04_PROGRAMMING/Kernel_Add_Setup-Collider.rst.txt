.. _Tuto-Setup-Collider:

Write your function ``setup_collider``
======================================

The example is given on Conservative Allen-Cahn equation of kernel ``NSAC_Comp``.

Objective
---------

.. admonition:: Write a function ``setup_collider``
   :class: error

   In LBM_Saclay, it is required to write a C++ function named ``setup_collider`` for each PDE we want to simulate. For example if we want to simulate the CAC equation with a BGK collision, that function must be defined in file ``LBMScheme_NS_AC_Comp.h``:

      .. code-block:: ruby

         void setup_collider(EquationTag1 tag, const IVect<dim> &IJK, BGK_Collider &collider) const {

            To complete
      
         }

where ``EquationTag1`` refers to the phase-field equation and ``BGK_Collider`` indicates that the function defines the inputs necessary for BGK collision. The distribution function for the phase-field :math:`\phi` is :math:`g_i(\boldsymbol{x},t)`. The BGK operator requires four inputs that must be defined in that function (see :ref:`Collision_Op`):

.. math::
   :label: Distrib_after_collision_Tutorial2

   g_{i}^{\star}(\boldsymbol{x},t)=\underbrace{g_{i}(\boldsymbol{x},t)}_{\text{collider.f[ipop]}}-\frac{1}{\underbrace{\tau_{g}}_{\text{collider.tau}}}\bigl[g_{i}(\boldsymbol{x},t)-\underbrace{\overline{g}_{i}^{eq,ADE}(\boldsymbol{x},t)}_{\text{collider.feq[ipop]}}\bigr]+\underbrace{\delta t{\color{red}\mathscr{S}_{i}^{\phi}}(\boldsymbol{x},t)}_{\text{collider.S0[ipop]}}

The inputs are the distribution function ``f[ipop]``, the equilibrium distribution function ``feq[ipop]``, the collision rate ``tau`` and the source term ``S0[ipop]``. For CAC equation, the equilibrium distribution function can be defined by:

.. math::
   :label: feq_for_CAC_Tutorial2

   \overline{g}_{i}^{eq,ADE}(\boldsymbol{x},t)=\overbrace{w_{i}}^{\text{w[ipop]}}\underbrace{{\color{red}\phi}}_{{\color{red}\text{Model.M0_PHI}}}\biggl[1+\frac{c\overbrace{\boldsymbol{e}_{i}\cdot\boldsymbol{u}}^{\text{Base::compute_scal}}}{c_{s}^{2}}\biggr]-\frac{1}{2}\underbrace{\delta t{\color{red}\mathscr{S}_{i}^{\phi}}}_{\text{collider.S0[ipop]}}

with a source term defined by:

.. math::
   :label: Source_term_for_CAC_Tutorial2

   {\color{red}\mathscr{S}_{i}^{\phi}}=w_{i}\biggl[(1-\chi)(\underbrace{\mathscr{S}_{st}}_{\text{Model.S_st}}+\underbrace{\mathscr{S}_{dw}}_{\text{Model.S_dw}})+\chi\underbrace{\mathscr{S}_{ct}}_{\text{Model.S_ct}}\times c\times\underbrace{\boldsymbol{e}_{i}\cdot\boldsymbol{n}}_{\text{Base::compute_scal}}\biggr]

The coefficient :math:`\chi` is either 0 or 1.

Solution
--------

Preliminary declarations
^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Declaration of local variables
   :class: hint

   Many variables such as the time step :math:`\delta t`, the space-step :math:`\delta x`, the lattice coefficient :math:`e^2`, etc. are already defined in the struture ``ModelParam`` contained in file ``Models_NS_AC_Comp.h``. We must get them

      .. code-block:: ruby

         void setup_collider(EquationTag1 tag, const IVect<dim> &IJK, BGK_Collider &collider) const {

            const real_t dt    = Model.dt;
            const real_t dx    = Model.dx;
            const real_t e2    = Model.e2;
            const real_t c     = dx / dt;
            const real_t c_cs2 = e2 / c; // Ratio c/cs2

.. admonition:: Get the moments and source terms
   :class: hint

   The C++ functions computing the source terms and the moments of order 0, 1 and 2 are also defined in file ``Models_NS_AC_Comp.h``. They must be set

      .. code-block:: ruby

         ...

         LBMState lbmState;
         Base::template setupLBMState2<LBMState, COMPONENT_SIZE>(IJK, lbmState);

         const real_t M0       = Model.M0_PHI(tag, lbmState);
         const RVect<dim> M1   = Model.M1_PHI<dim>(tag, lbmState);
         const real_t M2_AC    = Model.M2_PHI(tag, lbmState);
         const real_t M2_CH    = Model.M2_MU_PHI(tag, lbmState);

      Here ``M0_PHI`` refers to :math:`\phi`, ``M1_PHI`` refers to :math:`\boldsymbol{u}\phi`, and ``M2_PHI`` refers to :math:`\overline{\overline{\boldsymbol{I}}}\phi`. For Cahn-Hilliard equation, ``M2_MU_PHI`` refers to :math:`\overline{\overline{\boldsymbol{I}}}\mu_{\phi}`.

      .. code-block:: ruby

         const int CH          = Model.cahn_hilliard ;
         const real_t M2       = CH*M2_CH + (1-CH)*M2_AC ;

      where ``CH`` is either 0 or 1. The source terms are also defined in ``Models_NS_AC_Comp.h``:

      .. code-block:: ruby

         const real_t G_st     = Model.S_st(tag, lbmState);
         const real_t G_dw     = Model.S_dw(tag, lbmState);
         const RVect<dim> G_ct = Model.S_ct<dim>(lbmState);

Inputs for BGK operator
^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: First ``collider.`` input: collision rate ``tau``
   :class: important

   **Collision rate**

      .. code-block:: ruby
   
         collider.tau = Model.tau_PHI(tag, lbmState);

   The collision rate :math:`\tau_{\phi}` is also defined in ``Models_NS_AC_Comp.h``. It is useful to define a new coefficient involving ``collider.tau``

      .. code-block:: ruby

         real_t staudx = e2 / ((collider.tau - 0.5) * dx);

For :math:`i=0`
""""""""""""""""

.. admonition:: Other ``collider.`` inputs
   :class: important
   
   **Distribution function** ``f[0]``

      .. code-block:: ruby

         collider.f[0] = Base::get_f_val(tag, IJK, 0);

   **Source term** ``S0[0]``
   
      .. code-block:: ruby

         collider.S0[0] = w[0] * dt * (G_st + G_dw + staudx * Base::compute_scal(0, G_ct));

   **Equilibrium distribution function** ``feq[0]``

      .. code-block:: ruby

         collider.feq[0] = M0 - (1 - w[0]) * M2 - 0.5 * collider.S0[0];

For :math:`1\leqslant i\leqslant N_{pop}-1`: loop on ``ipop``
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. admonition:: Other ``collider.`` inputs
   :class: important

      .. code-block:: ruby

         for (int ipop = 1; ipop < npop; ++ipop) {
            collider.f[ipop] = this->get_f_val(tag, IJK, ipop);
            collider.S0[ipop] = w[ipop] * dt * (G_st + G_dw + staudx * Base::compute_scal(ipop, G_ct));
            collider.feq[ipop] = w[ipop] * (M2 + c_cs2 * Base::compute_scal(ipop, M1)) - 0.5 * (collider.S0[ipop]) ;
            }
         } // end of setup_collider for phase field equation

.. sectionauthor:: Alain Cartalade
   