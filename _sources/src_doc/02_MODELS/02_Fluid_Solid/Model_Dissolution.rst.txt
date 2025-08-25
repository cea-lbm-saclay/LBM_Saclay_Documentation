.. _Math-Dissolution:

Model of dissolution
====================

Mathematical model of dissolution
---------------------------------

The mathematical model of dissolution is composed of two coupled PDEs. The first one for interface-tracking on :math:`\phi` and the second one on the composition :math:`c`. The interface movement is based on the Allen-Cahn equation

.. math::
   :label: Allen_Cahn_Equation
   
   \frac{\partial\phi}{\partial t}=M_{\phi}\boldsymbol{\nabla}^{2}\phi-\frac{M_{\phi}}{W^{2}}2\phi(1-\phi)(1-2\phi)+\frac{\lambda M_{\phi}}{W^{2}}\mathscr{S}_{\phi}(\phi,\,\overline{\mu})

where :math:`W` is the interface width, :math:`M_{\phi}` is the interface mobility, and :math:`M_{\lambda}` is the coupling coefficient which is related to the interface surface tension. The source term :math:`\mathscr{S}_{\phi}(\phi,\,\overline{\mu})` is defined by

.. math::
   :label: Source_Term_Dissolution

   \mathscr{S}_{\phi}(\phi,\,\overline{\mu})=6\phi(1-\phi)(c_{s}^{eq}-c_{l}^{eq})(\overline{\mu}-\overline{\mu}^{eq})

where :math:`c_{s}^{eq}` and :math:`c_{l}^{eq}` are equilibrium compositions in solid and liquid respectively. They are both scalar values. :math:`\overline{\mu}^{eq}` is the equilibrium chemical potentiel which is also a scalar value. :math:`\overline{\mu}` is the chemical potential which is involved in the diffusion equation below:

.. math::
   :label: Diffusion_Equation
   
   \frac{\partial c}{\partial t}=\boldsymbol{\nabla}\cdot\left[D_{l}\phi\boldsymbol{\nabla}\overline{\mu}-\boldsymbol{j}_{at}(\phi,\,\overline{\mu})\right]

where :math:`c` is the composition, :math:`D_l` is the diffusion coefficient in the liquid phase. The flux is given by the gradient of chemical potential. It is related to the composition by:

.. math::
   :label: Chemical_Potential

   \overline{\mu}=\overline{\mu}^{eq}+c(\phi,\,\overline{\mu})-\left[c_{l}^{eq}\phi+c_{s}^{eq}\left(1-\phi\right)\right]

Finally in Eq. :eq:`Diffusion_Equation`, :math:`\boldsymbol{j}_{at}` is the anti-trapping current which is defined by:

.. math::
   :label: Anti_Trapping
   
   \boldsymbol{j}_{at}=\frac{1}{4}W(c_{s}^{eq}-c_{l}^{eq})\frac{\partial\phi}{\partial t}\boldsymbol{n}
   
Closure relationships
^^^^^^^^^^^^^^^^^^^^^

Input parameters in ``.ini`` file
---------------------------------
