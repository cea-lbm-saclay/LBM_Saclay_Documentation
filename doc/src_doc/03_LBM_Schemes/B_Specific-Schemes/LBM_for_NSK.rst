.. _LBM-NSK:

Lattice Boltzmann Methods for Navier-Stokes/Korteweg model
==========================================================

.. admonition:: Target macroscopic NS/K model
   :class: important

   The target macroscopic PDEs are fully described in :bdg-ref-primary:`Model_NSK`.

Since the historical method of "Shan-Chen" :footcite:p:`Shan-Chen_PRE1993` & :footcite:p:`Shan-Chen_PRE1994` many methods have been published to simulate those equations. An important family of methods is called **Pseudo-potential methods**. See a review e.g. in :footcite:p:`Li_etal_ProgECS2016`. We present here, one of them implemented in LBM_Saclay, called the Kupershtokh's forcing term :footcite:p:`KUPERSHTOKH20113537`. Next, we present an alternative method, more intuitive which discretizes the potential form of the tensor pressure. Finally we present a scheme, based on a modification of the equilibrium distribution function and called "Well-Balanced LBM" :footcite:p:`Guo_WellBalanced_PoF2021`.

.. admonition:: Standard LBM with a forcing term
   :class: note

   .. math::
      :label: LBE_Low_Mach

      f_{i}(\boldsymbol{x}+\boldsymbol{c}_{i}\delta t,t+\delta t)=f_{i}(\boldsymbol{x},\,t)-\frac{1}{\tau}\left[f_{i}(\boldsymbol{x},\,t)-f_{i}^{eq}(\boldsymbol{x},\,t)\right]+\delta t\mathcal{F}_{i}(\boldsymbol{x},t)

   .. math::
      :label: Feq_Pseudo_Potential

      f_{i}^{eq}(\boldsymbol{x},t)=w_{i}\rho\left[1+\frac{\boldsymbol{c}_{i}\cdot\boldsymbol{u}}{c_{s}^{2}}+\frac{(\boldsymbol{c}_{i}\cdot\boldsymbol{u})^{2}}{2c_{s}^{4}}-\frac{\boldsymbol{u}\cdot\boldsymbol{u}}{2c_{s}^{2}}\right]

   .. math::
      :label: Moment0_Pseudo_Potential

      \rho=\sum_{i}f_{i}\qquad
   
   .. math::
      :label: Moment1_Pseudo_Potential

      \boldsymbol{u}=\frac{1}{\rho}\sum_{i}f_{i}\boldsymbol{c}_{i}+\frac{\delta t}{2}\boldsymbol{F}


Pseudo-potential methods
------------------------

.. admonition:: Kupershtokh's forcing term

   In Eq. :eq:`LBE_Low_Mach`, the Kupershtokh's forcing term writes

   .. math::
      :label: Kupershtokh_Forcing

      \mathcal{F}_{i}(\boldsymbol{x},t)=f_{i}^{eq}(\boldsymbol{u}^{\star}+\Delta\boldsymbol{u})-f_{i}^{eq}(\boldsymbol{u}^{\star})
   
   where :math:`\boldsymbol{u}^{\star}` and :math:`\Delta\boldsymbol{u}` are defined by

   .. math::
      :label: Def_Delta_u_Kupershtokh

      \boldsymbol{u}^{\star}&=\frac{1}{\rho}\sum_{i}f_{i}\boldsymbol{c}_{i}\\
         \Delta\boldsymbol{u}&=\frac{1}{\rho}\boldsymbol{F}_{int}\delta t

   The force term :math:`\boldsymbol{F}_{int}` is defined in Eq. :eq:`Fint_Pseudo_Potential`. The subscript :math:`int` for  stands for *interaction*

   .. math::
      :label: Fint_Pseudo_Potential

      \boldsymbol{F}_{int}=\psi(\rho)\boldsymbol{\nabla}\psi(\rho)

   where :math:`\psi(\rho)\equiv \psi^{eos}(\rho)` is called the *pseudo-potential* which is defined by

   .. math::
      :label: Psi_Pseudo_Potential

      \psi(\rho)=\sqrt{\frac{2(\rho c_{s}^{2}-p^{eos}(\rho))}{c_{s}^{2}}}
   
   where :math:`p^{eos}(\rho)` is the :bdg-ref-primary:`Equations-Of-State`.

   The discrete version of :eq:`Fint_Pseudo_Potential` writes

   .. math::
      :label: Fint_Discrete

      \boldsymbol{F}_{int}(\boldsymbol{x},t)=\psi(\boldsymbol{x},t)\frac{1}{\delta x}\sum_{i}w_{i}\psi(\boldsymbol{x}+\boldsymbol{c}_{i}\delta t,t)\boldsymbol{c}_{i}

Discretization of Potential form of pressure tensor
---------------------------------------------------

.. admonition:: Standard scheme with Guo's forcing term (STD)

   In Eq. :eq:`LBE_Low_Mach`, the forcing term is defined by

   .. math::
      :label: Guo_Force

      \mathcal{F}_{i}(\boldsymbol{x},t)=w_{i}\left[\frac{\boldsymbol{c}_{i}-\boldsymbol{u}}{c_{s}^{2}}+\frac{(\boldsymbol{c}_{i}\cdot\boldsymbol{u})\boldsymbol{c}_{i}}{c_{s}^{4}}\right]\cdot\boldsymbol{F}_{tot}

   where the total force :math:`\boldsymbol{F}_{tot}` is defined by Eq.:

   .. math::
      :label: Ftot_Potential_Form

      \boldsymbol{F}_{tot}=\boldsymbol{\nabla}\rho c_{s}^{2}-\rho\boldsymbol{\nabla}\mu_{\rho}

   The chemical potential :math:`\mu_{\rho}` depends on the Equation of State which is used. They are defined for van der Waals and Carnahan-Starling in :bdg-ref-primary:`Equations-Of-State`. In Eq. :eq:`Ftot_Potential_Form` :math:`\boldsymbol{\nabla}\rho c_{s}^{2}` is added to cancel the perfect gas eos which arises from Chapman-Enskog when the standard EqDF Eq. :eq:`Feq_Pseudo_Potential` is used. Both gradients :math:`\boldsymbol{\nabla}\rho` and :math:`\boldsymbol{\nabla}\mu_{\rho}` are discretized by directional finite difference (see :bdg-ref-primary:`Directional-Deriv`).

Well-balanced LBM
-----------------

.. admonition:: Well-balanced LBM
   
   The Lattice Boltzmann Equation is unchanged:

   .. math::
      :label: LBE_WellBalanced

      f_{i}(\boldsymbol{x}+\boldsymbol{c}_{i}\delta t,t+\delta t)=f_{i}(\boldsymbol{x},t)-\frac{1}{\tau}\left[f_{i}(\boldsymbol{x},t)-f_{i}^{eq}(\boldsymbol{x},t)\right]+\left(1-\frac{1}{2\tau}\right)\delta t{\color{blue}\mathcal{F}_{i}(\boldsymbol{x},t)}

   But, in order to avoid parasitic currents arising from the finite difference discretization of :math:`\boldsymbol{\nabla}\rho c_{s}^{2}` in the previous scheme (STD), a new equilibrium distribution function is defined [Guo]_:

   .. math::
      :label: Feq_WellBalanced

      f_{i}^{eq}&=\begin{cases}
      \rho-(1-w_{0})\rho_{0}+w_{0}\rho\Gamma_{0}(\boldsymbol{u}) & i=0\\
      w_{i}\left[\rho_{0}+\rho\Gamma_{i}(\boldsymbol{u})\right] & i\neq0
      \end{cases}

   where :math:`\rho_0` is a constant often set as :math:`\rho_0=0` and the function :math:`\Gamma_i(\boldsymbol{u})` is:

   .. math::
      :label: Def_Gamma_WellBalanced

      \Gamma_{i}(\boldsymbol{u})=\frac{\boldsymbol{c}_{i}\cdot\boldsymbol{u}}{c_{s}^{2}}+\frac{1}{2}\left(\frac{\boldsymbol{c}_{i}\cdot\boldsymbol{u}}{c_{s}^{2}}\right)^{2}-\frac{\boldsymbol{u}\cdot\boldsymbol{u}}{2c_{s}^{2}}

   The forcing term must also be modified:

   .. math::
      :label: Forcing_WellBalanced

      \mathcal{F}_{i}=w_{i}\left[\frac{\boldsymbol{c}_{i}\cdot\boldsymbol{F}}{c_{s}^{2}}+\frac{\boldsymbol{u}(\boldsymbol{F}+c_{s}^{2}\boldsymbol{\nabla}\rho):(\boldsymbol{c}_{i}\boldsymbol{c}_{i}-c_{s}^{2}\overline{\overline{\boldsymbol{I}}})}{c_{s}^{4}}+\frac{1}{2}\left(\frac{\boldsymbol{c}_{i}^{2}}{c_{s}^{2}}-D\right)(\boldsymbol{u}\cdot\boldsymbol{\nabla}\rho)\right]

   where :math:`D` is the spatial dimension (:math:`D=2` for D2Q9).

References
----------

.. footbibliography::

.. sectionauthor:: Alain Cartalade
   