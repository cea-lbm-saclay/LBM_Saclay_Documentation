.. _Minimization-Free-Energy:

Appendix A : minimization of free energy functional
===================================================

We consider one function :math:`\phi(x,y,z):=\phi(\boldsymbol{x})` called a phase index, which is a function of position :math:`\boldsymbol{x}`. The following section is inspired of the action :math:`\mathscr{S}[q]` and the « least action principle » to introduce a « free energy functional » :math:`\mathscr{F}[\phi]`. That functional is defined by the integral over the volume of a « free energy density » :math:`\mathcal{F}(\phi(\boldsymbol{x}),\boldsymbol{\nabla}\phi)`:

.. math::
   :label:

   \mathscr{F}[\phi] &=\int_{x_{1}}^{x_{2}}\int_{y_{1}}^{y_{2}}\int_{z_{1}}^{z_{2}}\mathcal{F}(\phi,\underbrace{\partial_{x}\phi,\partial_{y}\phi,\partial_{z}\phi}_{\equiv\boldsymbol{\nabla}\phi})\underbrace{dxdydz}_{\equiv dV}\\&=\int_{V}\mathcal{F}(\phi,\boldsymbol{\nabla}\phi)dV
   
where :math:`V` is the volume. The Euler-Lagrange equation is derived in 1D and next in 3D.

Euler-Lagrange 1D : functions :math:`\phi(x)` and :math:`d\phi/dx`
-----------------------------------------------------------------

In 1D, the functional :math:`\mathcal{F}(\phi(x),\phi^{\prime}(x))` is the « free energy density » of the system and :math:`\phi^{\prime}(x)\equiv d\phi/dx`. The total free energy of the system writes (space integration):

.. math::
   :label: eq:EnergieLibre_F

   \mathscr{F}[\phi]=\int_{x_{1}}^{x_{2}}\mathcal{F}(\phi,\phi^{\prime})dx
   
By applying the :math:`\delta`-operator to Eq. :eq:`eq:EnergieLibre_F`, we obtain:

.. math::
   :label:

   \delta\mathscr{F}	&=\int_{x_{1}}^{x_{2}}\delta\mathcal{F}(\phi,\phi^{\prime})dx\\&=\int_{x_{1}}^{x_{2}}\left[\frac{\partial\mathcal{F}}{\partial\phi}\delta\phi+\frac{\partial\mathcal{F}}{\partial\phi^{\prime}}\delta\phi^{\prime}\right]dx

After integration by parts of the second term (with :math:`\delta\phi(x_{1})=\delta\phi(x_{2})=0`) we obtain:

.. math::
   :label:

   \delta\mathscr{F}=\int_{x_{1}}^{x_{2}}\left[\frac{\partial\mathcal{F}}{\partial\phi}-\frac{d}{dx}\left(\frac{\partial\mathcal{F}}{\partial\phi^{\prime}}\right)\right]\delta\phi dx=0

Finally, as the first order condition :math:`\delta\mathscr{F}=0` must be true whatever the variation :math:`\delta\phi`, we obtain:

.. math::
   :label:

   \boxed{\frac{\partial\mathcal{F}}{\partial\phi}-\frac{d}{dx}\left(\frac{\partial\mathcal{F}}{\partial\phi^{\prime}}\right)=0}

which is the 1D Euler-Lagrange equation for a given functional :math:`\mathcal{F}(\phi,\,\phi^{\prime})` where :math:`\phi` is a function of position :math:`x`. This is a similar equation to the one obtained with the action. The time derivative :math:`d/dt` is replaced by a spatial derivative :math:`d/dx`.

Euler-Lagrange 3D : functions :math:`\phi(\boldsymbol{x})` and :math:`\boldsymbol{\nabla}\phi`
----------------------------------------------------------------------------------------------

We consider now a function depending on three independent variables :math:`\phi(x,y,z)\equiv\phi(\boldsymbol{x})` and one free energy density which is a function of :math:`\phi`, and its three derivatives :math:`\partial_{x}\phi`, :math:`\partial_{y}\phi`` and :math:`\partial_{z}\phi`:

.. math::
   :label:

   \mathcal{F}(\phi,\partial_{x}\phi,\partial_{y}\phi,\partial_{z}\phi):=\mathcal{F}(\phi,\boldsymbol{\nabla}\phi)
   
The 3D, free energy density is a function of :math:`\phi` and its gradient :math:`\boldsymbol{\nabla}\phi`. Eq. ([eq:EnergieLibre_F]) writes:

.. math::
   :label:

   \mathscr{F}[\phi]=\int_{x_{1}}^{x_{2}}\int_{y_{1}}^{y_{2}}\int_{z_{1}}^{z_{2}}\mathcal{F}(\phi,\partial_{x}\phi,\partial_{y}\phi,\partial_{z}\phi)dxdydz
   
By applying the :math:`\delta` operator:

.. math::
   :label:

   \delta\mathscr{F}[\phi]	&=\int_{x_{1}}^{x_{2}}\int_{y_{1}}^{y_{2}}\int_{z_{1}}^{z_{2}}\delta\mathcal{F}(\phi,\partial_{x}\phi,\partial_{y}\phi,\partial_{z}\phi)dxdydz\\&=\int_{x_{1}}^{x_{2}}\int_{y_{1}}^{y_{2}}\int_{z_{1}}^{z_{2}}\Biggl[\frac{\partial\mathcal{F}}{\partial\phi}\delta\phi+\frac{\partial\mathcal{F}}{\partial(\partial_{x}\phi)}\delta(\partial_{x}\phi)+\frac{\partial\mathcal{F}}{\partial(\partial_{y}\phi)}\delta(\partial_{y}\phi)+\frac{\partial\mathcal{F}}{\partial(\partial_{z}\phi)}\delta(\partial_{z}\phi)\Biggr]dxdydz\\&=\int_{V}\left[\frac{\partial\mathcal{F}}{\partial\phi}\delta\phi+\sum_{\alpha=x,y,z}\frac{\partial\mathcal{F}}{\partial(\partial_{\alpha}\phi)}\delta(\partial_{\alpha}\phi)\right]dV
   
For the second term we use the Einstein summation convention for repeated indices (the summation sign is canceled) and the operators :math:`\delta` and :math:`\partial_{\alpha}` are commuted:

.. math::
   :label:

   \delta\mathscr{F}&=\int_{V}\frac{\partial\mathcal{F}}{\partial\phi}\delta\phi dV+\underbrace{\int_{V}\frac{\partial\mathcal{F}}{\partial(\boldsymbol{\nabla}\phi)}\boldsymbol{\nabla}(\delta\phi)dV}_{\text{integration by parts}}\\
   &=\int_{V}\frac{\partial\mathcal{F}}{\partial\phi}\delta\phi dV+\underbrace{\cancel{\int_{\partial V}\boldsymbol{\mathcal{F}}\cdot\hat{\boldsymbol{n}}\delta\phi d(\partial V)}}_{\text{hyp: }\boldsymbol{\mathcal{F}}\cdot\hat{\boldsymbol{n}}=0\text{ on }\partial V}-\int_{V}\boldsymbol{\nabla}\cdot\left[\frac{\partial\mathcal{F}}{\partial(\boldsymbol{\nabla}\phi)}\right]\delta\phi dV
   
The second term in the right-hand side, involving :math:`\hat{\boldsymbol{n}}` the normal vector at the boundary, has been negected:

.. math::
   :label:

   \delta\mathscr{F}[\phi]=\int_{V}\left[\frac{\partial\mathcal{F}}{\partial\phi}-\partial_{\alpha}\left(\frac{\partial\mathcal{F}}{\partial(\partial_{\alpha}\phi)}\right)\right]\delta\phi dV
   
We recognize the divergence operator. Finally the Euler-Lagrange equation is:

.. math::
   :label:

   \boxed{\frac{\partial\mathcal{F}}{\partial\phi}-\boldsymbol{\nabla}\cdot\left(\frac{\partial\mathcal{F}}{\partial(\boldsymbol{\nabla}\phi)}\right)=0}

.. sectionauthor:: Alain Cartalade
