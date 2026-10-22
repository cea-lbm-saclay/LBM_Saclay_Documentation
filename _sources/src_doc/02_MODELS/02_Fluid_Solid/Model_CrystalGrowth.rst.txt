.. _Math-Crystal:

Model of crystal growth
^^^^^^^^^^^^^^^^^^^^^^^

.. math::

   \begin{aligned}
   \tau(\mathbf{n})\frac{\partial\phi}{\partial t} & =W_{0}^{2}\pmb{\nabla}\cdot(a_{s}^{2}(\mathbf{n})\pmb{\nabla}\phi)+W_{0}^{2}\pmb{\nabla}\cdot\pmb{\mathcal{N}}+(\phi-\phi^{3})-\lambda u(1-\phi^{2})^{2},\label{eq:PhaseField_KarmaRappel}\\
   \frac{\partial u}{\partial t} & =\kappa\pmb{\nabla}^{2}u+\frac{1}{2}\frac{\partial\phi}{\partial t},\label{eq:Temp_Ramirez}\end{aligned}

where :math:`\pmb{\mathcal{N}}\equiv\pmb{\mathcal{N}}(\mathbf{x},\,t)` is defined by:

.. math::

    \pmb{\mathcal{N}}(\mathbf{x},\,t)=\bigl|\pmb{\nabla}\phi\bigr|^{2}a_{s}(\mathbf{n})\left(\frac{\partial a_{s}(\mathbf{n})}{\partial(\partial_{x}\phi)},\,\frac{\partial a_{s}(\mathbf{n})}{\partial(\partial_{y}\phi)},\,\frac{\partial a_{s}(\mathbf{n})}{\partial(\partial_{z}\phi)}\right)^{T}.\label{eq:TermesAnisotropes}

The anisotropy function :math:`a_{s}(\mathbf{n})` (dimensionless) for a growing direction :math:`\left\langle 100\right\rangle` is:

.. math::

    a_{s}(\mathbf{n})=1-3\varepsilon_{s}+4\varepsilon_{s}\sum_{\alpha=x,y,z}n_{\alpha}^{4}.\label{eq:As_Function_Classical}

In Eq. (`[eq:PhaseField_KarmaRappel] <#eq:PhaseField_KarmaRappel>`__), :math:`\phi` is the phase-field, :math:`W_{0}` is the interface
thickness, :math:`\lambda` is the coupling coefficient with the normalized temperature :math:`u(\mathbf{x},\,t)`. The normal vector
:math:`\mathbf{n}\equiv\mathbf{n}(\mathbf{x},\,t)` is defined such as:

.. math::

    \mathbf{n}(\mathbf{x},\,t)=-\frac{\pmb{\nabla}\phi}{\bigl|\pmb{\nabla}\phi\bigr|},\label{eq:Def_Normal_Vector}

directed from the solid to the liquid. The coefficient :math:`\tau(\mathbf{n})` is the kinetic coefficient of the interface, it is defined as :math:`\tau(\mathbf{n})=\tau_{0}a_{s}^{2}(\mathbf{n})` where :math:`\tau_{0}` is the kinetic characteristic time. Let us notice that each term of Eq. (`[eq:PhaseField_KarmaRappel] <#eq:PhaseField_KarmaRappel>`__) is dimensionless. The physical dimensions of :math:`W_{0}`, :math:`\pmb{\mathcal{N}}`, :math:`\tau_{0}` and :math:`\lambda` are respectively :math:`[W_{0}]\equiv[\mathscr{L}]`, :math:`[\pmb{\mathcal{N}}]\equiv[\mathscr{L}]^{-1}`, :math:`[\tau_{0}]\equiv[\mathcal{T}]` and :math:`[\lambda]\equiv[-]`, where :math:`[\mathscr{L}]` indicates the length dimension and :math:`[\mathcal{T}]` indicates the time dimension. In Eq. (`[eq:Temp_Ramirez] <#eq:Temp_Ramirez>`__), the physical dimension of :math:`\kappa` is :math:`[\mathscr{L}]^{2}/[\mathcal{T}]`.

