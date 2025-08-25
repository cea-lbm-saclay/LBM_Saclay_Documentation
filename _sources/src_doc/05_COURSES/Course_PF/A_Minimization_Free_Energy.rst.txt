.. _Minimization-Free-Energy:

Annexe A : minimisation d'une fonctionnelle d'énergie libre
===========================================================

On considère une fonction :math:`\phi(x,y,z):=\phi(\boldsymbol{x})` qu'on appelle « indicatrice de phase » qui est une fonction de la position :math:`\boldsymbol{x}`. On s'inspire de l'action :math:`\mathscr{S}[q]` et du « principe de moindre action » pour introduire une « fonctionnelle d'énergie libre » :math:`\mathscr{F}[\phi]` qui est définie par l'intégrale sur le volume d'une « densité d'énergie libre :math:`\mathcal{F}(\phi(\boldsymbol{x}),\boldsymbol{\nabla}\phi)` :

.. math::
   :label:

   \begin{eqnarray}
      \mathscr{F}[\phi] & = & \int_{x_{1}}^{x_{2}}\int_{y_{1}}^{y_{2}}\int_{z_{1}}^{z_{2}}\mathcal{F}(\phi,\underbrace{\partial_{x}\phi,\partial_{y}\phi,\partial_{z}\phi}_{\equiv\boldsymbol{\nabla}\phi})\underbrace{dxdydz}_{\equiv dV}\\
      & = & \int_{V}\mathcal{F}(\phi,\boldsymbol{\nabla}\phi)dV
   \end{eqnarray}
   
où V est un volume. On établit l'équation d'Euler-Lagrange en 1D puis en 3D.

Euler-Lagrange 1D : fonctions :math:`\phi(x)` et :math:`d\phi/dx`
-----------------------------------------------------------------

En 1D la fonctionnelle :math:`\mathcal{F}(\phi(x),\phi^{\prime}(x))` décrit la « densité d'énergie libre » du système et :math:`\phi^{\prime}(x)\equiv d\phi/dx`. L'énergie libre totale du système s'écrit (intégration en espace) :

.. math::
   :label: eq:EnergieLibre_F

   \mathscr{F}[\phi]=\int_{x_{1}}^{x_{2}}\mathcal{F}(\phi,\phi^{\prime})dx
   
En appliquant l'opérateur :math:`\delta` à l'Eq. :eq:`eq:EnergieLibre_F`, on obtient :

.. math::
   :label:

   \begin{eqnarray}
      \delta\mathscr{F}	& = & \int_{x_{1}}^{x_{2}}\delta\mathcal{F}(\phi,\phi^{\prime})dx\\
	   & = & \int_{x_{1}}^{x_{2}}\left[\frac{\partial\mathcal{F}}{\partial\phi}\delta\phi+\frac{\partial\mathcal{F}}{\partial\phi^{\prime}}\delta\phi^{\prime}\right]dx
   \end{eqnarray}

Puis en intégrant par parties (avec :math:`\delta\phi(x_{1})=\delta\phi(x_{2})=0`) le second terme on obtient :

.. math::
   :label:

   \delta\mathscr{F}=\int_{x_{1}}^{x_{2}}\left[\frac{\partial\mathcal{F}}{\partial\phi}-\frac{d}{dx}\left(\frac{\partial\mathcal{F}}{\partial\phi^{\prime}}\right)\right]\delta\phi dx=0

Finalement, comme la condition du premier ordre :math:`\delta\mathscr{F}=0` doit être vraie quelle que soit la variation :math:`\delta\phi`, on obtient :

.. math::
   :label:

   \boxed{\frac{\partial\mathcal{F}}{\partial\phi}-\frac{d}{dx}\left(\frac{\partial\mathcal{F}}{\partial\phi^{\prime}}\right)=0}

qui est l'équation d'Euler-Lagrange en 1D pour une fonctionnelle :math:`\mathcal{F}(\phi,\,\phi^{\prime})` donnée où :math:`\phi` est une fonction de la position :math:`x`. Il s'agit d'une équation similaire à celle à temps où la dérivée par rapport au temps :math:`d/dt` est remplacée par une dérivée par rapport à la position :math:`d/dx`.

Euler-Lagrange 3D : fonctions :math:`\phi(\boldsymbol{x})` et :math:`\boldsymbol{\nabla}\phi`
---------------------------------------------------------------------------------------------

On considère maintenant une fonction à trois variables indépendantes :math:`\phi(x,y,z)\equiv\phi(\boldsymbol{x})` et une densité d'énergie libre qui est fonction de :math:`\phi`, et de ses trois dérivées :math:`\partial_{x}\phi`, :math:`\partial_{y}\phi`` et :math:`\partial_{z}\phi` :

.. math::
   :label:

   \mathcal{F}(\phi,\partial_{x}\phi,\partial_{y}\phi,\partial_{z}\phi):=\mathcal{F}(\phi,\boldsymbol{\nabla}\phi)
   
En généralisant en 3D, la densité d'énergie libre est une fonction de :math:`\phi` et de son gradient :math:`\boldsymbol{\nabla}\phi`. L'Eq. ([eq:EnergieLibre_F]) s'écrit :

.. math::
   :label:

   \mathscr{F}[\phi]=\int_{x_{1}}^{x_{2}}\int_{y_{1}}^{y_{2}}\int_{z_{1}}^{z_{2}}\mathcal{F}(\phi,\partial_{x}\phi,\partial_{y}\phi,\partial_{z}\phi)dxdydz
   
En appliquant l'opérateur :math:`\delta`:

.. math::
   :label:

   \begin{eqnarray}
      \delta\mathscr{F}[\phi]	& = & \int_{x_{1}}^{x_{2}}\int_{y_{1}}^{y_{2}}\int_{z_{1}}^{z_{2}}\delta\mathcal{F}(\phi,\partial_{x}\phi,\partial_{y}\phi,\partial_{z}\phi)dxdydz\\
	   & = & \int_{x_{1}}^{x_{2}}\int_{y_{1}}^{y_{2}}\int_{z_{1}}^{z_{2}}\Biggl[\frac{\partial\mathcal{F}}{\partial\phi}\delta\phi+\frac{\partial\mathcal{F}}{\partial(\partial_{x}\phi)}\delta(\partial_{x}\phi)+\frac{\partial\mathcal{F}}{\partial(\partial_{y}\phi)}\delta(\partial_{y}\phi)+\frac{\partial\mathcal{F}}{\partial(\partial_{z}\phi)}\delta(\partial_{z}\phi)\Biggr]dxdydz\\
	   & = & \int_{V}\left[\frac{\partial\mathcal{F}}{\partial\phi}\delta\phi+\sum_{\alpha=x,y,z}\frac{\partial\mathcal{F}}{\partial(\partial_{\alpha}\phi)}\delta(\partial_{\alpha}\phi)\right]dV
   \end{eqnarray}   
   
Pour le 2nd terme, on utilise la convention de sommation d'Einstein pour les indices répétés (on supprime le signe somme) et on commute les opérateurs :math:`\delta` et :math:`\partial_{\alpha}`:

.. math::
   :label:

   \delta\mathscr{F}[\phi]=\int_{V}\left[\frac{\partial\mathcal{F}}{\partial\phi}\delta\phi+\frac{\partial\mathcal{F}}{\partial(\partial_{\alpha}\phi)}\partial_{\alpha}(\delta\phi)\right]dV
   
On intègre par parties le second terme et on obtient :

.. math::
   :label:

   \delta\mathscr{F}[\phi]=\int_{V}\left[\frac{\partial\mathcal{F}}{\partial\phi}-\partial_{\alpha}\left(\frac{\partial\mathcal{F}}{\partial(\partial_{\alpha}\phi)}\right)\right]\delta\phi dV
   
expression dans laquelle on reconnait l'opérateur divergence. Finalement d'Euler-Lagrange correspondante est :

.. math::
   :label:

   \boxed{\frac{\partial\mathcal{F}}{\partial\phi}-\boldsymbol{\nabla}\cdot\left(\frac{\partial\mathcal{F}}{\partial(\boldsymbol{\nabla}\phi)}\right)=0}

.. sectionauthor:: Alain Cartalade
