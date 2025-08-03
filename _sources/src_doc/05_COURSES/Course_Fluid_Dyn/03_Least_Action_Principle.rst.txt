.. _Least-Action:

Principe de moindre action
==========================

On rappelle dans cette annexe le **principe de moindre action** et les équations d'Euler-Lagrange qui en découlent lorsqu'on considère la position :math:`q(t)` et la vitesse :math:`\dot{q}(t)` comme fonctions indépendantes et ou la seule variable indépendante est le temps :math:`t`. Ces équations du mouvement sont établies en supposant que la trajectoire réelle de la particule est celle qui rend son action :math:`\mathscr{S}` stationnaire.

Action :math:`\mathscr{S}` et Lagrangien :math:`\mathcal{L}`
------------------------------------------------------------

On considère une particule caractérisée par deux fonctions qui dépendent de l'unique variable indépendante :math:`t` (le temps) : la position :math:`q(t)` et la vitesse :math:`\dot{q}(t)\equiv dq(t)/dt`. On définit un Lagrangien :math:`\mathcal{L}`, une fonctionnelle qui dépend de ces deux fonctions :math:`\mathcal{L}(q(t),\,\dot{q}(t))` et son action :math:`\mathscr{S}` qui est définie par l'intégrale en temps du Lagrangien :

.. math::
   :label: Def_Action

   \mathscr{S}[q]=\int_{t_{1}}^{t_{2}}\mathcal{L}(q(t),\,\dot{q}(t))dt

.. _Variational-Derivative:

Principe de stationnarité et dérivée variationnelle
---------------------------------------------------

La trajectoire de la particule est celle pour laquelle son action :math:`\mathscr{S}` est stationnaire. La condition nécessaire pour l'obtenir est que sa première variation doit s'annuler (condition du premier ordre) :

.. math::
   :label:

   \delta^{(1)}\mathscr{S}=0

où l'opérateur :math:`\delta` est l'opérateur variationnel (ou dérivée variationnelle) et l'indice supérieur :math:`^{(1)}` signifie « premier ordre » qui sera omis par la suite. L'opérateur :math:`\delta` est défini tel que :

.. math::
   :label:
   
   \delta[q(t)]=\overline{q}(t)-q(t)=\varepsilon\eta(t)

où :math:`\overline{q}(t)` est une trajectoire arbitraire, :math:`q(t)` la trajectoire optimale, :math:`\varepsilon` un petit paramètre scalaire et :math:`\eta(t)` une fonction quelconque telle que :math:`\eta(t_{1})=\eta(t_{2})=0`. On notera par la suite :math:`\varepsilon\eta(t)=\delta q(t)` avec :math:`\delta q(t_{1})=\delta q(t_{2})=0`, ce qui donne :

.. math::
   :label:

   \overline{q}(t)=q(t)+\delta q(t)

En appliquant l'opérateur :math:`\delta` à :math:`\mathcal{L}(q(t),\dot{q(t)})` et en effectuant un développement de Taylor pour le premier terme, on obtient :

.. math::
   :label:

   \begin{eqnarray}
      \delta\mathcal{L}	& = & \mathcal{L}\left(\overline{q}(t),\,\dot{\overline{q}}(t)\right)-\mathcal{L}\left(q(t),\dot{q}(t)\right)\\
	   & = & \mathcal{L}\left(q(t)+\delta q(t),\,\dot{q}(t)+\delta\dot{q}(t)\right)-\mathcal{L}\left(q(t),\,\dot{q}(t)\right)\\
	   & = & \frac{\partial\mathcal{L}}{\partial q}\delta q+\frac{\partial\mathcal{L}}{\partial\dot{q}}\delta\dot{q}+\mathcal{O}(\delta^{2})
   \end{eqnarray}

Équations d'Euler-Lagrange
--------------------------

Avec ces définitions, en appliquant l'opérateur \delta à l'équation Eq. ([eq:ActionS-1]), on obtient (on peut montrer que l'opérateur \delta commute avec l'intégrale) :

.. math::
   :label:

   \begin{eqnarray}
      \delta\mathscr{S}	& = & \int_{t_{1}}^{t_{2}}\delta\mathcal{L}(q(t),\,\dot{q}(t))dt\\
	   & = & \int_{t_{1}}^{t_{2}}\left[\frac{\partial\mathcal{L}}{\partial q}\delta q+\frac{\partial\mathcal{L}}{\partial\dot{q}}\delta\dot{q}\right]dt
   \end{eqnarray}

On intègre par partie le second terme de l'Eq. ([eq:Variation_Action-2]) :

.. math::
   :label:

   \int_{t_{1}}^{t_{2}}\frac{\partial\mathcal{L}}{\partial\dot{q}}\delta\dot{q}dt=\cancel{\left.\frac{\partial\mathcal{L}}{\partial\dot{q}}\delta q\right|_{t_{1}}^{t_{2}}}-\int_{t_{1}}^{t_{2}}\frac{d}{dt}\left(\frac{\partial\mathcal{L}}{\partial\dot{q}}\right)\delta qdt

Le premier terme du membre de droite s'annule à cause des conditions initiales :math:`\delta q(t_{1})=\delta q(t_{2})=0` et on obtient :

.. math::
   :label:

   \delta\mathscr{S}=\int_{t_{1}}^{t_{2}}\left[\frac{\partial\mathcal{L}}{\partial q}-\frac{d}{dt}\left(\frac{\partial\mathcal{L}}{\partial\dot{q}}\right)\right]\delta qdt
   
expression qui doit s'annuler quelle que soit la variation :math:`\delta q`, i.e.

.. math::
   :label:

   \frac{\partial\mathcal{L}}{\partial q}-\frac{d}{dt}\left(\frac{\partial\mathcal{L}}{\partial\dot{q}}\right)=0
   
qui est l'équation d'Euler-Lagrange.

**Remarque**

Cette équation peut se retrouver en reprenant les mêmes calculs et en considérant :

.. math::
   :label:

   \left.\frac{d\mathscr{S}[\overline{q}]}{d\varepsilon}\right|_{\varepsilon=0}=0

.. admonition:: Euler-Lagrange equation
   :class: error

   L'hypothèse de stationnarité de l'action :math:`\mathscr{S}` conduit à l'équation d'Euler-Lagrange:

   .. math::
      :label:

      \boxed{\frac{\partial\mathcal{L}}{\partial q}-\frac{d}{dt}\left(\frac{\partial\mathcal{L}}{\partial\dot{q}}\right)=0}
   
   où :math:`\mathcal{L}` is the Lagrangian which dependent of position :math:`q(t)` and velocity :math:`\dot{q}(t)`. The independent variable is the time :math:`t`.

**Plusieurs fonctions indépendantes**

Lorsque Lagrangien défini par plusieurs fonctions :math:`q_{i}(t)` et :math:`\dot{q}_{i}(t)` pour :math:`i=1,\ldots,n` : 

.. math::
   :label:

   \mathcal{L}(q_{1},\,q_{2},\,\ldots,\,q_{n};\,\dot{q}_{1},\,\dot{q}_{2},\,\ldots,\,\dot{q}_{n})\equiv\mathcal{L}(q_{i},\,\dot{q}_{i})
   
alors on peut montrer de la même façon que :

.. math::
   :label:

   \boxed{\frac{\partial\mathcal{L}}{\partial q_{i}}-\frac{d}{dt}\left(\frac{\partial\mathcal{L}}{\partial\dot{q}_{i}}\right)=0}
   
c'est-à-dire une équation d'Euler-Lagrange pour chaque couple de fonctions :math:`(q_{i},\dot{q}_{i})`. Par exemple pour :math:`i=1,2,3` avec :math:`q_{i}=x_{i}` et :math:`\dot{q}_{i}=\dot{x}_{i}`, alors on a trois équations d'Euler-Lagrange pour chaque indice :math:`i=1,2,3`.

Application: loi du mouvement de Newton
---------------------------------------

Le Lagrangien est défini par la différence entre l'énergie cinétique :math:`\mathcal{K}` et l'énergie potentielle :math:`\mathcal{V}` :

.. math::
   :label:

   \mathcal{L}(x,y,z,\dot{x},\dot{y},\dot{z})=\mathcal{K}(\dot{x},\dot{y},\dot{z})-\mathcal{V}(x,y,z)
   
i.e.

.. math::
   :label:

   \mathcal{L}(x_{i},\,\dot{x}_{i})=\mathcal{K}(\dot{x}_{i})-\mathcal{V}(x_{i})\qquad i=1,2,3
   
L'énergie cinétique est :

.. math::
   :label:

   \begin{eqnarray}
      \mathcal{K}(\dot{x},\dot{y},\dot{z})& = & \frac{1}{2}m|v|^{2}\\
      & = & \frac{1}{2}m\left(\sqrt{\dot{x}^{2}+\dot{y}^{2}+\dot{z}^{2}}\right)^{2}\\
	   & = & \frac{1}{2}m\left(\dot{x}^{2}+\dot{y}^{2}+\dot{z}^{2}\right)
   \end{eqnarray}

Dans ce cas, on a trois couples de fonctions dépendantes :math:`(q_{i},\dot{q}_{i})` pour :math:`i=1,2,3` : :math:`(x,\,\dot{x}), (y,\,\dot{y}), (z,\,\dot{z})`, et par conséquent trois équations d'Euler-Lagrange : :math:`m\ddot{x}=-\partial_{x}\mathcal{V}(\boldsymbol{x}),\,  m\ddot{y}=-\partial_{y}\mathcal{V}(\boldsymbol{x}),\, m\ddot{z}=-\partial_{z}\mathcal{V}(\boldsymbol{x})` i.e. en posant :math:`\boldsymbol{F}=-\boldsymbol{\nabla}\mathcal{V}(\boldsymbol{x})` et :math:`\boldsymbol{a}=(\ddot{x},\,\ddot{y},\,\ddot{z})^{T}`:

.. math::
   :label:

   \boldsymbol{F}=m\boldsymbol{a}

On trouvera en annexe des exemples d'application de cette formulation Lagrangienne des équations du mouvement : double pendule oscillant, orbite d'une planète, pendule oscillant avec un ressort.