.. _Math-Crystal:

Model of crystal growth
=======================

.. admonition:: Mathematical model
   :class: error

   .. math::
      :label: PhaseField_Eq

      \tau(\mathbf{n})\frac{\partial\phi}{\partial t}=W_{0}^{2}\pmb{\nabla}\cdot(a_{s}^{2}(\mathbf{n})\pmb{\nabla}\phi)+W_{0}^{2}\pmb{\nabla}\cdot\pmb{\mathcal{N}}+(\phi-\phi^{3})-\lambda u(1-\phi^{2})^{2}

   .. math::
      :label: Temp_Ramirez

      \frac{\partial u}{\partial t}=\kappa\pmb{\nabla}^{2}u+\frac{1}{2}\frac{\partial\phi}{\partial t}

   where :math:`\pmb{\mathcal{N}}\equiv\pmb{\mathcal{N}}(\mathbf{x},\,t)` is defined by:

   .. math::

      \pmb{\mathcal{N}}(\mathbf{x},\,t)=\bigl|\pmb{\nabla}\phi\bigr|^{2}a_{s}(\mathbf{n})\left(\frac{\partial a_{s}(\mathbf{n})}{\partial(\partial_{x}\phi)},\,\frac{\partial a_{s}(\mathbf{n})}{\partial(\partial_{y}\phi)},\,\frac{\partial a_{s}(\mathbf{n})}{\partial(\partial_{z}\phi)}\right)^{T}.\label{eq:TermesAnisotropes}

   The anisotropy function :math:`a_{s}(\mathbf{n})` (dimensionless) for a growing direction :math:`\left\langle 100\right\rangle` is:

   .. math::

      a_{s}(\mathbf{n})=1-3\varepsilon_{s}+4\varepsilon_{s}\sum_{\alpha=x,y,z}n_{\alpha}^{4}.\label{eq:As_Function_Classical}

   In Eq. (`[eq:PhaseField_KarmaRappel] <#eq:PhaseField_KarmaRappel>`__), :math:`\phi` is the phase-field, :math:`W_{0}` is the interface thickness, :math:`\lambda` is the coupling coefficient with the normalized temperature :math:`u(\mathbf{x},\,t)`. The normal vector :math:`\mathbf{n}\equiv\mathbf{n}(\mathbf{x},\,t)` is defined such as:

   .. math::

      \mathbf{n}(\mathbf{x},\,t)=-\frac{\pmb{\nabla}\phi}{\bigl|\pmb{\nabla}\phi\bigr|},\label{eq:Def_Normal_Vector}

   directed from the solid to the liquid. The coefficient :math:`\tau(\mathbf{n})` is the kinetic coefficient of the interface, it is defined as :math:`\tau(\mathbf{n})=\tau_{0}a_{s}^{2}(\mathbf{n})` where :math:`\tau_{0}` is the kinetic characteristic time. Let us notice that each term of Eq. (`[eq:PhaseField_KarmaRappel] <#eq:PhaseField_KarmaRappel>`__) is dimensionless. The physical dimensions of :math:`W_{0}`, :math:`\pmb{\mathcal{N}}`, :math:`\tau_{0}` and :math:`\lambda` are respectively :math:`[W_{0}]\equiv[\mathscr{L}]`, :math:`[\pmb{\mathcal{N}}]\equiv[\mathscr{L}]^{-1}`, :math:`[\tau_{0}]\equiv[\mathcal{T}]` and :math:`[\lambda]\equiv[-]`, where :math:`[\mathscr{L}]` indicates the length dimension and :math:`[\mathcal{T}]` indicates the time dimension. In Eq. (`[eq:Temp_Ramirez] <#eq:Temp_Ramirez>`__), the physical dimension of :math:`\kappa` is :math:`[\mathscr{L}]^{2}/[\mathcal{T}]`.


.. _Math-Dissolution:

Model of dissolution
====================

Mathematical model of dissolution
---------------------------------

The mathematical model of dissolution is derived in :footcite:p:`Boutin_etal_CMS2022`.

.. admonition:: Mathematical model
   :class: error
   
   The model is composed of two coupled PDEs. The first one for interface-tracking on :math:`\phi` and the second one on the composition :math:`c`. The interface movement is based on the Allen-Cahn equation

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
      :label: Chemical_Potential_Dissolution

      \overline{\mu}=\overline{\mu}^{eq}+c(\phi,\,\overline{\mu})-\left[c_{l}^{eq}\phi+c_{s}^{eq}\left(1-\phi\right)\right]

   Finally in Eq. :eq:`Diffusion_Equation`, :math:`\boldsymbol{j}_{at}` is the anti-trapping current which is defined by:

   .. math::
      :label: Anti_Trapping
   
      \boldsymbol{j}_{at}=\frac{1}{4}W(c_{s}^{eq}-c_{l}^{eq})\frac{\partial\phi}{\partial t}\boldsymbol{n}
   
Closure relationships
^^^^^^^^^^^^^^^^^^^^^

Input parameters in ``.ini`` file
---------------------------------
