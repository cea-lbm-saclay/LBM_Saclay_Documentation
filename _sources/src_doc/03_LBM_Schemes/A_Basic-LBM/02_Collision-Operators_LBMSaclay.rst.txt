.. _Collision_Op:

Collisions operators in LBM_Saclay
==================================

The collision operators are defined as C++ structures in the source file ``src/kernels/Collision_operators.h``. The most popular are implemented in LBM_Saclay: BGK, TRT, MRT and Central Moment (CM).

Batnaghar-Gross-Krook (BGK) operator
------------------------------------

In LBM_Saclay, that collision operator is performed in ``BGKCollider`` and writes

.. math::
   :label: Coll_BGK
   
   \Omega_{i}^{BGK}(f_{i},f_{i}^{eq})=-\frac{1}{\tau}\left[f_{i}-f_{i}^{eq}\right]

That collision operator requires four inputs:


.. admonition:: BGKCollider

   **Inputs**

   - :math:`f_i`: distribution function for current time :math:`t` and position contained in ``f``.
   - :math:`f_i^{eq}`: equilibrium distribution function for current time :math:`t` and position contained in ``feq``.
   - :math:`\tau`: relaxation rate contained in ``tau``.
   - :math:`\mathcal{S}_i` is the force or source term contained in ``S0``.

   **Output**

   - :math:`f_i^{\star}=f_i+\Omega_i^{BGK}+\mathcal{S}_i`: post-collision distribution function


.. admonition:: BGK in LBM_Saclay
   :class: important

   .. code-block:: ruby
   
      template <int dim, int npop> struct BGKCollider {
         public:
         using FState = typename Kokkos::Array<real_t, npop>;
         FState f;
         FState feq;
         FState S0;
         //~ FState S1;
         real_t tau;
         KOKKOS_INLINE_FUNCTION
         BGKCollider(const LBMLattice<dim, npop> &lattice){};

         KOKKOS_INLINE_FUNCTION
            real_t collide(int ipop) const {
            return (f[ipop] * (1.0 - 1.0 / tau) + feq[ipop] / tau + S0[ipop]);
         };
      
         KOKKOS_INLINE_FUNCTION
            real_t get_feq(int ipop) const { return feq[ipop]; };
      };
      
   
Two-Relaxation-Times (TRT) operator
-----------------------------------

The TRT collision operator is performed in ``TRTCollider`` and writes

.. math::
   :label: LBE_TRT
   
   \Omega_{i}^{TRT}(f_{i},f_{i}^{eq})=-\frac{1}{\tau^{+}}\left[f_{i}^{+}-f_{i}^{eq+}\right]-\frac{1}{\tau^{-}}\left[f_{i}^{-}-f_{i}^{eq-}\right]
   
where the symmetric parts of :math:`f_{i}` and :math:`f_{i}^{eq}` are defined by

.. math::
   :label: Sym_Part
   
   f_{i}^{+}=\frac{f_{i}+f_{\overline{i}}}{2}\qquad\text{and}\qquad f_{i}^{eq+}=\frac{f_{i}^{eq}+f_{\overline{i}}^{eq}}{2}

and the anti-symmetric parts by

.. math::
   :label: Antisym_Part
   
   f_{i}^{-}=\frac{f_{i}-f_{\overline{i}}}{2}\qquad\text{and}\qquad f_{i}^{eq-}=\frac{f_{i}^{eq}-f_{\overline{i}}^{eq}}{2}

In Eqs. :eq:`Sym_Part` and :eq:`Antisym_Part`, the bar notation means the opposite directions :math:`\boldsymbol{c}_{\overline{i}}=-\boldsymbol{c}_{i}`. Example on the standard D2Q9 lattice :math:`\boldsymbol{c}_{\overline{1}}=-\boldsymbol{c}_{1}=\boldsymbol{c}_{3}` . The TRT collision operator considers the collision stage with two relaxation parameters :math:`\tau^{+}` and :math:`\tau^{-}` acting respectively on the symmetric part and the anti-symmetric part. When the equilibrium distribution function is defined such as the Navier-Stokes equations are recovered, the kinematic viscosity is related to the parameter :math:`\tau^{-}` by:

.. math::
   :label: nu_TRT
   
   \nu=c_{s}^{2}\left(\tau^{-}-\frac{1}{2}\right)\delta t

and :math:`\tau^{+}` is a free paramater to tune to improve accuracy and stability. In practice, the parameter :math:`\Lambda` is often used for that purpose:

.. math::
   :label: lamgda_TRT
   
   \Lambda=\left(\tau^{+}-\frac{1}{2}\right)\left(\tau^{-}-\frac{1}{2}\right)

That collision operator requires five inputs:

.. admonition:: TRTCollider

   **Inputs**

   - :math:`f_i`: distribution function for current time :math:`t` and position contained in ``f``.
   - :math:`f_i^{eq}`: equilibrium distribution function for current time :math:`t` and position contained in ``feq``.
   - :math:`\tau^{+}`: symmetric relaxation rate contained in ``tauS``.
   - :math:`\tau^{-}`: anti-symmetric relaxation rate contained in ``tauA``.
   - :math:`\mathcal{S}_i` is the force or source term contained in ``S0``.

   **Output**

   - :math:`f_i^{\star}=f_i+\Omega_i^{TRT}+\mathcal{S}_i`: post-collision distribution function

The C++ structure TRTCollider is shown below:

.. admonition:: TRT in LBM_Saclay
   :class: important

   .. code-block:: ruby
   
      template <int dim, int npop> struct TRTCollider {
         using FState = typename Kokkos::Array<real_t, npop>;
         using LBM_speeds_opposite =
            typename LBMBaseFunctor<dim, npop>::LBM_speeds_opposite;
         LBM_speeds_opposite Ebar;

         FState f, feq;

         real_t tauS, tauA;

         FState S0;

         KOKKOS_INLINE_FUNCTION
         void setTau(real_t tau, int TRT_tauMethod) { tauA = tau; };

         KOKKOS_INLINE_FUNCTION
         TRTCollider(const LBMLattice<dim, npop> &lattice) { Ebar = lattice.Ebar; };
            //~ FState S1;
         KOKKOS_INLINE_FUNCTION
         real_t collide(int ipop) const {
            const int ipopb = Ebar[ipop];
            const real_t fi = f[ipop];
            const real_t fib = f[ipopb];
            const real_t feqi = feq[ipop];
            const real_t feqib = feq[ipopb];
            //~ real_t pS=0.5*((f[ipop]+f[ipopb])-(feq[ipop]+feq[ipopb]));
            //~ real_t pA=0.5*((f[ipop]-f[ipopb])-(feq[ipop]-feq[ipopb]));

            return (f[ipop] - 0.5 * (((fi + fib) - (feqi + feqib)) / tauS +
                                    ((fi - fib) - (feqi - feqib)) / tauA) + S0[ipop]);
         }
      
         KOKKOS_INLINE_FUNCTION
         real_t get_feq(int ipop) const { return feq[ipop]; }
      };

Multiple-Relaxation-Times (MRT) operator
----------------------------------------

**LBE with vector notations**

If we consider the space of distribution functions of dimension :math:`N_{pop}+1`, the vector notations can be used:

.. math::
   :label: Vector_Notations
   
   \boldsymbol{f}(\boldsymbol{x},t)=\left(\begin{array}{c}
   f_{0}(\boldsymbol{x},t)\\
   f_{1}(\boldsymbol{x},t)\\
   \vdots\\
   f_{N_{pop}}(\boldsymbol{x},t)
   \end{array}\right),\quad\boldsymbol{f}^{eq}(\boldsymbol{x},t)=\left(\begin{array}{c}
   f_{0}^{eq}(\boldsymbol{x},t)\\
   f_{1}^{eq}(\boldsymbol{x},t)\\
   \vdots\\
   f_{N_{pop}}^{eq}(\boldsymbol{x},t)
   \end{array}\right),\quad\boldsymbol{\mathcal{F}}(\boldsymbol{x},t)=\left(\begin{array}{c}
   \mathcal{F}_{0}(\boldsymbol{x},t)\\
   \mathcal{F}_{1}(\boldsymbol{x},t)\\
   \vdots\\
   \mathcal{F}_{N_{pop}}(\boldsymbol{x},t)
   \end{array}\right)

and the LBE writes

.. math::
   :label: LBE_MRT
   
   \boldsymbol{f}(\boldsymbol{x}+\boldsymbol{c}_{i}\delta t,t+\delta t)=\boldsymbol{f}(\boldsymbol{x},t)+\boldsymbol{\Omega}^{MRT}(\boldsymbol{f}(\boldsymbol{x},t),\boldsymbol{f}^{eq}(\boldsymbol{x},t))+\boldsymbol{\mathcal{F}}\delta t


**MRT collision operator**
   
The MRT collision operator considers the relaxation in the space of moments instead of the space of distribution functions. For that purpose a matrix :math:`\boldsymbol{M}` is used:

.. math::
   :label: MRT_Coll_Op
   
   \boldsymbol{\Omega}^{MRT}=-\boldsymbol{M}^{-1}\boldsymbol{S}(\boldsymbol{x})\boldsymbol{M}\left[\boldsymbol{f}(\boldsymbol{x},t)-\boldsymbol{f}^{eq}(\boldsymbol{x},t)\right]
   
where

- :math:`\boldsymbol{M}` represents a change of basis from “space of distribution functions” to :math:`\rightarrow` “space of moments”
- :math:`\boldsymbol{S}` contains the relaxation coefficients
- :math:`\boldsymbol{M}` and :math:`\boldsymbol{S}` are two invertible matrices of dim :math:`(N_{pop}+1)\times(N_{pop}+1)`


**Relaxation in space of moments**

Eq. :eq:`MRT_Coll_Op` means that a change of basis is first done:

.. math::
   :label: f_to_m
   
   \boldsymbol{M}(\boldsymbol{f}-\boldsymbol{f}^{eq})=\boldsymbol{m}-\boldsymbol{m}^{eq}

Next, in the space of moments, the relaxation occurs by applying the matrix :math:`\boldsymbol{S}`:

.. math::
   :label: Relaxation_moments
   
   \boldsymbol{m}^{\star}=\boldsymbol{S}(\boldsymbol{m}-\boldsymbol{m}^{eq})
   
Finally, we go back in the space of distribution functions by applying :math:`\boldsymbol{M}^{-1}`

.. math::
   :label: m_to_f
   
   \boldsymbol{f}^{\star}=\boldsymbol{M}^{-1}\boldsymbol{m}^{\star}
   
**Example for lattice D2Q9**

To construct the matrix :math:`\boldsymbol{M}`, two main procedures exist (see [1]_): Gram-Schmidt and Hermite. In LBM_Saclay, the first one is applied. One example is given with the D2Q9 lattice where the nine moving vectors are defined by :math:`\boldsymbol{e}_i` (for :math:`i=0,...,8`):

.. math::
   :label: Def_Basis_Vectors
   
   \begin{array}{cccccccccc}
    {\color{gray}\boldsymbol{e}_{0}} & {\color{gray}\boldsymbol{e}_{1}} & {\color{gray}\boldsymbol{e}_{2}} & {\color{gray}\boldsymbol{e}_{3}} & {\color{gray}\boldsymbol{e}_{4}} & {\color{gray}\boldsymbol{e}_{5}} & {\color{gray}\boldsymbol{e}_{6}} & {\color{gray}\boldsymbol{e}_{7}} & {\color{gray}\boldsymbol{e}_{8}}\\
    \left(\begin{array}{c}
    0\\
    0
    \end{array}\right) & \left(\begin{array}{c}
    1\\
    0
    \end{array}\right) & \left(\begin{array}{c}
    0\\
    1
    \end{array}\right) & \left(\begin{array}{c}
    -1\\
    0
    \end{array}\right) & \left(\begin{array}{c}
    0\\
    -1
    \end{array}\right) & \left(\begin{array}{c}
    1\\
    1
    \end{array}\right) & \left(\begin{array}{c}
    -1\\
    1
    \end{array}\right) & \left(\begin{array}{c}
    -1\\
    -1
    \end{array}\right) & \left(\begin{array}{c}
    1\\
    -1
    \end{array}\right) & \begin{array}{c}
    \leftarrow\boldsymbol{v}_{j_{x}}\\
    \leftarrow\boldsymbol{v}_{j_{y}}
    \end{array}
    \end{array}

In vector notations, the moment of order 0 (density)  can be obtained by

.. math::
   :label: Def_M0
   
   \rho=\sum_{i}f_{i}=\boldsymbol{v}_{\rho}\cdot\boldsymbol{f}

where the vector :math:`\boldsymbol{v}_{\rho}` must be defined by :math:`\boldsymbol{v}_{\rho}=(1,1,1,1,1,1,1,1,1)`. The moment of order 1 (impulsion) can be obtained by

.. math::
   :label: Def_M1_comp1
   
   \rho u_{x}=\sum_{i}f_{i}c_{ix}=\boldsymbol{v}_{j_{x}}\cdot\boldsymbol{f}

.. math::
   :label: Def_M1_comp2

   \rho u_{y}=\sum_{i}f_{i}c_{iy}=\boldsymbol{v}_{j_{y}}\cdot\boldsymbol{f}
   
where the vector :math:`\boldsymbol{v}_{j_{x}}=(0,1,0,-1,0,1,-1,-1,1)` is defined by the first line of the lattice D2Q9 and :math:`\boldsymbol{v}_{j_{y}}=(0,0,1,0,-1,1,1,-1,-1)` is the second line. To obtain the matrix :math:`\boldsymbol{M}` of dimension :math:`9\times9`, six supplementary orthogonal vectors must be defined. After application of the Gram-Schmidt procedure, the matrix :math:`\boldsymbol{M}` is

.. math::
   :label: Def_Matrix_M
   
   \boldsymbol{M}=\left(\begin{array}{c}
   \boldsymbol{v}_{\rho}\\
   \boldsymbol{v}_{e}\\
   \boldsymbol{v}_{\epsilon}\\
   \boldsymbol{v}_{j_{x}}\\
   \boldsymbol{v}_{q_{x}}\\
   \boldsymbol{v}_{j_{y}}\\
   \boldsymbol{v}_{q_{y}}\\
   \boldsymbol{v}_{p_{xx}}\\
   \boldsymbol{v}_{p_{xy}}
   \end{array}\right)=\left(\begin{array}{ccccccccc}
   1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1\\
   -4 & -1 & -1 & -1 & -1 & 2 & 2 & 2 & 2\\
   4 & -2 & -2 & -2 & -2 & 1 & 1 & 1 & 1\\
   0 & 1 & 0 & -1 & 0 & 1 & -1 & -1 & 1\\
   0 & -2 & 0 & 2 & 0 & 1 & -1 & -1 & 1\\
   0 & 0 & 1 & 0 & -1 & 1 & 1 & -1 & -1\\
   0 & 0 & -2 & 0 & 2 & 1 & 1 & -1 & -1\\
   0 & 1 & -1 & 1 & -1 & 0 & 0 & 0 & 0\\
   0 & 0 & 0 & 0 & 0 & 1 & -1 & 1 & -1
   \end{array}\right)
   
and its inverse is:

.. math::
   :label: Def_Matrix_Minv
   
   \boldsymbol{M}^{-1}=\left(\begin{array}{ccccccccc}
   \frac{1}{9} & -\frac{1}{9} & \frac{1}{9} & 0 & 0 & 0 & 0 & 0 & 0\\
   \frac{1}{9} & -\frac{1}{36} & -\frac{1}{18} & \frac{1}{6} & -\frac{1}{6} & 0 & 0 & \frac{1}{4} & 0\\
   \frac{1}{9} & -\frac{1}{36} & -\frac{1}{18} & 0 & 0 & \frac{1}{6} & -\frac{1}{6} & -\frac{1}{4} & 0\\
   \frac{1}{9} & -\frac{1}{36} & -\frac{1}{18} & -\frac{1}{6} & \frac{1}{6} & 0 & 0 & \frac{1}{4} & 0\\
   \frac{1}{9} & -\frac{1}{36} & -\frac{1}{18} & 0 & 0 & -\frac{1}{6} & \frac{1}{6} & -\frac{1}{4} & 0\\
   \frac{1}{9} & \frac{1}{18} & \frac{1}{36} & \frac{1}{6} & \frac{1}{12} & \frac{1}{6} & \frac{1}{12} & 0 & \frac{1}{4}\\
   \frac{1}{9} & \frac{1}{18} & \frac{1}{36} & -\frac{1}{6} & -\frac{1}{12} & \frac{1}{6} & \frac{1}{12} & 0 & -\frac{1}{4}\\
   \frac{1}{9} & \frac{1}{18} & \frac{1}{36} & -\frac{1}{6} & -\frac{1}{12} & -\frac{1}{6} & -\frac{1}{12} & 0 & \frac{1}{4}\\
   \frac{1}{9} & \frac{1}{18} & \frac{1}{36} & \frac{1}{6} & \frac{1}{12} & -\frac{1}{6} & -\frac{1}{12} & 0 & -\frac{1}{4}
   \end{array}\right)

   
For that definition of matrix :math:`\boldsymbol{M}`, we see that vector :math:`\boldsymbol{v}_{\rho}` is the first line of the matrix, :math:`\boldsymbol{v}_{j_{x}}` is the fourth line and :math:`\boldsymbol{v}_{j_{y}}` is the sixth line. The corresponding moment vector is:

.. math::
   :label: Def_moment_m
   
   \boldsymbol{m}=(\rho,m_{1},m_{2},\rho u_{x},m_{4},\rho u_{y},m_{7},m_{8})^T
   
One advantage of the Gram-Schmidt procedure is that the matrix :math:`\boldsymbol{S}` is diagonal:

.. math::
   :label: Def_Matrix_S
   
   \boldsymbol{S}=\text{diag}(0,\omega_{e},\omega_{\epsilon},0,\omega_{q},0,\omega_{q},\omega_{\nu},\omega_{\nu})

.. admonition:: MRTCollider

   **Inputs**

   - :math:`f_i`: distribution function for current time :math:`t` and position contained in ``f``.
   - :math:`f_i^{eq}`: equilibrium distribution function for current time :math:`t` and position contained in ``feq``.
   - :math:`\tau`: relaxation rate contained in ``tau`` and involved in matrix :math:`\boldsymbol{S}` below.
   - :math:`\mathcal{S}_i` is the force or source term contained in ``S0``.
   - :math:`\boldsymbol{M}` is the matrix contained in ``M``.
   - :math:`\boldsymbol{M}^{-1}` is the inverse matrix contained in ``Minv``.
   - :math:`\boldsymbol{S}` is the diagonal matrix contained in ``S``.

   **Output**

   - :math:`\boldsymbol{f}^{\star}=\boldsymbol{f}+\boldsymbol{\Omega}^{MRT}+\boldsymbol{\mathcal{S}}`: post-collision distribution function

Central moments collision operator
----------------------------------

In LBM_Saclay, the "central moment" collision operator is tested in ``NSAC_Comp`` kernel. In that kernel the equilibrium distribution function is formulated with a dimensionless pressure and the first-order moment is the velocity (and not the impulsion). The central moment method is inspired from reference [2]_.

General definition of moments
"""""""""""""""""""""""""""""

The general definition of 2D central moment is

.. math::
   :label: Def_Continuous_Moments

   M_{\alpha\beta}=\iint c_{x}^{\alpha}c_{y}^{\beta}f(\boldsymbol{x},t,\boldsymbol{c})dc_{x}dc_{y}

and discrete moments in velocity space:

.. math::
   :label: Def_Discrete_Moments

   m_{\alpha\beta}=\underset{i}{\sum}c_{ix}^{\alpha}c_{iy}^{\beta}f_{i}

where :math:`\alpha` and :math:`\beta` are two positive integers. Eq. :eq:`Def_Discrete_Moments` means for

- :math:`\alpha=0` and :math:`\beta=0`:

.. math::
   :label: Def_m_00

   m_{00}=\underset{i}{\sum}c_{ix}^{0}c_{iy}^{0}f_{i}=\underset{i}{\sum}f_{i}=\rho

- :math:`\alpha=1` and :math:`\beta=0`:

.. math::
   :label: Def_m_10
   
   m_{10}=\underset{i}{\sum}c_{ix}^{1}c_{iy}^{0}f_{i}=\underset{i}{\sum}f_{i}c_{ix}=\rho u_{x}

- :math:`\alpha=0` and :math:`\beta=1`:

.. math::
   :label: Def_m_01
   
   m_{10}=\underset{i}{\sum}c_{ix}^{0}c_{iy}^{1}f_{i}=\underset{i}{\sum}f_{i}c_{iy}=\rho u_{y}

and so on. As done in MRT collision operator, the vector of moments can be obtained with a transformation matrix :math:`\mathbb{M}` from space of distribution functions to space of moments. The matrix :math:`\mathbb{M}` is defined below.

Definition of central moments
"""""""""""""""""""""""""""""

The central moment definition is an extension of moment Eq. :eq:`Def_Continuous_Moments` with macroscopic velocity components :math:`u_x` and :math:`u_y`:

.. math::
   :label: Def_Continuous_Central_Moment

   K_{\alpha\beta}=\iint(c_{x}-u_{x})^{\alpha}(c_{y}-u_{y})^{\beta}f(\boldsymbol{x},t,\boldsymbol{c})dc_{x}dc_{y}

and its discrete version writes:

.. math::
   :label:

   \kappa_{\alpha\beta}=\underset{i}{\sum}(c_{ix}-u_x)^{\alpha}(c_{iy}-u_y)^{\beta}f_{i}

The central moment collision operator adds a new matrix of transformation :math:`\mathbb{N}` which contains the supplementary shift with velocity components :math:`u_x` and :math:`u_y`. The matrix :math:`\mathbb{N}` is defined below.

Collision in space of central moments
"""""""""""""""""""""""""""""""""""""

**Collision stage**

The collision stage is performed in the space of central moments which writes:

.. math::
   :label:

   \boldsymbol{\kappa}^{\star}=\boldsymbol{\kappa}-\mathbb{S}\left(\boldsymbol{\kappa}-\boldsymbol{\kappa}^{eq}\right)+\left(\mathbb{I}-\frac{1}{2}\mathbb{S}\right)\tilde{\boldsymbol{F}}

The central moment :math:`\boldsymbol{\kappa}` is obtained from distribution function :math:`\boldsymbol{f}` by applying successive matrix transformations:

.. math::
   :label:

   \begin{eqnarray}
      \boldsymbol{\kappa} & = & \mathbb{M}_{p}\mathbb{N}\mathbb{M}\boldsymbol{f}\\
      & = & \left[\kappa_{00},\kappa_{01},\kappa_{10},\kappa_{20}+\kappa_{02},\kappa_{20}-\kappa_{02},\kappa_{11},\kappa_{21},\kappa_{12},\kappa_{22}\right]^{T}
   \end{eqnarray}

where the matrices :math:`\mathbb{M}` and :math:`\mathbb{M}_p` are defined by

.. math::
   :label: Def_Matrix_M

   \mathbb{M}=\left[\begin{array}{ccccccccc}
      1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1\\
      0 & 1 & 0 & -1 & 0 & 1 & -1 & -1 & 1\\
      0 & 0 & 1 & 0 & -1 & 1 & 1 & -1 & -1\\
      0 & 1 & 0 & 1 & 0 & 1 & 1 & 1 & 1\\
      0 & 0 & 1 & 0 & 1 & 1 & 1 & 1 & 1\\
      0 & 0 & 0 & 0 & 0 & 1 & -1 & 1 & -1\\
      0 & 0 & 0 & 0 & 0 & 1 & 1 & -1 & -1\\
      0 & 0 & 0 & 0 & 0 & 1 & -1 & -1 & 1\\
      0 & 0 & 0 & 0 & 0 & 1 & 1 & 1 & 1
   \end{array}\right],
   \qquad
   \mathbb{M}_{p}=\left[\begin{array}{ccccccccc}
      1 & {\color{gray}0} & {\color{gray}0} & {\color{gray}0} & {\color{gray}0} & {\color{gray}0} & {\color{gray}0} & {\color{gray}0} & {\color{gray}0}\\
      {\color{gray}0} & 1 & {\color{gray}0} & {\color{gray}0} & {\color{gray}0} & {\color{gray}0} & {\color{gray}0} & {\color{gray}0} & {\color{gray}0}\\
      {\color{gray}0} & {\color{gray}0} & 1 & {\color{gray}0} & {\color{gray}0} & {\color{gray}0} & {\color{gray}0} & {\color{gray}0} & {\color{gray}0}\\
      {\color{gray}0} & {\color{gray}0} & {\color{gray}0} & 1 & 1 & {\color{gray}0} & {\color{gray}0} & {\color{gray}0} & {\color{gray}0}\\
      {\color{gray}0} & {\color{gray}0} & {\color{gray}0} & 1 & -1 & {\color{gray}0} & {\color{gray}0} & {\color{gray}0} & {\color{gray}0}\\
      {\color{gray}0} & {\color{gray}0} & {\color{gray}0} & {\color{gray}0} & {\color{gray}0} & 1 & {\color{gray}0} & {\color{gray}0} & {\color{gray}0}\\
      {\color{gray}0} & {\color{gray}0} & {\color{gray}0} & {\color{gray}0} & {\color{gray}0} & {\color{gray}0} & 1 & {\color{gray}0} & {\color{gray}0}\\
      {\color{gray}0} & {\color{gray}0} & {\color{gray}0} & {\color{gray}0} & {\color{gray}0} & {\color{gray}0} & {\color{gray}0} & 1 & {\color{gray}0}\\
      {\color{gray}0} & {\color{gray}0} & {\color{gray}0} & {\color{gray}0} & {\color{gray}0} & {\color{gray}0} & {\color{gray}0} & {\color{gray}0} & 1
   \end{array}\right]


The matrix :math:`\mathbb{N}:=\mathbb{N}(u_x,u_y)` depends on components of velocity :math:`u_x` and :math:`u_y`:

.. math::
   :label: Def_Matrix_N

   \mathbb{N}=\left[\begin{array}{ccccccccc}
      1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\
      -u_{x} & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\
      -u_{y} & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0\\
      u_{x}^{2} & -2u_{x} & 0 & 1 & 0 & 0 & 0 & 0 & 0\\
      u_{y}^{2} & 0 & -2u_{y} & 0 & 1 & 0 & 0 & 0 & 0\\
      u_{x}u_{y} & -u_{y} & -u_{x} & 0 & 0 & 1 & 0 & 0 & 0\\
      -u_{x}^{2}u_{y} & 2u_{x}u_{y} & u_{x}^{2} & -u_{y} & 0 & -2u_{x} & 1 & 0 & 0\\
      -u_{y}^{2}u_{x} & u_{y}^{2} & 2u_{x}u_{y} & 0 & -u_{x} & -2u_{y} & 0 & 1 & 0\\
      u_{x}^{2}u_{y}^{2} & -2u_{x}u_{y}^{2} & -2u_{y}u_{x}^{2} & u_{y}^{2} & u_{x}^{2} & 4u_{x}u_{y} & -2u_{y} & -2u_{x} & 1
   \end{array}\right]

   

.. admonition:: Matrix :math:`\mathbb{T}` in LBM_Saclay
   :class: important

   In LBM_Saclay, matrices :math:`\mathbb{M}`, :math:`\mathbb{N}` and :math:`\mathbb{M}_{p}` are not explicitely defined. Only the result of their product :math:`\mathbb{T}=\mathbb{M}_{p}\mathbb{N}\mathbb{M}` is written in ``Collision_operators.h``. All matrices are written inside a python script ``CMLBM_Sympy.py`` which performs the product  and generates the C++ code. The output :math:`\mathbb{T}` is "copy-paste" in function ``Matrix get_T(real_t u, real_t v)`` of ``struct CMCollider``.

   .. code-block:: ruby

      KOKKOS_INLINE_FUNCTION
         Matrix get_T(real_t u, real_t v) const { 
	      if constexpr(npop==NPOP_D2Q9){
            ...
         }

**Collision matrix** :math:`\mathbb{S}`

The collision matrix :math:`\mathbb{S}` is diagonal and contains the relaxation rates:

.. math::
   :label:

   \mathbb{S}=diag\left(s_{0},s_{1},s_{1},s_{b},s_{\nu},s_{\nu},s_{3},s_{3},s_{4}\right)

The collision frequencies :math:`s_{0}` and :math:`s_{1}` are fixed equal to 1 to ensure conservation of corresponding moments. The following two frequencies :math:`s_{b}` and :math:`s_{\nu}` are related to bulk and kinematic viscosities by:

.. math::
   :label:

   \begin{eqnarray}
      s_{\nu}=&\frac{1}{\frac{1}{2}+\frac{\nu}{c_{s}^{2}\delta t}}\qquad\qquad&s_{b}=&\frac{1}{\frac{1}{2}+\frac{\zeta}{c_{s}^{2}\delta t}}
   \end{eqnarray}

Finally :math:`s_{3}` and :math:`s_{4}` are tunable relaxation frequencies. Let us mention that here, the matrix :math:`\mathbb{S}` is diagonal compared to Eq. (16) of the reference. This is because we used a supplementary matrix :math:`\mathbb{M}_p` defined above to use a diagonal matrix in collision stage.

.. admonition:: Matrix :math:`\mathbb{S}` in LBM_Saclay
   :class: important

   In LBM_Saclay, the diagonal matrix :math:`\mathbb{S}` is written in file ``LBMScheme_NS_AC_Comp.h``

   .. code-block:: ruby

      // Remplissage de la matrice S
      for (int i = 0; i < npop; i++) {
         if (Model.tauMatrixNS[i] != -1.0){
            collider.S[i] = Model.tauMatrixNS[i];
         } else {
            collider.S[i] = tauInv;
         }
      }

Equilibrium and force in central moments framework
""""""""""""""""""""""""""""""""""""""""""""""""""

In central moment framework, the equilibrium central moment :math:`\boldsymbol{\kappa}^{eq}` and the force term are respectively defined by

.. math::
   :label: Def_Equilibrium_Central_Moment

   \boldsymbol{\kappa}^{eq}=\begin{bmatrix}m_{00}\\
   (1-m_{00})u_x\\
   (1-m_{00})u_y\\
   (m_{00}-1)(u_x^{2}+c_{s}^{2})+c_{s}^{2}\\
   (m_{00}-1)(u_y^{2}+c_{s}^{2})+c_{s}^{2}\\
   (m_{00}-1)u_x u_y\\
   (1-m_{00})u_y(c_{s}^{2}+u_x)\\
   (1-m_{00})u_x(c_{s}^{2}+u_y)\\
   (m_{00}-1)(u_x^{2}u_y^{2}+c_{s}^{2}(u_x^{2}+u_y^{2})+c_{s}^{4})+c_{s}^{4}
   \end{bmatrix}\qquad\text{and}\qquad\tilde{\boldsymbol{F}}=\begin{bmatrix}0\\
   F_{x}/\rho\\
   F_{y}/\rho\\
   0\\
   0\\
   0\\
   c_{s}^{2}F_{y}/\rho\\
   c_{s}^{2}F_{x}/\rho\\
   0
   \end{bmatrix}

.. admonition:: :math:`\boldsymbol{\kappa}^{eq}` and :math:`\tilde{\boldsymbol{F}}` in LBM_Saclay
   :class: important

   In LBM_Salcay, all components of equilibrium central moment :math:`\boldsymbol{\kappa}^{eq}` are written in ``LBMScheme_NS_AC_Comp.h``

   .. code-block:: ruby

      // Equilibrium moment
      collider.CMeq[0] = m00;
		collider.CMeq[1] = (1.0-m00)*lbmState[IU];
		collider.CMeq[2] = (1.0-m00)*lbmState[IV];
		collider.CMeq[3] = (m00-1.0)*(SQR(lbmState[IU]) + SQR(lbmState[IV])+2*cs2)+2*cs2;
		collider.CMeq[4] = (m00-1.0)*(SQR(lbmState[IU]) - SQR(lbmState[IV]));
		collider.CMeq[5] = (m00-1.0)*lbmState[IU]*lbmState[IV];
		collider.CMeq[6] = (1.0-m00)*lbmState[IV]*(SQR(lbmState[IU])+cs2);
		collider.CMeq[7] = (1.0-m00)*lbmState[IU]*(SQR(lbmState[IV])+cs2);
		collider.CMeq[8] = (m00-1.0)*(SQR(lbmState[IU]*lbmState[IV])+cs2*(SQR(lbmState[IU])+SQR(lbmState[IV]))+cs2*cs2)+cs2*cs2;

      ...

      // Forcing term
      collider.Ft[0] = 0.0;
		collider.Ft[1] = ForceTot[IX]*rhoinv;
		collider.Ft[2] = ForceTot[IY]*rhoinv;
		collider.Ft[3] = 0.0;
		collider.Ft[4] = 0.0;
		collider.Ft[5] = 0.0;
		collider.Ft[6] = cs2*ForceTot[IY]*rhoinv;
		collider.Ft[7] = cs2*ForceTot[IX]*rhoinv;
		collider.Ft[8] = 0.0;



Streaming
"""""""""

The streaming stage is performed, as usual, in space of distribution functions. After collision, the central moment :math:`\boldsymbol{\kappa}^{\star}` is transformed back by

.. math::
   :label:

   \boldsymbol{f}^{\star}(\boldsymbol{x},t)=\mathbb{M}^{-1}\mathbb{N}^{-1}\mathbb{M}^{-1}_{p}\boldsymbol{\kappa}^{\star}(\boldsymbol{x},t)

where the matrices are defined by

.. math::
   :label:

   \mathbb{M}^{-1}&=&\begin{bmatrix}1 & 0 & 0 & -1 & -1 & 0 & 0 & 0 & 1\\
      0 & \frac{1}{2} & 0 & \frac{1}{2} & 0 & 0 & 0 & -\frac{1}{2} & -\frac{1}{2}\\
      0 & 0 & \frac{1}{2} & 0 & \frac{1}{2} & 0 & -\frac{1}{2} & 0 & -\frac{1}{2}\\
      0 & -\frac{1}{2} & 0 & \frac{1}{2} & 0 & 0 & 0 & \frac{1}{2} & -\frac{1}{2}\\
      0 & 0 & -\frac{1}{2} & 0 & \frac{1}{2} & 0 & \frac{1}{2} & 0 & -\frac{1}{2}\\
      0 & 0 & 0 & 0 & 0 & \frac{1}{4} & \frac{1}{4} & \frac{1}{4} & \frac{1}{4}\\
      0 & 0 & 0 & 0 & 0 & -\frac{1}{4} & \frac{1}{4} & -\frac{1}{4} & \frac{1}{4}\\
      0 & 0 & 0 & 0 & 0 & \frac{1}{4} & -\frac{1}{4} & -\frac{1}{4} & \frac{1}{4}\\
      0 & 0 & 0 & 0 & 0 & -\frac{1}{4} & -\frac{1}{4} & \frac{1}{4} & \frac{1}{4}
   \end{bmatrix}

.. math::
   :label:

   \mathbb{M}_{p}^{-1}&=&diag\left(1,1,1,\begin{bmatrix}\frac{1}{2} & \frac{1}{2}\\
      \frac{1}{2} & -\frac{1}{2}
   \end{bmatrix},1,1,1,1\right)


.. math::
   :label:

   \mathbb{N}^{-1}&=&\begin{bmatrix}1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\
      u & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\
      v & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0\\
      u^{2} & 2u & 0 & 1 & 0 & 0 & 0 & 0 & 0\\
      v^{2} & 0 & 2v & 0 & 1 & 0 & 0 & 0 & 0\\
      uv & v & u & 0 & 0 & 1 & 0 & 0 & 0\\
      u^{2}v & 2uv & u^{2} & v & 0 & 2u & 1 & 0 & 0\\
      v^{2}u & v^{2} & 2uv & 0 & u & 2v & 0 & 1 & 0\\
      u^{2}v^{2} & 2uv^{2} & 2vu^{2} & v^{2} & u^{2} & 4uv & 2v & 2u & 1
   \end{bmatrix}


and the standard streaming stage can be applied:

.. math::
   :label:

   \boldsymbol{f}(\boldsymbol{x}+\boldsymbol{c}_{i}\delta t,t+\delta t)=\boldsymbol{f}^{\star}(\boldsymbol{x},t)

.. admonition:: Matrix :math:`\mathbb{T}^{-1}` in LBM_Saclay
   :class: important

   Once again, in LBM_Saclay, matrices :math:`\mathbb{M}^{-1}`, :math:`\mathbb{N}^{-1}` and :math:`\mathbb{M}_{p}^{-1}` are not explicitely defined. Only the result of their product :math:`\mathbb{T}^{-1}=\mathbb{M}^{-1}\mathbb{N}^{-1}\mathbb{M}^{-1}_{p}` is written in ``Collision_operators.h``. All inverse matrices are written inside the same python script ``CMLBM_Sympy.py`` which performs the product and generates the C++ code. The output :math:`\mathbb{T}^{-1}` is "copy-paste" in function ``Matrix get_Tinv(real_t u, real_t v)`` of ``struct CMCollider``.

   .. code-block:: ruby

      KOKKOS_INLINE_FUNCTION
         Matrix get_Tinv(real_t u, real_t v) const { 
	      if constexpr(npop==NPOP_D2Q9){
            ...
         }



Bibliography
------------
   
.. [1] Krüger T., H. Kusumaatmaja, A. Kuzmin, O. Shardt, G. Silva. E.M. Viggen, The Lattice Boltzmann Method -- Principles and Practice. Spinger, 2017. See :file:`BIBLIO/Kruger_etal_Book_LBM_2017.pdf`


.. [2] Gruszczyński G., T. Mitchell, C. Leonardi, Ł. Łaniewski-Wołłk, T. Barber, A cascaded phase-field lattice Boltzmann model for the simulation of incompressible, immiscible fluids with high density contrast. Computers & Mathematics with Applications, Volume 79, Issue 4, 15 February 2020, pages 1049-1071.  https://doi.org/10.1016/j.camwa.2019.08.018

.. sectionauthor:: Alain Cartalade
   