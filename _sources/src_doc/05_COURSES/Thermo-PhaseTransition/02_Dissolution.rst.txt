.. _Dissolution:

Dissolution with a grand-potential formulation
==============================================

Sharp interface model of dissolution
------------------------------------

.. admonition:: Stefan problems

   .. math::

      \frac{\partial c}{\partial t}&=\boldsymbol{\nabla}\cdot(D\boldsymbol{\nabla}\mu)&\qquad\text{on }\Gamma_{l}(t)\,\\
      (c-c_{s})v_{n}&=\left.-D\boldsymbol{\nabla}c\cdot\boldsymbol{n}\right|_{l}+\cancel{\left.D_{s}\boldsymbol{\nabla}c\cdot\boldsymbol{n}\right|_{s}}&\qquad\text{on }\Gamma_{ls}(t)\\
      \overline{\mu}_{I}-\overline{\mu}^{eq}&={\color{red}-d_{0}\kappa}-\beta v_{n}&\qquad\text{on }\Gamma_{ls}(t)

   where :math:`c` and :math:`c_{s}` are liquid and solid composition, :math:`v_{n}=\boldsymbol{v}_{s}\cdot\boldsymbol{n}` is the normal velocity of interface, :math:`\overline{\mu}` is the dimensionless chemical potential :math:`\overline{\mu}^{eq}` is the equilibirum chemical potential, :math:`\kappa` is the curvature, and :math:`d_{0}` is the capillary length.

Grand-potential functional energy
---------------------------------

The grand-potential energy :math:`\Omega` is composed of two contribution: the interface contribution :math:`\omega_{int}(\psi,\boldsymbol{\nabla}\psi)` and the bulk phases :math:`\omega_{bulk}(\psi,\mu)`:

.. math::
   :label: Def_Grand_Potential

   \Omega[\psi,\mu]=\int_{V}\left[\omega_{int}(\psi,\boldsymbol{\nabla}\psi)+\omega_{bulk}(\psi,\mu)\right]dV

The interface grand-potential density is

.. math::
   :label: Def-omega-Int

   \omega_{int}(\psi,\boldsymbol{\nabla}\psi)=H\psi^{2}(1-\psi)^{2}+\frac{\zeta}{2}\bigl|\boldsymbol{\nabla}\psi\bigr|^{2}

.. math::
   :label: Def-omega-Bulk

   \omega_{bulk}(\psi,\mu)=p(\psi){\color{red}\omega_{l}(\mu)}+\left[1-p(\psi)\right]{\color{red}\omega_{s}(\mu)}

.. math::
   :label: Def-Interpol-Polynom-p-psi

   p_{int}(\psi)=\psi^{2}(3-2\psi)

and its derivative w.r.t. :math:`\psi` is

.. math::

   p^{\prime}(\psi)=6\psi(1-\psi)
   
With that convention, if :math:`\psi=0` then :math:`\omega_{bulk}(\mu)=\omega_{s}(\mu)` and if :math:`\psi=1` then :math:`\omega_{bulk}(\mu)=\omega_{l}(\mu)`.

We work with the dimensionless composition :math:`c(\psi,\,\mu)` describing the local fraction of one chemical species and varying between zero and one. It is related to the concentration :math:`C(\psi,\,\mu)` (physical dimension :math:`[\text{mol}].[\text{L}]^{-3}`) by :math:`c(\psi,\,\mu)=V_{m}C(\psi,\,\mu)` where :math:`V_{m}` is the molar volume of (:math:`[\text{L}]^{3}.[\text{mol}]^{-1}`). For both chemical species, the molar volume is assumed to be constant and identical. In the rest of this paper :math:`V_{m}` will appear in the equations for reasons of physical dimension, but it will be considered equal to :math:`V_{m}=1` for all numerical simulations.

The concentration :math:`C` is now a function of :math:`\psi` and :math:`\mu`. It is related to the grand-potential by :footcite:p:`Plapp_GrandPotential_PRE2011` :math:`C(\psi,\,\mu)=-\delta\Omega/\delta\mu=-\partial\omega_{bulk}(\psi,\,\mu)/\partial\mu`. The application of that relationship with :math:`\omega_{bulk}(\psi,\,\mu)` defined by Eq. :eq:`Def-omega-Bulk` yields:

.. math::
   :label: Def_Concentration

   C(\psi,\,\mu)=p(\psi)\left[-\frac{\partial\omega_{l}(\mu)}{\partial\mu}\right]+\left[1-p(\psi)\right]\left[-\frac{\partial\omega_{s}(\mu)}{\partial\mu}\right]
   
The concentration :math:`C(\psi,\mu)` is defined by an interpolation of derivatives of :math:`\omega_{s}(\mu)` and :math:`\omega_{l}(\mu)` w.r.t. :math:`\mu`. Each derivative defines the concentration of bulk phase :math:`C_{s}(\mu)=-\partial\omega_{s}(\mu)/\partial\mu` and :math:`C_{l}(\mu)=-\partial\omega_{l}(\mu)/\partial\mu`.

In Eq. ([eq:Grand-potential_density]), the grand-potential densities of each bulk phase :math:`\omega_{l}(\mu)` and :math:`\omega_{s}(\mu)` are defined by the Legendre transform of free energy densities :math:`f_{s}(c)` and :math:`f_{l}(c)`:

.. math::
   :label:

   \omega_{\psi}(\mu)=f_{\psi}(c)-\mu C\qquad\text{for}\qquad\psi=s,l
   
where :math:`\mu=\partial f_{\psi}/\partial C`. Finally, the phase-field equations are obtained from the minimization of the grand-potential functional :math:`\Omega[\psi,\,\mu]`. The most general PDEs write (see :footcite:`Plapp_GrandPotential_PRE2011`, Eq. (43) and Eq. (47)):

.. math::
   :label:

   \frac{\partial\psi}{\partial t}=\mathcal{M}_{\psi}\Bigl\{\zeta\boldsymbol{\nabla}^{2}\psi-H\omega_{dw}^{\prime}(\psi)-p^{\prime}(\psi)\left[\omega_{l}(\mu)-\omega_{s}(\mu)\right]\Bigr\}

.. math::
   :label: Evol-Potchem-Eq-Omega

   \chi(\psi,\,\mu)\frac{\partial\mu}{\partial t}=\boldsymbol{\nabla}\cdot\left[\mathcal{D}(\psi,\,\mu)\chi(\psi,\,\mu)\boldsymbol{\nabla}\mu\right]-p^{\prime}(\psi)\left[\frac{\partial\omega_{s}(\mu)}{\partial\mu}-\frac{\partial\omega_{l}(\mu)}{\partial\mu}\right]\frac{\partial\psi}{\partial t}


Eq. :eq:`Evol-Potchem-Eq-Omega` is the evolution equation on chemical potential :math:`\mu(\boldsymbol{x},\,t)`. It is obtained from the conservation equation :math:`\partial_{t}C(\psi,\,\mu)=-\boldsymbol{\nabla}\cdot\boldsymbol{j}_{diff}` where the diffusive flux is given by :math:`\boldsymbol{j}_{diff}=-\mathcal{D}(\psi,\,\mu)\chi(\psi,\,\mu)\boldsymbol{\nabla}\mu`. The time derivative term has been expressed by the chain rule :math:`\partial C(\psi,\,\mu)/\partial t=(\partial C/\partial\mu)\partial_{t}\mu+(\partial C/\partial\psi)\partial_{t}\psi`. The function :math:`\chi(\psi,\,\mu)`, called the generalized susceptibility, is defined by the partial derivative of :math:`C(\psi,\,\mu)` with respect to :math:`\mu`. For most general cases, the coefficient :math:`\mathcal{D}(\psi,\,\mu)` is the diffusion coefficient which depends on :math:`\psi` and :math:`\mu`. Here we assume that the diffusion coefficients :math:`D_{s}` and :math:`D_{l}` are only interpolated by :math:`\psi`, i.e. :math:`\mathcal{D}(\psi,\,\mu)\equiv\mathcal{D}(\psi)`. Actually, in next section that equation on :math:`\mu` will be transformed back to an equation on :math:`C` (or :math:`c`) for reasons of mass conservation in simulations. Eq. :eq:`Def_Concentration` will be used to supply a relationship between :math:`\mu` and :math:`c`.

Quadratic free energy
---------------------

If we assume two quadratic free energies for each phase :math:`\psi=l,s`:

.. math::
   :label:

   f_{\psi}(c)=\frac{\varepsilon_{\psi}}{2}(c-m_{\psi})^{2}+f_{\psi}^{min}

where we assumed :math:`\varepsilon_{s}=\varepsilon_{l}`, then we can derive (see :footcite:p:`Boutin_etal_CMS2022` for details) for the equilibrium chemical potential:

.. math::

   \overline{\mu}^{eq}=\Delta\overline{f}^{min}/\Delta m

and equilibrium compositions for liquid and solid phases:

.. math::

   c_{l}^{eq}&=m_{l}+\overline{\mu}^{eq}\\
   c_{s}^{eq}&=m_{s}+\overline{\mu}^{eq}

Equivalent phase-field model
----------------------------


References
----------

.. footbibliography::

.. sectionauthor:: Alain Cartalade
