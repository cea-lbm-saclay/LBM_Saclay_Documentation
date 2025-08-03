.. _Feq-Alt:

Equilibrium distribution functions
----------------------------------

The equilibrium distribution function (EqDF) :math:`f_i^{eq}` is one of the most important functions in LBM because it indicates what macroscopic equation the algorithm simulates. The equilibrium distribution function :math:`f_i^{eq}` is involved in the collision operator :math:`\Omega` in the discrete LBE:

.. math::
   :label: LBE_Feq
   
   f_{i}(\boldsymbol{x}+\boldsymbol{c}_{i}\delta t,t+\delta t)=f_{i}(\boldsymbol{x},t)+\Omega_{i}(f_{i},f_{i}^{eq})+\mathcal{F}_i
   
One of the most attractive aspect of LBM, is to use the same evolution Eq. :eq:`LBE_Feq` and simply change the definition of :math:`f_i^{eq}` to simulate either the Navier-Stokes equations or the Conservative Allen-Cahn equation. For low Mach Navier-Stokes (NS) and standard Advection-Diffusion Equation (ADE), the EqDF are presented in :ref:`Overview-LBM`. Here we present those for incompressible two-phase NS and several variations of transport equation such as the Cahn-Hilliard equation and the Conservative Allen-Cahn one.

.. admonition:: Equilibrium distribution functions in LBM_Saclay
   :class: important
   
   The equilibrium distribution functions are problem dependent. They are defined for each kernel in the ``LBMScheme_Kernel_Name.h`` file of folder ``src/kernels``. For example for kernel ``NSAC_Comp``, the equilibrium distribution functions for all PDEs are written in ``LBMScheme_NS_AC_Comp.h`` file.
   
Incompressible Navier-Stokes equations for two-phase flows
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For low Mach Navier-Stokes (NS), the EqDF are presented in :ref:`Overview-LBM`. Here are presented some modification for simulating incompressible single-phase and two-phase flows. First we remind the macroscopic PDEs we want to simulate:

.. math::
   :label: Mass_Balance_Ref
   
   \boldsymbol{\nabla}\cdot\boldsymbol{u}=0
   
.. math::
   :label: Impulsion_Balance_Ref
   
   \varrho(\phi)\left[\frac{\partial\boldsymbol{u}}{\partial t}+\boldsymbol{\nabla}\cdot(\boldsymbol{u}\boldsymbol{u})\right]=-\boldsymbol{\nabla}p_{h}+\boldsymbol{\nabla}\cdot\eta(\boldsymbol{x},t)\left[\boldsymbol{\nabla}\boldsymbol{u}+(\boldsymbol{\nabla}\boldsymbol{u})^{T}\right]
   
where :math:`p_h` is the hydrodynamic pressure, :math:`\boldsymbol{u}` is the fluid velocity , and :math:`\varrho(\phi)` is the interpolation of constant bulk densities: each phase is characterized by constant densities, e.g. :math:`\rho_0` and :math:`\rho_1`. The total density :math:`\varrho(\boldsymbol{x},t)` is a function of position and time with the phase-field:

.. math::
   :label: Total_Density
   
   \varrho(\phi)=\rho_0\phi(\boldsymbol{x},t)+\rho_1(1-\phi(\boldsymbol{x},t))


Standard :math:`f_i^{eq}` for incompressible single-phase
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

For simulating incompressible NS equations for single-phase flows, the EqDF writes:

.. math::
   :label: Feq_Incompr_V0
   
   f_{i}^{eq}(\boldsymbol{x},t)=w_{i}\left[p_{h}+\rho_{0}c_{s}^{2}\left(\frac{\boldsymbol{c}_{i}\cdot\boldsymbol{u}}{c_{s}^{2}}+\frac{(\boldsymbol{c}_{i}\cdot\boldsymbol{u})^{2}}{2c_{s}^{4}}-\frac{\boldsymbol{u}\cdot\boldsymbol{u}}{2c_{s}^{2}}\right)\right]

where the macroscopic physical variables are the hydrodynamic pressure :math:`p_h`, the fluid velocity :math:`\boldsymbol{u}`, and the constant bulk density :math:`\rho_0`. The lattice is defined by its weights :math:`w_i` and its moving directions :math:`\boldsymbol{c}_i` where :math:`i=0,...,N_{pop}`.  :math:`c_s` is the lattice sound speed defined by :math:`c/\sqrt{3}` which depends the the time and space discretization. The lattice speed :math:`c` is defined by :math:`\delta x/\delta t`.

After collision and streaming, the moments are updated with the following relationships. First, the moment of order zero is the hydrodynamic pressure:

.. math::
   :label: M0_V0
   
   p_{h}(\boldsymbol{x},t)=\sum_{i}f_{i}(\boldsymbol{x},t)

Next, the moment of order one is the impulsion:

.. math::
   :label: M1_V0
   
   \rho_{0}\boldsymbol{u}(\boldsymbol{x},t)=\frac{1}{c_{s}^{2}}\sum_{i}f_{i}(\boldsymbol{x},t)\boldsymbol{c}_{i}
   
.. admonition:: Equivalent algorithm of artificial compressibility
   :class: error
   
   We can prove that the Chapman-Enskog expansion of LBE with EqDF :eq:`Feq_Incompr_V0` yields to the equivalent system of equations:
   
   .. math::
      :label: ComprArt_Mass
      
      \frac{\partial{\color{red}p_h}}{\partial t}+{\color{red}\rho_{0}c_{s}^{2}}\boldsymbol{\nabla}\cdot\boldsymbol{u}=0
   
   .. math::
      :label: ComprArt_Impulsion
      
      {\color{red}\rho_{0}\cancel{c_{s}^{2}}}\left[\frac{\partial\boldsymbol{u}}{\partial t}+\boldsymbol{\nabla}\cdot(\boldsymbol{u}\boldsymbol{u})\right]=-\boldsymbol{\nabla}{\color{red}p_h}\cancel{c_{s}^{2}}+\boldsymbol{\nabla}\cdot\left[{\color{red}\rho_{0}\cancel{c_{s}^{2}}}\nu(\boldsymbol{\nabla}\boldsymbol{u}+(\boldsymbol{\nabla}\boldsymbol{u})^{T})\right]+\mathcal{O}(\rho u^{3})

   The mass balance Eq. :eq:`ComprArt_Mass` is one particular method of classical CFD to simulate the incompressible Navier-Stokes equations, called the **articial compressibility algorithm**. In LBM the compressibility coefficient is :math:`\beta=\rho_0c_s^{2}`.
   
:math:`f_i^{eq}` for incompressible two-phase flows
"""""""""""""""""""""""""""""""""""""""""""""""""""

Now we consider two-phase flows by assuming that each phase is incompressible. 
   
From the previous EqDF, two methods are implemented in LBM_Saclay to account for that variation :eq:`Total_Density`. The first method is a direct extension of :eq:`Feq_Incompr_V0`. The second one is a slight modification which introduces the dimensionless pressure :math:`p_h^{\star}`.

**Version 1 for variable density**

That first version is a direct adaptation of Eq. :eq:`Feq_Incompr_V0` where the variable density :math:`\varrho(\phi)` simply replaces the constant density :math:`\rho_0`:

.. math::
   :label: Feq_Incompr_V1
   
   f_{i}^{eq}(\boldsymbol{x},t)=w_{i}\left[p_{h}+\varrho(\phi)c_{s}^{2}\left(\frac{\boldsymbol{c}_{i}\cdot\boldsymbol{u}}{c_{s}^{2}}+\frac{(\boldsymbol{c}_{i}\cdot\boldsymbol{u})^{2}}{2c_{s}^{4}}-\frac{\boldsymbol{u}\cdot\boldsymbol{u}}{2c_{s}^{2}}\right)\right]

Let us notice that the physical dimension of terms inside the brackets is equivalent to a pressure. The hydrodynamic pressure :math:`p_h` and the impulsion are respectively obtained by the moment of order zero:

.. math::
   :label: M0_V1
   
   p_{h}(\boldsymbol{x},t)=\sum_{i}f_{i}(\boldsymbol{x},t)

and its moment of order 1:

.. math::
   :label: M1_V1
   
   \varrho(\phi)\boldsymbol{u}(\boldsymbol{x},t)=\frac{1}{c_{s}^{2}}\sum_{i}f_{i}(\boldsymbol{x},t)\boldsymbol{c}_{i}


.. admonition:: Version 1: equivalent macroscopic PDE
   :class: important
   
   Once the Chapman-Enskog expansion is performed, the macroscopic equations which recovered are with that EqDF are:

   .. math::
      :label: Mass_Balance_V1
   
      \frac{\partial p_{h}}{\partial t}+\boldsymbol{\nabla}\cdot\left[\varrho(\phi)c_{s}^{2}\boldsymbol{u}\right]=0

   for the mass balance equation, and

   .. math::
      :label: Impulsion_Balance_V1
   
      \varrho(\phi)\cancel{c_{s}^{2}}\left[\frac{\partial\boldsymbol{u}}{\partial t}+\boldsymbol{\nabla}\cdot(\boldsymbol{u}\boldsymbol{u})\right]=-\boldsymbol{\nabla}p_{h}\cancel{c_{s}^{2}}+\boldsymbol{\nabla}\cdot\left[\varrho(\phi)\cancel{c_{s}^{2}}\nu(\boldsymbol{\nabla}\boldsymbol{u}+(\boldsymbol{\nabla}\boldsymbol{u})^{T})\right]+\mathcal{O}(\rho u^{3})

   for the impulsion balance, where the kinematic viscosity is given by

   .. math::
      :label: Kinematic_Viscos
   
      \nu=\frac{1}{3}\left(\tau-\frac{1}{2}\right)\frac{\delta x^{2}}{\delta t}
   
By expanding the divergence term, the mass balance Eq. :eq:`Mass_Balance_V1` can be rewritten:

.. math::
   :label: Mass_Balance_V1_Expand_div
   
   \frac{\partial p_{h}}{\partial t}+\varrho(\phi)c_{s}^{2}\boldsymbol{\nabla}\cdot\boldsymbol{u}=-\boldsymbol{u}\cdot\boldsymbol{\nabla}(\varrho(\phi)c_{s}^{2})

.. admonition:: Version 1: source term to add
   :class: error
   
   The mass balance recovered by the Chapman-Ensokg procedure Eq. :eq:`Mass_Balance_V1` slighty differs from the classic artificial mass balance equation because the density is a function of position :math:`\varrho(\phi)`. To correct that, it is needed to add a source term:
   
   .. math::
      :label: Source_Pressure
   
      S_p=\boldsymbol{u}\cdot\boldsymbol{\nabla}[\varrho(\phi)c_s^2]
   
   in the LBE.
   
**Version 2 for variable density**

That version is implemented in the kernel ``NSAC_Comp``. The pressure that is used in the equilibrium distribution function is a dimensionless pressure defined by:

.. math::
   :label: Def_p_Star
   
   p_h^{\star}=\frac{p_{h}}{\varrho(\phi)c_{s}^{2}}

The EqDF writes:

.. math::
   :label: Feq_Incompr_V2
   
   f_{i}^{eq}(\boldsymbol{x},t)=w_{i}\left[p_h^{\star}+\left(\frac{\boldsymbol{c}_{i}\cdot\boldsymbol{u}}{c_{s}^{2}}+\frac{(\boldsymbol{c}_{i}\cdot\boldsymbol{u})^{2}}{2c_{s}^{4}}-\frac{\boldsymbol{u}\cdot\boldsymbol{u}}{2c_{s}^{2}}\right)\right]

and the moments are

.. math::
   :label: M0_V2
   
   p_h^{\star}(\boldsymbol{x},t)=\sum_{i}f_{i}(\boldsymbol{x},t)

.. math::
   :label: M1_V2
   
   \boldsymbol{u}(\boldsymbol{x},t)=\sum_{i}f_{i}(\boldsymbol{x},t)\boldsymbol{c}_{i}

.. admonition:: Version 2: equivalent macroscopic PDE
   :class: important
   
   Once the Chapman-Enskog expansion is performed, the macroscopic equations which recovered are with that EqDF are:

   .. math::
      :label: Mass_Balance_V2
   
      \frac{\partial p^{\star}}{\partial t}+\boldsymbol{\nabla}\cdot\boldsymbol{u}=0
   
   .. math::
      :label: Impulsion_Balance_V2
   
      \frac{\partial\boldsymbol{u}}{\partial t}+\boldsymbol{\nabla}\cdot(\boldsymbol{u}\boldsymbol{u})=-\boldsymbol{\nabla}(p^{\star}c_{s}^{2})+\boldsymbol{\nabla}\cdot\left[\nu(\boldsymbol{\nabla}\boldsymbol{u}+(\boldsymbol{\nabla}\boldsymbol{u})^{T})\right]

In Eq. :eq:`Impulsion_Balance_V2`, the pressure gradient can be expanded:

.. math::
   :label: GradP_Expand
   
   -\frac{1}{\varrho}\boldsymbol{\nabla}p_{h}&=-\boldsymbol{\nabla}(p^{\star}c_{s}^{2})+\frac{1}{\varrho}\boldsymbol{F}_{p}\\{\color{red}\boldsymbol{F}_{p}}&=-\frac{p_{h}}{\varrho}\boldsymbol{\nabla}\varrho

The pressure term must be corrrected with a new force term :math:`\boldsymbol{F}_p` to match the gradient term of Eq. :eq:`Impulsion_Balance_Ref`. In that equation, The viscous term can be expanded:

.. math::
   :label: Viscos_Expand
   
   \frac{1}{\varrho(\phi)}\boldsymbol{\nabla}\cdot\left[\varrho(\phi)\nu(\boldsymbol{\nabla}\boldsymbol{u}+(\boldsymbol{\nabla}\boldsymbol{u})^{T})\right]=\boldsymbol{\nabla}\cdot\left[\nu(\boldsymbol{\nabla}\boldsymbol{u}+(\boldsymbol{\nabla}\boldsymbol{u})^{T})\right]+\nu\left[\boldsymbol{\nabla}\boldsymbol{u}+(\boldsymbol{\nabla}\boldsymbol{u})^{T}\right]\cdot\frac{\boldsymbol{\nabla}\varrho(\phi)}{\varrho(\phi)}

The second term of the right-hand side corresponds to the viscous term of Eq. :eq:`Impulsion_Balance_V2`. A supplementary force :math:`\boldsymbol{F}_v` has to be added to match Eq. :eq:`Impulsion_Balance_Ref`.

.. admonition:: Version 2: forces to add
   :class: error
   
   To match :eq:`Impulsion_Balance_V2` to Eq. :eq:`Impulsion_Balance_Ref`, two force terms must be added in the microscopic forcing term of LBE. The first one is the pressure force pressure force :math:`\boldsymbol{F}_p` defined by
   
   .. math::
      :label: Force_Pressure
   
      \boldsymbol{F}_{p}=-\frac{p_{h}}{\varrho}\boldsymbol{\nabla}\varrho

   The second one is the viscosity force :math:`\boldsymbol{F}_v` defined by

   .. math::
      :label: Force_Viscos

      \boldsymbol{F}_{v}=\nu\left[\boldsymbol{\nabla}\boldsymbol{u}+(\boldsymbol{\nabla}\boldsymbol{u})^{T}\right]\cdot\boldsymbol{\nabla}\varrho(\phi)

.. _EdF-For-Transport-Equation:

Transport equations
^^^^^^^^^^^^^^^^^^^

For standard Advection-Diffusion Equation (ADE), the EqDF are presented in :ref:`Overview-LBM`. We present here the EqDF for several ADE-type equations such as the Conservative Allen-Cahn equation, the Cahn-Hilliard equation and phase-field equation for crystal growth. For those phase-field equations, a new distribution function :math:`g_i` is introduced. The lattice Boltzmann equation for that :math:`g_i` with the BGK collision operator writes:

.. math::
   :label: LBE_ADE_Sterm
   
   g_{i}(\boldsymbol{x}+\boldsymbol{c}_{i}\delta t,t+\delta t)=g_{i}(\boldsymbol{x},t)-\frac{1}{\tau_{g}+0.5}\left[g_{i}(\boldsymbol{x},t)-g_{i}^{eq,\iota}(\boldsymbol{x},t)\right]+\delta t\mathcal{G}_i
   
where :math:`\mathcal{G}_i` is the microscopic source term. In :math:`g_i^{eq,\iota}`, the superscript :math:`\iota` can be :math:`ADE,CH,CAC`. Those options are described below. In the rest of this section, the coefficient :math:`M_{\phi}` involved in the transport equation is related to the collision rate :math:`\tau_g` by:

.. math::
   :label: Mobility
   
   M_{\phi}=\tau_{g}c_{s}^{2}\delta t

where :math:`c_s=c/\sqrt{3}` and :math:`c=\delta x/\delta t`.

:math:`g_i^{eq}` for ADE with source term
"""""""""""""""""""""""""""""""""""""""""

**Target macroscopic equation**

The ADE with a source term writes:

.. math::
   :label: ADE_Sterm
   
   \partial_{t}\underbrace{\phi}_{\mathcal{M}_{0}}+\boldsymbol{\nabla}\cdot(\underbrace{\boldsymbol{u}\phi}_{\boldsymbol{\mathcal{M}}_{1}})=\boldsymbol{\nabla}\cdot\Bigl[M_{\phi}\boldsymbol{\nabla}\cdot(\underbrace{\phi\boldsymbol{I}}_{\boldsymbol{\mathcal{M}}_{2}})\Bigr]+\mathscr{S}_{\phi}

where the notation :math:`\phi` is used here as the conserved quantity (e.g. concentration), :math:`\boldsymbol{u}` is the velocity, the notation :math:`M_{\phi}` represents the diffusion coefficient and :math:`\mathscr{S}_{\phi}` is the macroscopic source term to be defined. Inside the bracket, :math:`\boldsymbol{I}` is the identity tensor of second order. In that equation, the moments are noted:

-  :math:`\mathcal{M}_{0}`: is the moment of order 0 (scalar)
-  :math:`\boldsymbol{\mathcal{M}}_{1}`: is the moment of order 1 (vector)
-  :math:`\boldsymbol{\mathcal{M}}_{2}`: is the moment of order 2 (tensor of rank 2)

**Source term**

The microscopic source term is simply defined by

.. math::
   :label: Source_Term_ADE
   
   \mathcal{G}_i=w_i\mathscr{S}_{\phi}
   
Its moment of order zero is :math:`\mathscr{S}_{\phi}` because :math:`\sum_iw_i=1`.

**Equilibrium with source term**

The EqDF :math:`g_i^{eq,ADE}` must be defined such as :math:`\mathcal{M}_{0}=\phi`, :math:`\boldsymbol{\mathcal{M}}_{1}=\boldsymbol{u}\phi` and :math:`\boldsymbol{\mathcal{M}}_{2}=\phi\boldsymbol{I}`. One can prove that one possible solution is

.. math::
   :label: Geq_ADE_Sterm

   g_{i}^{eq,ADE}(\boldsymbol{x},t)=w_{i}\phi\left[1+\frac{\boldsymbol{u}\cdot\boldsymbol{c}_{i}}{c_{s}^{2}}\right]=w_{i}\underbrace{\phi}_{\mathcal{M}_{0}\text{ and }\boldsymbol{\mathcal{M}}_{2}}+w_{i}\frac{(\overbrace{\boldsymbol{u}\phi}^{\boldsymbol{\mathcal{M}}_{1}})\cdot\boldsymbol{c}_{i}}{c_{s}^{2}}

When using a source term in LBE :eq:`LBE_ADE_Sterm`, a second order of accuracy is obtained provided that the following variable change :math:`\overline{g}_{i}^{eq,ADE}` is used:

.. math::
   :label: Geq_ADE_Change
   
   \overline{g}_{i}^{eq,ADE}(\boldsymbol{x},t)=g_{i}^{eq,ADE}-\frac{\delta t}{2}\mathcal{G}_{i}

**Moment**

After collision and streaming, the new :math:`\phi` function is obtained by the moment of order zero corrected by the source term :math:`\mathcal{G}_{i}\delta t/2`:

.. math::
   :label: M0_ADE_Sterm
   
   \phi=\sum_{i}g_{i}+\frac{\delta t}{2}\mathscr{S}_{\phi}
    

:math:`g_i^{eq}` for Cahn-Hilliard equation
"""""""""""""""""""""""""""""""""""""""""""

**Target macroscopic equation**

The Cahn-Hilliard equation writes:

.. math::
   :label: Eq_CH
   
   \partial_{t}\underbrace{\phi}_{\mathcal{M}_{0}}+\boldsymbol{\nabla}\cdot(\underbrace{\boldsymbol{u}\phi}_{\boldsymbol{\mathcal{M}}_{1}})=\boldsymbol{\nabla}\cdot\Bigl[M_{\phi}\boldsymbol{\nabla}\cdot(\underbrace{\mu_{\phi}\boldsymbol{I}}_{\boldsymbol{\mathcal{M}}_{2}})\Bigr]

where  The chemical potential is a function of :math:`\phi` defined by

.. math::
   :label: mu_CH
   
   \mu_{\phi}=4H\phi(\phi-1)(\phi-1/2)-\zeta\underbrace{\boldsymbol{\nabla}^{2}\phi}_{\text{Laplacian}}

The first term of the right-hand side is the derivative of double-well and the second one involves the Laplacian of :math:`\phi`. Compared to the ADE :eq:`ADE_Sterm`, in Cahn-Hilliard equation :eq:`Eq_CH`, the source term is null :math:`\mathscr{S}_{\phi}=0`, and the chemical potential :math:`\mu_{\phi}` replaces :math:`\phi` for the moment of second order.

**Equilibrium for CH equation**

To design the EqDF, its moment of order zero ant its moment of first order must remain unchanged i.e. :math:`\mathcal{M}_{0}=\phi` and :math:`\boldsymbol{\mathcal{M}}_{1}=\boldsymbol{u}\phi`. But now its moment of second order must be equal to :math:`\boldsymbol{\mathcal{M}}_{2}=\mu_{\phi}\boldsymbol{I}`. One solution writes:

.. math::
   :label: Geq_CH
   
   g_{i}^{eq,\,CH}=\mathcal{A}_{i}(\phi,\,\mu_{\phi})+w_{i}\frac{\boldsymbol{c}_{i}\cdot(\overbrace{\boldsymbol{u}\phi}^{\boldsymbol{\mathcal{M}}_{1}})}{c_{s}^{2}}

where

.. math::
   :label: CoeffA_Geq
   
   \mathcal{A}_{i}(\phi,\,\mu_{\phi})=\begin{cases}
   \phi-3\mu_{\phi}(1-w_{0}) & \text{if }i=0\quad\mathcal{M}_{0}\\
   3w_{i}\mu_{\phi} & \text{if }i\neq0\quad\boldsymbol{\mathcal{M}}_{2}
   \end{cases}
   
The chemical potential :math:`\mu_{\phi}` appears in :eq:`CoeffA_Geq`. For the computation of the Laplacian which is involved in its definition :eq:`mu_CH`, see Section :ref:`Directional-Deriv`.
   
**Moment**

After collision and streaming, the new :math:`\phi` function is obtained by the moment of order zero

.. math::
   :label: M0_CH
   
   \phi=\sum_{i}g_{i}

   
:math:`g_i^{eq}` for Conservative Allen-Cahn equation
"""""""""""""""""""""""""""""""""""""""""""""""""""""

**Target macroscopic equation**

The Conservative Allen-Cahn equation writes:

.. math::
   :label: Eq_CAC
   
   \partial_{t}\underbrace{\phi}_{\mathcal{M}_{0}}+\boldsymbol{\nabla}\cdot(\underbrace{\boldsymbol{u}\phi}_{\boldsymbol{\mathcal{M}}_{1}})+\boldsymbol{\nabla}\cdot\biggl[\underbrace{M_{\phi}\frac{4}{W}\phi(1-\phi)\boldsymbol{n}}_{\boldsymbol{j}_{ct}\equiv\boldsymbol{\mathcal{M}}_{1}}\biggr]=\boldsymbol{\nabla}\cdot\Bigl[M_{\phi}\boldsymbol{\nabla}\cdot(\underbrace{\phi\boldsymbol{I}}_{\boldsymbol{\mathcal{M}}_{2}})\Bigr]

Compared to ADE with source term, a new term appears: the last one in the left-hand side. That term involves a *counter term* noted :math:`\boldsymbol{j}_ct` which cancels the interface movement due to the curvature. The EqDF is designed such as its moments of order 0 and 2 are unchanged compared to ADE. Its moment of order 1 must be shlightly modified to account for the new counter term. Two methods are possible for that purpose.

**Method 1: equilibrium for CAC without source term** (:math:`\mathcal{G}_i=0`)

The first method consists in modifying the EqDF by adding a new equilibrium for that counter term. That :math:`g_{i}^{eq,CAC}` is the sum of the classical ADE equiblibrium plus an equilibrium designed for :math:`\boldsymbol{j}_{ct}`:

.. math::
   :label: Geq_CAC
   
   g_{i}^{eq,CAC}=g_{i}^{eq,ADE}+g_{i}^{eq,ct}\qquad\text{with }\begin{cases}
   g_{i}^{eq,ADE} & =w_{i}\phi+(\boldsymbol{u}\phi)\cdot\left(\frac{w_{i}\boldsymbol{c}_{i}}{c_{s}^{2}}\right)\\
   g_{i}^{eq,ct} & =\boldsymbol{j}_{ct}\cdot\left(\frac{w_{i}\boldsymbol{c}_{i}}{c_{s}^{2}}\right)
   \end{cases}

where :math:`g_{i}^{eq,ct}` is simply obtained by the scalar product of :math:`\boldsymbol{j}_{ct}` with :math:`w_i\boldsymbol{c}_{i}/c_{s}^{2}` like the advective term :math:`\boldsymbol{u}\phi`.

.. math::
   :label: Geq_CAC_Full_Expr
   
   g_{i}^{eq,CAC}(\boldsymbol{x},\,t)=\underbrace{w_{i}\phi\left[1+\frac{\boldsymbol{c}_{i}\cdot\boldsymbol{u}}{c_{s}^{2}}\right]}_{g_{i}^{eq,ADE}}+\underbrace{M_{\phi}\left[\frac{4}{W}\phi(1-\phi)\right]\boldsymbol{n}}_{\boldsymbol{j}_{ct}}\cdot\left(\frac{w_{i}\boldsymbol{c}_{i}}{c_{s}^{2}}\right)

The evolution of :math:`g_i` follows :eq:`LBE_ADE_Sterm` with :math:`\mathcal{G}_i=0`.

**Method 2: equilibrium for ADE with source term** (:math:`\mathcal{G}_i\neq0`)

Because the moments of order 0, 1 and 2 are the same than ADE, the second method uses the :math:`g_i^{eq,ADE}` and considers the divergence of the counter term as a source term :math:`\mathcal{G}_i`:

.. math::
   :label: Geq_VarChange
   
   \overline{g}_{i}^{eq,ADE}(\boldsymbol{x},t)=w_{i}\phi\left[1+\frac{\boldsymbol{c}_{i}\cdot\boldsymbol{u}}{c_{s}^{2}}\right]-\frac{\delta t}{2}\mathcal{G}_{i}

where the source term is defined by

.. math::
   :label: SourceT_CAC
   
   \mathcal{G}_{i}=\frac{4}{W}\phi(1-\phi)w_{i}\boldsymbol{c}_{i}\cdot\boldsymbol{n}

Let us notice that in the right-hand side, the mobility coefficient does not appear compared to the expression which appears in the equilibrium :eq:`Geq_CAC_Full_Expr`.

**Moment**

Finally, after collision and streaming, the new :math:`\phi` is updated by

.. math::
   :label: M0_CAC
   
   \phi=\sum_{i}g_{i}+\frac{\delta t}{2}\mathcal{G}_{i}

For the first method :math:`\mathcal{G}_i=0`.

.. sectionauthor:: Alain Cartalade
   