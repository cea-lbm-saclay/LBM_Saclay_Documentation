Variable change in LBE for source term
======================================

L’équation de Boltzmann discrète avec un terme source (ou terme force
externe) :math:`\mathcal{S}_{i}^{\vartheta}` peut s’écrire sous la forme
suivante avec le terme de collision BGK :

.. math::
   :label: eq:DLBE
   
   \frac{\partial\vartheta_{i}}{\partial t}+\mathbf{c}_{i}\cdot\boldsymbol{\nabla}\vartheta_{i}=-\frac{\vartheta_{i}-\vartheta_{i}^{eq}}{\tau_{\vartheta}}+S_{i}^{\vartheta}.

Dans ce qui suit, les calculs sont développés en posant
:math:`\vartheta\equiv f`,
:math:`\mathcal{S}_{i}^{\vartheta}=\mathcal{S}_{i}^{f}=\mathcal{S}_{i}`
et :math:`\tau_{\vartheta}\equiv\tau`, mais l’approche du changement de
variable est également valable pour :math:`\vartheta\equiv h` et
:math:`\vartheta\equiv s`. Les termes qui sont évalués en
:math:`\boldsymbol{x}` et :math:`t` sont notés
:math:`f_{i}\equiv f_{i}(\boldsymbol{x},\,t)`,
:math:`f_{i}^{eq}\equiv f_{i}^{eq}(\boldsymbol{x},\,t)` et
:math:`\mathcal{S}_{i}\equiv\mathcal{S}_{i}(\boldsymbol{x},\,t)`, tandis
que les termes évalués en
:math:`\boldsymbol{x}+\boldsymbol{c}_{i}\delta t` et :math:`t+\delta t`
sont notés avec une étoile :
:math:`f_{i}^{\star}\equiv f_{i}(\boldsymbol{x}+\boldsymbol{c}_{i}\delta t,\,t+\delta t)`,
:math:`f_{i}^{\star eq}\equiv f_{i}^{eq}(\boldsymbol{x}+\boldsymbol{c}_{i}\delta t,\,t+\delta t)`
et
:math:`\mathcal{S}_{i}^{\star}\equiv\mathcal{S}_{i}(\boldsymbol{x}+\boldsymbol{c}_{i}\delta t,\,t+\delta t)`.
Avec ces notations, l’intégration de l’Eq. :eq:`eq:DLBE`
entre :math:`t` et :math:`t+\delta t` donne :

.. math::
   :label: eq:LBE_Trapezoidal
   
   f_{i}^{\star}=f_{i}-\frac{\delta t}{2\tau}\left(f_{i}^{\star}-f_{i}^{\star eq}\right)-\frac{\delta t}{2\tau}\left(f_{i}-f_{i}^{eq}\right)+\frac{\delta t}{2}\mathcal{S}_{i}^{\star}+\frac{\delta t}{2}\mathcal{S}_{i}

où la loi des trapèzes à été appliquée pour le membre de droite de l’Eq.
:eq:`eq:DLBE`. Dans cette expression, pour les termes en
:math:`\mathbf{x}+\mathbf{c}_{i}\delta t` et :math:`t+\delta t`, on
introduit le changement de variable suivant :

.. math::
   :label: eq:VariableChange
   
   \overline{f}_{i}^{\star}=f_{i}^{\star}+\frac{\delta t}{2\tau}\left(f_{i}^{\star}-f_{i}^{\star eq}\right)-\frac{\delta t}{2}\mathcal{S}_{i}^{\star}

Le même changement de variable est utilisé pour les termes en
:math:`\boldsymbol{x}` et :math:`t` :

.. math::
   :label: eq:VariableChange_Expl
   
   \overline{f}_{i}=f_{i}+\frac{\delta t}{2\tau}\left(f_{i}-f_{i}^{eq}\right)-\frac{\delta t}{2}\mathcal{S}_{i}

En inversant cette dernière relation pour exprimer :math:`f_{i}` en
fonction de :math:`\overline{f}_{i}`, on obtient :

.. math::
   :label: eq:f_versus_fbarre
   
   f_{i}=\frac{2\tau}{2\tau+\delta t}\left(\overline{f}_{i}+\frac{\delta t}{2\tau}f_{i}^{eq}+\frac{\delta t}{2}\mathcal{S}_{i}\right)

Avec les Eqs. :eq:`eq:VariableChange` et :eq:`eq:f_versus_fbarre`, l’Eq. :eq:`eq:LBE_Trapezoidal` devient

.. math::
   :label: eq:LBE_Intermediate
   
   \overline{f}_{i}^{\star}=\overline{f}_{i}-\frac{\delta t}{\tau+\delta t/2}\left(\overline{f}_{i}-f_{i}^{eq}+\frac{\delta t}{2}\mathcal{S}_{i}\right)+\delta t\mathcal{S}_{i}

Si on définit un nouveau changement de variable

.. math::
   :label: eq:Feq_barre
   
   \overline{f}_{i}^{eq}=f_{i}^{eq}-\frac{\delta t}{2}\mathcal{S}_{i}

alors l’Eq. :eq:`eq:LBE_Intermediate` est équivalente à

.. math::
   :label: eq:LBE_Form1
   
   \overline{f}_{i}^{\star}=\overline{f}_{i}-\frac{\delta t}{\tau+\delta t/2}\left(\overline{f}_{i}-\overline{f}_{i}^{eq}\right)+\delta t\mathcal{S}_{i}

Sans le changement de variable sur :math:`f_{i}^{eq}`, l’Eq.
:eq:`eq:LBE_Intermediate` est équivalente à

.. math::
   :label: eq:LBE_Form2
   
   \overline{f}_{i}^{\star}=\overline{f}_{i}-\frac{\delta t}{\tau+\delta t/2}\left(\overline{f}_{i}-f_{i}^{eq}\right)+\frac{\tau\delta t}{\tau+\delta t/2}\mathcal{S}_{i}

où seul le facteur devant le terme source est modifié.

En introduisant le taux de collision sans dimension défini par
:math:`\overline{\tau}=\tau/\delta t`, l’Eq.
:eq:`eq:LBE_Form1` s’écrit finalement

.. math::
   :label: eq:LBE_2ndOrderTime_Form1
   
   \overline{f}_{i}^{\star}=\overline{f}_{i}-\frac{1}{\overline{\tau}+1/2}\left(\overline{f}_{i}-\overline{f}_{i}^{eq}\right)+\delta t\mathcal{S}_{i}

ou alternativement,

.. math::
   :label: eq:LBE_2ndOrderTime_Form2
   
   \overline{f}_{i}^{\star}=\overline{f}_{i}-\frac{1}{\overline{\tau}+1/2}\left(\overline{f}_{i}-f_{i}^{eq}\right)+\frac{\overline{\tau}\delta t}{\overline{\tau}+1/2}\mathcal{S}_{i}

Dans les chapitres de cette documentation, l’Eq.
:eq:`eq:LBE_2ndOrderTime_Form1` est
l’équation d’évolution utilisée dans les algorithmes LBM. Le changement
de variable Eq. :eq:`eq:VariableChange_Expl` conduit à
calculer les moments d’ordre zéro par :

.. math::
   :label: eq:Moment_Order0
   
   \mathcal{M}_{0}=\sum_{i}\overline{f}_{i}+\frac{\delta t}{2}\sum_{i}\mathcal{S}_{i}

Equivalence 
-----------

On montre ici l'équivalence entre l’Eq. 6.25 dans [1]_ (page 239) et de l’Eq. :eq:`eq:LBE_2ndOrderTime_Form2`

Démonstrations de l’équivalence
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Dans Krüger *et al*., l’équation d’évolution pour :math:`\overline{f}_{i}` s’écrit (Eq. 6.25) :

.. math::
   :label: eq:Eq6.25
   
   \overline{f}_{i}^{\star}=\overline{f}_{i}-\frac{\delta t}{\lambda}\left(\overline{f}_{i}-f_{i}^{eq}\right)+\left(1-\frac{\delta t}{2\lambda}\right)F_{i}\delta t

où :math:`\overline{f}_{i}^{\star}\equiv\overline{f}_{i}(\boldsymbol{x}+\boldsymbol{c}_{i}\delta t,\,t+\delta t)`. On note que le temps de relaxation :math:`\lambda` est homogène à un
temps et il est défini sous 6.25 par

.. math::
   :label: eq:Lambda
   
   \lambda=\tau+\frac{\delta t}{2}

On définit le taux de relaxation (sans dimension) par :

.. math::
   :label: eq:TauxRelax
   
   \overline{\tau}=\frac{\tau}{\delta t}

En l’utilisant dans :eq:`eq:Lambda`, on obtient :

.. math::

   \begin{aligned}
      \lambda & =\overline{\tau}\delta t+\frac{\delta t}{2}\nonumber \\
      & =\left(\overline{\tau}+1/2\right)\delta t\label{eq:Lambda_adim}
   \end{aligned}

En remplaçant dans Eq. :eq:`eq:Eq6.25`, on obtient :

.. math:: \overline{f}_{i}^{\star}=\overline{f}_{i}-\frac{1}{\overline{\tau}+1/2}\left(\overline{f}_{i}-f_{i}^{eq}\right)+\left(1-\frac{\delta t}{2\left(\overline{\tau}+1/2\right)\delta t}\right)F_{i}\delta t

En simplifiant le facteur devant :math:`F_{i}`, on obtient :

.. math:: \left(1-\frac{\delta t}{2\left(\overline{\tau}+1/2\right)\delta t}\right)=\frac{2\overline{\tau}}{2\overline{\tau}+1}=\frac{\overline{\tau}}{\overline{\tau}+1/2}

Finalement, on obtient :

.. math::
   :label: eq:EqC.11
   
   \overline{f}_{i}^{\star}=\overline{f}_{i}-\frac{1}{\overline{\tau}+1/2}\left(\overline{f}_{i}-f_{i}^{eq}\right)+\frac{\overline{\tau}}{\overline{\tau}+1/2}F_{i}\delta t

qui correspond à l’Eq. :eq:`eq:LBE_2ndOrderTime_Form2`.

Lien avec la formulation qui introduit :math:`\overline{f}_{i}^{eq}`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

L’Eq. :eq:`eq:Eq6.25` avec :math:`\lambda` défini par l’Eq. :eq:`eq:Lambda` s’écrit :

.. math::

   \begin{aligned}
      \overline{f}_{i}^{\star} & =\overline{f}_{i}-\frac{\delta t}{\tau+\frac{\delta t}{2}}\left(\overline{f}_{i}-f_{i}^{eq}\right)+\left(1-\frac{\delta t}{2\tau+\delta t}\right)F_{i}\delta t
   \end{aligned}

En manipulant le dernier terme du membre de droite, on obtient :

.. math::

   \begin{aligned}
      \overline{f}_{i}^{\star} & =\overline{f}_{i}-\frac{\delta t}{\tau+\frac{\delta t}{2}}\left(\overline{f}_{i}-f_{i}^{eq}\right)-\frac{\delta t}{2(\tau+\delta t/2)}F_{i}\delta t+F_{i}\delta t\\
      & =\overline{f}_{i}-\frac{\delta t}{\tau+\frac{\delta t}{2}}\left(\overline{f}_{i}-f_{i}^{eq}\right)-\frac{\delta t}{(\tau+\delta t/2)}\frac{\delta t}{2}F_{i}+F_{i}\delta t
   \end{aligned}

En factorisant les second et troisième termes on obtient :

.. math:: \overline{f}_{i}^{\star}=\overline{f}_{i}-\frac{\delta t}{\tau+\frac{\delta t}{2}}\left(\overline{f}_{i}-f_{i}^{eq}+\frac{\delta t}{2}F_{i}\right)+F_{i}\delta t

Si on pose :

.. math:: \overline{f}_{i}^{eq}=f_{i}^{eq}-\frac{\delta t}{2}F_{i}

Alors on obtient :

.. math:: \overline{f}_{i}^{\star}=\overline{f}_{i}-\frac{\delta t}{\tau+\frac{\delta t}{2}}\left(\overline{f}_{i}-\overline{f}_{i}^{eq}\right)+F_{i}\delta t

Encore une fois si on pose :math:`\overline{\tau}=\tau/\delta t` alors :

.. math:: \overline{f}_{i}^{\star}=\overline{f}_{i}-\frac{1}{\overline{\tau}+1/2}\left(\overline{f}_{i}-\overline{f}_{i}^{eq}\right)+F_{i}\delta t

qui est l’équation d’évolution LBE utilisée dans ce document.

Bibliography
------------

.. [1] Krüger T., H. Kusumaatmaja, A. Kuzmin, O. Shardt, G. Silva, E. Viggen, The Lattice Boltzmann Method: Principles and Practice, Graduate Texts in Physics, Springer, 2017.

.. sectionauthor:: Alain Cartalade
