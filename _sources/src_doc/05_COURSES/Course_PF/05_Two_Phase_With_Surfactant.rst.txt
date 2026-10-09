.. _TwoPhase-With-Surfactant:

Two-phase with surfactant
=========================

Free energy
-----------

.. math::
   :label:

   \mathscr{F}[\phi,{\color{red}c}]=\underbrace{\int_{V}\left[H\phi^{2}(1-\phi)^{2}+\frac{\zeta}{2}(\boldsymbol{\nabla}\phi)^{2}\right]dV}_{\text{usual free energy for phase-field }\equiv\mathscr{F}[\phi]}+{\color{red}\int_{V}\underbrace{f_{c}(\phi,\boldsymbol{\nabla}\phi,c)}_{\text{free energy for surfactant}}}dV

.. math::
   :label:

   {\color{red}f_{c}(\phi,\boldsymbol{\nabla}\phi,c)}=\frac{1}{\beta}\underbrace{\left[c\ln(c)+(1-c)\ln(1-c)\right]}_{(I)}{\color{red}-}\underbrace{\frac{\epsilon}{2}c\left|\boldsymbol{\nabla}\phi\right|^{2}}_{(II)}+\underbrace{\frac{k}{2}c\left[\phi-\frac{1}{2}\right]^{2}}_{(III)}

• (I): Mixing entropy, penalization of homogeneous mixtures (:math:`c=0` or :math:`c=1`)

• (II): Energetic preferency for composition at interface (negative sign because :math:`c\nearrow` when :math:`\mathscr{F}\searrow`)

• (III): Penalization of high compositions in the bulk

Derivation of 1D analytical solution
------------------------------------

**Derivation of chemical potential** :math:`\mu_{c}`

.. math::
   :label:

   \mathscr{F}[\phi,c]=\mathscr{F}[\phi]+\int\biggl\{\frac{1}{\beta}[c\ln(c)+(1-c)\ln(1-c)]-\frac{\epsilon}{2}c\left|\boldsymbol{\nabla}\phi\right|^{2}+\frac{k}{2}c\left[\phi-\frac{1}{2}\right]^{2}\biggr\} dV

.. math::
   :label: Chem-Pot_c_Surfactant

   \mu_{c}(\boldsymbol{x},t)&\,\hat{=}\,\frac{\delta\mathscr{F}}{\delta c}\\
   &=\frac{\partial f_{c}(\phi,\boldsymbol{\nabla}\phi,c)}{\partial c}\\
   &=\frac{1}{\beta}\ln\left(\frac{c}{1-c}\right)-\frac{\epsilon}{2}\left|\boldsymbol{\nabla}\phi\right|^{2}+\frac{k}{2}\left[\phi-\frac{1}{2}\right]^{2}

**Derivation of bulk chemical potential at equilibrium** :math:`\mu_{c}^{b}`

.. grid:: 2
   :gutter: 4
   :margin: 3 3 0 5

   .. grid-item:: 
      :columns: 6

      With following hypotheses:

      .. math::

         \begin{cases}
            c_{b}\ll1 & \text{(input param)}\\
            \phi_{b}=0\text{ or }\phi_{b}=1\\
            \left|\boldsymbol{\nabla}\phi\right|=0
         \end{cases}

   .. grid-item-card:: Bulk chemical potential
      :columns: 6

      Eq. :eq:`Chem-Pot_c_Surfactant` becomes

      .. math::
         :label: Chem-Pot_b_Surfactant

         \mu_{c}^{b}=\frac{1}{\beta}\ln(c_{b})+\frac{k}{8}

**1D analytical solution at equilibrium** :math:`c^{eq}(x)`

Equilibrium: equality of chemical potential :math:`\mu_{c}^{b}=\mu_{c}(x)` (Eq. :eq:`Chem-Pot_c_Surfactant` = Eq. :eq:`Chem-Pot_b_Surfactant`

.. math::

   \frac{1}{\beta}\ln(c_{b})+\frac{k}{8}&=\frac{1}{\beta}\ln\left[\frac{c^{eq}(x)}{1-c^{eq}(x)}\right]-\frac{\epsilon}{2}\underbrace{\left|\partial_{x}\phi^{eq}\right|^{2}}_{\text{Eq. }(\ref{eq:Kernel3D})}+\frac{k}{2}\left(\phi^{eq}-\frac{1}{2}\right)^{2}\\\frac{1}{\beta}\left\{ \ln(c_{b})-\ln\left[\frac{c^{eq}(x)}{1-c^{eq}(x)}\right]\right\}&=\underbrace{-\frac{\epsilon}{2}\left[\frac{4}{W}\phi(1-\phi)\right]^{2}+\frac{k}{2}\phi\left(\phi-1\right)}_{\equiv-G(\phi)}\\
   \ln\left[\frac{1-c^{eq}(x)}{c^{eq}(x)}c_{b}\right]&=-\beta G(\phi)

.. admonition:: 1D analytical solution :math:`c^{eq}(x)` at equilibrium

   .. grid:: 2
      :gutter: 4
      :margin: 3 3 0 5

      .. grid-item-card:: :math:`c^{eq}(x)`
         :columns: 6

         .. math::
            :label: Analy-Sol-Surfactant

            c^{eq}(x)=\frac{c_{b}}{c_{b}+exp(-G(\phi))}

      .. grid-item-card:: With :math:`G(\phi)` defined by
         :columns: 6

         .. math::
            :label: Def_G_function

            G(\phi)=\beta\phi(1-\phi)\left[\frac{8\epsilon}{W^{2}}\phi(1-\phi)+\frac{k}{2}\right]

Derivation of counter term for composition equation
---------------------------------------------------

The conservation equation for :math:`c` writes:

.. math::
   :label:

   \partial_{t}c=-\boldsymbol{\nabla}\cdot\boldsymbol{j}_{tot}

where the total flux :math:`\boldsymbol{j}_{tot}` is the sum of three terms:

.. math::
   :label:

   \boldsymbol{j}_{tot}=\boldsymbol{j}_{Adv}+\boldsymbol{j}_{Diff}+\boldsymbol{j}_{CT}

The advective and diffusive fluxes are defined by their classical forms:

.. grid:: 2
   :gutter: 4
   :margin: 3 3 0 5

   .. grid-item-card:: Advective flux
      :columns: 6

      .. math::

         \boldsymbol{j}_{Adv}=c\boldsymbol{u}

   
   .. grid-item-card:: Diffusive flux
      :columns: 6

      .. math::

         \boldsymbol{j}_{Diff}=-M_{c}\boldsymbol{\nabla}c

To derive the counter term flux :math:`\boldsymbol{j}_{CT}`, we consider the diffusive flux at equilibrium:

.. math::
   :label:

   \boldsymbol{j}_{Diff}^{eq}=-M_{c}\boldsymbol{\nabla}c^{eq}

By using the analytical solution :eq:`Analy-Sol-Surfactant`:

.. math::

   \boldsymbol{j}_{Diff}^{eq}&=-M_{c}\boldsymbol{\nabla}\left[\frac{c_{b}}{c_{b}+c_{0}(s)}\right]\\
   &=-M_{c}\boldsymbol{n}_{\phi}\frac{\partial}{\partial s}\left[\frac{c_{b}}{c_{b}+c_{0}(s)}\right]\\
   &=-M_{c}c^{eq}(1-c^{eq})\mathcal{P}(\phi^{eq})\boldsymbol{n}_{\phi}

where

.. math::
   :label:

   \mathcal{P}(\phi)=\beta\frac{4}{W}\phi(1-\phi)\left(1-2\phi\right)\left[\frac{k}{2}+\frac{16}{W²}\epsilon(1-\phi)\phi\right]

Finally, the counter flux is defined such as it cancels the diffusive flux at equilibrium: :math:`\boldsymbol{j}_{CT}=-\boldsymbol{j}_{Diff}^{eq}`

.. admonition:: Counter term flux

   .. grid:: 2
      :gutter: 4
      :margin: 3 3 0 5

      .. grid-item-card:: Counter term flux
         :columns: 6

         .. math::
            :label: Def_Counter_Term_Surfactant

            \boldsymbol{j}_{CT}=+M_{c}c(1-c)\mathcal{P}(\phi)\boldsymbol{n}_{\phi}

      .. grid-item-card:: Definition of polynom :math:`\mathcal{P}(\phi)`
         :columns: 6

         .. math::
            :label: Def-Polynom-P-Surfactant

            \mathcal{P}(\phi)=\beta\frac{4}{W}\phi(1-\phi)\left(1-2\phi\right)\left[\frac{k}{2}+\frac{16}{W²}\epsilon(1-\phi)\phi\right]
   
Model of incompressible two-phase flows with surfactant
-------------------------------------------------------

.. admonition:: Mathematical model of surfactant
   :class: error

   **Incompressible Navier-Stokes**

   .. math::
      :label: Continuity-Mass-Surfactant

      \boldsymbol{\nabla}\cdot\boldsymbol{u}	=0,

   .. math::
      :label: Conservation-Impulsion-Surfactant

      \rho\left[\frac{\partial\boldsymbol{u}}{\partial t}+\boldsymbol{\nabla}\cdot(\boldsymbol{u}\boldsymbol{u})\right]	=-\boldsymbol{\nabla}p_{h}+\boldsymbol{\nabla}\cdot\left[\eta(\boldsymbol{\nabla}\boldsymbol{u}+\boldsymbol{\nabla}\boldsymbol{u}^{T})\right]+\boldsymbol{F}_{tot}

   **Conservative Allen-Cahn**

   .. math::
      :label: Conservation-Allen-Cahn-Surfactant

      \frac{\partial\phi}{\partial t}+\boldsymbol{\nabla}\cdot(\boldsymbol{u}\phi)	=\boldsymbol{\nabla}\cdot\left[M_{\phi}\left(\boldsymbol{\nabla}\phi-\frac{4}{W}\phi(1-\phi)\boldsymbol{n}_{\phi}\right)\right],

   
   **Transport equation**

   .. math::
      :label: Conservation-Composition-Surfactant

      \frac{\partial c}{\partial t}+\boldsymbol{\nabla}\cdot(c\boldsymbol{u})	=\boldsymbol{\nabla}\cdot\left[M_{c}\left(\boldsymbol{\nabla}c{\color{red}-c(1-c)\mathcal{P}(\phi)\boldsymbol{n}_{\phi}}\right)\right]

   .. math::
      :label: 

      {\color{red}\mathcal{P}(\phi)}	=\beta\frac{4}{W}\phi(1-\phi)\left(1-2\phi\right)\left[\frac{k}{2}+\frac{16}{W{{}^2}}\epsilon(1-\phi)\phi\right]

   **Force**

   In Eq. :eq:`Conservation-Impulsion-Surfactant` the total force contains the gravity force, the capillary force and the Marangoni force :math:`\boldsymbol{F}_{tot}=\boldsymbol{F}_{c}+\boldsymbol{F}_{g}+\boldsymbol{F}_{M}`.