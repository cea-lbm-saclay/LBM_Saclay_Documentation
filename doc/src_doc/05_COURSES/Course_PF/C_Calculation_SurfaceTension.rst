.. _Calculation-Surface-Tension:

Appendix C: calculation of surface tension 
==========================================

On montre dans cette annexe que la tension de surface :math:`\sigma` est de la forme :math:`\sigma=I\sqrt{2\zeta H}` où :math:`I` est une intégrale de la racine carrée du double-puits. Dans cette annexe, :math:`I` est calculé pour trois formes typiques de double-puits usuellement rencontrées dans la littérature : :math:`_{1}(\phi)=\phi^{2}(1-\phi)^{2}` qui possède des minima en :math:`\phi=0` et :math:`\phi=1`; puis :math:`g_{2}(\phi)=(\phi-\phi_{l})^{2}(\phi-\phi_{g})^{2}` qui possède des minima en :math:`\phi=\phi_{g}` et :math:`\phi=\phi_{l}` et enfin on calculera :math:`I` pour :math:`g_{3}(\phi)=(\phi-\phi^{\star})^{2}(\phi+\phi^{\star})^{2}` qui possède des minima en :math:`\phi=\pm\phi^{\star}`.

Calcul de la tension de surface
-------------------------------

On part de la définition de la tension de surface en 1D :

.. math::
   :label:

   \sigma=\int_{-\infty}^{+\infty}\left[ Hg(\phi^{eq})+\frac{\zeta}{2}\left(\frac{d\phi^{eq}}{dx}\right)^{2}\right]dx

où l'indice supérieur :math:`^{eq}` signifie qu'il s'agit de la solution d'équilibre (solution fondamentale Eq. :eq:`Hyperbolic_Tangent_Solution_Course`). Dans la suite on le supprime  pour alléger les notations. En utilisant la relation Eq. :eq:`Equality_For_Surface_Tension`, on obtient :

.. math::
   :label:

   \sigma=\int_{-\infty}^{+\infty}2Hg(\phi)dx=\int_{-\infty}^{+\infty}\zeta \left(\frac{d\phi}{dx}\right)^{2}dx

On effectue le changement de variable en transformant l'intégrale en :math:`x` en intégrale en :math:`\phi` en utilisant la relation Eq. :eq:`eq:Chgt_Variable` :

.. math::
   :label:

   \begin{eqnarray}
      \sigma & = & \int_{\phi^{min}}^{\phi^{max}}\frac{2Hg(\phi)}{\sqrt{2Hg(\phi)/\zeta}}d\phi\\
	   & = & \int_{\phi^{min}}^{\phi^{max}}\sqrt{2\zeta Hg(\phi)}d\phi\\
	   & = & \sqrt{2\zeta H}\int_{\phi^{min}}^{\phi^{max}}\sqrt{g(\phi)}d\phi
   \end{eqnarray}

Les bornes de l'intégrale en :math:`\phi` dépendent du choix de la fonction de double-puits. En toute généralité, sans faire aucune hypothèse sur la forme de la fonction :math:`g(\phi)`, la tension de surface s'écrit :

.. math::
   :label:

   \sigma=I\sqrt{2\zeta H}

avec

.. math::
   :label:

   I=\int_{\phi^{min}}^{\phi^{max}}\sqrt{g(\phi)}d\phi
   
où les bornes :math:`\phi^{min}` et :math:`\phi^{max}` de l'intégrale :math:`I` dépendent du choix de la fonction :math:`g(\phi)`. Dans les sections suivantes, on calcule ces intégrales :math:`I` pour plusieurs formes typiques de :math:`g(\phi)`.

Cas :math:`g_{1}(\phi)=\phi^{2}(1-\phi)^{2}`
-----------------------------------------------------

Dans le cas où :math:`g(\phi)=\phi^{2}(1-\phi)^{2}`, les bornes de l'intégrale sont :math:`\phi^{min}=0` et :math:`\phi^{max}=1` :

.. math::
   :label:

   \begin{eqnarray}
      \sigma & = & \sqrt{2\zeta H}\int_{0}^{1}\sqrt{g_{1}(\phi)}d\phi\\
      & = & \sqrt{2\zeta H}\int_{0}^{1}\phi(1-\phi)d\phi
   \end{eqnarray}

L'intégration est directe et vaut :math:`\int_{0}^{1}\phi(1-\phi)d\phi=1/6`. Finalement

.. math::
   :label:

   \boxed{\sigma=\frac{1}{6}\sqrt{2\zeta H}}

**Cas particulier où** :math:`g(\phi)=8\phi^{2}(1-\phi)^{2}=8g_{1}(\phi)`

Dans un cas particulier où on mulitiplie cette fonction double-puits par un coefficient constant, par exemple :math:`k=8`, on obtient :

.. math::
   :label:

   \begin{eqnarray}
      \sigma &	= & \sqrt{2\zeta H}\int_{0}^{1}\sqrt{g(\phi)}d\phi\\
      & = & \sqrt{2\zeta H}\int_{0}^{1}\sqrt{8g_{1}(\phi)}d\phi\\
	   & = & \sqrt{2\zeta H\times8}\int_{0}^{1}\phi(1-\phi)d\phi\\
      & = & \frac{2}{3}\sqrt{\zeta H}
   \end{eqnarray}

Cas :math:`g_{2}(\phi)=(\phi_{l}-\phi)^{2}(\phi-\phi_{g})^{2}`
-----------------------------------------------------------------------------

Pour certains problèmes de changement de phase liquide/gaz, le double-puits prend la forme :math:`g_{2}(\phi)=(\phi_{l}-\phi)^{2}(\phi-\phi_{g})^{2}` en supposant que :math:`\phi_{g}<\phi<\phi_{l}`. On fera attention en prenant la racine de cette fonction à bien respecter l'ordre :math:`\phi_{l}-\phi` et :math:`\phi-\phi_{g}` car les différences doivent rester positives (car :math:`\phi_{g}<\phi<\phi_{l}`). Dans ce cas les bornes de l'intégrale varient de :math:`\phi^{min}=\phi_{g}` à :math:`\phi^{max}=\phi_{l}` :

.. math::
   :label:

   \begin{eqnarray}
      \sigma &	= & \sqrt{2\zeta H}\int_{\phi_{g}}^{\phi_{l}}\sqrt{g_{2}(\phi)}d\phi\\
	   & = & \sqrt{2\zeta H}\int_{\phi_{g}}^{\phi_{l}}(\phi_{l}-\phi)(\phi-\phi_{g})d\phi
   \end{eqnarray}

Pour le calcul de l'intégrale, on peut utiliser :math:`\texttt{wxmaxima}`, et on trouve :math:`\int_{\phi_{g}}^{\phi_{l}}(\phi_{l}-\phi)(\phi-\phi_{g})d\phi=(\phi_{l}-\phi_{g})^{3}/6`. Finalement, on obtient

.. math::
   :label:

   \boxed{\sigma=\frac{(\phi_{l}-\phi_{g})^{3}}{6}\sqrt{2\zeta H}}

Cas :math:`g_{3}(\phi)=(\phi^{\star}-\phi)^{2}(\phi+\phi^{\star})^{2}`
-------------------------------------------------------------------------------------

Une autre fonction double-puits typique est :math:`g_{3}(\phi)=(\phi^{\star}-\phi)^{2}(\phi+\phi^{\star})^{2}` qui possède ses deux minima en :math:`-\phi^{\star}` à :math:`+\phi^{\star}`. Le choix :math:`\phi^{\star}=1` est souvent utilisé en solidification et croissance cristalline. Il s'agit d'un cas particulier du cas précédent en posant :math:`\phi_{l}=\phi^{\star}` et :math:`\phi_{g}=-\phi^{\star}`. Avec ces changements on peut directement déduire que le coefficient devant la racine carrée vaut :math:`(2\phi^{\star})^{3}/6=4\phi^{\star3}/3`.
On le vérifie en calculant :math:`\sigma` en repartant de la relation générale. Dans ce cas les bornes de l'intégrale varient de :math:`\phi^{min}=-\phi^{\star}` à :math:`\phi^{max}=+\phi^{\star}` :

.. math::
   :label:

   \begin{eqnarray}
      \sigma &	= & \int_{-\phi^{\star}}^{+\phi^{\star}}\frac{2Hg_{3}(\phi)}{\sqrt{2Hg_{3}(\phi)/\zeta}}d\phi\\
	   & = & \sqrt{2\zeta H}\int_{-\phi^{\star}}^{+\phi^{\star}}(\phi^{\star}-\phi)(\phi+\phi^{\star})d\phi
   \end{eqnarray}
   
En utilisant :math:`\texttt{wxmaxima}` on trouve bien que l'intégrale vaut :math:`\int_{-\phi^{\star}}^{+\phi^{\star}}(\phi-\phi^{\star})(\phi+\phi^{\star})d\phi=4\phi^{\star3}/3`. Finalement on obtient :

.. math::
   :label:

   \sigma=\frac{4\phi^{\star3}}{3}\sqrt{2\zeta H}


.. sectionauthor:: Alain Cartalade
