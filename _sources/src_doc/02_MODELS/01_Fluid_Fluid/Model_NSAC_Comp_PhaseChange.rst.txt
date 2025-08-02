.. _Math-NSAC-PhaseChange:

Model of Navier-Stokes/CAC with Liquid-Gas phase change
=======================================================

Incompressible two-phase flows with phase change
------------------------------------------------

The mathematical model is composed of incompressible Navier-Stokes equations coupled with the phase-field equation and temperature equation. The basic model is the previous one ``NSAC_Comp`` except that the mass balance is modified with a source term and the temperature equation replaces the composition one. The modifications are highlighted in the orange boxes below.

.. admonition:: Mass balance with source term
   :class: warning

   The mass balance writes:

   .. math::
      :label: Mass_Balance_PhaseChange
   
      \boldsymbol{\nabla}\cdot\boldsymbol{u}=\dot{m}'''\left(\frac{1}{\rho_{g}}-\frac{1}{\rho_{l}}\right)

   where :math:`\boldsymbol{u}\equiv\boldsymbol{u}(\boldsymbol{x},t)=(u_x,u_y,u_z)^T` is the fluid velocity, and :math:`\dot{m}'''` is the volumic production of one phase at the interface. It is defined in Eq. :eq:`CAC_ProdTerm`.

**Impulsion balance equation**

The impulsion balance equation writes:

.. math::
   :label: Impulsion_Balance_PhaseChange
   
   \varrho(\phi,c)\left[\frac{\partial\boldsymbol{u}}{\partial t}+\boldsymbol{\nabla}\cdot(\boldsymbol{u}\boldsymbol{u})\right]=-\boldsymbol{\nabla}p_{h}+\boldsymbol{\nabla}\cdot\left[\eta(\phi)\left(\boldsymbol{\nabla}\boldsymbol{u}+\boldsymbol{\nabla}\boldsymbol{u}^{T}\right)\right]+\boldsymbol{F}_{tot}

where :math:`p_{h}\equiv p_{h}(\boldsymbol{x},t)` is the hydrodynamic pressure, :math:`\varrho` is the total densiy and :math:`\eta` is the dynamic viscosity. Those quantities are obtained from the interpolation of bulk properties with the phase-field :math:`\phi`. Their expressions will be given in the subsection "Closure".

.. admonition:: Phase-field equation
   :class: warning

   The interface is followed by an additional PDE on the phase-field:

   .. math::
      :label: CAC_PhaseChange
   
      \frac{\partial\phi}{\partial t}+\boldsymbol{\nabla}\cdot(\boldsymbol{u}\phi)=\boldsymbol{\nabla}\cdot\left[M_{\phi}\left(\boldsymbol{\nabla}\phi-\frac{4}{W}\phi(1-\phi)\boldsymbol{n}\right)\right]+\frac{\dot{m}'''}{\rho_{g}}

   where :math:`\phi\equiv\phi(\boldsymbol{x},t)` is the phase-field, :math:`M_{\phi}` is the mobility and :math:`W` is the interface width. :math:`\dot{m}'''` is a production term at interface defined by

   .. math::
      :label: CAC_ProdTerm

      \frac{\dot{m}'''}{\rho_{g}}=-\frac{4\alpha}{\mathscr{A}W^{2}}(\theta_{I}-\theta)\phi(1-\phi)

   where the coefficient :math:`\mathscr{A}` is equal to :math:`\mathscr{A}=10/48\approx0.21`.

Finally, the temperature equation is also considered in that model:

.. admonition:: Temperature equation
   :class: warning

   .. math::
      :label: Temperature_PhaseChange
   
      \frac{\partial T}{\partial t}+\boldsymbol{\nabla}\cdot(\boldsymbol{u}T)=\alpha\boldsymbol{\nabla}^{2}T-\frac{\mathcal{L}}{\mathcal{C}_{p}}\left[\frac{\partial\phi}{\partial t}+\boldsymbol{\nabla}\cdot(\boldsymbol{u}\phi)\right].
      
   where :math:`T\equiv T(\boldsymbol{x},t)` is the temperature, :math:`\mathcal{C}_{p}` is the specific heat, :math:`\alpha` is the thermal diffusivity, :math:`\mathcal{L}` is the latent heat..

Force and source terms
^^^^^^^^^^^^^^^^^^^^^^

Several forces are defined in ``NSAC_Comp`` kernel.

**Total force**

The total force :math:`\boldsymbol{F}_{tot}` in Eq. :eq:`Impulsion_Balance_PhaseChange` is defined by

.. math::
   :label: Force_Total
   
   \boldsymbol{F}_{tot}=\boldsymbol{F}_{c}+\boldsymbol{F}_{g}
   
where :math:`\boldsymbol{F}_{c}` is the capillary force, :math:`\boldsymbol{F}_{g}` is the gravity force and :math:`\boldsymbol{F}_{M}` is the Marangoni force. They are detailed below.

.. container:: sphinx-features

   .. admonition:: Capillary force
      :class: hint

      The capillary force :math:`\boldsymbol{F}_{c}` is defined by

      .. math::
         :label: Force_Capillary
   
         \boldsymbol{F}_{c}=\mu_{\phi}\boldsymbol{\nabla}\phi

      where the chemical potential :math:`\mu_{\phi}` is defined by

      .. math::
         :label: pot_chem_phi
   
         \mu_{\phi}=\frac{3}{2}\sigma\left[\frac{16}{W}\phi(1-\phi)(1-2\phi)-W\boldsymbol{\nabla}^{2}\phi\right]

      :math:`\sigma` is the surface tension and :math:`W` is the interface width.

   :math:`\hspace{5mm}`
      
   .. admonition:: Gravity force
      :class: hint

      The gravity force :math:`\boldsymbol{F}_{g}` is defined by

      .. math::
         :label: Force_Gravity
   
         \boldsymbol{F}_{g}=\varrho(\phi,c)\boldsymbol{g}

      where :math:`\varrho(\phi,c)` is an interpolation of bulk densities by Eq. :eq:`Density_Total_Surf`

.. sectionauthor:: Alain Cartalade
   