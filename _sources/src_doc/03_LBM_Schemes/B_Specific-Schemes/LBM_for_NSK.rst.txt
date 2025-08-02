.. _LBM-NSK:

LBM for Navier-Stokes/Korteweg model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. math::
   :label: LBE_Low_Mach

   f_{i}(\boldsymbol{x}+\boldsymbol{c}_{i}\delta t,t+\delta t)=f_{i}(\boldsymbol{x},\,t)-\frac{1}{\tau}\left[f_{i}(\boldsymbol{x},\,t)-f_{i}^{eq}(\boldsymbol{x},\,t)\right]+\delta t\mathcal{F}_{i}(\boldsymbol{x},t)

.. math::
   :label: Feq_Pseudo_Potential

   f_{i}^{eq}(\boldsymbol{x},t)=w_{i}\rho\left[1+\frac{\boldsymbol{c}_{i}\cdot\boldsymbol{u}}{c_{s}^{2}}+\frac{(\boldsymbol{c}_{i}\cdot\boldsymbol{u})^{2}}{2c_{s}^{4}}-\frac{\boldsymbol{u}\cdot\boldsymbol{u}}{2c_{s}^{2}}\right]

.. math::
   :label: Moment0_Pseudo_Potential

   \rho=\sum_{i}f_{i}\qquad
   
.. math::
   :label: Moment1_Pseudo_Potential

   \boldsymbol{u}=\frac{1}{\rho}\sum_{i}f_{i}\boldsymbol{c}_{i}+\frac{\delta t}{2}\boldsymbol{F}


Pseudo-potential methods
""""""""""""""""""""""""

Since the historical method of "Shan-Chen" many methods have been published. They are called **Pseudo-potential methods**. We present here, one of them implemented in LBM_Saclay.

.. container:: sphinx-features

   .. admonition:: Kupershtokh's forcing term

      In Eq. :eq:`LBE_Low_Mach`, the Kupershtokh's forcing term writes

      .. math::

         \mathcal{F}_{i}(\boldsymbol{x},t)=f_{i}^{eq}(\boldsymbol{u}^{\star}+\Delta\boldsymbol{u})-f_{i}^{eq}(\boldsymbol{u}^{\star})
   
      where :math:`\boldsymbol{u}^{\star}` and :math:`\Delta\boldsymbol{u}` are defined by

      .. math::
      
         \boldsymbol{u}^{\star}&=\frac{1}{\rho}\sum_{i}f_{i}\boldsymbol{c}_{i}\\
         \Delta\boldsymbol{u}&=\frac{1}{\rho}\boldsymbol{F}_{int}\delta t

      The force term :math:`\boldsymbol{F}_{int}` is defined in Eq. :eq:`Fint_Pseudo_Potential`.
      
      The subscript :math:`int` for  stands for *interaction*

   .. math::

      \hspace{4mm}

   .. admonition:: Definition of :math:`\boldsymbol{F}_{int}`

      .. math::
         :label: Fint_Pseudo_Potential

         \boldsymbol{F}_{int}=\psi(\rho)\boldsymbol{\nabla}\psi(\rho)

      where :math:`\psi(\rho)\equiv \psi^{eos}(\rho)` is called the *pseudo-potential* which is defined by

      .. math::
         :label: Psi_Pseudo_Potential

         \psi(\rho)=\sqrt{\frac{2(\rho c_{s}^{2}-p^{eos}(\rho))}{c_{s}^{2}}}
   
      where :math:`p^{eos}(\rho)` is the :ref:`Equations-Of-State`.

      The discrete version of :eq:`Fint_Pseudo_Potential` writes

      .. math::
         :label: Fint_Discrete

         \boldsymbol{F}_{int}(\boldsymbol{x},t)=\psi(\boldsymbol{x},t)\frac{1}{\delta x}\sum_{i}w_{i}\psi(\boldsymbol{x}+\boldsymbol{c}_{i}\delta t,t)\boldsymbol{c}_{i}

Potential form of pressure tensor
"""""""""""""""""""""""""""""""""

.. container:: sphinx-features

   .. admonition:: Guo's forcing term

      In Eq. :eq:`LBE_Low_Mach`, the forcing term is defined by

      .. math::
         :label: Guo_Force

         \mathcal{F}_{i}(\boldsymbol{x},t)=w_{i}\left[\frac{\boldsymbol{c}_{i}-\boldsymbol{u}}{c_{s}^{2}}+\frac{(\boldsymbol{c}_{i}\cdot\boldsymbol{u})\boldsymbol{c}_{i}}{c_{s}^{4}}\right]\cdot\boldsymbol{F}_{tot}

      where the total force :math:`\boldsymbol{F}_{tot}` is defined by Eq. :eq:`Ftot_Potential_Form`

   .. math::

      \hspace{4mm}

   .. admonition:: Definition of :math:`\boldsymbol{F}_{tot}`

      .. math::
         :label: Ftot_Potential_Form

         \boldsymbol{F}_{tot}=\boldsymbol{\nabla}\rho c_{s}^{2}-\rho\boldsymbol{\nabla}\mu_{\rho}

      where :math:`\mu_{\rho}` are defined for van der Waals and Carnahan-Starling In
      
      :ref:`Equations-Of-State` 

      
.. sectionauthor:: Alain Cartalade
   