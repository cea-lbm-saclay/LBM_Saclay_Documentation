.. _Mass-Transfer:

Mass transfer through interfaces
================================

.. _Gibbs-Thomson-Condition:

Gibbs-Thomson condition
-----------------------

Gibbs-Thomson condition for a curved interface
""""""""""""""""""""""""""""""""""""""""""""""

.. admonition:: Gibbs-Thomson condition

   For a curved interface at equilibrium:

   .. math::
      :label: Equilib_mu_Curved

      \mu_{in}^{eq}(\phi_{in})=\mu_{out}^{eq}(\phi_{out})=\mu_{i}^{eq}

   where the index :math:`i` is for "interface". The pressure difference is given by the Laplace's law:

   .. math::
      :label: Equilib_p_Curved

      p_{in}(\phi_{in})-p_{out}(\phi_{out})=\sigma\kappa

   With its definition:

   With its def (Eq. ([eq:Def_p-c_local])), Eq. ([eq:Equilib_p_Curved]) writes

   .. math::
      :label:

      \phi_{in}\mu_{in}^{eq}-f(\phi_{in})-\phi_{out}\mu_{out}^{eq}+f(\phi_{out})=\sigma\kappa

   Using common tangent construction Eq. :eq:`Mu-Common-Tangent` for :math:`f_{dw}(\phi_{out})-f_{dw}(\phi_{in})`:

   .. math::
      :label:

      \mu_{i}^{eq}(\phi_{in}-\phi_{out})+\mu^{eq}(\phi_{out}-\phi_{in})=\sigma\kappa

   and finally:

   .. math::
      :label:

      \boxed{\mu_{i}^{eq}=\mu^{eq}+\frac{\sigma\kappa}{(\phi_{out}-\phi_{in})}}

   This is the Gibbs-Thomson condition which means that the equilibrium chemical potential of a curved interface is equal to the equilibrium chemical potential for a flat interface corrected by the curvature and the surface tension.

Ostwald ripening
----------------

Consequence of Gibbs-Thomson condition with :math:`\boldsymbol{j}_{CH}`: Ostwald ripening
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. admonition:: Ostwald ripening

   The Gibbs-Thomson condition writes:

   .. math::
      :label: Gibbs-Thomson_jCH

      \mu_{i}=\mu^{eq}+\frac{1}{(\phi_{out}-\phi_{in})}\frac{2\sigma}{R}

   If we consider two droplets of radius :math:`R_{1}` and :math:`R_{2}` with :math:`R_{1}<R_{2}`, Eq. :eq:`Gibbs-Thomson_jCH` implies:

   .. math::
      :label:

      \mu_{i}(R_{2})<\mu_{i}(R_{1})

   There exists a flux from :math:`\mu_{i}(R_{1})` to :math:`\mu_{i}(R_{2})` because :math:`\boldsymbol{j}_{CH}\propto-\boldsymbol{\nabla}\mu_{\phi}(\boldsymbol{x},t)` (see Fig. :numref:`Fig-Ostawald-Ripening`). Consequence: the smallest droplet disappears and the biggest one grows. This is the Ostwald ripening.

.. figure:: ../../FIGS/04_FIGS_COURSES/Ostwald-Ripening.png
   :name: Fig-Ostawald-Ripening
   :figclass: align-center
   :align: center
   :height: 400
   :width: 920
   :scale: 45%

   Principle of Ostwald ripening

Droplet growth
--------------


