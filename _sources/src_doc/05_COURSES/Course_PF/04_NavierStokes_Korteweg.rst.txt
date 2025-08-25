.. _Model_NSK_Course:

Isothermal Navier-Stokes/Korteweg model
=======================================

Historically, the thermodynamic theory of capillarity was developed by van der Waals under the hypothesis of a continuous variation of density [1]_. In that sense, this is the very first diffuse interface theory. Next Korteweg has modified the Navier-Stokes equations to take into account the surface tension force through what we call the Korteweg's tensor [2]_. Those equations are known as the Navier-Stokes/Korteweg model (NSK) which is a popular model for simulating two-phase flows. That model is a low Mach formulation of the Navier-Stokes equations, where :math:`\rho` plays the role of phase index. The two-phase behavior is obtained by an appropriate choice of the Equation of State (EoS). The NSK model is an alternative model to the Navier-Stokes/Conservative Allen-Cahn model for two incompressible fluids (see :ref:`Model_iNS_with_PhaseField_Course`).

Free energy functional with :math:`\rho`
----------------------------------------

For a sake of simplicity of this presentation, we assume an isothermal fluid: the temperature :math:`T` will appear in the equation of states but it will be considered as a constant. The free energy is defined by

.. math::
   :label: Free_Energy_NSK_Course

   \mathscr{F}[\rho]=\int_{V}\underbrace{\mathcal{W}(\rho)+\frac{\kappa}{2}\bigl|\boldsymbol{\nabla}\rho\bigr|^{2}}_{\equiv\mathcal{F}(\rho,\boldsymbol{\nabla}\rho)}dV

where :math:`\rho\equiv \rho(\boldsymbol{x},t)` is the fluid density which replaces the phase-field :math:`\phi` previously used as order parameter for incompressible flows. :math:`\mathcal{W}(\rho)` plays the role of double-well, and the gradient energy term is given by the last term :math:`\kappa |\boldsymbol{\nabla}\rho\bigr|^{2}/2`. The coefficient :math:`\kappa` is named the capillary coefficient. It will be considered as a constant in this section. As seen in :ref:`Free-Energy-Double-Wells`, the gradient energy term is non-local and it is responsible for the surface tension :math:`\sigma` and width :math:`W` of diffuse interface.

**Double-well potentiel**

In two-phase flows literature the free energy density :math:`\mathcal{W}(\rho)` can take two different forms. In the first one, it takes a similar form as previously noted :math:`f_{dw}(\phi)`:

.. math::
   :label:

   \mathcal{W}(\rho):=\mathcal{W}_{dw}(\rho)=H(\rho-\rho_l)^2(\rho-\rho_g)^2

where :math:`\rho_l` and :math:`\rho_g` are the bulk densities of liquid and gas and the subscript :math:`_{dw}` means double-well. That expression is equivalent to the double-well :math:`f_{dw}(\phi)=Hg_2(\phi)` of :ref:`Free-Energy-Double-Wells`. In particular, the equilibrium solution of Euler-Lagrange equation is:

.. math::
   :label:

   \rho(x)=\frac{\rho_{l}+\rho_{g}}{2}+\frac{\rho_{l}-\rho_{g}}{2}\tanh\left[\frac{2x}{W}\right]

The solution of density :math:`\rho(x)` follows a hyperbolic tangent profile and varies continuously between a minimum value :math:`\rho_g` and maximum value :math:`\rho_l`. The slope of that variation is controlled by the parameter :math:`W` which is the interface width. The expressions of interface width :math:`W` and surface tension :math:`\sigma` can also be re-used:

.. math::
   :label:

   W=\frac{4}{(\rho_{l}-\rho_{g})}\sqrt{\frac{\kappa}{2H}}

.. math::
   :label:

   \sigma=\frac{1}{6}(\rho_{l}-\rho_{g})^{3} \sqrt{2\kappa H}

**Potential and Equation of State**

In the rest of this section, we will focus on another way to define the potential :math:`\mathcal{W}(\rho)` and we will relate it to the thermodynamic pressure :math:`p^{eos}(\rho)` where the superscript :math:`^{eos}` means *Equation of State*.

van der Waals equation of state and Maxwell construction
--------------------------------------------------------

The equation of state for an ideal gas is given by (1 mole):

.. math::
   :label: EoS_Perfect_Gas_NSK_Course
   
    PV=RT
    
which is derived from point-like particles whitout interaction. Expressed with density :math:`V=1/\rho` that equation of state takes the expression

.. math::
   :label: EoS_Perfect_Gas_Density_NSK_Course

   p^{eos}_{pg}(\rho,T)=\rho RT

where the subscript :math:`_{pg}` means *perfect gas*. That EoS of perfect gas is monotonous: for one pressure corresponds only a unique density. That relationship is also local in the sense that, at a same point :math:`\boldsymbol{x}`, the pressure :math:`p^{eos}(\boldsymbol{x})` is related to the density :math:`\rho(\boldsymbol{x})` and temperature :math:`T(\boldsymbol{x})`. We will see below that the gradient energy term in Eq. :eq:`Free_Energy_NSK_Course` is responsible for a *non-local pressure* :math:`\mathcal{P}`. 

**van der Waals equation of state**

Van der Waals modified that assumption. A new equation of state was formulated with short range repulsion (excluded volume) and long range attractions:

.. math::
   :label: EoS_VdW_NSK_Course
   
   P(V,T)+\frac{a}{V^2}=\frac{RT}{V-b}
   
where :math:`a` represents attractive interactions which modify the pressure and :math:`b` corresponds to the excluded volume occupied by hard sphere atoms. Those interactions can be described by interactomic potential, e.g. Lennard-Jones. Expressed with density, that Equation of State writes:

.. math::
   :label: EoS_VdW_Density_NSK_Course

   p^{eos}_{vdW}(\rho,T)=\frac{\rho RT}{1-b\rho}-a\rho^2

The main advantage of that form of EoS, is that, for certain values of temperature, the EoS is not any more monotonous, and for one pressure corresponds two values of densities. Indeed, on :numref:`Fig-EoS_vdW_Volume_NSK_Course` the pressure is presented as a function of volume :math:`V` whereas on :numref:`Fig-EoS_vdW_Density_NSK_Course` it is presented as a function of density :math:`\rho`. On those figures, one temperature :math:`T_5` (the magenta curve) is above the critical temperature. The curve is monotonous and only one density corresponds to one pressure. For temperature :math:`T_4` (cyan curve) there is an inflexion point corresponding to the critical temperature (zero derivative with respect to \rho). At last, for three next temperatures :math:`T_1,T_2,T_3` (respectively black, red and blue curves), the pressure presents a cubic form enabling the existence of two densities corresponding to one pressure.

.. container:: sphinx-features

   .. _Fig-EoS_vdW_Volume_NSK_Course:

   .. figure:: ../../FIGS/03_FIGS_THERMO/EOS_vdWaals_P-V.png
      :height: 250
      :width: 350
      :scale: 100
      :align: center

      Phase diagram :math:`P-V`

   .. _Fig-EoS_vdW_Density_NSK_Course:

   .. figure:: ../../FIGS/03_FIGS_THERMO/EOS_vdWaals_P-Rho.png
      :height: 250
      :width: 350
      :scale: 100
      :align: center
      
      Phase diagram :math:`P-\rho`

**Critical point**

The critical point corresponds to the presence of an inflexion point on the curve :math:`p^{eos}(V)`. It is defined by:

.. math::
   :label:

   \begin{eqnarray}
      \frac{\partial P}{\partial V} & = & 0\\
      \frac{\partial^2 P}{\partial V^2} & = & 0
   \end{eqnarray}

The application of those two conditions to the van der Waals EoS, yields a critical point which is defined by:

.. math::
   :label: Critical_Point_VdW

   V_c=3b,\quad T_c=\frac{8a}{27Rb},\quad P_c=\frac{a}{27b^2}

Free energy density and non-local pressure
------------------------------------------

From EoS, we can define a thermodynamic potential :math:`\mathcal{W}(V)`, which is the work (an energy) of pressure force per volume unit:

.. math::
   :label: Potential_W_Volume_for_EoS

   \mathcal{W}(V)=-\frac{1}{V}\int p^{eos}(V)dV

i.e. with the variable change :math:`\rho=1/V`:

.. math::
   :label: Potential_W_Density_for_EoS

   \mathcal{W}(\rho)=\rho\int\frac{p^{eos}(\rho)}{\rho^{2}}d\rho

For van der Waals EoS, such a potential writes:

.. math::
   :label: Thermo_Potential_vdW_eos

   \mathcal{W}^{vdW}(\rho)=\rho RT\ln\left(\frac{\rho}{1-b\rho}\right)-a\rho^{2}

It is straightforward (derive Eq. :eq:`Potential_W_Density_for_EoS` wrt :math:`\rho`) to show that the thermodynamic pressure :math:`p^{eos}(\rho)` can derive from a thermodynamic potential :math:`\mathcal{W}(\rho)`:

.. math::
   :label: Def_Thermo_Pressure

   \boxed{p^{eos}(\rho)=\rho \frac{\partial \mathcal{W}(\rho)}{\partial \rho}-\mathcal{W}(\rho)}

The potential :math:`\mathcal{W}(\rho)` is more general because once it is set, we can derive the thermodynamic pressure :math:`p^{eos}(\rho)` but also other quantities such as the chemical potential :math:`\mu_{\rho}^{(0)}` where the superscript :math:`^{(0)}` means "local". Moreover, we can use it in Eq. :eq:`Free_Energy_NSK_Course` and derive other non-local quantities such as the non-local pressure :math:`\mathcal{P}(\rho,\boldsymbol{\nabla}\rho)` and the non-local chemical potential :math:`\mu_{\rho}(\rho,\boldsymbol{\nabla}\rho)`. Both quantities are called "non-local" because they depend on :math:`\boldsymbol{\nabla}\rho`.

The **non-local pressure** :math:`\mathcal{P}(\rho,\boldsymbol{\nabla}\rho)` is obtained by applying the definition Eq. :eq:`Def_Thermo_Pressure`, but with free energy density :math:`\mathcal{F}(\rho,\boldsymbol{\nabla}\rho)` replacing the potential :math:`\mathcal{W}(\rho)`. The partial derivative :math:`\partial /\partial\rho` must also be replaced by the variational derivative :math:`\delta / \delta \rho` because the two independent variables :math:`\rho` and :math:`\boldsymbol{\nabla}\rho` are involded in the free energy density :math:`\mathcal{F}`:

.. math::
   :label: Nonlocal_Pressure_NSK_Course

   \begin{eqnarray}
      \mathcal{P}(\rho,\boldsymbol{\nabla}\rho) & = & \rho \frac{\delta \mathcal{F}(\rho,\boldsymbol{\nabla}\rho)}{\delta \rho}-\mathcal{F}(\rho,\boldsymbol{\nabla}\rho)\\
      & = & \rho \left[ \frac{\partial \mathcal{W}(\rho)}{\partial \rho} - \kappa \boldsymbol{\nabla}\cdot \boldsymbol{\nabla}\rho \right] - \mathcal{W}(\rho) - \frac{\kappa}{2}|\boldsymbol{\nabla}\rho|^{2}\\
      & = & p^{eos}(\rho) - \kappa\rho \boldsymbol{\nabla}^2\rho - \frac{\kappa}{2}|\boldsymbol{\nabla}\rho|^{2}
   \end{eqnarray}

where the Euler-Lagrange equation is used in the brackets (see :ref:`Free-Energy-Double-Wells`) for the second line and :eq:`Def_Thermo_Pressure` for the third line. Now we see the consequence on pressure of adding a gradient energy term in the free energy density: the pressure is not any more equal to the eos pressure, it is modified by two non-local terms (i.e. depending on :math:`\boldsymbol{\nabla}\rho`), both depending on the capillary coefficient :math:`\kappa`. The gradient energy term is responsible for the surface tension, the diffuse interface and the modification of pressure which becomes non-local.

In :ref:`Free-Energy-Double-Wells`, we have seen that :math:`\delta \mathcal{F}/\delta \rho` is the definition of chemical potential :math:`\mu_{\rho}`. In the second line of Eq. :eq:`Nonlocal_Pressure_NSK_Course`, the term inside the brackets is the **non-local chemical potential** :math:`\mu_{\rho}`. Its expression for a van der Waals EoS (i.e. with :math:`\mathcal{W}` defined by Eq. :eq:`Thermo_Potential_vdW_eos`) writes

.. math::
   :label: Non_Local_Chemical_Potential_NSK_Course

   \begin{eqnarray}
      \mu_{\rho}^{vdW} & = & \left[ \frac{\partial \mathcal{W}^{vdW}(\rho)}{\partial \rho} - \kappa \boldsymbol{\nabla}\cdot \boldsymbol{\nabla}\rho \right]\\
      & = & RT\left[\ln\left(\frac{\rho}{1-b\rho}\right)+\frac{1}{1-b\rho}\right]-2a\rho-\kappa\boldsymbol{\nabla}^{2}\rho
   \end{eqnarray}

Let us emphasize that the non-local terms in Eqs. :eq:`Nonlocal_Pressure_NSK_Course` and :eq:`Non_Local_Chemical_Potential_NSK_Course` have an impact only at the interface between both fluids or in the vicinity of the interface because in the bulk phases, the densities are constant of values :math:`\rho_l` and :math:`\rho_g`, and consequently their gradients are zero.

.. admonition:: Summary of van der Waals EoS

   The Van der Waal EoS writes

   .. math::
      :label: EoS_van_der_Waals_NSK_Course
   
      p_{vdW}^{eos}(\rho,T)=\frac{\rho RT}{1-b\rho}-a\rho^{2}

   which can be derived from potential :math:`\mathcal{W^{vdW}}`:

   .. math::
      :label: W_van_der_Waals_NSK_Course

      \mathcal{W}_{vdW}(\rho)=\rho RT\ln\left(\frac{\rho}{1-b\rho}\right)-a\rho^{2}

   The chemical potential writes:

   .. math::
      :label: mu_van_der_Waals_NSK_Course

      \mu_{\rho}^{vdW}=RT\left[\ln\left(\frac{\rho}{1-b\rho}\right)+\frac{1}{1-b\rho}\right]-2a\rho-\kappa\boldsymbol{\nabla}^{2}\rho

Maxwell construction for bulk densities :math:`\rho_l` and :math:`\rho_g`
-------------------------------------------------------------------------

**Common tangent construction**

The van der Waals EoS indicates how the pressure varies as a function of density. Under the critical point, the equilibrium solutions, or bulk densities :math:`\rho_l` and :math:`\rho_g` are obtained with the Maxwell construction. We remind that the thermodynamic equilibrium is reached when the intensive variables are equal and constant inside the whole domain. More precisely, for two phases of density :math:`\rho_l` and :math:`\rho_g`:

.. math::
   :label:

   \begin{eqnarray}
      p^{eos}(\rho_l) & = & p^{eos}(\rho_g)\\
      \mu^{(0)}(\rho_l) & = & \mu^{(0)}(\rho_g)
   \end{eqnarray}

With the definition of thermodynamic pressure Eq. :eq:`Def_Thermo_Pressure`, it is straightforward to obtain

.. math::
   :label:

   \mu^{(0)}=\frac{\mathcal{W}(\rho_l)-\mathcal{W}(\rho_g)}{\rho_l-\rho_g}

This means that :math:`(\rho_l,\mathcal{W}(\rho_l))` and :math:`(\rho_g,\mathcal{W}(\rho_g))` lie on a common tangent line of :math:`\mathcal{W}(\rho)` of slope :math:`\mu^{(0)}`.

**Graphic interpretation**

The graphic interpretation of Maxwell construction is known as an "equal area rule". That construction states that, for one particular pressure :math:`P_b`, the bulk volumes (or densities) :math:`V_{l}` and :math:`V_{g}` are obtained such as 

.. math::
   
   \underbrace{\int_{V_{l}}^{V_{g}}p^{eos}(V)dV}_{S_{1}}=\underbrace{P_{b}(V_{g}-V_{l})}_{S_{2}}

That relation can be interpreted as equal surfaces :math:`S_{1}=S_{2}` where the area between :math:`P_b` and the upper part of the vdW EoS and the area between :math:`P_b` and the lower part of the vdW EoS are equal. For example, with vdW eos:

.. math::

   p^{eos}(V)=\frac{RT}{V-b}-a\left(\frac{1}{V}\right)^{2}

the bulk pressure :math:`P_b` and the two equilibrium densities :math:`\rho_g` and :math:`\rho_l` are solution of :math:`S_1=S_2`:

.. math::

   \begin{cases}
      S_{1} & =\left[RT\ln(V_{g}-b)+\frac{a}{V_{g}}\right]-\left[RT\ln(V_{l}-b)+\frac{a}{V_{l}}\right]\\
      S_{2} & =P_{b}(V_{g}-V_{l})
   \end{cases}

By solving semi-analytically we obtain the equilibrium densities (or coexistence densities) of bulks :math:`\rho_l` and :math:`\rho_g` for several temperatures as presented in :numref:`Fig-DensityBulk_EoS_vdW_NSK_Course` and :numref:`Fig-VolumeBulk_vdW_Volume_NSK_Course`. For example, on :numref:`Fig-DensityBulk_EoS_vdW_NSK_Course`, at :math:`T=280` two fluids will coexist. The first one density :math:`\rho_g \approx 4` and the second one of density :math:`\rho_l \approx 12`.

.. container:: sphinx-features

   .. _Fig-DensityBulk_EoS_vdW_NSK_Course:

   .. figure:: ../../FIGS/03_FIGS_THERMO/Construction-Maxwell_EOSvdWaals_rho.png
      :height: 250
      :width: 350
      :scale: 100
      :align: center

      Equilibrium densities for vdW eos

   .. _Fig-VolumeBulk_vdW_Volume_NSK_Course:

   .. figure:: ../../FIGS/03_FIGS_THERMO/Construction-Maxwell_EOSvdWaals.png
      :height: 250
      :width: 350
      :scale: 100
      :align: center
      
      Equilibrium volumes for vdW eos

Pressure tensor and Korteweg tensor
-----------------------------------

For a sake of simplicity of this presentation, here we follow the argument presented in reference [3]_ to derive the tensor pressure and the Korteweg's tensor. As seen in :ref:`Free-Energy-Double-Wells`, when the order parameter is conserved (this is the case for :math:`\rho`), the chemical potential :math:`\mu_{\rho}` can be interpreted as a the Lagrange multiplier associated with the constraint of mass conservation. The integrand of :math:`\mathcal{F}` as well as that of the mass constraint are independent of the spatial coordinates. Consequently, it follows from Noether’s theorem (see [4]_ sections 12-3 p. 555 and 12-7 p. 588) that there is a corresponding conservation law given by

.. math::
   :label: Conservation_Law_From_Noether

   \boldsymbol{\nabla}\cdot\overline{\overline{\boldsymbol{P}}}=\boldsymbol{0}

where the pressure tensor :math:`\overline{\overline{\boldsymbol{P}}}` is a tensor of second rank which is given by

.. math::
   :label: Def_Pressure_Tensor

   \overline{\overline{\boldsymbol{P}}}=\mathcal{L}\overline{\overline{\boldsymbol{I}}}-\boldsymbol{\nabla}\rho\otimes\frac{\partial\mathcal{L}}{\partial(\boldsymbol{\nabla}\rho)}

where :math:`\overline{\overline{\boldsymbol{I}}}` is the identity tensor, and :math:`\mathcal{L}(\rho,\boldsymbol{\nabla}\rho)` is 

.. math::
   :label:

   \mathcal{L}(\rho,\boldsymbol{\nabla}\rho)=\mathcal{F}(\rho,\boldsymbol{\nabla}\rho)-\rho\mu_{\rho}

where the free energy density is defined by Eq. :eq:`Free_Energy_NSK_Course` i.e. :math:`\mathcal{F}=\mathcal{W}(\rho)+\kappa|\boldsymbol{\nabla}\rho|^2/2` and the Lagrange multiplier :math:`\mu_{\rho}` (or chemical potential) is given by :math:`\mu_{\rho}=\delta\mathcal{F}/\delta\rho` (Euler-Lagrange)

.. math::
   :label:

   \mu_{\rho}=\partial_{\rho}\mathcal{W}-\kappa\boldsymbol{\nabla}^2\rho

It is straightforward to obtain

.. math::
   :label: Def_PressureTensor_KortewegTensor_NSK_Course

   \overline{\overline{\boldsymbol{P}}}=\left[ -p^{eos}(\rho)+\rho\kappa\boldsymbol{\nabla}^2\rho+\frac{\kappa}{2}(\boldsymbol{\nabla}\rho)^2 \right]\overline{\overline{\boldsymbol{I}}}-\kappa \boldsymbol{\nabla}\rho \otimes \boldsymbol{\nabla}\rho

where we recognize the non-local pressure :math:`\mathcal{P}` inside the brackets, but also a second term which gives birth to the surface tension force between both fluids. The second rank tensor

.. math::
   :label: Def_Korteweg_Tensor

   \overline{\overline{\boldsymbol{\varsigma}}}=\left[ \rho\kappa\boldsymbol{\nabla}^2\rho+\frac{\kappa}{2}(\boldsymbol{\nabla}\rho)^2 \right]\overline{\overline{\boldsymbol{I}}}-\kappa \boldsymbol{\nabla}\rho \otimes \boldsymbol{\nabla}\rho

is called the korteweg's tensor.

Equivalence of tensor pressure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In most of numerical methods that implement the NSK model, the pressure tensor Eq. :eq:`Def_PressureTensor_KortewegTensor_NSK_Course` is not directly discretized because there exist two equivalent algebraic forms which are easier to implement. The first one is the potential form and the second involves the chemical potential.

.. admonition:: First form: potential form

   The first form is called the potential form and writes:

   .. math::
      :label: Potential_Form_NSK_Course
   
      -\boldsymbol{\nabla}\cdot\overline{\overline{\boldsymbol{P}}}=-\boldsymbol{\nabla}p^{eos}+\kappa\rho\boldsymbol{\nabla}(\boldsymbol{\nabla}^{2}\rho)


Demo:

.. math::

   \partial_{\beta}P_{\alpha\beta}&=\partial_{\beta}\left\{ \left[p^{eos}-\kappa\rho\partial_{\gamma}\partial_{\gamma}\rho-\frac{1}{2}\kappa(\partial_{\gamma}\rho)^{2}\right]\delta_{\alpha\beta}+\kappa(\partial_{\alpha}\rho)(\partial_{\beta}\rho)\right\} \\&=\partial_{\alpha}p^{eos}-\partial_{\alpha}(\kappa\rho\partial_{\gamma}\partial_{\gamma}\rho)-\frac{1}{2}\underbrace{\partial_{\alpha}(\kappa(\partial_{\gamma}\rho)^{2})}_{\text{development}}+\underbrace{\partial_{\gamma}(\kappa(\partial_{\alpha}\rho)(\partial_{\gamma}\rho))}_{\text{index }\beta\rightarrow\gamma}\\&=\partial_{\alpha}p^{eos}-\partial_{\alpha}(\kappa\rho\partial_{\gamma}\partial_{\gamma}\rho)-\left[\kappa(\partial_{\gamma}\rho)(\partial_{\alpha}\partial_{\gamma}\rho)\right]+\underbrace{\partial_{\gamma}(\kappa(\partial_{\alpha}\rho)(\partial_{\gamma}\rho))}_{\text{Development}}\\&=\partial_{\alpha}p^{eos}-\underbrace{\partial_{\alpha}(\kappa\rho\partial_{\gamma}\partial_{\gamma}\rho)}_{\text{Development}}-\left[\cancel{\kappa(\partial_{\gamma}\rho)(\partial_{\alpha}\partial_{\gamma}\rho)}\right]+\left[\cancel{\kappa\partial_{\gamma}(\partial_{\alpha}\rho)(\partial_{\gamma}\rho)}+\kappa(\partial_{\alpha}\rho)\partial_{\gamma}(\partial_{\gamma}\rho)\right]\\&=\partial_{\alpha}p^{eos}-\left[\bcancel{\kappa(\partial_{\alpha}\rho)\partial_{\gamma}\partial_{\gamma}\rho}+\kappa\rho\partial_{\alpha}\partial_{\gamma}\partial_{\gamma}\rho\right]+\bcancel{\kappa(\partial_{\alpha}\rho)\partial_{\gamma}(\partial_{\gamma}\rho)}\\&=\partial_{\alpha}p^{eos}-\kappa\rho\partial_{\alpha}(\partial_{\gamma}\partial_{\gamma}\rho)

.. admonition:: Second form: chemical potential form

   .. math::
      :label: Chemical_Form_NSK_Course
   
      -\boldsymbol{\nabla}\cdot\overline{\overline{\boldsymbol{P}}}=-\rho\boldsymbol{\nabla}\mu_{\rho}
   
   with

   .. math::
      :label: Chemical_Potential_NSK_Course
   
      \mu_{\rho}=\mathcal{W}^{\prime}(\rho)-\kappa\boldsymbol{\nabla}^{2}\rho

Demo

As function of potential :math:`\mathcal{W}` the chemical potential writes:

.. math::
   :label: Chem_pot_rho_NSK_Course

   \mu_{\rho}=\mathcal{W}^{\prime}(\rho)-\kappa\boldsymbol{\nabla}^{2}\rho

and the thermodynamic pressure is:

.. math::
   :label: Thermo_Pressure_NSK_Course

   p^{eos}(\rho)=\rho\mathcal{W}^{\prime}(\rho)-\mathcal{W}(\rho)

.. math::

   \rho\boldsymbol{\nabla}\mu_{\rho}&=\rho\boldsymbol{\nabla}\left[\frac{1}{\rho}\left(p^{eos}+\mathcal{W}(\rho)\right)-\kappa\boldsymbol{\nabla}^{2}\rho\right]\\&=\left(p^{eos}+\mathcal{W}(\rho)\right)\rho\boldsymbol{\nabla}\left(\frac{1}{\rho}\right)+\boldsymbol{\nabla}\left(p^{eos}+\mathcal{W}(\rho)\right){\color{gray}-\rho\kappa\boldsymbol{\nabla}(\boldsymbol{\nabla}^{2}\rho)}\\&=\left(p^{eos}+\mathcal{W}(\rho)\right)\cancel{\rho}\left(-\frac{1}{\rho^{\cancel{2}}}\right)\boldsymbol{\nabla}\rho+\boldsymbol{\nabla}p^{eos}+\mathcal{W}^{\prime}(\rho)\boldsymbol{\nabla}\rho{\color{gray}-\rho\kappa\boldsymbol{\nabla}(\boldsymbol{\nabla}^{2}\rho)}\\&=\bigl[-p^{eos}\underbrace{-\mathcal{W}(\rho)+\rho\mathcal{W}^{\prime}(\rho)}_{\equiv+p^{eos}}\bigr]\frac{\boldsymbol{\nabla}\rho}{\rho}{\color{gray}+\boldsymbol{\nabla}p^{eos}-\rho\kappa\boldsymbol{\nabla}(\boldsymbol{\nabla}^{2}\rho)}\\&=\boldsymbol{\nabla}p^{eos}-\rho\kappa\boldsymbol{\nabla}(\boldsymbol{\nabla}^{2}\rho)

where in the first line we used the definition of :math:`\mu_{\rho}` Eq. :eq:`Chem_pot_rho_NSK_Course` with :math:`\mathcal{W}^{\prime}(\rho)` derived from Eq. :eq:`Thermo_Pressure_NSK_Course`.

Mathematical model of van der Waals fluids
------------------------------------------

The model of Navier-Stokes/Korteweg is obtained from a low Mach formulation of Navier-Stokes equations by simply replacing the gradient of pressure :math:`-\boldsymbol{\nabla}p` by the divergence of the pressure tensor :math:`-\boldsymbol{\nabla}\cdot\overline{\overline{\boldsymbol{P}}}`. That tensor contains the pressure defined by the equation of state and others terms which are responsible for the surface tension force.

.. admonition:: Model of Navier-Stokes/Korteweg
   :class: error

   The mathematical model is based on the low Mach formulation of the Navier-Stokes equations. The mass balance writes

   .. math::
      :label: Mass_Balance_NSK_Course
   
      \frac{\partial\rho}{\partial t}+\boldsymbol{\nabla}\cdot(\rho\boldsymbol{u})=0

   The impulsion balance equation makes appear the pressure tensor

   .. math::
      :label: Impulsion_Balance_NSK_Course
   
      \frac{\partial(\rho\boldsymbol{u})}{\partial t}+\boldsymbol{\nabla}\cdot(\rho\boldsymbol{u}\boldsymbol{u})=-\boldsymbol{\nabla}\cdot\overline{\overline{\boldsymbol{P}}}+\boldsymbol{\nabla}\cdot\left[\eta\left(\boldsymbol{\nabla}\boldsymbol{u}+\boldsymbol{\nabla}\boldsymbol{u}^{T}\right)\right]

   where :math:`\overline{\overline{\boldsymbol{P}}}` is the pressure tensor which is defined by

   .. math::
      :label: Def_Pressure_Tensor_NSK_Course
   
      \overline{\overline{\boldsymbol{P}}}=\left[p^{eos}(\rho,T)-\kappa\rho\boldsymbol{\nabla}^{2}\rho-\frac{1}{2}\kappa\bigl|\boldsymbol{\nabla}\rho\bigr|^{2}\right]\overline{\overline{\boldsymbol{I}}}+\kappa\boldsymbol{\nabla}\rho\otimes\boldsymbol{\nabla}\rho
   
   - For numerical implementation, the divergence of pressure tensor :math:`\boldsymbol{\nabla}\cdot\overline{\overline{\boldsymbol{P}}}` can advantageously be replaced by one of the two following forms given either by Eq. :eq:`Potential_Form_NSK_Course` or by Eq. :eq:`Chemical_Form_NSK_Course` with Eq. :eq:`Chemical_Potential_NSK_Course`.

   - In Eq. :eq:`Def_Pressure_Tensor_NSK_Course` :math:`p^{eos}(\rho,T)` is the thermodynamic pressure which is related to the density and temperature by one Equation of State. Several ones exist: the van der Waals EoS (Eq. :eq:`EoS_van_der_Waals_NSK_Course`) can be used or others defined in the next section.

Let us mention that other methods exist to derive the Navier-Stokes/Korteweg models, especially when the coupling with temperature [5]_ or surfactant [6]_ are considered. In those references, the constitutive laws (closures for energy flux, expression of stress tensor, etc.) are derived such that the dissipation (given by the Clausius-Duhem inequality) is positive or null. The main advantage of that approach is to derive models of two-phase flows which are thermodynamicaly-consistent. But that rigorous approach has a cost: the algebraic calculations are expensive and are beyond the scope of that introduction.

.. _Equations-Of-State:

Other equations of state (EoS)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Several Equations of State (EoS) exist in the literature to simulate two-phase flows: van der Waals, Carnahan-Starling, Peng-Robinson, Redlich-Kwong, etc. The van der Waals EoS is at the heart of this presentation. We present below a summary of other ones.

.. admonition:: Carnahan-Starling EoS

   The Carnahan-Starling EoS writes:

   .. math::
      :label: EoS_Carnahan_Starling_NSK_Course
   
      p_{CS}^{eos}(\rho,T)=\rho RT\frac{1+b\rho/4+(b\rho/4)^{2}-(b\rho/4)^{3}}{(1-b\rho/4)^{3}}-a\rho^{2}

   .. math::
      :label: W_Carnahan_Starling_NSK_Course

      \mathcal{W}_{CS}(\rho)=\rho RT\left[\frac{3-b\rho/2}{(1-b\rho/4)^{2}}+\ln(b\rho/4)\right]-a\rho^{2}

   .. math::
      :label: ChemPot_Carnahan_Starling_NSK_Course

      \mu_{\rho}^{CS}=RT\left[\frac{3-b\rho/4}{(1-b\rho/4)^{3}}+\ln(b\rho/4)+1\right]-2a\rho-\kappa\boldsymbol{\nabla}^{2}\rho


In Eqs. :eq:`EoS_van_der_Waals_NSK_Course` and :eq:`EoS_Carnahan_Starling_NSK_Course`, the input parameters are :math:`a`, :math:`b` :math:`R` and :math:`T`.

Redlich-Kwong (RK)
""""""""""""""""""

.. math::
   :label: Redlich_Kwong_EoS_NSK_Course

   p_{RK}^{eos}(\rho,T)&=\frac{\rho RT}{1-b\rho}-\frac{a\alpha(T)\rho^{2}}{1+b\rho}\\\alpha(T)&=1/\sqrt{T}\\\text{Soave modif }\alpha(T)&=[1+(\alpha_{1}+\alpha_{2}\omega-\alpha_{3}\omega^{2})(1-\sqrt{T/T_{c}})]^{2}\\\text{coeff}&\alpha_{1}=0.480,\quad\alpha_{2}=1.574,\quad\alpha_{3}=0.176

Peng-Robinson (PR)
""""""""""""""""""

.. math::
   :label: Peng_Robinson_EoS_NSK_Course

   p_{PR}^{eos}(\rho,T)&=\frac{\rho RT}{1-b\rho}-\frac{a\alpha(T)\rho^{2}}{1+2b\rho-b^{2}\rho^{2}}\\\alpha(T)&=[1+(\alpha_{1}+\alpha_{2}\omega+\alpha_{3}\omega^{2})(1-\sqrt{T/T_{c}})]^{2}\\\text{coeff}&\alpha_{1}=0.37464,\quad\alpha_{2}=1.54226,\quad\alpha_{3}=0.26992

Bibliography
------------

.. [1] van der Waals J.D., The thermodynamic theory of capillarity under the hypothesis of a continuous variation of density. Translation of "The Thermodynamic Theory of Capillarity" by J.S. Rowlinson. Journal of Statistical Physics, Vol. 20, No. 2, 1979.

.. [2] Korteweg D.J., Sur la forme que prennent les équations du mouvement des fluides si l'on tient compte des forces capillaires causées par des variations de densités considérables mais continues et sur la théorie de la capillarité dans l'hypothèse d'une variation continue de la densité. Archives Néerlandaises, Série II, Tome VI. 1901.

.. [3] Anderson D.M., G.B. McFadden, A.A. Wheeler, Diffuse-interface methods in fluid mechanics, Annu. Rev. Fluid Mech. 1998. 30:139–65.

.. [4] Goldstein H., Classical mechanics, 2nd Edition, Addison Wesley, 1981.

.. [5] Liu J., C.M. Landis, H. Gomez, T.J.R. Hughes, Liquid–vapor phase transition: Thermomechanical theory, entropy stable numerical formulation, and boiling simulations. Comput. Methods Appl. Mech. Engrg. 297 (2015) 476–553, http://dx.doi.org/10.1016/j.cma.2015.09.007

.. [6] Bueno J., H. Gomez, Liquid-vapor transformations with surfactants. Phase-field model and Isogeometric Analysis. Journal of Computational Physics 321 (2016) 797–818, http://dx.doi.org/10.1016/j.jcp.2016.06.008

.. sectionauthor:: Alain Cartalade
   