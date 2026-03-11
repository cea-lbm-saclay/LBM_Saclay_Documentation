.. include:: ../../Substitutions.rst

.. _Model_iNS_with_PhaseField_Course:

Derivation of incompressible Navier-Stokes with interface-capturing equation model
==================================================================================

Mass balance & interface equation
---------------------------------

:mediumbold:`Bulk and local densities`

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

:mediumbold:`Mass balance and interface equation`

   A mass balance for each local density yields

   .. math::
      :label: Mass_Balance_rhoA

      \frac{\partial\varrho_{A}}{\partial t}+\boldsymbol{\nabla}\cdot(\varrho_{A}\boldsymbol{u}+\rho_{A}\boldsymbol{j}_{A})=-\dot{m}'''
      
   .. math::
      :label: Mass_Balance_rhoB

      \frac{\partial\varrho_{B}}{\partial t}+\boldsymbol{\nabla}\cdot(\varrho_{B}\boldsymbol{u}+\rho_{B}\boldsymbol{j}_{B})=+\dot{m}'''

   where :math:`\varrho_{B}\boldsymbol{u}` and :math:`\varrho_{A}\boldsymbol{u}` are two advective fluxes and :math:`\rho_{A}\boldsymbol{j}_{A}` and :math:`\rho_{B}\boldsymbol{j}_{B}` are two diffusive fluxes. Here we assume that :math:`\boldsymbol{j}_{A}` and :math:`\boldsymbol{j}_{B}` are equal and opposite:

   .. math::
      :label: Fluxes_Assumption

      \boldsymbol{j}_{\phi}=\boldsymbol{j}_{B}=-\boldsymbol{j}_{A}

   On the right-hand side, :math:`\dot{m}'''` is a production source term: if it is added in one equation, then that quantity is substracted from the other equation. The three primes :math:`'''` means that the production is volumic. Its physical dimension is :math:`[\text{M}]/([\text{L}]^3.[\text{T}])`. Its value is non zero when phase change occurs. For two immiscible fluids we can consider that :math:`\dot{m}'''=0`.

   Expressed with :math:`\phi`, those two equations write

   .. math::
      :label: Eqs_phi

      \frac{\partial\phi}{\partial t}+\boldsymbol{\nabla}\cdot(\boldsymbol{u}\phi+\boldsymbol{j}_{\phi}) &=+\frac{\dot{m}'''}{\rho_{B}}\\\frac{\partial(1-\phi)}{\partial t}+\boldsymbol{\nabla}\cdot(\boldsymbol{u}(1-\phi)-\boldsymbol{j}_{\phi}) &=-\frac{\dot{m}'''}{\rho_{A}}

   By summing those two equations, we obtain:

   .. math::
      :label: Mass_Conservation_TwoPhase_with_m_Course

      \boldsymbol{\nabla}\cdot\boldsymbol{u}=\dot{m}'''\left(\frac{1}{\rho_{B}}-\frac{1}{\rho_{A}}\right)

:mediumbold:`Incompressible two-phase flows without phase change`

   Without phase change :math:`\dot{m}'''=0` and we retrieve the classical mass balance:

   .. math::
      :label: Mass_Balance_TwoPhase_Course

      \boldsymbol{\nabla}\cdot\boldsymbol{u}=0

   For interface tracking equation, Eq. :eq:`Eqs_phi` becomes:

   .. math::

      \frac{\partial\phi}{\partial t}+\boldsymbol{\nabla}\cdot(\boldsymbol{u}\phi)=-\boldsymbol{\nabla}\cdot\boldsymbol{j}_{\phi}

   where :math:`\boldsymbol{j}_{\phi}` has to be determined. With the material derivative:

   .. math::
      :label: Material-Derivative

      \frac{d}{dt}\,\hat{=}\,\frac{\partial}{\partial t}+\boldsymbol{u}\cdot\boldsymbol{\nabla}

   the interface-tracking equation writes:

   .. math::

      \frac{\partial\phi}{\partial t}+\boldsymbol{u}\cdot\boldsymbol{\nabla}\phi+\phi\boldsymbol{\nabla}\cdot\boldsymbol{u}&=-\boldsymbol{\nabla}\cdot\boldsymbol{j}_{\phi}\\
      \frac{d\phi}{dt}+\phi\boldsymbol{\nabla}\cdot\boldsymbol{u}&=-\boldsymbol{\nabla}\cdot\boldsymbol{j}_{\phi}


Derivation of constitutive laws
-------------------------------

:mediumbold:`Summary of balance equations`

   .. admonition:: Summary of balance equations

      Finally, we summarize the three balance equations with the material derivative. First, the mass balance equation writes:

      .. math::
         :label: Mass-Balance_iNS-PFCourse

         \frac{d\rho_{0}}{dt}=-\rho_{0}\boldsymbol{\nabla}\cdot\boldsymbol{u}
   
      The impulsion balance equation is:

      .. math::
         :label: Impulsion-Balance_iNS-PFCourse
   
         \rho_{0}\frac{d\boldsymbol{u}}{dt}=\boldsymbol{\nabla}\cdot{\color{red}\overline{\overline{\boldsymbol{T}}}}
   
      where the stress tensor :math:`{\color{red}\overline{\overline{\boldsymbol{T}}}}` has to be determined. At last, the balance of phase-field :math:`\phi` writes:

      .. math::
         :label: Phi-Balance-iNS-PFCourse

         \frac{d\phi}{dt}+\phi\boldsymbol{\nabla}\cdot\boldsymbol{u}=-\boldsymbol{\nabla}\cdot{\color{red}\boldsymbol{j}_{\phi}}

      where :math:`{\color{red}\boldsymbol{j}_{\phi}}` has also to be determined.

:mediumbold:`Objective`

   .. admonition:: Objective
   
      In Section :bdg-ref-primary-line:`CH-CAC-Models` the diffusive flux :math:`\boldsymbol{j}_{diff}` has been derived such as :math:`\partial\mathscr{F}[\phi]/\partial t < 0`. Here we consider the total energy :math:`\mathscr{E}_{tot}` which is a functional depending on two functions: the phase-field :math:`\phi` and the velocity :math:`\boldsymbol{u}`. It is composed of two parts:

      .. math::
         :label: Total_Energy

         \mathscr{E}_{tot}[\phi,{\color{red}\boldsymbol{u}}]=\int_{V}\biggl[\underbrace{\frac{1}{2}\rho_{0}\bigl|{\color{red}\boldsymbol{u}}\bigr|^{2}}_{\text{kinetic energy}}+\underbrace{\mathcal{F}(\phi,\boldsymbol{\nabla}\phi)}_{\text{potential energy}}\biggr]dV

      where :math:`\rho_{0}\bigl|\boldsymbol{u}\bigr|^{2}/2` is the kinetic energy (:math:`\rho_0` is the constant density) and the potential energy is given by the free energy density:

      .. math::
         :label: Potential_Energy

         \mathcal{F}(\phi,\boldsymbol{\nabla}\phi)=f_{dw}(\phi)+\frac{\zeta}{2}\bigl|\boldsymbol{\nabla}\phi\bigr|^{2}

      In Eq. :eq:`Potential_Energy`, :math:`f_{dw}(\phi)` is the double-well free energy density, and :math:`\zeta` is the capillary coefficient.

      The objectice is determine the constitutive laws for the stress tensor :math:`\overline{\overline{\boldsymbol{T}}}` in Eq. :eq:`Impulsion-Balance_iNS-PFCourse` and the flux :math:`\boldsymbol{j}_{\phi}` in Eq. :eq:`Phi-Balance-iNS-PFCourse` such as

      .. math::
         :label: Decrease_Etot

         \frac{d\mathscr{E}_{tot}}{dt}-\int_{V}\underbrace{\lambda\boldsymbol{\nabla}\cdot\boldsymbol{u}}_{\hat{=}\mathscr{L}}\leqslant0

      where :math:`\lambda` is the lagrange multiplier of constraint :math:`\boldsymbol{\nabla}\cdot\boldsymbol{u}=0`.

:mediumbold:`Method`

   Express

   .. math::
      :label: dEtot_dt

      \frac{d\mathscr{E}_{tot}}{dt}	=\frac{d}{dt}\int_{V}\left[\mathcal{F}(\phi,\boldsymbol{\nabla}\phi)+\frac{1}{2}\rho_{0}\bigl|\boldsymbol{u}\bigr|^{2}\right]dV

   on the form

   .. math::
      :label: DEtot_dt_Dissipation

      \frac{d\mathscr{E}_{tot}}{dt}=-\mathcal{D}(V){\color{gray}+\underbrace{\mathcal{W}(V)+\Phi(\partial V)}_{\text{neglected here}}}\leqslant0

   where :math:`\mathcal{D}` is the dissipation with :math:`\mathcal{D}\geqslant0`, :math:`\mathcal{W}` is the work of external forces and :math:`\Phi` is the flux through surface.

   For that purpose we use the Reynolds transport theorem:

   .. math::
      :label: Reynolds-Transport-Theorem

      \frac{d}{dt}\left[\int_{V}\Psi dV\right]\,\hat{=}\,\int_{V}\left[\frac{d\Psi}{dt}+\Psi\boldsymbol{\nabla}\cdot\boldsymbol{u}\right]dV

   Example:

   .. math::

      \frac{d\mathscr{E}_{tot}}{dt}&=\frac{d}{dt}\int_{V}\left[\mathcal{F}(\phi,\boldsymbol{\nabla}\phi)+\frac{1}{2}\rho_{0}\bigl|\boldsymbol{u}\bigr|^{2}\right]dV\\
	   &=\int_{V}\left\{ \frac{d}{dt}\left[\mathcal{F}+\frac{1}{2}\rho_{0}\bigl|\boldsymbol{u}\bigr|^{2}\right]+\left[\mathcal{F}+\frac{1}{2}\rho_{0}\bigl|\boldsymbol{u}\bigr|^{2}\right]\boldsymbol{\nabla}\cdot\boldsymbol{u}\right\} dV\\
	   &=\int_{V}\biggl\{\left[\frac{d\mathcal{F}}{dt}+\mathcal{F}\boldsymbol{\nabla}\cdot\boldsymbol{u}\right]+\biggl[\cancel{\frac{1}{2}\frac{d\rho_{0}}{dt}\bigl|\boldsymbol{u}\bigr|^{2}}+\frac{1}{2}\rho_{0}\frac{d\bigl|\boldsymbol{u}\bigr|^{2}}{dt}+\cancel{\frac{1}{2}\rho_{0}\bigl|\boldsymbol{u}\bigr|^{2}\boldsymbol{\nabla}\cdot\boldsymbol{u}}\biggr]\biggr\} dV\\
      &=\int_{V}\biggl\{\underbrace{\left[\frac{d\mathcal{F}}{dt}+\mathcal{F}\boldsymbol{\nabla}\cdot\boldsymbol{u}\right]}_{\hat{=}\mathcal{I}}+\underbrace{\frac{1}{2}\rho_{0}\frac{d\bigl|\boldsymbol{u}\bigr|^{2}}{dt}}_{\hat{=}\mathcal{K}}\biggr\} dV

   The next stages require to make appear balance equations in :math:`\mathcal{I}` and :math:`\mathcal{K}` and evaluate the differentials :math:`d\mathcal{F}` and :math:`d\bigl|\boldsymbol{u}\bigr|^{2}`.

   The details of derivation are presented in :bdg-ref-primary-line:`Constitutive-laws`. Finally the constitutive laws which satisfy the condition :math:`\frac{d\mathscr{E}_{tot}}{dt}=-\mathcal{D}(V)\leqslant0` can be chosen such as:

   .. admonition:: Constitutive laws
      :class: error

      .. grid:: 2
         :gutter: 4
         :margin: 3 3 0 5

         .. grid-item-card:: Stress tensor :math:`\overline{\overline{\boldsymbol{T}}}`
            :columns: 6

            .. math::
               :label: Def-Stress-Tensor-iNS

               \overline{\overline{\boldsymbol{T}}}=-\overline{\overline{\boldsymbol{P}}}+\eta(\boldsymbol{\nabla}\boldsymbol{u}+\boldsymbol{\nabla}\boldsymbol{u}^{T})

            with the pressure tensor is defined by

            .. math::
               :label: Def-Pressure-Tensor-iNS

               \overline{\overline{\boldsymbol{P}}}=\Bigl[(p_{h}-\mathcal{F})\overline{\overline{\boldsymbol{I}}}+\zeta\boldsymbol{\nabla}\phi\otimes\boldsymbol{\nabla}\phi\Bigr]

         .. grid-item-card:: Flux :math:`\boldsymbol{j}_{\phi}`
            :columns: 6

            .. math::
               :label: Def-Flux-iNS

               \boldsymbol{j}_{\phi}=-\mathcal{M}_{\phi}\boldsymbol{\nabla}\mu_{\phi}

            where the chemical potential is defined by

            .. math::
               :label: Def-ChemPot-iNS

               \mu_{\phi}=f_{dw}^{\prime}(\phi)-\zeta\boldsymbol{\nabla}^{2}\phi

      By replacing :eq:`Def-Stress-Tensor-iNS` in Eq. :eq:`Impulsion-Balance_iNS-PFCourse` we obtain two terms in the right-hand side: :math:`-\boldsymbol{\nabla}\cdot\overline{\overline{\boldsymbol{P}}}` and :math:`\boldsymbol{\nabla}\cdot\eta(\boldsymbol{\nabla}\boldsymbol{u}+\boldsymbol{\nabla}\boldsymbol{u}^{T})`. The first one can be written with its potential form:

      .. grid:: 3
         :gutter: 4
         :margin: 3 3 0 5

         .. grid-item::
            :columns: 3

         .. grid-item-card:: Potential form of pressure tensor
            :columns: 6

            .. math::
               :label: Potential-Form-Pressure-Tensor-iNS

               -\boldsymbol{\nabla}\cdot\overline{\overline{\boldsymbol{P}}}=-\boldsymbol{\nabla}p_{h}+\mu_{\phi}\boldsymbol{\nabla}\phi

         .. grid-item::
            :columns: 3

      The interpretation of term :math:`\mu_{\phi}\boldsymbol{\nabla}\phi` is the capillary force :math:`\boldsymbol{F}_{c}` (see proof below), and :math:`p_h` is the hydrodynamic pressure ensuring the continuity equation.


   Proof of Eq. :eq:`Potential-Form-Pressure-Tensor-iNS`:

   .. math::

      -\boldsymbol{\nabla}\cdot\overline{\overline{\boldsymbol{P}}}&=-\boldsymbol{\nabla}p_{h}+\boldsymbol{\nabla}\mathcal{F}-\zeta\boldsymbol{\nabla}\cdot(\boldsymbol{\nabla}\phi\otimes\boldsymbol{\nabla}\phi)\\&=-\boldsymbol{\nabla}p_{h}+\boldsymbol{\nabla}\Bigl[f_{dw}+\frac{\zeta}{2}\bigl|\boldsymbol{\nabla}\phi\bigr|^{2}\Bigr]-\zeta\boldsymbol{\nabla}\cdot(\boldsymbol{\nabla}\phi\otimes\boldsymbol{\nabla}\phi)\\&=-\boldsymbol{\nabla}p_{h}+\boldsymbol{\nabla}f_{dw}+\cancel{\frac{\zeta}{2}\boldsymbol{\nabla}(\bigl|\boldsymbol{\nabla}\phi\bigr|^{2})}-\cancel{\frac{\zeta}{2}\boldsymbol{\nabla}(\bigl|\boldsymbol{\nabla}\phi\bigr|^{2})}-\zeta(\boldsymbol{\nabla}^{2}\phi)\boldsymbol{\nabla}\phi\\&=-\boldsymbol{\nabla}p_{h}+\Bigl[\underbrace{f_{dw}^{\prime}-\zeta(\boldsymbol{\nabla}^{2}\phi)}_{\equiv\mu_{\phi}}\Bigr]\boldsymbol{\nabla}\phi



Model of incompressible Navier-Stokes with interface-capturing equation
-----------------------------------------------------------------------

Incompressible Navier-Stokes with capillary force term
""""""""""""""""""""""""""""""""""""""""""""""""""""""

The model of two-phase flows is simply composed of incompressible Navier-Stokes equations which hold in both fluids :math:`A` and :math:`B`. An interpolation with :math:`\phi` is performed for local densities and local viscosities, and an additional force term is added in the impulsion balance equation: the capillary force representative of surface tension :math:`\sigma` between both fluids. The model writes:

.. math::
   :label:

   \boldsymbol{\nabla}\cdot\boldsymbol{u} &=0\\\varrho(\phi)\underbrace{\left[\frac{\partial\boldsymbol{u}}{\partial t}+\boldsymbol{\nabla}\cdot(\boldsymbol{u}\boldsymbol{u})\right]}_{\text{Acceleration}} &=\underbrace{-\boldsymbol{\nabla}p_{h}}_{\text{Pressure force}}+\underbrace{\boldsymbol{\nabla}\cdot\left[\varrho(\phi)\vartheta(\phi)(\boldsymbol{\nabla}\boldsymbol{u}+\boldsymbol{\nabla}\boldsymbol{u}^{T})\right]}_{\text{Viscous force}}+\underbrace{\mu_{\phi}\boldsymbol{\nabla}\phi}_{\text{Capillary force }\boldsymbol{F}_{c}}+\underbrace{\varrho(\phi)\boldsymbol{g}}_{\text{Buoyancy}}

where :math:`\boldsymbol{u}` is the mean velocity, :math:`p_h` is the hydrodynamic pressure, :math:`\boldsymbol{g}` is the gravity. The local properties of fluids are noted :math:`\varrho(\phi)` for density and :math:`\vartheta(\phi)` for kinematic viscosity. Their expressions will will summarized below. The physical dimensions of each term must be :math:`[\text{F}]/[\text{L}]^3` where :math:`[\text{F}]` is used for force: :math:`[\text{F}]=[\text{M.L}]/[\text{T}]^2`. For example for the buoyancy force term

.. math::
   :label: Physical_Dim_grhog

   [\varrho(\phi)\boldsymbol{g}]=\frac{[\text{M}]}{[\text{L}]^3} \frac{[\text{L}]}{[\text{T}]^2}=\frac{[\text{F}]}{[\text{L}]^3}

.. _Interpretation_mu_grad_phi:

Interpretation of term :math:`\mu_{\phi}\boldsymbol{\nabla}\phi`
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. admonition:: Interpretation of term :math:`\mu_{\phi}\boldsymbol{\nabla}\phi`

   The capillary force :math:`\boldsymbol{F}_c=\mu_{\phi}\boldsymbol{\nabla}\phi` has been formulated in :footcite:p:`Brackbill_etal_JCP1992` and :footcite:p:`Jacqmin_JCP1999`. That form is equivalent to the surface tension force :math:`-\delta_d \sigma \kappa \boldsymbol{n}_{\phi}` where :math:`\kappa` is the curvature, :math:`\sigma` is the surface tension, :math:`\boldsymbol{n}_{\phi}` is the normal vector at the interface and :math:`\delta_d` is the Kronecker's symbol but expressed in the phase-field framework, i.e. with a diffuse interface:

   .. math::
      :label: Proof-Equiv-Surface-Tension_NSAC

      \boldsymbol{F}_{c}=\mu_{\phi}\boldsymbol{\nabla}\phi=-\delta_{d}\sigma\kappa\boldsymbol{n}_{\phi}\hspace{1cm}\text{with}\hspace{1cm}\delta_{d}=\frac{3}{2}W\left|\boldsymbol{\nabla}\phi\right|^{2}

   That term is homogeneous to an inverse of length: :math:`[\delta_d]=1/[\text{L}]`. We can check that the capillary force is homogeneous to a volumic force:

   .. math::
      :label: Check_PhysDim_Fc

      [\delta_{d}\sigma\kappa\boldsymbol{n}_{\phi}]=\frac{1}{[\text{L}]}\times \frac{[\text{F}]}{[\text{L}]}\times \frac{1}{[\text{L}]}=\frac{[\text{F}]}{[\text{L}]^3}

   When expressed by its potential form:

   .. math::
      :label: 

      [\mu_{\phi}\boldsymbol{\nabla}\phi]=\frac{\text{E}}{[\text{L}]^3}\times \frac{1}{[\text{L}]}=\frac{[\text{F.L}]}{[\text{L}]^3}\times \frac{1}{[\text{L}]}=\frac{[\text{F}]}{[\text{L}]^3}


**Proof**

.. grid:: 2
   :gutter: 4
   :margin: 3 3 0 5

   .. grid-item::
      :columns: 5

      .. math::

         \boldsymbol{F}_{c} &=\mu_{\phi}\boldsymbol{\nabla}\phi\\
         &=\Bigl[4H\phi(\phi-1)(\phi-1/2)-\zeta\boldsymbol{\nabla}^{2}\phi\Bigr]\boldsymbol{\nabla}\phi\\
         &=-\frac{3}{2}W\sigma\Bigl[\Delta\phi-\frac{16}{W^{2}}\phi(1-\phi)(1-2\phi)\Bigr]\boldsymbol{\nabla}\phi\\
         &=-\frac{3}{2}W\sigma\kappa\left|\boldsymbol{\nabla}\phi\right|\boldsymbol{\nabla}\phi\\
         &=-\delta_{d}\sigma\kappa\boldsymbol{n}

   .. grid-item::
      :columns: 7

      Where we have used

      - Eq. :eq:`Chemical_Potential_Course` for :math:`\mu_{\phi}` in the second line.
      - Replace :math:`H` and :math:`\zeta` by :math:`H=12\sigma/W` and :math:`\zeta=(3/2)W\sigma` in the third line.
      - Eq. :eq:`Equiv_Derivative_Curvature` for :math:`\kappa\left|\boldsymbol{\nabla}\phi\right|` in the fourth line.
      - Multiply and divide by :math:`\left|\boldsymbol{\nabla}\phi\right|` to make appear :math:`\boldsymbol{n}` in the last line.


Summary
"""""""

.. admonition:: Two-phase incompressible Navier-Stokes
   :class: error

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


.. admonition:: Interface-capturing model 1: Cahn-Hilliard equation
   :class: error

   Once the diffusive flux :eq:`Def-Flux-iNS` is replaced in Eq. :eq:`Phi-Balance-iNS-PFCourse`, the advective Cahn-Hilliard equation (Eq. :eq:`Adv_CH_Model_Course_Summary`) is obtained:

   .. math::
      :label: CH_Eq_TwoPhase

      \frac{\partial\phi(\boldsymbol{x},t)}{\partial t}+\boldsymbol{\nabla}\cdot(\boldsymbol{u}\phi)=\boldsymbol{\nabla}\cdot\left\{M_{\phi}\boldsymbol{\nabla}\left[2\phi(1-\phi)(1-2\phi)-\frac{W^2}{8}\boldsymbol{\nabla}^{2}\phi  \right]\right\}

   That model can advantageously be replaced by the Conservative Allen-Cahn equation (Eq. :eq:`CAC_Course`) for immiscible two fluid flows:

   .. math::
      :label: CAC_Eq_TwoPhase

      \frac{\partial\phi}{\partial t}+\boldsymbol{\nabla}\cdot(\boldsymbol{u}\phi)=\boldsymbol{\nabla}\cdot\left[M_{\phi}\left(\boldsymbol{\nabla}\phi-\frac{4}{W}\phi(1-\phi)\boldsymbol{n}_{\phi}\right)\right]

   where :math:`M_{\phi}` is the mobility coefficient of interface, :math:`W` is the interface width and the unit normal vector :math:`\boldsymbol{n}_{\phi}` is defined by

   .. math::
      :label: TwoPhase_Def_n

      \boldsymbol{n}_{\phi}=\frac{\boldsymbol{\nabla}\phi}{|\boldsymbol{\nabla}\phi|}

Appendix: details for deriving constitutive laws
------------------------------------------------

.. toctree::
   :maxdepth: 1

   ./D_Constitutive_Laws.rst

References
----------

.. footbibliography::

.. sectionauthor:: Alain Cartalade
   