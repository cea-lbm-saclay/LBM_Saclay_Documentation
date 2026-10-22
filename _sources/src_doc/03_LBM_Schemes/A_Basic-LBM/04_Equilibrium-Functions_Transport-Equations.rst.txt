.. _EdF-For-Transport-Equation:

Equilibrium distribution functions for Transport equations
==========================================================

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
-----------------------------------------

.. admonition:: Target macroscopic equation
   :class: important

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
-------------------------------------------

.. admonition:: Target macroscopic equation
   :class: important

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

.. _LBMScheme-for-CAC:

:math:`g_i^{eq}` for Conservative Allen-Cahn equation
-----------------------------------------------------

.. admonition:: Target macroscopic equation
   :class: important

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

.. admonition:: Method 2: ADE equilibrium with a source term (:math:`\mathcal{G}_i\neq0`)
   :class: caution

   **Equilibrium distribution function**

   Because the moments of order 0, 1 and 2 are the same than ADE, the second method uses the :math:`g_i^{eq,ADE}` and considers the divergence of the counter term as a source term :math:`\mathcal{G}_i`:

   .. math::
      :label: Geq_VarChange
   
      \overline{g}_{i}^{eq,ADE}(\boldsymbol{x},t)=w_{i}\phi\left[1+\frac{\boldsymbol{c}_{i}\cdot\boldsymbol{u}}{c_{s}^{2}}\right]-\frac{\delta t}{2}\mathcal{G}_{i}

   **Source term**

   The source term :math:`\mathcal{G}_{i}` is defined by

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
   