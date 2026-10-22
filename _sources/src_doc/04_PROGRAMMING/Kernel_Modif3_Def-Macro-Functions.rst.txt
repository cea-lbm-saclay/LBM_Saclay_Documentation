.. _Tuto_Macro-Functions:

Write new closure relationships in ``Models_NS_AC_Comp.h``
==========================================================

The *closure relationships* are all *functions* such as **source terms** of PDEs, **interpolation functions**, **force terms**, **fluxes**, **moments of distribution functions**, etc. which are needed for the numerical scheme. The example is given on Conservative Allen-Cahn (CAC) equation of kernel ``NSAC_Comp``.

Objective
---------

.. admonition:: Write all macroscopic functions needed for ``setup_collider``
   :class: error

   Write in file ``Models_NS_AC_Comp.h`` all macroscopic quantities or functions which are needed for LBM algorithm.

Examples
--------

.. admonition:: Definition of relaxation rate :math:`\tau_{\phi}`
   :class: important

   The collision rate :math:`\tau_{\phi}` is defined with mobility coefficient :math:`M_{ \phi}`

   .. math::
      :label: Def_tau_Tutorial1

      \underbrace{\tau_{g}}_{\text{tau}}=\frac{1}{2}+3M_{\phi}\frac{\delta t}{\delta x^{2}}

   Its value ``tau`` is defined inside the function ``tau_PHI`` by

      .. code-block:: ruby
   
         KOKKOS_INLINE_FUNCTION
         real_t tau_PHI(EquationTag1 tag, const LBMState &lbmState) const {
            real_t tau = 0.5 + (e2 * Mphi * dt / SQR(dx));
            return (tau);
         }

.. admonition:: Moment of order zero
   :class: important

   The moment of order zero returned by the function ``M0_PHI`` is simply the function :math:`\phi`. Its value is stored in container ``lbmState[IPHI]``

      .. code-block:: ruby
   
         KOKKOS_INLINE_FUNCTION
         real_t M0_PHI(EquationTag1 tag, const LBMState &lbmState) const {
            return lbmState[IPHI];
         }

.. admonition:: Moment of second order for Cahn-Hilliard equation
   :class: important

   The chemical potential :math:`\mu_{\phi}` is defined by :math:`\mu_{\phi}=\underbrace{2H\phi(1-\phi)(1-2\phi)}_{f_{dw}^{\prime}(\phi)}-\zeta\boldsymbol{\nabla}^{2}\phi`. With :math:`H=12\sigma/W` and :math:`\zeta=3/2W\sigma`:

   .. math::
      :label: Def_mu_phi_Tutorial1

      \mu_{\phi}=\frac{3}{2}\frac{\sigma}{W}\left[g^{\prime}(\phi)-W^2\boldsymbol{\nabla}^{2}\phi\right]
      
   It is computed by the function ``M2_MU_PHI``:

      .. code-block:: ruby

         KOKKOS_INLINE_FUNCTION
         real_t M2_MU_PHI(EquationTag1 tag, const LBMState &lbmState) const {
	         const real_t mu_phi = sigma * 1.5 / W * (g_prime(lbmState[IPHI]) - SQR(W) * lbmState[ILAPLAPHI]);
            return mu_phi;
         }

.. admonition:: Counter term
   :class: important

   .. math::
      :label: Def_Counter_Term_Tutorial1

      \boldsymbol{j}_{CT}=M_{\phi}\frac{4}{W}\phi(1-\phi)\frac{\boldsymbol{\nabla}\phi}{\left|\boldsymbol{\nabla}\phi\right|}

   It is defined in the function ``RVect<dim> S_ct``:

      .. code-block:: ruby
      
         template <int dim>
         KOKKOS_INLINE_FUNCTION RVect<dim> S_ct(const LBMState &lbmState) const {
            const real_t norm = sqrt(SQR(lbmState[IDPHIDX]) + SQR(lbmState[IDPHIDY]) + SQR(lbmState[IDPHIDZ])) + NORMAL_EPSILON;
            real_t val_ct = Mphi * counter_term * 4.0 * lbmState[IPHI] * (1.0 - lbmState[IPHI]) / (W * norm);
            real_t force_ct = (1-cahn_hilliard)*val_ct ;

   Where ``counter_term`` and ``cahn_hilliard`` are either 0 or 1

      .. code-block:: ruby

            RVect<dim> term;
            term[IX] = force_ct * lbmState[IDPHIDX];
            term[IY] = force_ct * lbmState[IDPHIDY];
            if (dim == 3) {
               term[IZ] = force_ct * lbmState[IDPHIDZ];
            }
            return term;
         }

.. admonition:: Source term
   :class: important

   .. math::
      :label: Def_Source_Term_Tutorial1

      \mathscr{S}_{\psi}(\psi,\,\overline{\mu})=-\frac{\lambda M_{\psi}}{W^{2}}6\psi(1-\psi)(c_{s}^{co}-c_{l}^{co})(\overline{\mu}(c,\phi)-\overline{\mu}^{eq})

   The source term is :math:`\mathscr{S}_{\phi}` is defined in function ``S_st``

      .. code-block:: ruby

         KOKKOS_INLINE_FUNCTION
         real_t S_st(EquationTag1 tag, const LBMState &lbmState) const {
            real_t S = p_prime(lbmState[IPHI]) * (c0_co - c1_co) * (mu(lbmState[IC], lbmState[IPHI]) - mu_eq);
            return -lambda * Mphi / SQR(W) * S;
         }

   where the function :math:`\mu(c,\phi)` (``mu``) is defined by

      .. code-block:: ruby

         // =======================================================
         // 					Model for composition
         // =======================================================

         KOKKOS_INLINE_FUNCTION
         real_t mu(real_t c, real_t phi) const { return mu_eq + c - c_co(phi); }


.. sectionauthor:: Alain Cartalade
   