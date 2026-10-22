.. _Fluid-Dynamics-Models:

Summary of basic models
-----------------------

The Mach number is defined by

.. math::
   :label: Def_Mach
   
   Ma=\frac{\bigl|\boldsymbol{u}\bigr|}{c_{s}}

where :math:`\boldsymbol{u}\equiv\boldsymbol{u}(\boldsymbol{x},t)` is the fluid velocity and :math:`c_{s}` is the sound speed. At 20°C the sound speed is 344 m/s (1240 km/h) in air and 1500 m/s (5400 km/h) in
water.

In the rest of this section, two popular models of Navier-Stokes equations are detailed for :math:`Ma\ll1`. The first one is the “low Mach model” and the second one is the incompressible model.

Low Mach Navier-Stokes
^^^^^^^^^^^^^^^^^^^^^^

.. math::
   :label: Mass_Balance

   \partial_{t}\rho+\boldsymbol{\nabla}\cdot(\rho\boldsymbol{u})=0

.. math::
   :label: Impulsion_Balance
   
   \partial_{t}(\rho\boldsymbol{u})+\boldsymbol{\nabla}\cdot(\rho\boldsymbol{u}\boldsymbol{u})=-\boldsymbol{\nabla}p+\boldsymbol{\nabla}\cdot\left[\eta(\boldsymbol{\nabla}\boldsymbol{u}+(\boldsymbol{\nabla}\boldsymbol{u})^{T})+\left(\eta_{B}-\frac{2}{3}\eta\right)(\boldsymbol{\nabla}\cdot\boldsymbol{u})\boldsymbol{I}\right]+\boldsymbol{F}

where :math:`\rho\equiv\rho(\boldsymbol{x},t)` is the fluid density, :math:`\boldsymbol{u}\equiv\boldsymbol{u}(\boldsymbol{x},t)` is the
fluid velocity, :math:`p\equiv p(\boldsymbol{x},t)` is the pressure, :math:`\eta=\rho\nu` is the dynamic viscosity and :math:`\nu` is the
kinematic viscosity, :math:`\eta_{B}` is the bulk viscosity and :math:`\boldsymbol{I}` is the identity tensor. In Eq.
:eq:`Impulsion_Balance`, :math:`\boldsymbol{F}` is the force term and for isothermal fluid, the system is closed by the Equation of State
(EoS)

.. math:: p=\rho RT_{0}

where :math:`T_{0}` is the constant temperature and :math:`R` is the specific gas constant.

Incompressible Navier-Stokes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. math::
   :label: Incompr_MB
   
   \boldsymbol{\nabla}\cdot\boldsymbol{u}=0


.. math::
   :label: Incompr_NS

   \rho_{0}\left[\partial_{t}\boldsymbol{u}+\boldsymbol{\nabla}\cdot(\boldsymbol{u}\boldsymbol{u})\right]=-\boldsymbol{\nabla}p_{h}+\boldsymbol{\nabla}\cdot\left[\rho_{0}\nu(\boldsymbol{\nabla}\boldsymbol{u}+(\boldsymbol{\nabla}\boldsymbol{u})^{T})\right]+\boldsymbol{F}

where :math:`p_{h}(\boldsymbol{x},t)` is the hydrodynamic pressure and :math:`\rho_{0}` is the constant density.


Advection-Diffusion equations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Levelset or phase-field equations**

.. math::
   :label: PF_Eq

   \frac{\partial\phi}{\partial t}+\boldsymbol{\nabla}\cdot(\boldsymbol{u}\phi)=\boldsymbol{\nabla}\cdot\left[M_{\phi}\left(\boldsymbol{\nabla}\phi-\frac{4}{W}\phi(1-\phi)\boldsymbol{n}\right)\right]

where the unknown is the phase-field :math:`\phi\equiv\phi(\boldsymbol{x},t)` and the inputs are the fluid velocity :math:`\boldsymbol{u}` and two parameters: the interface mobility :math:`M_{\phi}` and the interface width :math:`W`. The unit normal vector of interface is defined by

.. math::
   :label: Def_Normal
   
   \boldsymbol{n}\equiv\boldsymbol{n}(\boldsymbol{x},t)=\frac{\boldsymbol{\nabla}\phi}{\bigl|\boldsymbol{\nabla}\phi\bigr|}

**Advection-Diffusion Equation (ADE)**

.. math::
   :label: ADE

   C_{p}\frac{\partial T}{\partial t}+\boldsymbol{\nabla}\cdot(T\boldsymbol{u})=\boldsymbol{\nabla}\cdot(\kappa\boldsymbol{\nabla}T)+\mathscr{S}_{T}

where the unknown is the temperature :math:`T\equiv T(\boldsymbol{x},t)` and the inputs are the fluid velocity :math:`\boldsymbol{u}` and two parameters: the thermal conductivity :math:`\kappa` and the specific heat :math:`C_{p}`. A source term :math:`\mathscr{S}_{T}` can be defined for phase change problems.


Boundary Conditions (BC)
^^^^^^^^^^^^^^^^^^^^^^^^

**For Navier-Stokes equations**

Dirichlet BC

.. math:: \boldsymbol{u}(\boldsymbol{x}_{b},t)=\boldsymbol{U}_{b}(\boldsymbol{x}_{b},t)

.. math:: (\boldsymbol{u}-\boldsymbol{U}_{b})\cdot\boldsymbol{n}_{w}=0

.. math:: (\boldsymbol{u}-\boldsymbol{U}_{b})\cdot\boldsymbol{t}_{w}=0\qquad\text{(no-slip)}

where :math:`\boldsymbol{n}_{w}` is normal boundary vector and
:math:`\boldsymbol{t}_{w}` tangential boundary vector (:math:`w`: wall)

Neumann BC

.. math:: \boldsymbol{n}_{w}\cdot\boldsymbol{\sigma}(\boldsymbol{x}_{b},t)=\boldsymbol{T}_{b}(\boldsymbol{x}_{b},t)


**For ADE**

A generic formulation of bounday conditions for ADE writes:

.. math:: a_{1}\left.\frac{\partial f}{\partial n}\right|_{\boldsymbol{x}_{b},t}+a_{2}f(\boldsymbol{x}_{b},t)=a_{3}

where :math:`f` is the differentiable function (here :math:`\phi` or
:math:`T`), and :math:`a_{1}`, :math:`a_{2}`, :math:`a_{3}` three scalar
values.

            ========= ============= ============= =============
            **Name**  :math:`a_{1}` :math:`a_{2}` :math:`a_{3}`
            ========= ============= ============= =============
            Dirichlet 0             –             –
            Neumann   –             0             –
            Robin     –             –             –
            ========= ============= ============= =============

where “–” means non zero value

.. sectionauthor:: Alain Cartalade
