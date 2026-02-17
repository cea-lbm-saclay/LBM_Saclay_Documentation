.. _Feq-Alt:

Equilibrium distribution functions for incompressible Navier-Stokes equations
=============================================================================

The equilibrium distribution function (EqDF) :math:`f_i^{eq}` is one of the most important functions in LBM because it indicates what macroscopic equation the algorithm simulates. The equilibrium distribution function :math:`f_i^{eq}` is involved in the collision operator :math:`\Omega` in the discrete LBE:

.. math::
   :label: LBE_Feq
   
   f_{i}(\boldsymbol{x}+\boldsymbol{c}_{i}\delta t,t+\delta t)=f_{i}(\boldsymbol{x},t)+\Omega_{i}(f_{i},f_{i}^{eq})+\mathcal{F}_i
   
One of the most attractive aspect of LBM, is to use the same evolution Eq. :eq:`LBE_Feq` and simply change the definition of :math:`f_i^{eq}` to simulate either the Navier-Stokes equations or the Conservative Allen-Cahn equation. For low Mach Navier-Stokes (NS) and standard Advection-Diffusion Equation (ADE), the EqDF are presented in :bdg-ref-primary:`Overview-LBM`. Here we present those for incompressible two-phase NS and several variations of transport equation such as the Cahn-Hilliard equation and the Conservative Allen-Cahn one.

.. admonition:: Equilibrium distribution functions in LBM_Saclay
   :class: important
   
   The equilibrium distribution functions are problem dependent. They are defined for each kernel in the ``LBMScheme_Kernel_Name.h`` file of folder ``src/kernels``. For example for kernel ``NSAC_Comp``, the equilibrium distribution functions for all PDEs are written in ``LBMScheme_NS_AC_Comp.h`` file.


For low Mach Navier-Stokes (NS), the EqDF are presented in :bdg-ref-primary:`Overview-LBM`. Here are presented some modifications for simulating incompressible single-phase and two-phase flows. First we remind the target macroscopic PDEs we want to simulate:

.. admonition:: Target macroscopic PDEs
   :class: important

   .. math::
      :label: Mass_Balance_Ref
   
      \boldsymbol{\nabla}\cdot\boldsymbol{u}=0
   
   .. math::
      :label: Impulsion_Balance_Ref
   
      \varrho(\phi)\left[\frac{\partial\boldsymbol{u}}{\partial t}+\boldsymbol{\nabla}\cdot(\boldsymbol{u}\boldsymbol{u})\right]=-\boldsymbol{\nabla}p_{h}+\boldsymbol{\nabla}\cdot\eta(\boldsymbol{x},t)\left[\boldsymbol{\nabla}\boldsymbol{u}+(\boldsymbol{\nabla}\boldsymbol{u})^{T}\right]
   
   where :math:`p_h` is the hydrodynamic pressure, :math:`\boldsymbol{u}` is the fluid velocity , and :math:`\varrho(\phi)` is the interpolation of constant bulk densities: each phase is characterized by constant densities, e.g. :math:`\rho_0` and :math:`\rho_1`. The total density :math:`\varrho(\boldsymbol{x},t)` and the total dynamic viscosity are two functions of position and time with the phase-field :math:`\phi`. The first one is obtained by a linear interpolation of :math:`\rho_0` and :math:`\rho_1`: 

   .. math::
      :label: Total_Density
   
      \varrho(\phi)=\rho_0\phi(\boldsymbol{x},t)+\rho_1(1-\phi(\boldsymbol{x},t))

   and the second with a harmonic interpolation of :math:`\eta_0` and :math:`\eta_1`:

   .. math::
      :label: HarmoniInterpolation_Viscosity

      \frac{1}{\eta(\phi)}=\frac{\phi}{\eta_{1}}+\frac{1-\phi}{\eta_{2}}


Standard :math:`f_i^{eq}` for single-phase incompressible NS
------------------------------------------------------------

.. admonition:: :math:`f_i^{eq}` for single-phase iNS

   For simulating incompressible NS equations for single-phase flows, the EqDF writes :footcite:p:`Zou_etal_Incompressible_JSP1995` & :footcite:p:`He-Luo_Incompressible_JSP1997`:

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
---------------------------------------------------

Now we consider two-phase flows by assuming that each phase is incompressible. 
   
From the previous EqDF, two methods are implemented in LBM_Saclay to account for that variation :eq:`Total_Density`. The first method is a direct extension of :eq:`Feq_Incompr_V0`. The second one is a slight modification which introduces the dimensionless pressure :math:`p_h^{\star}`.

Version 1 for variable density
""""""""""""""""""""""""""""""

.. admonition:: Version 1 for variable density

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
   
Version 2 for variable density
""""""""""""""""""""""""""""""

.. admonition:: Version 2 for variable density

   That version is implemented in the kernel ``NSAC_Comp``. The pressure that is used in the equilibrium distribution function is a dimensionless pressure defined by :footcite:p:`Zu-He_PRE2013`:

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

References
----------

.. footbibliography::

.. sectionauthor:: Alain Cartalade
   