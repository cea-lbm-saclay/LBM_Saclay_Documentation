.. _CH-CAC-Models:

Time-evolution: Cahn-Hilliard and Allen-Cahn models
===================================================

In the previous section :ref:`Free-Energy-Double-Wells` we have derived the equilibrium properties (in space) by postulating the principle of stationarity of one specific thermodynamic potential, the free energy :math:`\mathscr{F}[\phi]`. That principle has lead to the Euler-Lagrange equation and its fundamental solution with a hyperbolic tangent profile. The diffuse interface was characterized by two parameters: the interface width :math:`W` and the surface tension :math:`\sigma`.

In this section, we focus on the **dynamics**, i.e. the time-evolution of the phase-field :math:`\phi`. Two cases are considered: when the phase-field is a conservative order parameter and when it is not. In both cases, the spatial part must follow the stationary principle of the previous section. When the order parameter is a conserved quantity then we get the **Cahn-Hilliard model**. When the order parameter is not a conserved quantity, then we get the **Allen-Cahn** model which will be extended for **Conservative Allen-Cahn model**.

.. _CH-Model:

Cahn-Hilliard (CH) model for conservative order parameter
---------------------------------------------------------

The Cahn-Hilliard equation is a very popular model which is capable of simulating spinodal decomposition, coalescence of droplets, and so on. That model is derived for an order parameter which is conserved over the whole computational domain. The phase-field :math:`\phi(\boldsymbol{x},t)` plays two roles: it tracks the interface and indicates the local value of composition. This is the reason why in the literature, the Cahn-Hilliard equation is alternatively formulated in :math:`c(\boldsymbol{x},t)`. Here for consistency, we present the equation with the main variable :math:`\phi`.

The Cahn-Hilliard model is simply an equation of conservation (mass balance):

.. math::
   :label: Conservation_Cahn-Hilliard_Course

   \frac{\partial\phi(\boldsymbol{x},t)}{\partial t}=-\boldsymbol{\nabla}\cdot\boldsymbol{j}_{diff}(\boldsymbol{x},t)

where the diffusive flux :math:`\boldsymbol{j}_{diff}` must be defined such as the free energy decreases with time i.e.:

.. math::
   :label:

   \frac{\partial\mathscr{F}[\phi]}{\partial t} < 0

**Expression of diffusive flux**

With the definition of free energy Eq. :eq:`Free_Energy`:

.. math::
   :label:

   \begin{eqnarray}
      \frac{\partial \mathscr{F}}{\partial t} & = & \frac{\partial}{\partial t}\int_{V}\mathcal{F}(\phi,\boldsymbol{\nabla}\phi)dV\\
      & = & \int_{V} \left[\frac{\delta \mathcal{F}}{\delta \phi}\frac{\partial \phi}{\partial t} \right]dV\\
      & = & \int_V \frac{\delta \mathcal{F}}{\delta \phi}(-\boldsymbol{\nabla}\cdot\boldsymbol{j}_{diff}(\boldsymbol{x},t))
   \end{eqnarray}

where the chain rule was applied for the second line and the conservation equation Eq. :eq:`Conservation_Cahn-Hilliard_Course` for the third line. The simplest choice to define the flux is to consider it proportional to the gradient of :math:`\delta \mathcal{F}/\delta \phi`:

.. math::
   :label: Diffusive_Flux_CH_Course

   \boldsymbol{j}_{diff}(\boldsymbol{x},t)=-\mathcal{M}_{\phi}\boldsymbol{\nabla}\left( \frac{\delta \mathcal{F}}{\delta \phi} \right)

because:

.. math::
   :label:

   \begin{eqnarray}
      \frac{\partial\mathscr{F}}{\partial t}	& = & \int_{V}\frac{\delta\mathcal{F}}{\delta\phi}(-\boldsymbol{\nabla}\cdot\boldsymbol{j}_{diff})dV\\
	   & = & \int_{V}\frac{\delta\mathcal{F}}{\delta\phi}\left[\boldsymbol{\nabla}\cdot\mathcal{M}_{\phi}\boldsymbol{\nabla}\left(\frac{\delta\mathcal{F}}{\delta\phi}\right)\right]dV\\
	   & = & \mathcal{M}_{\phi}\int_{V}\frac{\delta\mathcal{F}}{\delta\phi}\left[\boldsymbol{\nabla}^{2}\left(\frac{\delta\mathcal{F}}{\delta\phi}\right)\right]dV
   \end{eqnarray}

After an integration by parts

.. math::
   :label:

   \frac{\partial\mathscr{F}}{\partial t}=-\mathcal{M}_{\phi}\int_{V}\left[\boldsymbol{\nabla}\left(\frac{\delta\mathcal{F}}{\delta\phi}\right)\right]^{2}dV

which is necessarily negative if :math:`\mathcal{M}_{\phi}` is positive. The quantity :math:`\delta \mathcal{F}/\delta \phi` is the chemical potential :math:`\mu_{\phi}`. Finally, the diffusive flux defined by

.. math::
   :label: Diffusive_Flux_CH_PotChem_Course

   \boxed{\boldsymbol{j}_{diff}(\boldsymbol{x},t)=-\mathcal{M}_{\phi}\boldsymbol{\nabla}\mu_{\phi}}

is sufficient to ensure a decrease of free energy. The minus sign indicates that the flux is directed from the high values of :math:`\mu_{\phi}` to the small ones. The coefficient of proportionality :math:`\mathcal{M}_{\phi}` plays an identical role as the diffusion coefficient. It is called the mobility coefficient.

By replacing Eq. :eq:`Diffusive_Flux_CH_PotChem_Course` in Eq. :eq:`Conservation_Cahn-Hilliard_Course` we obtain

.. math::
   :label: CH_Expressed_Mobility

   \boxed{\frac{\partial\phi(\boldsymbol{x},t)}{\partial t}=\boldsymbol{\nabla}\cdot\left[\mathcal{M}_{\phi}\boldsymbol{\nabla}\mu_{\phi}(\boldsymbol{x},t)  \right]}

The chemical potential :math:`\mu_{\phi}` is obtained from the Euler-Lagrange equation :math:`\mu_{\phi}=\delta \mathcal{F}/\delta \phi`. If we define the free energy density :math:`\mathcal{F}(\phi,\boldsymbol{\nabla}\phi)` equal to (see :ref:`Free-Energy-Double-Wells`):

.. math::
   :label: DP_CH_Course

   \mathcal{F}(\phi,\boldsymbol{\nabla}\phi)=H\phi^{2}(1-\phi)^{2}+\frac{\zeta}{2}(\boldsymbol{\nabla}\phi)^{2}

then, the chemical potential writes:

.. math::
   :label: Chemical_Potential_CH_Course

   \mu_{\phi}=\underbrace{2H\phi(1-\phi)(1-2\phi)}_{f_{dw}^{\prime}(\phi)}-\zeta\boldsymbol{\nabla}^{2}\phi

**Mobility and diffusivity**

We have seen that the physical dimension of :math:`\mu_{\phi}` is :math:`[\text{E}]/[\text{L}]^3` meaning that the physical dimension of :math:`\mathcal{M}_{\phi}` is :math:`[\text{L}]^5/[\text{E.T}]`. It is possible to make appear a diffusivity coefficient :math:`M_{\phi}` of dimension :math:`[\text{L}]^2/[\text{T}]`. By replacing Eq. :eq:`Chemical_Potential_CH_Course` in Eq. :eq:`CH_Expressed_Mobility` and by defining

.. math::
   :label: Def_Diffusivity_CH

   M_{\phi}=H\mathcal{M}_{\phi}

We obtain:

.. math::
   :label: CH_Expressed_Diffusivity

   \frac{\partial\phi(\boldsymbol{x},t)}{\partial t}=\boldsymbol{\nabla}\cdot\left\{M_{\phi}\boldsymbol{\nabla}\left[2\phi(1-\phi)(1-2\phi)-\frac{W^2}{8}\boldsymbol{\nabla}^{2}\phi  \right]\right\}

For coupling with fluid flow of velocity :math:`\boldsymbol{u}`, the advective flux :math:`\boldsymbol{j}_{adv}=\boldsymbol{u}\phi` must be considered. In that case, the conservation involves the total flux :math:`\boldsymbol{j}_{tot}=\boldsymbol{j}_{adv}+\boldsymbol{j}_{diff}` and the advective Cahn-Hilliard model writes:

.. math::
   :label: Adv_CH_Model_Course
   \frac{\partial\phi}{\partial t}+\boldsymbol{\nabla}\cdot(\boldsymbol{u}\phi)=\mathcal{M}_{\phi}\boldsymbol{\nabla}^{2}\mu_{\phi}

.. admonition:: Summary: Advective Cahn-Hilliard model for conserved order parameter
   :class: error

   Finally, for the simplest form of free energy density, the advective Cahn-Hilliard model writes:

   .. math::
      :label: Adv_CH_Model_Course_Summary

      \frac{\partial\phi(\boldsymbol{x},t)}{\partial t}+\boldsymbol{\nabla}\cdot(\boldsymbol{u}\phi)=\boldsymbol{\nabla}\cdot\left\{M_{\phi}\boldsymbol{\nabla}\left[2\phi(1-\phi)(1-2\phi)-\frac{W^2}{8}\boldsymbol{\nabla}^{2}\phi  \right]\right\}

   The Cahn-Hilliard model is powerful model which is capable of simulating interface phenomena and particularly  *spinodal decomposition*. However, it is a particular model in the sense that the phase-field :math:`\phi` plays two roles: first it tracks the interface and second it gives the local value of compositions. More specifically, the compositions values of bulk phases cannot be freely chosen equal to 0 and 1. They must be equal to :math:`c_0^{eq}` and :math:`c_1^{eq}` where those two values come from the thermodynamic. Another difficulty lays in the bilaplacian and specific numerical methods are needed to tackle that fourth-order derivative.

.. _AC-Model_Course:

Allen-Cahn model for non-conservative order parameter
-----------------------------------------------------

For non-conservative order parameter

.. math::
   :label: Non-Conservation-AC_Course

   \frac{\partial \phi}{\partial t}=S

where :math:`S` is a source term to be defined such as the free energy decreases:

.. math::
   :label:

   \frac{\partial\mathscr{F}[\phi]}{\partial t} < 0

With the definition of free energy Eq. :eq:`Free_Energy`:

.. math::
   :label:

   \begin{eqnarray}
      \frac{\partial \mathscr{F}}{\partial t} & = & \frac{\partial}{\partial t}\int_{V}\mathcal{F}(\phi,\boldsymbol{\nabla}\phi)dV\\
      & = & \int_{V} \left[\frac{\delta \mathcal{F}}{\delta \phi}\frac{\partial \phi}{\partial t} \right]dV\\
      & = & \int_V \frac{\delta \mathcal{F}}{\delta \phi}SdV
   \end{eqnarray}

where the chain rule was applied for the second line and the non-conservation equation Eq. :eq:`Non-Conservation-AC_Course` for the third line. The simplest choice to define the source term is to consider it proportional to :math:`\delta \mathcal{F}/\delta \phi`:

.. math::
   :label:

   S=-\mathscr{M}_{\phi}\frac{\delta \mathcal{F}}{\delta \phi}

so that

.. math::
   :label:

   \frac{\partial \mathscr{F}}{\partial t}=-\mathscr{M}_{\phi} \int_V \left[ \frac{\delta \mathcal{F}}{\delta \phi}\right]^2dV

which is necessarily negative if :math:`\mathscr{M}_{\phi}` is positive.

The Allen-Cahn model acts for non-conservative order parameter. Problems of phase change give an example of such a non-conservative phase-field because its integrations over the whole domain yield different values at the starting time and final time of simulation. In that case, the evolution of interface obeys simply to

.. math::
   :label: Allen_Cahn_Course

   \boxed{\frac{\partial\phi}{\partial t}=-\mathscr{M}_{\phi}\mu_{\phi}}

where, once again, the chemical potential is defined by :math:`\mu_{\phi}=\delta \mathcal{F}/\delta \phi`:

.. math::
   :label: Chem_Pot_AC_Course

   \boxed{\mu_{\phi}=2H\phi(1-\phi)(1-2\phi)-\zeta\boldsymbol{\nabla}^{2}\phi}

and :math:`\mathscr{M}_{\phi}` is a positive coefficient of proportionality. As seen in :ref:`Free-Energy-Double-Wells`, the physical dimension of :math:`\mu_{\phi}` is :math:`[\text{E}]/[\text{L}]^3`. Hence, the physical dimension of :math:`\mathscr{M}_{\phi}` is :math:`[\text{L}]^3/[\text{E}].[\text{T}]`.

.. admonition:: Important
   :class: Important

   The Allen-Cahn equation has a physical meaning only if it is coupled to a heat PDE (Eq. on :math:`T`) or a composition PDE (Eq. on :math:`c`) because the temperature (or composition) is responsible for the phase change, and consequently the displacement of interface. For those problems, the free energy must depend on that new variable (:math:`T` or :math:`c`) :math:`\mathscr{F}[\phi,T]`. A new free energy density must also be added in the definition of the free energy functional to take into account that coupling between :math:`\phi` and :math:`T` (or :math:`c`). That coupling makes appear a source term in Eq. :eq:`Allen_Cahn_Course`. Examples of derivation of such phase-field models are presented in :ref:`Phase-Field-Phase-Change`.

.. _CAC-Model:

Conservative Allen-Cahn (CAC) model
-----------------------------------

The advective Cahn-Hilliard model is a very popular model to track an interface for a conserved quantity. However, as already mentioned, it presents two difficulties: the two roles played by the phase-field (interface position and composition) and its fourth-order derivative. In particular, for phase change problems involving composition, the composition must follow its own PDE whereas the interface position must obey to the Allen-Cahn model with a source term.

In order to capture the interface between two immiscible fluids, without phase change, a new phase-field equation of second-order derivative is derived. Without phase change, the two immiscible fluids are conserved. To design such an equation, we assume that the phase-field :math:`\phi` is a conservative order parameter which obeys to

.. math::
   :label: Mass_Balance_CAC_Course

   \partial_{t}\phi=-\nabla\cdot\boldsymbol{j}_{tot}

where the total flux :math:`\boldsymbol{j}_{tot}` is the sum of three contributions. The first two are standard.The first one is the diffusive flux 

.. math::
   :label: Diff_Flux_CAC_Course

   \boldsymbol{j}_{diff}=-M_{\phi}\boldsymbol{\nabla}\phi

where :math:`M_{\phi}` is a positive coefficient characterizing the mobility of the interface. Its physical dimension is :math:`[\text{L}]^2/[\text{T}]`. The second one is the advective flux

.. math::
   :label: Adv_Flux_CAC_Course

   \boldsymbol{j}_{adv}=\boldsymbol{u}\phi

where :math:`\boldsymbol{u}` is the velocity fluid calculated by the Navier-Stokes equations. The last one :math:`\boldsymbol{j}_{CT}`, where :math:`CT` means "Counter Term", is designed such as at equilibrium, :math:`\boldsymbol{j}_{CT}` cancels the diffusive flux :math:`\boldsymbol{j}_{diff}=-M_{\phi}\boldsymbol{\nabla}\phi`. When the steady state is reached and at equilibrium, the profile of :math:`\phi` must be the fundamental solution of Euler-Lagrange equation :math:`\phi^{eq}` given by Eq. :eq:`Hyperbolic_Tangent_Solution_Course`. We can calculate the equilibrium diffusive flux:

.. math::
   :label: Diff_Flux_Equilibrium_Course

   \begin{eqnarray}
      \boldsymbol{j}_{diff}^{eq} & = & -M_{\phi}\boldsymbol{\nabla}\phi^{eq}\\
      & = & -M_{\phi}\boldsymbol{\nabla}\left[\frac{1}{2}\left(1+\text{tanh}\left(\frac{2s}{W}\right)\right)\right]\\
      & = & -M_{\phi}\boldsymbol{n}_{\phi}\frac{\partial}{\partial s}\left[\frac{1}{2}\left(1+\text{tanh}\left(\frac{2s}{W}\right)\right)\right]\\
      & = & -M_{\phi}\frac{4}{W}\phi^{eq}(1-\phi^{eq})\boldsymbol{n}_{\phi}
   \end{eqnarray}

where :math:`s` is the normal coordinate at the interface and :math:`\boldsymbol{n}_{\phi}` is the normal vector of interface defined by :math:`\boldsymbol{n}_{\phi}=\boldsymbol{\nabla}\phi/|\boldsymbol{\nabla}\phi|`. Finally the counter term flux :math:`\boldsymbol{j}_{CT}` is defined such as it cancels at equilibrium the diffusive flux, i.e. it must be equal and opposite to :math:`\boldsymbol{j}_{diff}^{eq}`:

.. math::
   :label: Counter_Term_Flux_Course

   \boldsymbol{j}_{CT}=+M_{\phi}\frac{4}{W}\phi(1-\phi)\boldsymbol{n}_{\phi}

.. admonition:: Summary of Conservative Allen-Cahn
   :class: error

   The Conservative Allen-Cahn (CAC) model is a conservative PDE of second-order which captures a diffuse interface between two immiscible fluids:

   .. math::
      :label: CAC_Course

      \frac{\partial\phi}{\partial t}+\boldsymbol{\nabla}\cdot(\boldsymbol{u}\phi)=\boldsymbol{\nabla}\cdot\left[M_{\phi}\left(\boldsymbol{\nabla}\phi-\frac{4}{W}\phi(1-\phi)\boldsymbol{n}_{\phi}\right)\right]

   The interface position is given by :math:`\phi`, :math:`\boldsymbol{u}` is the fluid velocity and :math:`\boldsymbol{n}_{\phi}=\boldsymbol{\nabla}\phi/|\boldsymbol{\nabla}\phi|` is the unit normal vector at the interface. That model involves two additional parameters representative of the diffuse interface: the interface mobility :math:`M_{\phi}`, homogeneous to a diffusion coefficient :math:`[\text{L}]^2/[\text{T}]`, and the interface width :math:`W` of dimension :math:`[\text{L}]`.

**Interpretation of Counter Term**

Another way to derive the CAC model is to start from Allen-Cahn equation :eq:`Allen_Cahn_Course` with :eq:`Chem_Pot_AC_Course`

.. math::
   :label:

   \begin{eqnarray}
      \frac{\partial\phi}{\partial t}& = & -\mathscr{M}_{\phi}[2H\phi(1-\phi)(1-2\phi)-\zeta\boldsymbol{\nabla}^{2}\phi]\\
      & = & -\mathscr{M}_{\phi}\zeta[2\frac{H}{\zeta}\phi(1-\phi)(1-2\phi)-\boldsymbol{\nabla}^{2}\phi]\\
      & = & -\mathscr{M}_{\phi}\zeta[\frac{16}{W^2}\phi(1-\phi)(1-2\phi)-\boldsymbol{\nabla}^{2}\phi]
   \end{eqnarray}

where :math:`\zeta` is put in factor for the second line and the equivalence :math:`H/\zeta=8/W^2` has been used (see ration of Eqs. :eq:`Def_H_Course` and :eq:`Def_zeta_Course` in :ref:`Free-Energy-Double-Wells`) for the third line. The product :math:`\mathscr{M}_{\phi}\zeta` is homogeneous to a diffusivity coefficient because :math:`[\mathscr{M}_{\phi}]=[\text{L}]^3/[\text{E}].[\text{T}]` and :math:`[\zeta]=[\text{E}]/[\text{L}]`. So, we define a new coefficient :math:`M_{\phi}=\mathscr{M}_{\phi}\zeta` wich is homogeneous to :math:`[M_{\phi}]=[\text{L}]/[\text{T}]`.

.. math::
   :label:

   \frac{\partial\phi}{\partial t}=M_{\phi}\left[\boldsymbol{\nabla}^{2}\phi-\frac{16}{W^2}\phi(1-\phi)(1-2\phi)\right]

The term inside the bracket is interpreted as a movement of interface due to the curvature. Indeed, we can prove that

.. math::
   :label: Equiv_Derivative_Curvature

   \begin{eqnarray}
      \kappa\left|\boldsymbol{\nabla}\phi\right| & = & (\boldsymbol{\nabla}\cdot\boldsymbol{n})\left|\boldsymbol{\nabla}\phi\right|\\
      & = & \boldsymbol{\nabla}\cdot(\left|\boldsymbol{\nabla}\phi\right|\boldsymbol{n})-\boldsymbol{n}\cdot\boldsymbol{\nabla}\left|\boldsymbol{\nabla}\phi\right|\\
      & = & \boldsymbol{\nabla}\cdot\left(\cancel{\left|\boldsymbol{\nabla}\phi\right|}\frac{\boldsymbol{\nabla}\phi}{\cancel{\left|\boldsymbol{\nabla}\phi\right|}}\right)-\boldsymbol{n}\cdot\boldsymbol{\nabla}\left|\boldsymbol{\nabla}\phi\right|\\
      & = & \boldsymbol{\nabla}^{2}\phi-\frac{16}{W^{2}}\phi(1-\phi)(1-2\phi)
   \end{eqnarray}


At this stage, in order to cancel curvature-driven motion of interface, an additional term, the counter term :math:`-M_{\phi}\kappa|\boldsymbol{\nabla}\phi|` is added in the right-hand side of that equation:

.. math::

   \frac{\partial\phi}{\partial t}=M_{\phi}\left[\boldsymbol{\nabla}^{2}\phi-\frac{16}{W^2}\phi(1-\phi)(1-2\phi)\right]-M_{\phi}\kappa|\boldsymbol{\nabla}\phi|

.. math::

   \begin{eqnarray}
      \frac{\partial\phi}{\partial t} & = & M_{\phi}\Bigl[\boldsymbol{\nabla}^{2}\phi-\boldsymbol{n}_{\phi}\cdot\boldsymbol{\nabla}\left|\boldsymbol{\nabla}\phi\right|-\left|\boldsymbol{\nabla}\phi\right|\boldsymbol{\nabla}\cdot\boldsymbol{n}_{\phi}\Bigr]\\
      & = & M_{\phi}\Bigl[\boldsymbol{\nabla}^{2}\phi-\boldsymbol{\nabla}\cdot(\left|\boldsymbol{\nabla}\phi\right|\boldsymbol{n}_{\phi})\Bigr]
   \end{eqnarray}

where, for the second line we used Eq. :eq:`Grad_Kernel_Function_Scal_n` for the second term inside the brackets and Eq. :eq:`Def_Curvature_Course` for curvature :math:`\kappa`. For the third line the last two terms are gathered inside the divergence operator. Finally by using the kernel function we obtain the same Conservative Allen-Cahn model:

.. math::
   :label: CAC_2nd_Method_Course

   \frac{\partial\phi}{\partial t}+\boldsymbol{\nabla}\cdot(\boldsymbol{u}\phi)=\boldsymbol{\nabla}\cdot\left[M_{\phi}\left(\boldsymbol{\nabla}\phi-\frac{4}{W}\phi(1-\phi)\boldsymbol{n}_{\phi}\right)\right]

.. sectionauthor:: Alain Cartalade
   