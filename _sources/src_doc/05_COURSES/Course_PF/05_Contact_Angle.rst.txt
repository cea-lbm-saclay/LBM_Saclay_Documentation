.. _Contact-Angle:

Contact angle
=============

Law of Young-Dupré
------------------

.. admonition:: Law of Young-Dupré

   When a liquid (phase :math:`L`) and a gas (phase :math:`G`) are in contact with a solid wall, there is an equilibrium angle :math:`\theta^{eq}` corresponding to the equilibrium of three capillary forces :math:`\vec{\sigma}_{Ls}` the capillary force between Liquid and solid, :math:`\vec{\sigma}_{Gs}` the capillary force between Gas and solid, and :math:`\vec{\sigma}_{LG}` the capillary force between Liquid and Gas (see Fig. :numref:`Contact-Angle-Concept`). The contact angle :math:`\theta^{eq}` can be expressed with the three surface tensions by the Young-Dupré law. Its derivation (see :footcite:p:`DeGennes_etal2004`) can be performed with the work :math:`d\mathcal{W}` of a small displacement :math:`dx` (see Fig. :numref:`Young-Dupre-Derivation`):

   .. math::
      :label:

      d\mathcal{W}=(\sigma_{Gs}-\sigma_{Ls})dx-\sigma_{LG}dx\cos(\theta^{eq})

   At equilibrium :math:`d\mathcal{W}=0` and we obtain:

   .. math::
      :label:

      \boxed{\cos(\theta^{eq})=\frac{\sigma_{Gs}-\sigma_{Ls}}{\sigma_{LG}}}

.. grid:: 2
   :gutter: 4
   :margin: 3 3 0 5

   .. grid-item::
      :columns: 6

      .. figure:: ../../FIGS/04_FIGS_COURSES/Contact-Angle.png
         :name: Contact-Angle-Concept
         :figclass: align-center
         :align: center
         :height: 460
         :width: 920
         :scale: 40 %

         Contact angle

   .. grid-item::
      :columns: 6

      .. figure:: ../../FIGS/04_FIGS_COURSES/Deriving_Young.png
         :name: Young-Dupre-Derivation
         :figclass: align-center
         :align: center
         :height: 460
         :width: 920
         :scale: 40 %

         Derivation of Young-Dupré Law


Boundary condition for diffuse interface
----------------------------------------

.. admonition:: Wall free energy

   In the case of phase-field theory, the minimization is now carried out with an additional free energy: the wall free energy :math:`\mathscr{F}+\mathscr{F}_{w}` where

   .. math::
      :label: Free-Energy-Wall

      \mathscr{F}_{w}=\int_{\partial V}[(\sigma_{Gs}-\sigma_{Ls})p(\phi)+\sigma_{Ls}]d(\partial V)

   where :math:`d(\partial V)` is the wall surface, and :math:`p(\phi)` is the interpolation polynomial :math:`p(\phi)=\phi^{2}(3-2\phi)`. The variation :math:`\delta(\mathscr{F}+\mathscr{F}_{w})/\delta\phi` yields:

   .. math::
      :label:

      \int_{\partial V}\biggl[\zeta\boldsymbol{\nabla}\phi\cdot\hat{\boldsymbol{n}}+\underbrace{(\sigma_{Gs}-\sigma_{Ls})}_{\text{use Young-Dupré law}}p^{\prime}(\phi)\biggr]d(\partial V)=0

   where :math:`\hat{\boldsymbol{n}}` is the normal vector at the wall boundary. After using the Young-Dupré law, we obtain the boundary condition for the phase-field :math:`\phi` at the solid surface:

   .. math::
      :label:

      \boxed{\zeta\boldsymbol{\nabla}\phi\cdot\hat{\boldsymbol{n}}=-\sigma_{LG}\cos(\theta^{eq})p^{\prime}(\phi)}

   Remark: if :math:`\theta^{eq}=90{^\circ}` then :math:`\boldsymbol{\nabla}\phi\cdot\hat{\boldsymbol{n}}=0`

.. figure:: ../../FIGS/04_FIGS_COURSES/Diffuse_Contact-Angle.png
         :name: Diffuse-Contact-Angle
         :figclass: align-center
         :align: center
         :height: 460
         :width: 920
         :scale: 50 %

         Contact angle for diffuse interface

References
----------

.. footbibliography::

.. sectionauthor:: Alain Cartalade