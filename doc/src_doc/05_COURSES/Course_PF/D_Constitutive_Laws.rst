.. _Constitutive-laws:

Derivation details of consitutive laws
======================================

Differentials
-------------

The term :math:`\mathcal{I}` is the differential of free energy density :math:`\mathcal{F}`:

.. math::
   :label: Differential-dF

   d\mathcal{F}(\phi,\boldsymbol{\nabla}\phi)=\frac{\partial\mathcal{F}}{\partial\phi}d\phi+\underbrace{\frac{\partial\mathcal{F}}{\partial(\boldsymbol{\nabla}\phi)}}_{\hat{=}\boldsymbol{\mathcal{F}}}\cdot d(\boldsymbol{\nabla}\phi)

where we note :math:`\boldsymbol{\mathcal{F}}\hat{=}\partial\mathcal{F}/\partial(\boldsymbol{\nabla}\phi)`. For :math:`\mathcal{F}` defined by Eq. :eq:`Potential_Energy`, :math:`\boldsymbol{\mathcal{F}}=\zeta\boldsymbol{\nabla}\phi`. For more generality we keep using the notation :math:`\boldsymbol{\mathcal{F}}` in the rest of this section. After division of Eq. :eq:`Differential-dF` by dt, we obtain:

.. math::
   :label:

   \frac{d\mathcal{F}(\phi,\boldsymbol{\nabla}\phi)}{dt}=\frac{\partial\mathcal{F}}{\partial\phi}{\frac{d\phi}{dt}}+\boldsymbol{\mathcal{F}}\cdot\underbrace{\frac{d(\boldsymbol{\nabla}\phi)}{dt}}_{\text{re-write}}

Replace :math:`d\phi/dt` by Eq. :eq:`Phi-Balance-iNS-PFCourse`  and re-write :math:`d(\boldsymbol{\nabla}\rho)/dt`


Term :math:`\mathcal{K}` kinetic energy: use impulsion balance Eq. :eq:`Impulsion-Balance_iNS-PFCourse`

.. math::
   :label:

   \frac{1}{2}\rho_{0}\frac{d\bigl|\boldsymbol{u}\bigr|^{2}}{dt}=\rho_{0}\boldsymbol{u}\cdot\frac{d\boldsymbol{u}}{dt}=\boldsymbol{u}\cdot\boldsymbol{\nabla}\cdot{\color{red}\overline{\overline{\boldsymbol{T}}}}

Algebraic calculation: usual tips and tricks
--------------------------------------------

.. admonition:: Tips and tricks
   :class: hint

   .. grid:: 2
      :gutter: 4
      :margin: 3 3 0 5

      .. grid-item-card::
         :columns: 6

         • Trick 1

            .. math::

               f\boldsymbol{\nabla}g=\boldsymbol{\nabla}(fg)-g\boldsymbol{\nabla}f

         • Trick 2

            .. math::

               f\boldsymbol{\nabla}f=\frac{1}{2}\boldsymbol{\nabla}f^{2}

      .. grid-item-card::
         :columns: 6

         • Use chain rule

            .. math::

               \boldsymbol{\nabla}f(\phi)	=\frac{\partial f}{\partial\phi}\boldsymbol{\nabla}\phi=f^{\prime}(\phi)\boldsymbol{\nabla}\phi

         • Use of index notations

.. admonition:: Examples
   :class: note

   .. grid:: 2
      :gutter: 4
      :margin: 3 3 0 5

      .. grid-item-card:: Example 1
         :columns: 6

         .. math::

            \mu_{\phi}\boldsymbol{\nabla}\phi	=\boldsymbol{\nabla}f_{dw}-\zeta\boldsymbol{\nabla}^{2}\phi\boldsymbol{\nabla}\phi

         Demo

         .. math::

            \mu_{\phi}\boldsymbol{\nabla}\phi&=\left[\partial_{\phi}f_{dw}-\zeta\boldsymbol{\nabla}^{2}\phi\right]\boldsymbol{\nabla}\phi\\
	         &=\underbrace{\partial_{\phi}f_{dw}\boldsymbol{\nabla}\phi}_{\text{chain rule}}-\zeta\boldsymbol{\nabla}^{2}\phi\boldsymbol{\nabla}\phi\\
	         &=\boldsymbol{\nabla}f_{dw}-\zeta\boldsymbol{\nabla}^{2}\phi\boldsymbol{\nabla}\phi

      .. grid-item-card:: Example 2
         :columns: 6

         .. math::

            \boldsymbol{\nabla}\cdot(\boldsymbol{\nabla}\phi\otimes\boldsymbol{\nabla}\phi)=\frac{1}{2}\boldsymbol{\nabla}(\bigl|\boldsymbol{\nabla}\phi\bigr|^{2})+(\boldsymbol{\nabla}^{2}\phi)\boldsymbol{\nabla}\phi

         Demo

         .. math::

            \partial_{\beta}(\partial_{\alpha}\phi\partial_{\beta}\phi)&=(\underbrace{\partial_{\beta}\partial_{\alpha}}_{\text{intervert}}\phi)(\partial_{\beta}\phi)+(\partial_{\alpha}\phi)(\partial_{\beta\beta}^{2}\phi)\\
	         &=\underbrace{[\partial_{\alpha}(\partial_{\beta}\phi)](\partial_{\beta}\phi)}_{\text{form }f\boldsymbol{\nabla}f=\boldsymbol{\nabla}f^{2}/2}+(\partial_{\alpha}\phi)(\partial_{\beta\beta}^{2}\phi)\\
	         &=\partial_{\alpha}(\partial_{\beta}\phi)^{2}/2+(\partial_{\alpha}\phi)(\partial_{\beta\beta}^{2}\phi)

.. admonition:: Other useful relations
   :class: note

   .. grid:: 2
      :gutter: 4
      :margin: 3 3 0 5

      .. grid-item-card::
         :columns: 6

         **Relation 1**

         .. math::

            \boxed{\frac{d}{dt}(\boldsymbol{\nabla}\phi)=\boldsymbol{\nabla}\left(\frac{d\phi}{dt}\right)-(\boldsymbol{\nabla}\boldsymbol{u})(\boldsymbol{\nabla}\phi)}

         Demo

         .. math::

            \frac{d}{dt}(\boldsymbol{\nabla}\phi)&=\frac{d}{dt}(\partial_{\alpha}\phi)\\
	         &=(\partial_{t}+u_{\beta}\partial_{\beta})(\partial_{\alpha}\phi)\\
	         &=\underbrace{\partial_{t}(\partial_{\alpha}}_{\text{intervert}}\phi)+u_{\beta}\underbrace{\partial_{\beta}(\partial_{\alpha}}_{\text{intervert}}\phi)\\
	         &=\partial_{\alpha}(\partial_{t}\phi)+\underbrace{u_{\beta}\partial_{\alpha}(\partial_{\beta}\phi)}_{\text{trick}}\\
	         &=\partial_{\alpha}(\partial_{t}\phi)+\partial_{\alpha}[u_{\beta}(\partial_{\beta}\phi)]-(\partial_{\alpha}u_{\beta})(\partial_{\beta}\phi)\\
	         &=\partial_{\alpha}[(\partial_{t}\phi)+u_{\beta}(\partial_{\beta}\phi)]-(\partial_{\alpha}u_{\beta})(\partial_{\beta}\phi)\\
	         &=\boldsymbol{\nabla}\left(\frac{d\phi}{dt}\right)-(\boldsymbol{\nabla}\boldsymbol{u})(\boldsymbol{\nabla}\phi)

      .. grid-item-card::
         :columns: 6

         **Relation 2**

         .. math::
            
            \boxed{\boldsymbol{\mathcal{F}}\cdot\frac{d}{dt}(\boldsymbol{\nabla}\phi)=\boldsymbol{\mathcal{F}}\cdot\boldsymbol{\nabla}\left(\frac{d\phi}{dt}\right)-\boldsymbol{\mathcal{F}}\otimes\boldsymbol{\nabla}\phi:\boldsymbol{\nabla}\boldsymbol{u}}

         Demo (use Eq. ([eq:Trick_Material-Derivative-1]))

         .. math::

            \boldsymbol{\mathcal{F}}\cdot\frac{d}{dt}(\boldsymbol{\nabla}\phi)&={\color{gray}\boldsymbol{\mathcal{F}}\cdot\boldsymbol{\nabla}\left(\frac{d\phi}{dt}\right)}-\mathcal{F}_{\alpha}(\partial_{\alpha}u_{\beta})(\partial_{\beta}\phi)\\
	         &={\color{gray}\boldsymbol{\mathcal{F}}\cdot\boldsymbol{\nabla}\left(\frac{d\phi}{dt}\right)}-\underbrace{\mathcal{F}_{\alpha}(\partial_{\beta}\phi)}_{\equiv\boldsymbol{\mathcal{F}}\otimes\boldsymbol{\nabla}\phi}\underbrace{(\partial_{\alpha}u_{\beta})}_{\equiv\boldsymbol{\nabla}\boldsymbol{u}}

         **Relation 3**

         .. math::

            \boxed{\boldsymbol{\nabla}\cdot\boldsymbol{u}=\overline{\overline{\boldsymbol{I}}}:\boldsymbol{\nabla}\boldsymbol{u}}

         Demo

         .. math::

            \overline{\overline{\boldsymbol{I}}}:\boldsymbol{\nabla}\boldsymbol{u}&=\delta_{\alpha\beta}\partial_{\alpha}u_{\beta}\\
	         &=\partial_{\alpha}(u_{\beta}\delta_{\alpha\beta})-u_{\beta}\cancel{\partial_{\alpha}\delta_{\alpha\beta}}\\
	         &=\partial_{\alpha}u_{\alpha}


Derivation
----------

1) Terms :math:`\mathcal{I}` and :math:`\mathcal{K}` of Eq. ([eq:Reynolds-Transport_Appli])

   .. math::

      \int_{V}\mathcal{I}dV&=\int_{V}\biggl[\frac{\partial\mathcal{F}}{\partial\phi}\frac{d\phi}{dt}+\underbrace{\boldsymbol{\mathcal{F}}\cdot\boldsymbol{\nabla}\left(\frac{d\phi}{dt}\right)}_{\text{integration by parts}}-\boldsymbol{\mathcal{F}}\otimes\boldsymbol{\nabla}\phi:\boldsymbol{\nabla}\boldsymbol{u}+\mathcal{F}\boldsymbol{\nabla}\cdot\boldsymbol{u}\biggr]dV\\
      \int_{V}(\mathcal{K}+\mathscr{L})dV&=\int_{V}[\underbrace{\boldsymbol{u}\cdot\boldsymbol{\nabla}\cdot{\color{red}\overline{\overline{\boldsymbol{T}}}}}_{\text{ibp}}]-[\lambda\boldsymbol{\nabla}\cdot\boldsymbol{u}]dV

   Results of integration by parts (ibp):

   .. math::

      \int_{V}\left[\boldsymbol{\mathcal{F}}\cdot\boldsymbol{\nabla}\left(\frac{d\phi}{dt}\right)\right]dV&=\int_{\partial V}\frac{d\phi}{dt}\boldsymbol{\mathcal{F}}\cdot\boldsymbol{n}d(\partial V)-\int_{V}\boldsymbol{\nabla}\cdot\boldsymbol{\mathcal{F}}\frac{d\phi}{dt}dV\\
      -\int_{V}\frac{\partial\mathcal{F}}{\partial\phi}\boldsymbol{\nabla}\cdot\boldsymbol{j}_{\phi}dV&=-\int_{\partial V}\frac{\partial\mathcal{F}}{\partial\phi}\boldsymbol{j}_{\phi}\cdot\boldsymbol{n}d(\partial V)+\int_{V}\boldsymbol{j}_{\phi}\cdot\boldsymbol{\nabla}\left(\frac{\partial\mathcal{F}}{\partial\phi}\right)dV\\
      \int_{V}\boldsymbol{u}\cdot\boldsymbol{\nabla}\cdot\overline{\overline{\boldsymbol{T}}}dV&=\int_{\partial V}\boldsymbol{u}\cdot\overline{\overline{\boldsymbol{T}}}\boldsymbol{n}d(\partial V)-\int_{V}\overline{\overline{\boldsymbol{T}}}:\boldsymbol{\nabla}\boldsymbol{u}dV

   Hypothesis: all :math:`\int_{\partial V}d(\partial V)` terms are neglected

2) Group terms :math:`\cdot\boldsymbol{\nabla}\mu_{\phi}` and :math:`:\boldsymbol{\nabla}\boldsymbol{u}`

   Sum Eq. ([eq:Integral_I])+Eq. ([eq:Integrals_K+L])

   .. math::

      \int_{V}(\mathcal{I}+\mathcal{K}+\mathcal{L})dV&=\int_{V}\biggl\{\biggl[\underbrace{\frac{\partial\mathcal{F}}{\partial\phi}-\boldsymbol{\nabla}\cdot\boldsymbol{\mathcal{F}}}_{\equiv\mu_{\phi}}\biggr]\underbrace{\frac{d\phi}{dt}}_{\text{Eq. }(\ref{eq:Balance_phi_Incompr})}-\boldsymbol{\mathcal{F}}\otimes\boldsymbol{\nabla}\phi:\boldsymbol{\nabla}\boldsymbol{u}+\mathcal{F}\boldsymbol{\nabla}\cdot\boldsymbol{u}-{\color{red}\overline{\overline{\boldsymbol{T}}}}:\boldsymbol{\nabla}\boldsymbol{u}-\lambda\boldsymbol{\nabla}\cdot\boldsymbol{u}\biggr\} dV\\
	   &=\int_{V}\biggl\{\mu_{\phi}\biggl[-\phi\boldsymbol{\nabla}\cdot\boldsymbol{u}-\boldsymbol{\nabla}\cdot{\color{red}\boldsymbol{j}_{\phi}}\biggr]{\color{gray}-\boldsymbol{\mathcal{F}}\otimes\boldsymbol{\nabla}\phi:\boldsymbol{\nabla}\boldsymbol{u}+\mathcal{F}\boldsymbol{\nabla}\cdot\boldsymbol{u}-{\color{red}\overline{\overline{\boldsymbol{T}}}}:\boldsymbol{\nabla}\boldsymbol{u}-\lambda\boldsymbol{\nabla}\cdot\boldsymbol{u}}\biggr\} dV\\
	   &=\int_{V}\biggl\{(-\mu_{\phi}\phi+\mathcal{F}-\lambda)\underbrace{\boldsymbol{\nabla}\cdot\boldsymbol{u}}_{\text{Eq. }(\ref{eq:Equiv-divu})}-\biggl[\boldsymbol{\mathcal{F}}\otimes\boldsymbol{\nabla}\phi+{\color{red}\overline{\overline{\boldsymbol{T}}}}\biggr]:\boldsymbol{\nabla}\boldsymbol{u}-\mu_{\phi}\boldsymbol{\nabla}\cdot{\color{red}\boldsymbol{j}_{\phi}}\biggr\} dV\\
	   &=\int_{V}\biggl\{\biggl[(-\mu_{\phi}\phi+\mathcal{F}-\lambda)\overline{\overline{\boldsymbol{I}}}-\boldsymbol{\mathcal{F}}\otimes\boldsymbol{\nabla}\phi-{\color{red}\overline{\overline{\boldsymbol{T}}}}\biggr]:\boldsymbol{\nabla}\boldsymbol{u}-\underbrace{\mu_{\phi}\boldsymbol{\nabla}\cdot{\color{red}\boldsymbol{j}_{\phi}}}_{\text{ibp}}\biggr\} dV \\
	   &=-\int_{V}\biggl\{\biggl[\underbrace{(\mu_{\phi}\phi-\mathcal{F}+\lambda)\overline{\overline{\boldsymbol{I}}}+\boldsymbol{\mathcal{F}}\otimes\boldsymbol{\nabla}\phi+{\color{red}\overline{\overline{\boldsymbol{T}}}}}_{\overline{\overline{\boldsymbol{T}}}\text{ def such as }=-\overline{\overline{\boldsymbol{P}}}+\overline{\overline{\boldsymbol{\tau}}}}\biggr]:\boldsymbol{\nabla}\boldsymbol{u}dV+\int_{V}\underbrace{{\color{red}\boldsymbol{j}_{\phi}}\cdot\boldsymbol{\nabla}\mu_{\phi}}_{\boldsymbol{j}_{\phi}\text{ def such as }\propto-\boldsymbol{\nabla}\mu_{\phi}}dV

3) Appropriate choice of :math:`\boldsymbol{j}_{\phi}` and :math:`\overline{\overline{\boldsymbol{T}}}`

   .. admonition:: Appropriate choice of :math:`\boldsymbol{j}_{\phi}` and :math:`\overline{\overline{\boldsymbol{T}}}`
      :class: error

      .. math::

         \boldsymbol{j}_{\phi}&=-\mathcal{M}_{\phi}\boldsymbol{\nabla}\mu_{\phi}\\
         \overline{\overline{\boldsymbol{T}}}&=-\overline{\overline{\boldsymbol{P}}}+\overline{\overline{\boldsymbol{\tau}}}\\
         \overline{\overline{\boldsymbol{\tau}}}&=\eta(\boldsymbol{\nabla}\boldsymbol{u}+\boldsymbol{\nabla}\boldsymbol{u}^{T})

      where pressure tensor :math:`\overline{\overline{\boldsymbol{P}}}` and hydrodynamic pressure :math:`p_{h}`

      .. math::

         \overline{\overline{\boldsymbol{P}}}&=(p_{h}-\mathcal{F})\overline{\overline{\boldsymbol{I}}}-\boldsymbol{\mathcal{F}}\otimes\boldsymbol{\nabla}\phi\\
         p_{h}&=\lambda+\phi\mu_{\phi}

      are appropriate constitutive laws such as the dissipation is positive

      .. math::

         \mathcal{D}=\int_{V}\overline{\overline{\boldsymbol{T}}}:\boldsymbol{\nabla}\boldsymbol{u}dV-\int_{V}\boldsymbol{j}_{\phi}\cdot\boldsymbol{\nabla}\mu_{\phi}dV\geqslant0

   Remarks:

      • :math:`\overline{\overline{\boldsymbol{\tau}}}`: viscous stress tensor is such as :math:`\overline{\overline{\boldsymbol{\tau}}}:\boldsymbol{\nabla}\boldsymbol{u}\geqslant0`

      • External force :math:`\rho\boldsymbol{g}` could have been considered and set in :math:`\mathcal{W}(V)`

      • If the integrals of surface are not neglected they must be considered in :math:`\Phi(\partial V)`


.. sectionauthor:: Alain Cartalade
   