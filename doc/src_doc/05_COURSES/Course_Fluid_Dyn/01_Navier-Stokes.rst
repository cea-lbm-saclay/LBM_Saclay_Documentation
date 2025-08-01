.. _Reminder-Navier-Stokes:

Navier-Stokes equations for single-phase flows
==============================================

This section is a summary of [1]_ (section V.2 p. 88, section V.4 p. 92 and appendix p. 112) and reminds the derivation of Navier-Stokes (NS) equations for single phase flows. Among several forms that exist, we only write here the **local conservative form** of NS equations.

Mass balance
------------

We consider a volume of fluid :math:`V`. The total mass contained in that volume is:

.. math::
   :label: eq:Total-Mass-NS-Course
   
   m=\int_{V}\rho dV

where :math:`\rho` is the local density. Without source (or well) term the total mass is constant and

.. math::
   :label: eq:Variation-m-NS-Course
   
   \frac{d}{dt}m=\frac{d}{dt}\int_{V}\rho dV=0

We apply the Reynolds’ transport theorem:

.. math::
   :label: eq:Reynolds-Theorem
   
   \frac{d}{dt}\int_{V}\rho dV=\int_{V}\frac{\partial\rho}{\partial t}dV+\int_{A}\rho\boldsymbol{u}\cdot\boldsymbol{n}dA

so that:

.. math::
   :label: eq:After-Reynolds-Theorem
   
   \int_{V}\frac{\partial\rho}{\partial t}dV+\int_{A}\rho\boldsymbol{u}\cdot\boldsymbol{n}dA=0

With Green-Ostrogradsky’s theorem, the surfacic integral can be
transformed into volumic one:

.. math::
   :label:
   
   \int_{A}\rho\boldsymbol{u}\cdot\boldsymbol{n}dA=\int_{V}\boldsymbol{\nabla}\cdot(\rho\boldsymbol{u})dV

Eq. :eq:`eq:After-Reynolds-Theorem`

.. math::
   
   \int_{V}\left[\frac{\partial\rho}{\partial t}+\boldsymbol{\nabla}\cdot(\rho\boldsymbol{u})\right]dV=0

The volume of integration is arbitrary and consequently the integrand
must be zero:

.. math::
   :label: Final-Mass-Balance-NS-Course

   \boxed{\frac{\partial\rho}{\partial t}+\boldsymbol{\nabla}\cdot(\rho\boldsymbol{u})=0}

Impulsion balance
-----------------

The impulsion inside that volume is

.. math::
   :label: eq:Total-Impulsion-NS-Course

   \int_{V}\rho\boldsymbol{u}dV

The fundamental principle of dynamics says that the variation of
impulsion of that material system is equal to all external forces:

.. math::
   :label: eq:Principle-Of-Dynamics

   \frac{d}{dt}\int_{V}\rho\boldsymbol{u}dV=\boldsymbol{F}

Two kinds of forces act on fluid contained in that volume:

- Volumic forces

.. math::
   :label: eq:Volumic-Forces-NS-Course

   \int_{V}\rho\boldsymbol{g}dV

- Surfacic forces:

.. math::
   :label: eq:Surfacic-Forces-NS-Course
   
   \int_{A}\boldsymbol{t}(\boldsymbol{n})dA

where :math:`\boldsymbol{t}(\boldsymbol{n})` is the stress vector acting
on :math:`dA` of normal :math:`\boldsymbol{n}`.

.. math::
   :label: eq:PoD-With-V-S-Forces-NS-Course
   
   \frac{d}{dt}\int_{V}\rho\boldsymbol{u}dV=\int_{V}\rho\boldsymbol{g}dV+\int_{A}\boldsymbol{t}(\boldsymbol{n})dA

The stress vector :math:`\boldsymbol{t}(\boldsymbol{n})` can be
expressed with the symmetric stress tensor
:math:`\overline{\overline{\boldsymbol{T}}}`:

.. math::
   :label: eq:Stress-Tensor-NS-Course
   
   \boldsymbol{t}(\boldsymbol{n})=\overline{\overline{\boldsymbol{T}}}\cdot\boldsymbol{n}

and the stress tensor is decomposed into a stress due to pressure and
another one due to viscous strain. The first one is isotropic and its
value depends only on the thermodynamic state of fluid whereas the second one, the viscous stress,
is related to the fluid strain and we can write:

.. math::
   :label: eq:Decomposition-Stress-Tensor-NS-Course
   
   \underbrace{\overline{\overline{\boldsymbol{T}}}}_{\text{Stress tensor}}=\underbrace{-p^{eos}\overline{\overline{\boldsymbol{I}}}}_{\text{Pressure stress tensor}}+\underbrace{\overline{\overline{\boldsymbol{\tau}}}}_{\text{Viscous stress tensor}}

where :math:`p^{eos}` is the thermodynamic pressure which must be given by an Equation of State (eos). For simple fluids, the law of perfect gas (or ideal gas) hold:

.. math::
   :label: EoS_Perfect-Gases

   \boxed{p^{eos}_{pg}(\rho,T)=\rho RT}

where :math:`R`` is the gas constant and :math:`T` is the temperature. Expressed with components, that tensor writes:

.. math::

   \left(\begin{array}{ccc}
   T_{_{xx}} & T_{xy} & T_{xz}\\
   T_{yx} & T_{yy} & T_{yz}\\
   T_{zx} & T_{zy} & T_{zz}
   \end{array}\right)=\left(\begin{array}{ccc}
   -p^{eos} & 0 & 0\\
   0 & -p^{eos} & 0\\
   0 & 0 & -p^{eos}
   \end{array}\right)+\left(\begin{array}{ccc}
   \tau_{_{xx}} & \tau_{xy} & \tau_{xz}\\
   \tau_{yx} & \tau_{yy} & \tau_{yz}\\
   \tau_{zx} & \tau_{zy} & \tau_{zz}
   \end{array}\right)

With Eqs. :eq:`eq:Stress-Tensor-NS-Course` and :eq:`eq:Decomposition-Stress-Tensor-NS-Course`,
Eq. :eq:`eq:PoD-With-V-S-Forces-NS-Course` becomes

.. math::
   
   \frac{d}{dt}\int_{V}\rho\boldsymbol{u}dV=\int_{V}\rho\boldsymbol{g}dV+\int_{A}(-p\overline{\overline{\boldsymbol{I}}}+\overline{\overline{\boldsymbol{\tau}}})\cdot\boldsymbol{n}dA

the surfacic integral is changed into volumic integral with
Green-Ostrogradsky theorem:

.. math::
   :label: 
   
   \frac{d}{dt}\int_{V}\rho\boldsymbol{u}dV=\int_{V}\rho\boldsymbol{g}dV+\int_{V}-\boldsymbol{\nabla}\cdot(p\overline{\overline{\boldsymbol{I}}}+\overline{\overline{\boldsymbol{\tau}}})dV

For the left-hand side, we use the Reynolds’ transport theorem:

.. math::

   \begin{aligned}
   \frac{d}{dt}\int_{V}\rho\boldsymbol{u}dV & =\int_{V}\frac{\partial(\rho\boldsymbol{u})}{\partial t}dV+\int_{A}\rho\boldsymbol{u}(\boldsymbol{u}\cdot\boldsymbol{n})dA\\
    & =\int_{V}\left[\frac{\partial(\rho\boldsymbol{u})}{\partial t}+\boldsymbol{\nabla}\cdot(\rho\boldsymbol{u}\boldsymbol{u})\right]dV\end{aligned}

where, once again the Green-Ostrograski’s theorem has been used for
surfacic integral. Finally:

.. math::
   :label: NS-Without-Stress-Tensor
   
   \frac{\partial(\rho\boldsymbol{u})}{\partial t}+\boldsymbol{\nabla}\cdot(\rho\boldsymbol{u}\boldsymbol{u})=-\boldsymbol{\nabla}p^{eos}+\boldsymbol{\nabla}\cdot\overline{\overline{\boldsymbol{\tau}}}+\rho\boldsymbol{g}

Constitutive relation: viscous stress tensor for Newtonian fluids
-----------------------------------------------------------------

The viscous stress tensor is usually expressed as a function of strain rate. For newtonian fluids, the viscous stress tensor writes:

.. math::
   :label: Newtonian-Law-NS-Course

   \overline{\overline{\boldsymbol{\tau}}}=2\eta\overline{\overline{\boldsymbol{D}}}+(\eta_{B}-\frac{2}{3}\eta)(\boldsymbol{\nabla}\cdot\boldsymbol{u})\overline{\overline{\boldsymbol{I}}}

where :math:`\eta` is the dynamic viscosity, :math:`\eta_B` is
the bulk viscosity and :math:`\overline{\overline{\boldsymbol{D}}}` is the symmetric part of velocity gradient:

with

.. math:: \overline{\overline{\boldsymbol{D}}}=\frac{1}{2}(\boldsymbol{\nabla}\boldsymbol{u}+\boldsymbol{\nabla}\boldsymbol{u}^{T})

In most of applications, we consider :math:`\eta_{B}=0` (Stokes' hypothesis) and finally:

.. math::
   :label: Viscous-Stress-Tensor-Newtonian-NS-Course

   \overline{\overline{\boldsymbol{\tau}}}=\eta(\boldsymbol{\nabla}\boldsymbol{u}+\boldsymbol{\nabla}\boldsymbol{u}^{T})-\frac{2}{3}\eta(\boldsymbol{\nabla}\cdot\boldsymbol{u})\overline{\overline{\boldsymbol{I}}}

We replace the viscous stress tensor expressed by Eq. :eq:`Viscous-Stress-Tensor-Newtonian-NS-Course` in Eq. :eq:`NS-Without-Stress-Tensor` and we finally obtain

.. math::
   :label: Final_Impulsion-Balance-NS-Course

   \boxed{\frac{\partial(\rho\boldsymbol{u})}{\partial t}+\boldsymbol{\nabla}\cdot(\rho\boldsymbol{u}\boldsymbol{u})=-\boldsymbol{\nabla}p^{eos}+\boldsymbol{\nabla}\cdot\eta\left[(\boldsymbol{\nabla}\boldsymbol{u}+\boldsymbol{\nabla}\boldsymbol{u}^{T})-\frac{2}{3}(\boldsymbol{\nabla}\cdot\boldsymbol{u})\overline{\overline{\boldsymbol{I}}}\right]+\rho\boldsymbol{g}}

.. admonition:: Summary
   :class: error

   The low-Mach Navier-Stokes equations are composed of one equation of mass conservation

   .. math::
      :label: Mass-Balance-Summary-NS-Course

      \frac{\partial\rho}{\partial t}+\boldsymbol{\nabla}\cdot(\rho\boldsymbol{u})=0

   plus one equation of impulsion balance

   .. math::
      :label: Impusion-Balance-Summary-NS-Course

      \frac{\partial(\rho\boldsymbol{u})}{\partial t}+\boldsymbol{\nabla}\cdot(\rho\boldsymbol{u}\boldsymbol{u})=-\boldsymbol{\nabla}p^{eos}(\rho,T)+\boldsymbol{\nabla}\cdot\eta\left[(\boldsymbol{\nabla}\boldsymbol{u}+\boldsymbol{\nabla}\boldsymbol{u}^{T})-\frac{2}{3}(\boldsymbol{\nabla}\cdot\boldsymbol{u})\overline{\overline{\boldsymbol{I}}}\right]+\rho\boldsymbol{g}

   with the equation of state

   .. math::
      :label: EoS_Perfect-Gases_Summary_NS-Course

      p^{eos}_{pg}(\rho,T)=\rho RT

   The temperature :math:`T` is computed by an additional equation (heat equation). The dynamic viscosity :math:`\eta` is related to the kinematic viscosity :math:`\nu` by:

   .. math::
      :label: Def_Dynamic-Kinematic_Viscosity

      \eta=\rho \nu

Index notations
---------------

For chapman-Enskog expansions, the algebraic calculations are performed with index notations with Einstein's convention of summation.

.. math::
   :label: Def_Index_Notations_NS-Course

   \partial_{t}:=\frac{\partial}{\partial t}

.. math::
   :label:

   \begin{eqnarray}
   \partial_{\alpha}(\rho u_{\alpha}) & := & \partial_{x}(\rho u_{x})+\partial_{y}(\rho u_{y})+\partial_{z}(\rho u_{z})\\
   & := & \boldsymbol{\nabla}\cdot(\rho\boldsymbol{u})
   \end{eqnarray}

.. math::
   :label: Mass-Balance-Eq-Index_NS-Course

   \partial_{t}\rho+\partial_{\alpha}(\rho u_{\alpha})=0

.. math::
   :label: Impulsion-Balance-Eq-Index_NS-Course

   \partial_{t}(\rho u_{\alpha})+\partial_{\beta}(\rho u_{\alpha}u_{\beta})=\partial_{\alpha}p+\partial_{\beta}\tau_{\alpha\beta}+\rho g_{\alpha}

With the viscous stress tensor defined by

.. math::
   :label: Viscous-Stress-Index_NS-Course

   \tau_{\alpha\beta}=\eta\left[\partial_{\alpha}u_{\beta}+\partial_{\beta}u_{\alpha}-\frac{2}{3}\partial_{\gamma}u_{\gamma}\delta_{\alpha\beta}\right]

the impulsion balance equation writes

.. math::
   :label: Impulsion-Balance-Eq-with-Stress-Index_NS-Course

   \partial_{t}(\rho u_{\alpha})+\partial_{\beta}(\rho u_{\alpha}u_{\beta})=\partial_{\alpha}p+\partial_{\beta}\left\{ \eta\left[\partial_{\alpha}u_{\beta}+\partial_{\beta}u_{\alpha}-\frac{2}{3}\partial_{\gamma}u_{\gamma}\delta_{\alpha\beta}\right]\right\} +\rho g_{\alpha}

Bibliography
------------

.. [1] Candel S., Mécanique des fluides, 2e édition, Dunod, 2001.
