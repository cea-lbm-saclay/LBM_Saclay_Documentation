.. _Directional-Deriv:

Gradients and Laplacian
^^^^^^^^^^^^^^^^^^^^^^^

Sometimes it is necessary to compute gradients or Laplacian of one function e.g. :math:`\phi(\boldsymbol{x},t)`. For example, the conservative Allen-Cahn equation involves the unit normal vector :math:`\boldsymbol{n}=\boldsymbol{\nabla}\phi/|\boldsymbol{\nabla}\phi|` whereas the Cahn-Hilliard equation involves the Laplacian of :math:`\phi`. That Laplacian :math:`\boldsymbol{\nabla}^2\phi` also appears explicitely in the chemical potential :math:`\mu_{\phi}` of capillary force :math:`\boldsymbol{F}_c=\mu_{\phi}\boldsymbol{\nabla}\phi` in the impulsion balance equation.

.. important::
    
   In LBM_Saclay, those gradients and Laplacian are computed in the source file ``src/kernels/LBMSchemeBase.h``

Bulk: directional derivatives
"""""""""""""""""""""""""""""

When the node :math:`\boldsymbol{x}` is inside the computational domain, not close to the boundary, the gradients and Laplacian are computed by *directional derivatives* method which is a finite difference method applied for every direction :math:`\boldsymbol{e}_i` of lattice.


**Gradients**

For gradient, the directional derivative :math:`\boldsymbol{e}_{i}\cdot\boldsymbol{\nabla}\phi\bigr|_{\boldsymbol{x}}` for each direction :math:`\boldsymbol{e}_i` writes:

.. math::
   :label: DD_Grad
   
    \boldsymbol{e}_{i}\cdot\boldsymbol{\nabla}\phi\bigr|_{\boldsymbol{x}}=\frac{1}{2\delta x}\left[\phi(\boldsymbol{x}+\boldsymbol{e}_{i}\delta x)-\phi(\boldsymbol{x}-\boldsymbol{e}_{i}\delta x)\right]

where :math:`\delta x` is the discretization step in space and :math:`e^2` is a lattice-dependent coefficient. Except for D2Q5, its value is :math:`e^2=1/3` meaning that :math:`1/e^2=3`. In Eq. :eq:`DD_Grad`, let us notice that for one particular direction (e.g. :math:`x`-direction i.e. :math:`i=1`), the directional derivative corresponds to the second order central finite difference method. The gradient is obtained by a weighted sum of all those directional derivatives:

.. math::
   :label: Grad
   
   \boldsymbol{\nabla}\phi=\frac{1}{e^{2}}\sum_{i=0}^{N_{pop}}w_{i}\boldsymbol{e}_{i}\left(\boldsymbol{e}_{i}\cdot\boldsymbol{\nabla}\phi\bigr|_{\boldsymbol{x}}\right)



**Laplacian**

For Laplacian, the method is identical. First we compute the components for all directions

.. math::
   :label: DD_Lapl

   (\boldsymbol{e}_{i}\cdot\boldsymbol{\nabla})^{2}\phi\bigr|_{\boldsymbol{x}}=\frac{1}{\delta x^{2}}\left[\phi(\boldsymbol{x}+\boldsymbol{e}_{i}\delta x)-2\phi(\boldsymbol{x})+\phi(\boldsymbol{x}-\boldsymbol{e}_{i}\delta x)\right]

Once again, for one particular direction (e.g. :math:`x`-direction i.e. :math:`i=1`), the directional derivative corresponds to the second order central finite difference method. The Laplcian is obtained by the weighted sum:

.. math::
   :label: Lapl

   \boldsymbol{\nabla}^{2}\phi\bigr|_{\boldsymbol{x}}=3\sum_{i=0}^{N_{pop}}w_{i}(\boldsymbol{e}_{i}\cdot\boldsymbol{\nabla})^{2}\phi\bigr|_{\boldsymbol{x}}

Boundaries
""""""""""

When the node :math:`\boldsymbol{x}` is close to one of boundaries, in that case, the classic 

.. sectionauthor:: Alain Cartalade
   