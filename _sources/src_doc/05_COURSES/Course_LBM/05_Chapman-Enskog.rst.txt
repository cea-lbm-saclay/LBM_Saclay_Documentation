.. _Chapman-Enskog-Expansions:

Chapman-Enskog expansion for Navier-Stokes equations
====================================================

We detail here the algebraic calculations of Chapman-Enskog expansion of Lattice Boltzmann Equation for simulating Navier-Stokes (NS) equations. Here, the expansions are inspired from [1]_ (pp 332--336). An introduction of that method can be found in [2]_ (page 106). An alternative method, but equivalent to C-E expansions, is presented in [3]_. Here we assume that the equilibrium distribution function and the lattice are known to focus on derivation and approximation. The intermediate calculations of Chapman-Enskog expansion are rarely detailed in publications except in appendices in few of them which improve the numerical methods. Here we present the classical procedure without force term in NS.

Starting point
--------------

The LBM aims to simulate the discrete Boltzmann equation:

.. math::
   :label: eq:LBE-BGK
   
   f_{i}(\mathbf{x}+\mathbf{e}_{i}\Delta t,\,t+\Delta t)=f_{i}(\mathbf{x},\,t)-\frac{1}{\lambda}\left[f_{i}(\mathbf{x},\,t)-f_{i}^{(0)}(\mathbf{x},\,t)\right]

where :math:`\mathbf{x}=(x,y,z)^{T}` is the position, :math:`\Delta x` is the spatial discretization, :math:`\Delta t` is the time-step and :math:`\lambda` is a relaxation coefficient of distribution function
:math:`f_{i}(\mathbf{x},\,t)` toward an equilibrium function
:math:`f_{i}^{(0)}(\mathbf{x},\,t)`. Those functions depend on the lattice speeds :math:`\mathbf{e}_{i}` with :math:`i=1,...,N`. The equilibrium distribution function is defined by:

.. math::
   :label: eq:Feq
   
   f_{i}^{(0)}(\mathbf{x},\,t)=\rho(\mathbf{x},\,t)w_{i}\left[1+3\frac{(\mathbf{e}_{i}\cdot\mathbf{u}(\mathbf{x},\,t))}{c^{2}}+\frac{9}{2}\frac{(\mathbf{e}_{i}\cdot\mathbf{u}(\mathbf{x},\,t))^{2}}{c^{4}}-\frac{3}{2}\frac{\mathbf{u}^{2}(\mathbf{x},\,t)}{c^{2}}\right]

where :math:`\rho(\mathbf{x},\,t)` is the density,
:math:`\mathbf{u}=(u_{x},\,u_{y},\,u_{z})^{T}` is the fluid velocity,
:math:`c=\frac{\Delta x}{\Delta t}` is the lattice speed and 
:math:`w_{i}` are weights depending on the lattice.

In the remainder of this page, in order to alleviate the notations, the dependences with :math:`\mathbf{x}` and :math:`t` will be canceled in distribution functions  :math:`f_{i}` et :math:`f_{i}^{(0)}` and macroscopic variables :math:`\rho` et :math:`\mathbf{u}`. We also choose the popular lattice D2Q9 defined by ( for :math:`i=0,...,8`):

.. math::
   :label: eq:DirE0

   \mathbf{e}_{0}=\left(\begin{array}{c}
   0\\
   0
   \end{array}\right)

.. math::
   :label: eq:DirE1-E4

   \mathbf{e}_{1}=\left(\begin{array}{c}
   1\\
   0
   \end{array}\right)c,\,\mathbf{e}_{2}=\left(\begin{array}{c}
   0\\
   1
   \end{array}\right)c,\,\mathbf{e}_{3}=\left(\begin{array}{c}
   -1\\
   0
   \end{array}\right)c,\,\mathbf{e}_{4}=\left(\begin{array}{c}
   0\\
   -1
   \end{array}\right)c

.. math::
   :label: eq:DirE5-E8

   \mathbf{e}_{5}=\left(\begin{array}{c}
   1\\
   1
   \end{array}\right)c,\,\mathbf{e}_{6}=\left(\begin{array}{c}
   -1\\
   1
   \end{array}\right)c,\,\mathbf{e}_{7}=\left(\begin{array}{c}
   -1\\
   -1
   \end{array}\right)c,\,\mathbf{e}_{8}=\left(\begin{array}{c}
   1\\
   -1
   \end{array}\right)c

The weights :math:`w_{i}` are:

.. math::
   :label: eq:PoidsD2Q9

   w_{0}=\frac{4}{9},\qquad w_{1,\,...,\,4}=\frac{1}{9},\qquad w_{5,\,...,\,8}=\frac{1}{36}

Objectives
----------

The purpose of this section is to demonstrate with the Chapman-Enskog expansion that Eq.  :eq:`eq:LBE-BGK` with equilibrium  :eq:`eq:Feq` and lattice D2Q9 (relations :eq:`eq:DirE0` -- :eq:`eq:DirE5-E8` and
:eq:`eq:PoidsD2Q9`) simulate the low-Mach Navier-Stokes equations:

.. math::
   :label: eq:Conversation-Masse

   \partial_{t}\rho+\partial_{\alpha}(\rho u_{\alpha})=0

.. math::
   :label: eq:Conservation-Qmvt
   
   \partial_{t}(\rho u_{\alpha})+\partial_{\beta}(\rho u_{\alpha}u_{\beta})=-\partial_{\alpha}p+\partial_{\beta}\left[\nu\rho(\partial_{\beta}u_{\alpha}+\partial_{\alpha}u_{\beta})\right]+\mathcal{O}(\rho u^{3})

Eq. :eq:`eq:Conversation-Masse` is the mass balance equation and :eq:`eq:Conservation-Qmvt` and the impulsion balance equation. In those equations, the greek indices are :math:`\alpha=x,y` and
:math:`\beta=x,y` (2D) respectively. The Einstein's convention of summation aver repeated indices is used (for instance :math:`\partial_{\alpha}u_{\alpha}=\partial_{x}u_{x}+\partial_{y}u_{y})`.
The symbol :math:`\partial_{\alpha}` is a notation to express the partial derivative
:math:`\frac{\partial}{\partial\alpha}`. For example
:math:`\partial_{x}\equiv\frac{\partial}{\partial x}`,
:math:`\partial_{y}\equiv\frac{\partial}{\partial y}` and
:math:`\partial_{t}\equiv\frac{\partial}{\partial t}`. In Eq.
:eq:`eq:Conservation-Qmvt` :math:`p` is the (thermodynamic)
pressure, :math:`\nu` is the kinematic viscosity.


Conservative quantities and moments of equilibrium distribution functions
-------------------------------------------------------------------------

The macroscopic quantities which have to be conserved are the density and the impulsion:

.. math::
   :label: eq:Def_F

   \begin{cases}
   \sum_{i}f_{i} & =\rho\\
   \sum_{i}f_{i}\mathbf{e}_{i} & =\rho\mathbf{u}
   \end{cases}

The conservation of those quantities during a collision implies:

.. math::
   :label: eq:DefF0

   \begin{cases}
   \sum_{i}f_{i}^{(0)} & =\rho\\
   \sum_{i}f_{i}^{(0)}\mathbf{e}_{i} & =\rho\mathbf{u}
   \end{cases}

Without loss of generality, we set :math:`\Delta x=\Delta t=1` (lattice units) in order to simplify the notations. In general case, :math:`\Delta x` and :math:`\Delta t` can take values different of unity. We get in Eq. :eq:`eq:Feq` :math:`c=1`. We also set:

.. math::
   :label: eq:VitesseSon

   c_{s}^{2}=\frac{1}{3}

With greek indices, the equilibrium distribution function writes:

.. math::
   :label: eq:Feq_grecs

   f_{i}^{(0)}=\rho w_{i}\left[1+3e_{i\gamma}u_{\gamma}+\frac{9}{2}e_{i\gamma}e_{i\theta}u_{\gamma}u_{\theta}-\frac{3}{2}u_{\gamma}u_{\theta}\delta_{\gamma\theta}\right]

On a D2Q9 lattice, we can show that the moments of order  0, 1, 2 et 3 of :math:`f_{i}^{(0)}` are:

.. math::
   :label: eq:M0_f0

   \sum_{i}f_{i}^{(0)}=\rho

.. math::
   :label: eq:M1_f0

   \sum_{i}f_{i}^{(0)}e_{i\alpha}=\rho u_{\alpha}

.. math::
   :label: eq:M2_f0

   \sum_{i}f_{i}^{(0)}e_{i\alpha}e_{i\beta}=c_{s}^{2}\rho\delta_{\alpha\beta}+\rho u_{\alpha}u_{\beta}

.. math::
   :label: eq:M3_f0

   \sum_{i}f_{i}^{(0)}e_{i\alpha}e_{i\beta}e_{i\gamma}=c_{s}^{2}\rho(u_{\alpha}\delta_{\beta\gamma}+u_{\beta}\delta_{\alpha\gamma}+u_{\gamma}\delta_{\alpha\beta})

Those results will be used in calculations of following section.

**Remark**

When we seek to simulate a specific macroscopic PDE, we need to establish the equilibrium distribution function :math:`f_{i}^{(0)}` and the number of moving directions, such as the moments of order zero and one :math:`f_{i}^{(0)}` are equal to conserved macroscopic quantities.

Chapman-Enskog expansion
------------------------

First part: Taylor's expansion and scale separation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The expansions presented in this first part are classical and can be found in references cited above. We can refer to them for physical interpretation of small parameter :math:`\varepsilon` in kinetic theory of gases (Knudsen numner).

By setting :math:`\Delta x=\Delta t=1` and using the greek indices, the LBE writes:

.. math::
   :label: eq:LBE-BGK-Unite

   f_{i}(x+e_{i\beta},\,t+1)=f_{i}(x,\,t)-\frac{1}{\lambda}\left[f_{i}(x,\,t)-f_{i}^{(0)}(x,\,t)\right]

The Taylor's expansion of left-hand side of Eq. :eq:`eq:LBE-BGK-Unite` up to second order in space and times yields:

.. math::
   
   f_{i}(x+e_{i\beta},\,t+1)\simeq f_{i}+e_{i\beta}\partial_{\beta}f_{i}+\frac{1}{2}e_{i\alpha}e_{i\beta}\partial_{\alpha}\partial_{\beta}f_{i}+\partial_{t}f_{i}+\frac{1}{2}\partial_{t}^{2}f_{i}+e_{i\beta}\partial_{\beta}\partial_{t}f_{i}

By replacing in Eq. :eq:`eq:LBE-BGK-Unite`, we obtain:

.. math::
   :label: eq:LBE-Taylor

   e_{i\beta}\partial_{\beta}f_{i}+\frac{1}{2}e_{i\alpha}e_{i\beta}\partial_{\alpha}\partial_{\beta}f_{i}+\partial_{t}f_{i}+\frac{1}{2}\partial_{t}^{2}f_{i}+e_{i\beta}\partial_{\beta}\partial_{t}f_{i}=-\frac{1}{\lambda}\left[f_{i}-f_{i}^{(0)}\right]

We perform a scale separation in space (:math:`x_{1}=\varepsilon x`) and time. For the latter, we distinguish one characteristic time of convection :math:`t_{0}=\varepsilon t` and one characteristic time of diffusion :math:`t_{1}=\varepsilon^{2}t` such that:

.. math::
   :label: eq:Scales

   \begin{cases}
   t & =\frac{1}{\varepsilon}t_{0}+\frac{1}{\varepsilon^{2}}t_{1}\\
   x & =\frac{1}{\varepsilon}x_{1}
   \end{cases}

That leads to following partial derivatives:

.. math::
   :label: eq:ScalesPartial

   \begin{cases}
   \partial_{t} & =\varepsilon\partial_{t_{0}}+\varepsilon^{2}\partial_{t_{1}}\\
   \partial_{\alpha} & =\varepsilon\partial_{\alpha}^{(1)}
   \end{cases}

The distribution function is expanded up to the second order:

.. math::
   :label: eq:F_Expansion

   f_{i}\simeq f_{i}^{(0)}+\varepsilon f_{i}^{(1)}+\varepsilon f_{i}^{(2)}

That expansion and Eqs. :eq:`eq:Def_F` and :eq:`eq:DefF0` imply that:

.. math::
   :label: eq:M0_fneq

   \sum_{i}f_{i}^{(1)}=\sum_{i}f_{i}^{(2)}=0

.. math::
   :label: eq:M1_fneq

   \sum_{i}f_{i}^{(1)}e_{i\alpha}=\sum_{i}f_{i}^{(2)}e_{i\alpha}=0

**Remark**

Eq. :eq:`eq:M1_fneq` est derived because the impulsion is a conservative local quantity for Navier-Stokes equations. For advection-diffusion equation, this is not any more the case, and it will be necessary to calculate the first order moment of :math:`f_{i}^{(1)}`.

Moments des termes en :math:`\varepsilon`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The partial derivative in space and times are replaced in :eq:`eq:LBE-Taylor` by using Eq :eq:`eq:ScalesPartial` and we also use the expansion of distribution function iwth Eq. 
:eq:`eq:F_Expansion`. We gather the terms of order :math:`\varepsilon` and :math:`\varepsilon^{2}`.

The gathering of first order terms in :math:`\varepsilon` yields the following equality:

.. math::
   :label: eq:Eq_Ordre1_Flow

   \partial_{\alpha}^{(1)}e_{i\alpha}f_{i}^{(0)}+\partial_{t_{0}}f_{i}^{(0)}=-\frac{1}{\lambda}f_{i}^{(1)}

With preliminary results Eqs. :eq:`eq:M0_f0` and :eq:`eq:M1_f0`, the moment of zeroth-order (sum over
:math:`i`) of that equation is:

.. math::
   :label: eq:M0_Eq-Ordre1_Flow

   \partial_{t_{0}}\rho+\partial_{\alpha}^{(1)}(\rho u_{\alpha})=0

Similarily, by using Eqs. :eq:`eq:M1_f0` and :eq:`eq:M2_f0`, the moment of first order (multiplication of Eq. 
:eq:`eq:Eq_Ordre1_Flow` by :math:`e_{i\beta}` and sum over :math:`i`) leads to:

.. math::
   :label: eq:M1_Eq-Ordre1_Flow

   \partial_{t_{0}}(\rho u_{\alpha})+\partial_{\beta}^{(1)}(c_{s}^{2}\rho\delta_{\alpha\beta}+\rho u_{\alpha}u_{\beta})=0

Those two moments of order 0 and 1 of terms in :math:`\varepsilon`
(Eqs. :eq:`eq:M0_Eq-Ordre1_Flow` and :eq:`eq:M1_Eq-Ordre1_Flow`) will be used for calculation of the 2nd order moment of :math:`f_{i}^{(1)}` in the second part of this expansion.

Moments of terms of order :math:`\varepsilon^{2}`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gathering the :math:`\varepsilon^{2}` terms leads to the relation:

.. math::
   :label: eq:TermesOrdre2_Flow

   e_{i\beta}\partial_{\beta}^{(1)}f_{i}^{(1)}+\frac{1}{2}e_{i\alpha}e_{i\beta}\partial_{\alpha}^{(1)}\partial_{\beta}^{(1)}f_{i}^{(0)}+\partial_{t_{0}}f_{i}^{(1)}+\partial_{t_{1}}f_{i}^{(0)}+\frac{1}{2}\partial_{t_{0}}^{2}f_{i}^{(0)}+e_{i\beta}\partial_{\beta}^{(1)}\partial_{t_{0}}f_{i}^{(0)}=-\frac{1}{\lambda}f_{i}^{(2)}

Applying separately :math:`\frac{1}{2}e_{i\beta}\partial_{\beta}` and :math:`\frac{1}{2}\partial_{t_{0}}` on Eq. :eq:`eq:Eq_Ordre1_Flow` and summing those two results, that Eq. :eq:`eq:TermesOrdre2_Flow` se simplifies into:

.. math::
   
   \partial_{t_{1}}f_{i}^{(0)}+\left(1-\frac{1}{2\lambda}\right)\left[\partial_{\beta}^{(1)}e_{i\beta}f_{i}^{(1)}+\partial_{t_{0}}f_{i}^{(1)}\right]=-\frac{1}{\lambda}f_{i}^{(2)}

With equations :eq:`eq:M0_f0`, :eq:`eq:M0_fneq` and :eq:`eq:M1_fneq`, the moment of order 0 of that equation yiedls:

.. math::
   :label: eq:M0_Eq-Ordre2_Flow

   \partial_{t_{1}}\rho=0

and its first-order moment:

.. math::
   :label: eq:M1_Eq-Ordre2_Flow

   \partial_{t_{1}}(\rho u_{\alpha})+\left(1-\frac{1}{2\lambda}\right)\left[\partial_{\beta}^{(1)}\sum_{i}f_{i}^{(1)}e_{i\alpha}e_{i\beta}\right]=0

Gathering moments
^^^^^^^^^^^^^^^^^

We gather the moments of zeroth- and first-order that have been derived separately for terms in :math:`\varepsilon` and :math:`\varepsilon^{2}`. We carry out :math:`\varepsilon\times`\ Eq
:eq:`eq:M0_Eq-Ordre1_Flow` + :math:`\varepsilon^{2}\times`\ Eq :eq:`eq:M0_Eq-Ordre2_Flow`, the moment of order zero is:

.. math::
   :label: eq:ConservMasse

   \partial_{t}\rho+\partial_{\alpha}(\rho u_{\alpha})=0

which is the first equation of NS system i.e. the mass balance equation. We perform now :math:`\varepsilon\times`\ Eq :eq:`eq:M1_Eq-Ordre1_Flow` + :math:`\varepsilon^{2}\times`\ Eq :eq:`eq:M1_Eq-Ordre2_Flow`, the first-order moment is:

.. math::
   :label: eq:ConservQmvt

   \partial_{t}(\rho u_{\alpha})+\partial_{\beta}(\Pi_{\alpha\beta}^{(0)}+\Pi_{\alpha\beta}^{(1)})=0

where we set:

.. math::
   :label: eq:Pi0

   \Pi_{\alpha\beta}^{(0)}=\sum_{i}f_{i}^{(0)}e_{i\alpha}e_{i\beta}

.. math::
   :label: eq:Pi1

   \Pi_{\alpha\beta}^{(1)}=\left(1-\frac{1}{2\lambda}\right)\varepsilon\sum_{i}f_{i}^{(1)}e_{i\alpha}e_{i\beta}

The notations :math:`\Pi_{\alpha\beta}^{(0)}` and :math:`\Pi_{\alpha\beta}^{(1)}` are the second-order moments of :math:`f_{i}^{(0)}` and :math:`f_{i}^{(1)}` respectively. :math:`\Pi_{\alpha\beta}^{(0)}` is known with definition of EDF and preliminary results :eq:`eq:M2_f0`. We have to derive now the second-order moment of :math:`f_{i}^{(1)}`. It is the purpose of the following second part.

Second part: viscosity coefficient and impulsion balance
--------------------------------------------------------

**Viscosity**

For :math:`f_{i}^{(1)}` (:math:`\sum_{i}f_{i}^{(1)}e_{i\alpha}e_{i\beta}`), we use the preliminary results :eq:`eq:M2_f0` and :eq:`eq:M3_f0` for moments of second- and third-order of EDF :math:`f_{i}^{(0)}`:

.. math::

   \begin{aligned}
   \sum_{i}f_{i}^{(1)}e_{i\alpha}e_{i\beta} & =-\lambda\left[\partial_{\gamma}^{(1)}(\sum_{i}f_{i}^{(0)}e_{i\alpha}e_{i\beta}e_{i\gamma})+\partial_{t_{0}}(\sum_{i}f_{i}^{(0)}e_{i\alpha}e_{i\beta})\right]\\
    & =-\lambda\left[\partial_{\gamma}^{(1)}c_{s}^{2}\rho(u_{\alpha}\delta_{\beta\gamma}+u_{\beta}\delta_{\alpha\gamma}+u_{\gamma}\delta_{\alpha\beta})+\partial_{t_{0}}(c_{s}^{2}\rho\delta_{\alpha\beta}+\rho u_{\alpha}u_{\beta})\right]\\
    & =-\lambda c_{s}^{2}\left[\partial_{\beta}^{(1)}(\rho u_{\alpha})+\partial_{\alpha}^{(1)}(\rho u_{\beta})+\partial_{\gamma}^{(1)}(\rho u_{\gamma})\delta_{\alpha\beta}\right]-\lambda\partial_{t_{0}}(c_{s}^{2}\rho\delta_{\alpha\beta})-\lambda\partial_{t_{0}}(\rho u_{\alpha}u_{\beta})\end{aligned}

For last two terms, the time derivative are transformed into space-derivative by using moments of order zero and one of equation of order :math:`\varepsilon` (Eq. :eq:`eq:M0_Eq-Ordre1_Flow` and :eq:`eq:M1_Eq-Ordre1_Flow` respectively). For the penultimate term we obtain:

.. math:: -\lambda\partial_{t_{0}}(c_{s}^{2}\rho\delta_{\alpha\beta})=+\lambda c_{s}^{2}\partial_{\gamma}^{(1)}(\rho u_{\gamma})\delta_{\alpha\beta}

That term cancels with one of opposite sign contained in the bracket. For last term, we use the following result:

.. math::
   :label: eq:Equivalence

   \partial_{t_{0}}(\rho u_{\alpha}u_{\beta})=-\partial_{\gamma}^{(1)}(\rho u_{\alpha}u_{\beta}u_{\gamma})-c_{s}^{2}(u_{\alpha}\partial_{\beta}^{(1)}\rho+u_{\beta}\partial_{\alpha}^{(1)}\rho)

By expansing the partial derivatives in the bracket, we finally get:

.. math::

   \begin{aligned}
   \sum_{i}f_{i}^{(1)}e_{i\alpha}e_{i\beta} & =-\lambda c_{s}^{2}\left[\partial_{\beta}^{(1)}(\rho u_{\alpha})+\partial_{\alpha}^{(1)}(\rho u_{\beta})\right]+\lambda\partial_{\gamma}^{(1)}(\rho u_{\alpha}u_{\beta}u_{\gamma})+\lambda c_{s}^{2}(u_{\alpha}\partial_{\beta}^{(1)}\rho+u_{\beta}\partial_{\alpha}^{(1)}\rho)\\
    & =-\lambda c_{s}^{2}\left[\rho\partial_{\beta}^{(1)}u_{\alpha}+\rho\partial_{\alpha}^{(1)}u_{\beta}\right]+\lambda\partial_{\gamma}^{(1)}(\rho u_{\alpha}u_{\beta}u_{\gamma})
   \end{aligned}

The term :math:`\Pi_{\alpha\beta}^{(1)}` becomes:

.. math::

   \begin{aligned}
   \Pi_{\alpha\beta}^{(1)} & =\left(1-\frac{1}{2\lambda}\right)\varepsilon\sum_{i}f_{i}^{(1)}e_{i\alpha}e_{i\beta}\\
    & =\left(1-\frac{1}{2\lambda}\right)\varepsilon\left\{ -\lambda c_{s}^{2}\left[\rho\partial_{\beta}^{(1)}u_{\alpha}+\rho\partial_{\alpha}^{(1)}u_{\beta}\right]+\lambda\partial_{\gamma}^{(1)}(\rho u_{\alpha}u_{\beta}u_{\gamma})\right\} \\
    & =c_{s}^{2}\left(\lambda-\frac{1}{2}\right)\left\{ -\left[\rho\partial_{\beta}u_{\alpha}+\rho\partial_{\alpha}u_{\beta}\right]+\frac{1}{c_{s}^{2}}\partial_{\gamma}(\rho u_{\alpha}u_{\beta}u_{\gamma})\right\} \end{aligned}

By setting:

.. math::
   :label: eq:ViscositeCin

   \nu=c_{s}^{2}\left(\lambda-\frac{1}{2}\right)

we obtain:

.. math::
   :label: eq:Res-Pi1

   \Pi_{\alpha\beta}^{(1)}=-\nu\left[\rho\partial_{\beta}u_{\alpha}+\rho\partial_{\alpha}u_{\beta}\right]+\frac{1}{c_{s}^{2}}\nu\partial_{\gamma}(\rho u_{\alpha}u_{\beta}u_{\gamma})

L’équation :eq:`eq:ViscositeCin` donne la relation
entre le paramètre de relaxation :math:`\lambda` de l’équation cinétique
de Boltzmann et la viscosité cinématique :math:`\nu` du fluide.

Remarque
   : en toute rigueur, lors du développement de Taylor, il est
   nécessaire de considérer :math:`\Delta x\neq1` et
   :math:`\Delta t\neq1` et on voit apparaître le rapport
   :math:`\Delta x^{2}/\Delta t` en facteur devant le terme entre
   parenthèses :

.. math:: \nu=c_{s}^{2}\left(\lambda-\frac{1}{2}\right)\frac{\Delta x^{2}}{\Delta t}

**Impulsion balance equation**

En remplaçant :eq:`eq:M2_f0` et
:eq:`eq:Res-Pi1` dans
:eq:`eq:ConservQmvt`, on obtient :

.. math:: \partial_{t}(\rho u_{\alpha})+\partial_{\beta}\left[c_{s}^{2}\rho\delta_{\alpha\beta}+\rho u_{\alpha}u_{\beta}-\nu(\rho\partial_{\beta}u_{\alpha}+\rho\partial_{\alpha}u_{\beta})\right]+\frac{1}{c_{s}^{2}}\partial_{\beta}\nu\partial_{\gamma}(\rho u_{\alpha}u_{\beta}u_{\gamma})=0

.. math:: \partial_{t}(\rho u_{\alpha})+\partial_{\beta}(\rho u_{\alpha}u_{\beta})=-\partial_{\alpha}(c_{s}^{2}\rho)+\partial_{\beta}\left[\nu(\rho\partial_{\beta}u_{\alpha}+\rho\partial_{\alpha}u_{\beta})\right]+\mathcal{O}(\rho u^{3})

où on a considéré
:math:`-\frac{1}{c_{s}^{2}}\partial_{\beta}\nu\partial_{\gamma}(\rho u_{\alpha}u_{\beta}u_{\gamma})=\mathcal{O}(\rho u^{3})`.
Finalement, en posant :math:`p=c_{s}^{2}\rho`, on obtient l’équation de
conservation de la quantité de mouvement :

.. math:: \partial_{t}(\rho u_{\alpha})+\partial_{\beta}(\rho u_{\alpha}u_{\beta})=-\partial_{\alpha}p+\partial_{\beta}\left[\nu\rho(\partial_{\beta}u_{\alpha}+\partial_{\alpha}u_{\beta})\right]+\mathcal{O}(\rho u^{3})

qui correspond à la seconde équation recherchée du système d’équations
de Navier-Stokes.

Récapitulatif
-------------

En effectuant le développement de Chapman-Enskog (ordre deux en espace,
ordre deux en temps et en :math:`\varepsilon^{2}`) et en calculant les
moments d’ordre 0 et 1 des équations en :math:`\varepsilon` et
:math:`\varepsilon^{2}`, on a montré que les équations
:eq:`eq:LBE-BGK` et :eq:`eq:Feq` permettent
de résoudre sur un réseau D2Q9 les équations de Navier-Stokes :

.. math::
   :label: eq:Res-Eq1_ChapmanEnskog

   \partial_{t}\rho+\partial_{\alpha}(\rho u_{\alpha})=0

.. math::
   :label: eq:Res-Eq2_ChapmanEnskog

   \partial_{t}(\rho u_{\alpha})+\partial_{\beta}(\rho u_{\alpha}u_{\beta})=-\partial_{\alpha}p+\partial_{\beta}\left[\nu\rho(\partial_{\beta}u_{\alpha}+\partial_{\alpha}u_{\beta})\right]+\mathcal{O}(u^{3})

avec la pression reliée à la densité par la relation
:math:`p=c_{s}^{2}\rho` et une viscosité cinématique :math:`\nu` donnée
par :

.. math::
   :label: eq:Viscosite

   \nu=c_{s}^{2}\left(\lambda-\frac{1}{2}\right)\frac{\Delta x^{2}}{\Delta t}

Dans l’équation
:eq:`eq:Res-Eq2_ChapmanEnskog`, le terme
en :math:`\mathcal{O}(u^{3})` est de la forme
:math:`-\frac{1}{c_{s}^{2}}\partial_{\beta}\nu\partial_{\gamma}(\rho u_{\alpha}u_{\beta}u_{\gamma})`
qui est négligeable pour les faibles nombres de Mach. Lorsque ce dernier
devient important, il est nécessaire de corriger la fonction de
distribution à l’équilibre pour éliminer/diminuer l’influence de ce
terme. On pourra se référer à [4]_ qui analyse
plusieurs :math:`f_{i}^{(0)}` ou termes forces en ce sens.

Démonstration de l’égalité :eq:`eq:Equivalence`
-----------------------------------------------

On démontre dans cette annexe la relation :

.. math:: \partial_{t_{0}}(\rho u_{\alpha}u_{\beta})=-\partial_{\gamma}^{(1)}(\rho u_{\alpha}u_{\beta}u_{\gamma})-c_{s}^{2}(u_{\alpha}\partial_{\beta}^{(1)}\rho+u_{\beta}\partial_{\alpha}^{(1)}\rho)

Le développement du membre de gauche donne :

.. math:: \partial_{t_{0}}(\rho u_{\alpha}u_{\beta})=u_{\alpha}u_{\beta}\partial_{t_{0}}\rho+\rho u_{\alpha}\partial_{t_{0}}u_{\beta}+\rho u_{\beta}\partial_{t_{0}}u_{\alpha}

En remarquant que
:math:`\rho u_{\alpha}\partial_{t_{0}}u_{\beta}=u_{\alpha}\partial_{t_{0}}(\rho u_{\beta})-u_{\alpha}u_{\beta}\partial_{t_{0}}\rho`
et que
:math:`\rho u_{\beta}\partial_{t_{0}}u_{\alpha}=u_{\beta}\partial_{t_{0}}(\rho u_{\alpha})-u_{\alpha}u_{\beta}\partial_{t_{0}}\rho`,
on obtient :

.. math:: \partial_{t_{0}}(\rho u_{\alpha}u_{\beta})=-u_{\alpha}u_{\beta}\partial_{t_{0}}\rho+u_{\alpha}\partial_{t_{0}}(\rho u_{\beta})+u_{\beta}\partial_{t_{0}}(\rho u_{\alpha})

Les dérivées partielles en temps sont converties en dérivées partielles
en espace à l’aide des équations
:eq:`eq:M0_Eq-Ordre1_Flow` pour le premier
terme et :eq:`eq:M1_Eq-Ordre1_Flow` pour les
deux derniers :

.. math::

   \begin{aligned}
   \partial_{t_{0}}(\rho u_{\alpha}u_{\beta}) & =u_{\alpha}u_{\beta}\partial_{\gamma}^{(1)}(\rho u_{\gamma})-u_{\alpha}\left[\partial_{\gamma}^{(1)}(c_{s}^{2}\rho\delta_{\beta\gamma})+\partial_{\gamma}^{(1)}(\rho u_{\beta}u_{\gamma})\right]-u_{\beta}\left[\partial_{\gamma}^{(1)}(c_{s}^{2}\rho\delta_{\alpha\gamma})+\partial_{\gamma}^{(1)}(\rho u_{\alpha}u_{\gamma})\right]\nonumber \\
    & =u_{\alpha}u_{\beta}\partial_{\gamma}^{(1)}(\rho u_{\gamma})-u_{\alpha}\left[\partial_{\beta}^{(1)}(c_{s}^{2}\rho)+\partial_{\gamma}^{(1)}(\rho u_{\beta}u_{\gamma})\right]-u_{\beta}\left[\partial_{\alpha}^{(1)}(c_{s}^{2}\rho)+\partial_{\gamma}^{(1)}(\rho u_{\alpha}u_{\gamma})\right]\nonumber \\
    & =-\left[u_{\alpha}\partial_{\gamma}^{(1)}(\rho u_{\beta}u_{\gamma})+u_{\beta}\partial_{\gamma}^{(1)}(\rho u_{\alpha}u_{\gamma})-u_{\alpha}u_{\beta}\partial_{\gamma}^{(1)}(\rho u_{\gamma})\right]-c_{s}^{2}\left[u_{\alpha}\partial_{\beta}^{(1)}\rho+u_{\beta}\partial_{\alpha}^{(1)}\rho\right]\label{eq:Intermediaire}\end{aligned}

Les trois premiers termes contenus dans le premier crochet peuvent être
exprimés sous la forme condensée
:math:`\partial_{\gamma}^{(1)}(\rho u_{\alpha}u_{\beta}u_{\gamma})`. Il
existe plusieurs façons de la démontrer, on présente dans cette annexe
une façon de procéder.

Un premier développement donne
:math:`\partial_{\gamma}^{(1)}(\rho u_{\alpha}u_{\beta}u_{\gamma})=u_{\alpha}\partial_{\gamma}^{(1)}(\rho u_{\beta}u_{\gamma})+\rho u_{\beta}u_{\gamma}(\partial_{\gamma}^{(1)}u_{\alpha})`
c’est-à-dire :

.. math::
   :label: eq:Cond1

   u_{\alpha}\partial_{\gamma}^{(1)}(\rho u_{\beta}u_{\gamma})=\partial_{\gamma}^{(1)}(\rho u_{\alpha}u_{\beta}u_{\gamma})-\rho u_{\beta}u_{\gamma}(\partial_{\gamma}^{(1)}u_{\alpha})

Un second développement conduit à
:math:`\partial_{\gamma}^{(1)}(\rho u_{\alpha}u_{\beta}u_{\gamma})=u_{\beta}\partial_{\gamma}^{(1)}(\rho u_{\alpha}u_{\gamma})+\rho u_{\alpha}u_{\gamma}(\partial_{\gamma}^{(1)}u_{\beta})`
c’est-à-dire :

.. math::
   :label: eq:Cond2
   
   u_{\beta}\partial_{\gamma}^{(1)}(\rho u_{\alpha}u_{\gamma})=\partial_{\gamma}^{(1)}(\rho u_{\alpha}u_{\beta}u_{\gamma})-\rho u_{\alpha}u_{\gamma}(\partial_{\gamma}^{(1)}u_{\beta})

Enfin, un dernier développement donne
:math:`\partial_{\gamma}^{(1)}(\rho u_{\alpha}u_{\beta}u_{\gamma})=u_{\alpha}u_{\beta}\partial_{\gamma}^{(1)}(\rho u_{\gamma})+\rho u_{\gamma}\partial_{\gamma}^{(1)}(u_{\alpha}u_{\beta})`
c’est-à-dire :

.. math::
   :label: eq:Cond3

   -u_{\alpha}u_{\beta}\partial_{\gamma}^{(1)}(\rho u_{\gamma})=-\partial_{\gamma}^{(1)}(\rho u_{\alpha}u_{\beta}u_{\gamma})+\rho u_{\gamma}\partial_{\gamma}^{(1)}(u_{\alpha}u_{\beta})

En effectuant la somme :eq:`eq:Cond1`, :eq:`eq:Cond2` et :eq:`eq:Cond3`, on obtient
:

.. math:: u_{\alpha}\partial_{\gamma}^{(1)}(\rho u_{\beta}u_{\gamma})+u_{\beta}\partial_{\gamma}^{(1)}(\rho u_{\alpha}u_{\gamma})-u_{\alpha}u_{\beta}\partial_{\gamma}^{(1)}(\rho u_{\gamma})=\partial_{\gamma}^{(1)}(\rho u_{\alpha}u_{\beta}u_{\gamma})-\rho u_{\beta}u_{\gamma}(\partial_{\gamma}^{(1)}u_{\alpha})-\rho u_{\alpha}u_{\gamma}(\partial_{\gamma}^{(1)}u_{\beta})+\rho u_{\gamma}\partial_{\gamma}^{(1)}(u_{\alpha}u_{\beta})

Dans l’équation ci-dessus, les trois derniers termes du membre de droite
s’annulent entre eux, on a donc bien démontré que :

.. math:: \left[u_{\alpha}\partial_{\gamma}^{(1)}(\rho u_{\beta}u_{\gamma})+u_{\beta}\partial_{\gamma}^{(1)}(\rho u_{\alpha}u_{\gamma})-u_{\alpha}u_{\beta}\partial_{\gamma}^{(1)}(\rho u_{\gamma})\right]=\partial_{\gamma}^{(1)}(\rho u_{\alpha}u_{\beta}u_{\gamma})

Finalement en remplaçant ce résultat dans
(`[eq:Intermediaire] <#eq:Intermediaire>`__), on obtient la relation
recherchée :

.. math:: \partial_{t_{0}}(\rho u_{\alpha}u_{\beta})=-\partial_{\gamma}^{(1)}(\rho u_{\alpha}u_{\beta}u_{\gamma})-c_{s}^{2}\left[u_{\alpha}\partial_{\beta}^{(1)}\rho+u_{\beta}\partial_{\alpha}^{(1)}\rho\right]

Bibliography
------------

.. [1] Chen S., G. Doolen, Lattice boltzmann method for fluid flows, Annual Reviews of Fluid Mechanics 30 (1998), pp. 329–364. https://doi.org/10.1146/annurev.fluid.30.1.329

.. [2] Krüger T., H. Kusumaatmaja, A. Kuzmin, O. Shardt, G. Silva, E. Viggen, The Lattice Boltzmann Method: Principles and Practice, Graduate Texts in Physics, Springer, 2017.

.. [3] Dubois F., Equivalent partial differential equations of a lattice Boltzmann scheme, Computers & Mathematics with Applications 55 (7) (2008) 1441 – 1449, mesoscopic Methods in Engineering and Science. https://doi.org/10.1016/j.camwa.2007.08.003

.. [4] Huang H., M. Sukop, X.-Y. Lu, Multiphase Lattice Boltzmann Methods. Theory and Application, Wiley & Sons, 2015.

.. sectionauthor:: Alain Cartalade
