.. _Model_iNS_with_PhaseField_Course:

Model of incompressible Navier-Stokes with interface-capturing equation
=======================================================================

Bulk and local densities
------------------------

We consider two fluids :math:`A` and :math:`B` of constant densities :math:`\rho_A` and :math:`\rho_B` and constant viscosities :math:`\nu_A` and :math:`\nu_B`. Those properties are called *bulk densities* and *bulk viscosities*. We introduce a phase index :math:`\phi(\boldsymbol{x},t)` of value 0 in the first phase :math:`A` and +1 in the second phase :math:`B`. With the phase-field :math:`\phi(\boldsymbol{x},t)` we can define local densities depending on position and time :math:`\varrho_A(\boldsymbol{x},t)` and :math:`\varrho_B(\boldsymbol{x},t)` by:

.. math::
   :label: Local_Density_A

   \varrho_{A}(\boldsymbol{x},t)=\rho_{A}(1-\phi(\boldsymbol{x},t))

and 

.. math::
   :label: Local_Density_B

   \varrho_{B}(\boldsymbol{x},t)=\rho_{B}\phi(\boldsymbol{x},t)

The total local density is

.. math::
   :label: Local_Density_Total

   \varrho(\boldsymbol{x},t)=\rho_{B}\phi(\boldsymbol{x},\,t)+\rho_{A}(1-\phi(\boldsymbol{x},t))

With that definition, if :math:`\phi(\boldsymbol{x},t)=0`, then :math:`\varrho(\boldsymbol{x},t)=\rho_A` and if :math:`\phi(\boldsymbol{x},t)=1`, then :math:`\varrho(\boldsymbol{x},t)=\rho_B`.

Mass balance
------------

A mass balance for each local density yields

.. math::
   :label: Mass_Balance_TwoPhase_Course

   \begin{eqnarray}
      \frac{\partial\varrho_{A}}{\partial t}+\boldsymbol{\nabla}\cdot(\varrho_{A}\boldsymbol{u}+\rho_{A}\boldsymbol{j}_{A})& = & -\dot{m}'''\\
      \frac{\partial\varrho_{B}}{\partial t}+\boldsymbol{\nabla}\cdot(\varrho_{B}\boldsymbol{u}+\rho_{B}\boldsymbol{j}_{B})& = & +\dot{m}'''
   \end{eqnarray}

where :math:`\varrho_{B}\boldsymbol{u}` and :math:`\varrho_{A}\boldsymbol{u}` are two advective fluxes and :math:`\rho_{A}\boldsymbol{j}_{A}` and :math:`\rho_{B}\boldsymbol{j}_{B}` are two diffusive fluxes. Here we assume that :math:`\boldsymbol{j}_{A}` and :math:`\boldsymbol{j}_{B}` are equal and opposite:

.. math::
   :label: Fluxes_Assumption

   \boldsymbol{j}=\boldsymbol{j}_{B}=-\boldsymbol{j}_{A}

On the right-hand side, :math:`\dot{m}'''` is a production source term: if it is added in one equation, then that quantity is substracted from the other equation. The three primes :math:`'''` means that the production is volumic. Its physical dimension is :math:`[\text{M}]/([\text{L}]^3.[\text{T}])`. Its value is non zero when phase change occurs. For two immiscible fluids we can consider that :math:`\dot{m}'''=0`.

Expressed with :math:`\phi`, those two equations write

.. math::
   :label: Eqs_phi

   \begin{eqnarray}
      \frac{\partial\phi}{\partial t}+\boldsymbol{\nabla}\cdot(\boldsymbol{u}\phi+\boldsymbol{j})& = & +\frac{\dot{m}'''}{\rho_{B}}\\
      \frac{\partial(1-\phi)}{\partial t}+\boldsymbol{\nabla}\cdot(\boldsymbol{u}(1-\phi)-\boldsymbol{j}) & = & -\frac{\dot{m}'''}{\rho_{A}}
   \end{eqnarray}

By summing those two equations, we obtain:

.. math::
   :label: Mass_Conservation_TwoPhase_with_m_Course

   \boldsymbol{\nabla}\cdot\boldsymbol{u}=\dot{m}'''\left(\frac{1}{\rho_{B}}-\frac{1}{\rho_{A}}\right)

Incompressible two-phase flows without phase change
---------------------------------------------------

Without phase change :math:`\dot{m}'''=0` and we retrieve the classical mass balance:

.. math::
   :label: Mass_Balance_TwoPhase_Course

   \boldsymbol{\nabla}\cdot\boldsymbol{u}=0

For flux :math:`\boldsymbol{j}`, two hypotheses are used.

- For the first one, the flux is given by the gradient of chemical potential :math:`\mu_{\phi}`:

.. math::
   :label: Cahn_Hilliard_Flux

   \begin{eqnarray}
      \boldsymbol{j} & = & -\mathcal{M}_{\phi}\boldsymbol{\nabla}\mu_{\phi}\\
      & = & -M_{\phi}\boldsymbol{\nabla}\left[2\phi(1-\phi)(1-2\phi)-\frac{W^2}{8}\boldsymbol{\nabla}^{2}\phi  \right]
   \end{eqnarray}

and Eq. :eq:`Eqs_phi` becomes the CH model:

.. math::
   :label: Cahn_Hilliard_TwoPhase

   \frac{\partial\phi(\boldsymbol{x},t)}{\partial t}=\boldsymbol{\nabla}\cdot\left\{M_{\phi}\boldsymbol{\nabla}\left[2\phi(1-\phi)(1-2\phi)-\frac{W^2}{8}\boldsymbol{\nabla}^{2}\phi  \right]\right\}

- For the second one, the flux is chosen as standard diffusive flux :math:`\boldsymbol{j}_{diff}` with counter term flux :math:`\boldsymbol{j}_{CT}` (see :ref:`CAC-Model` for origin and interpretation of counter term):

.. math::
   :label: Counter_Term_Flux_Course

   \boldsymbol{j}=-M_{\phi}\boldsymbol{\nabla}\phi+\frac{4}{W}\phi(1-\phi)\boldsymbol{n}_{\phi}

and Eq. :eq:`Eqs_phi` becomes the CAC model:

.. math::
   :label: CAC_TwoPhase

   \frac{\partial\phi}{\partial t}+\boldsymbol{\nabla}\cdot(\boldsymbol{u}\phi)=\boldsymbol{\nabla}\cdot\left[M_{\phi}\left(\boldsymbol{\nabla}\phi-\frac{4}{W}\phi(1-\phi)\boldsymbol{n}_{\phi}\right)\right]

Model of Navier-Stokes with interface-capturing equation
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

The model of two-phase flows is simply composed of incompressible Navier-Stokes equations which hold in both fluids :math:`A` and :math:`B`. An interpolation with :math:`\phi` is performed for local densities and local viscosities, and an additional force term is added in the impulsion balance equation: the capillary force representative of surface tension :math:`\sigma` between both fluids. The model writes:

.. math::
   :label:

   \begin{eqnarray}
      \boldsymbol{\nabla}\cdot\boldsymbol{u} & = & 0\\
      \varrho(\phi)\underbrace{\left[\frac{\partial\boldsymbol{u}}{\partial t}+\boldsymbol{\nabla}\cdot(\boldsymbol{u}\boldsymbol{u})\right]}_{\text{Acceleration}}& = & \underbrace{-\boldsymbol{\nabla}p_{h}}_{\text{Pressure force}}+\underbrace{\boldsymbol{\nabla}\cdot\left[\varrho(\phi)\vartheta(\phi)(\boldsymbol{\nabla}\boldsymbol{u}+\boldsymbol{\nabla}\boldsymbol{u}^{T})\right]}_{\text{Viscous force}}+\underbrace{\mu_{\phi}\boldsymbol{\nabla}\phi}_{\text{Capillary force }\boldsymbol{F}_{c}}+\underbrace{\varrho(\phi)\boldsymbol{g}}_{\text{Buoyancy}}
   \end{eqnarray}

where :math:`\boldsymbol{u}` is the mean velocity, :math:`p_h` is the hydrodynamic pressure, :math:`\boldsymbol{g}` is the gravity. The local properties of fluids are noted :math:`\varrho(\phi)` for density and :math:`\vartheta(\phi)` for kinematic viscosity. Their expressions will will summarized below. The physical dimensions of each term must be :math:`[\text{F}]/[\text{L}]^3` where :math:`[\text{F}]` is used for force: :math:`[\text{F}]=[\text{M.L}]/[\text{T}]^2`. For example for the buoyancy force term

.. math::
   :label: Physical_Dim_grhog

   [\varrho(\phi)\boldsymbol{g}]=\frac{[\text{M}]}{[\text{L}]^3} \frac{[\text{L}]}{[\text{T}]^2}=\frac{[\text{F}]}{[\text{L}]^3}

The capillary force :math:`\boldsymbol{F}_c=\mu_{\phi}\boldsymbol{\nabla}\phi` has been formulated in [1]_ and [2]_. That form is equivalent to the surface tension force :math:`-\delta_d \sigma \kappa \boldsymbol{n}` where :math:`\kappa` is the curvature, :math:`\sigma` is the surface tension, :math:`\boldsymbol{n}` is the normal vector at the interface and :math:`\delta_d` is the Kronecker's symbol but expressed in the phase-field framework, i.e. with a diffuse interface:

.. math::
   :label:

   \delta_{d}=\frac{3}{2}W\left|\boldsymbol{\nabla}\phi\right|^{2}

That term is homogeneous to an inverse of length: :math:`[\delta_d]=1/[\text{L}]`. We can prove that

.. math::
   :label: Proof-Equiv-Surface-Tension_NSAC

   \begin{eqnarray}
      \boldsymbol{F}_{c} & = & \mu_{\phi}\boldsymbol{\nabla}\phi\\
      & = & \Bigl[4H\phi(\phi-1)(\phi-1/2)-\zeta\boldsymbol{\nabla}^{2}\phi\Bigr]\boldsymbol{\nabla}\phi\\
      & = & -\frac{3}{2}W\sigma\Bigl[\Delta\phi-\frac{16}{W^{2}}\phi(1-\phi)(1-2\phi)\Bigr]\boldsymbol{\nabla}\phi\\
      & = & -\frac{3}{2}W\sigma\kappa\left|\boldsymbol{\nabla}\phi\right|\boldsymbol{\nabla}\phi\\
      & = & -\delta_{d}\sigma\kappa\boldsymbol{n}
   \end{eqnarray}

where we have used

- Eq. :eq:`Chemical_Potential_Course` for :math:`\mu_{\phi}` in the second line.
- Replace :math:`H` and :math:`\zeta` by :math:`H=12\sigma/W` and :math:`\zeta=(3/2)W\sigma` in the third line.
- Eq. :eq:`Equiv_Derivative_Curvature` for :math:`\kappa\left|\boldsymbol{\nabla}\phi\right|` in the fourth line.
- Multiply and divide by :math:`\left|\boldsymbol{\nabla}\phi\right|` to make appear :math:`\boldsymbol{n}` in the last line.

We can check that the capillary force is homogeneous to a volumic force:

.. math::
   :label: Check_PhysDim_Fc

   [\delta_{d}\sigma\kappa\boldsymbol{n}]=\frac{1}{[\text{L}]}\times \frac{[\text{F}]}{[\text{L}]}\times \frac{1}{[\text{L}]}=\frac{[\text{F}]}{[\text{L}]^3}

When expressed by its potential form:

.. math::
   :label: 

   [\mu_{\phi}\boldsymbol{\nabla}\phi]=\frac{\text{E}}{[\text{L}]^3}\times \frac{1}{[\text{L}]}=\frac{[\text{F.L}]}{[\text{L}]^3}\times \frac{1}{[\text{L}]}=\frac{[\text{F}]}{[\text{L}]^3}

.. admonition:: Two-phase incompressible Navier-Stokes
   :class: hint

   The two-phase flows model is composed of incompressible Navier-Stokes equations. The first one is the mass balance equation

   .. math::
      :label: TwoPhase_MassBalance

      \boldsymbol{\nabla}\cdot\boldsymbol{u}=0

   The second one is the impulsion balance equation:

   .. math::
      :label: NS_Eqs_TwoPhase

      \varrho(\phi)\left[\frac{\partial\boldsymbol{u}}{\partial t}+\boldsymbol{\nabla}\cdot(\boldsymbol{u}\boldsymbol{u})\right]=-\boldsymbol{\nabla}p_{h}+\boldsymbol{\nabla}\cdot\left[\varrho(\phi)\vartheta(\phi)\left(\boldsymbol{\nabla}\boldsymbol{u}+\boldsymbol{\nabla}\boldsymbol{u}^{T}\right)\right]+\mu_{\phi}\boldsymbol{\nabla}\phi+\varrho(\phi)\boldsymbol{g}

   where the local density :math:`\varrho(\phi)` is defined by Eq. :eq:`Local_Density_Total`:

   .. math::
      :label: Interpolation_Density

      \varrho(\boldsymbol{x},t)=\rho_{B}\phi(\boldsymbol{x},\,t)+\rho_{A}(1-\phi(\boldsymbol{x},t))

   and the kinematic viscosity :math:`\vartheta(\phi)` is interpolated with the harmonic mean:

   .. math::
      :label: Interpolation_Viscosity

      \frac{1}{\vartheta(\phi)}=\frac{\phi}{\nu_{B}}+\frac{1-\phi}{\nu_{A}}

   In capillary force of Eq. :eq:`NS_Eqs_TwoPhase` the chemical potential :math:`\mu_{\phi}` is defined by

   .. math::
      :label: Chem_Pot_TwoPhase

      \mu_{\phi}=\frac{3}{2}\sigma W\left[\frac{16}{W^2}\phi(1-\phi)(1-2\phi)-\boldsymbol{\nabla}^{2}\phi\right]

The phase-field :math:`\phi` follows one of the two phase-field equation. The Conservative Allen-Cahn equation writes

.. admonition:: Interface-capturing model 1: Conservative Allen-Cahn equation
   :class: hint

   .. math::
      :label: CAC_Eq_TwoPhase

      \frac{\partial\phi}{\partial t}+\boldsymbol{\nabla}\cdot(\boldsymbol{u}\phi)=\boldsymbol{\nabla}\cdot\left[M_{\phi}\left(\boldsymbol{\nabla}\phi-\frac{4}{W}\phi(1-\phi)\boldsymbol{n}_{\phi}\right)\right]

   where :math:`M_{\phi}` is the mobility coefficient of interface, :math:`W` is the interface width and the unit normal vector :math:`\boldsymbol{n}_{\phi}` is defined by

   .. math::
      :label: TwoPhase_Def_n

      \boldsymbol{n}_{\phi}=\frac{\boldsymbol{\nabla}\phi}{|\boldsymbol{\nabla}\phi|}

.. admonition:: Interface-capturing model 2: Cahn-Hilliard equation
   :class: hint

   Whereas the Cahn-Hilliard equation writes

   .. math::
      :label: CH_Eq_TwoPhase

      \frac{\partial\phi(\boldsymbol{x},t)}{\partial t}=\boldsymbol{\nabla}\cdot\left\{M_{\phi}\boldsymbol{\nabla}\left[2\phi(1-\phi)(1-2\phi)-\frac{W^2}{8}\boldsymbol{\nabla}^{2}\phi  \right]\right\}

Bibliography
------------

.. [1] J. Brackbill, D.B. Kothe, C. Zemach, A continuum method for modeling surface tension, Journal of Computational Physics, Volume 100, Issue 2, June 1992, Pages 335-354. 1992. https://doi.org/10.1016/0021-9991(92)90240-Y

.. [2] Jacqmin D., Calculation of Two-Phase Navier–Stokes Flows Using Phase-Field Modeling, Journal of Computational Physics, Volume 155, Issue 1, Pages 96-127, 1999. https://doi.org/10.1006/jcph.1999.6332