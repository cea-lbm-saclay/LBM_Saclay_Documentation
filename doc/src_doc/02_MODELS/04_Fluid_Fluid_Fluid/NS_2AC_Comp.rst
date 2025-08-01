.. _Math-NS2AC-Comp:

Model of fluid flow for three immiscible phases
===============================================

That model is an extension of :ref:`Math-NSAC-Comp` for three immiscible fluids. The philosophy is identical as :ref:`Math-NSAC-Comp-Solid`. Two other phase-fields are introduced to model every fluid phase: :math:`\phi_{k}` for :math:`k=0,1,2`. Two PDEs are solved, the first one for :math:`\phi_{1}` and the second one for :math:`\phi_{2}`. The last phase-field is obtained by the conservation principle which writes:

.. math::
   :label: Closure_NS2AC_Comp
   
   \phi_{0}=1-\phi_{1}-\phi_{2}

In what follows, the notation :math:`\boldsymbol{\phi}=(\phi_{0},\phi_{1},\phi_{2})` will be used.


Mathematical model
------------------

**Mass balance**

The mass balance equation writes

.. math:: 
   :label: NS2AC_Comp_Mass_Balance
   
   \boldsymbol{\nabla}\cdot\boldsymbol{u}=0

where :math:`\boldsymbol{u}=(u_{x},u_{y},u_{z})` is the velocity vector.

**Impulsion balance**

The impulsion balance equation is

.. math::
   :label: NS2AC_Comp_Impulsion_Balance
   
   \varrho(\boldsymbol{\phi})\left[\frac{\partial\boldsymbol{u}}{\partial t}+\boldsymbol{\nabla}\cdot(\boldsymbol{u}\boldsymbol{u})\right]=-\boldsymbol{\nabla}p_{h}+\boldsymbol{\nabla}\cdot\left[\varrho\vartheta(\boldsymbol{\phi})\left(\boldsymbol{\nabla}\boldsymbol{u}+\boldsymbol{\nabla}\boldsymbol{u}^{T}\right)\right]+\boldsymbol{F}_{tot}

where :math:`\varrho(\boldsymbol{\phi})` is the total density and :math:`\vartheta(\boldsymbol{\phi})` is the total viscosity. They are respectively defined by Eqs :eq:`NS2AC_Comp_Total_Density` and :eq:`NS2AC_Comp_Total_Viscosity`. The hydrodynamic pressure is noted :math:`p_{h}` and :math:`\boldsymbol{F}_{tot}` is the total force defined by Eq. :eq:`NS2AC_Comp_Total_Force`.

**First phase-field equation**

.. math::
   :label: NS2AC_Comp_Phi1
   
   \frac{\partial\phi_{1}}{\partial t}+\boldsymbol{\nabla}\cdot(\boldsymbol{u}\phi_{1})=\boldsymbol{\nabla}\cdot\Bigl[M_{\phi}\bigl(\boldsymbol{\nabla}\phi_{1}-\bigl|\boldsymbol{\nabla}\phi_{1}\bigr|^{eq}\boldsymbol{n}_{1}+\mathscr{L}(\boldsymbol{\phi})\bigr)\Bigr]

where the Lagrange multiplier is defined by

.. math:: \mathscr{L}(\boldsymbol{\phi})=\frac{1}{3}\sum\bigl|\boldsymbol{\nabla}\phi_{k}\bigr|^{eq}\boldsymbol{n}_{k}

and the unit normal vector for each phase :math:`k` is defined by

.. math::
   :label: NS2AC_Comp_Normal_Vect
   
   \boldsymbol{n}_{k}=\frac{\boldsymbol{\nabla}\phi}{\bigl|\boldsymbol{\nabla}\phi\bigr|}


**Second phase-field equation**

.. math::
   :label: NS2AC_Comp_Phi2
   
   \frac{\partial\phi_{2}}{\partial t}+\boldsymbol{\nabla}\cdot(\boldsymbol{u}\phi_{2})=\boldsymbol{\nabla}\cdot\Bigl[M_{\phi}\bigl(\boldsymbol{\nabla}\phi_{2}-\bigl|\boldsymbol{\nabla}\phi_{2}\bigr|^{eq}\boldsymbol{n}_{2}+\mathscr{L}(\boldsymbol{\phi})\bigr)\Bigr]

**Composition equation**


.. math::
   :label: NS2AC_Comp_Composition
   
   \frac{\partial c}{\partial t}+\boldsymbol{\nabla}\cdot(\boldsymbol{u}c)=\boldsymbol{\nabla}\cdot\left\{ (D_{k}\phi_{k})\boldsymbol{\nabla}\bigl[\mu_{c}^{eq}+c(\phi,\mu_{c})-c_{k}^{eq}\phi_{k}\bigr]\right\}
   

.. note::
   
   Compared to the :ref:`Math-NSAC-Comp-Solid`, the differences come from the form of PDE on :math:`\phi_2` (resp. :math:`\psi`) and the form of the Lagrange multiplier :math:`\mathscr{L}(\boldsymbol{\phi})`.

Force terms
-----------

**Total force**

The total force is the sum of the capillary force :math:`\boldsymbol{F}_{c}` and the gravity force :math:`\boldsymbol{F}_{g}`:

.. math::
   :label: NS2AC_Comp_Total_Force
   
   \boldsymbol{F}_{tot}=\boldsymbol{F}_{c}+\boldsymbol{F}_{g}

**Capillary forces**

The capillary force is the sum of contribution of every phase-field:

.. math::
   :label: NS2AC_Comp_Capillary_Force

   \boldsymbol{F}_{c}=\mu_{\phi_{0}}\boldsymbol{\nabla}\phi_{0}+\mu_{\phi_{1}}\boldsymbol{\nabla}\phi_{1}+\mu_{\phi_{2}}\boldsymbol{\nabla}\phi_{2}
   
where the chemical potential :math:`\mu_{\phi_{k}}` for each phase :math:`k` is defined by

.. math:: 
   :label: NS2AC_Comp_ChemPot
   
   \mu_{\phi_{k}}(\boldsymbol{x},t)=\frac{4\gamma_{T}}{W}\sum_{\ell\neq k}\left[\frac{1}{\gamma_{\ell}}\left(\frac{\partial f_{dw}}{\partial\phi_{k}}-\frac{\partial f_{dw}}{\partial\phi_{\ell}}\right)\right]-\frac{3}{4}W\gamma_{k}\boldsymbol{\nabla}^{2}\phi_{k}

and the spreading coefficient :math:`\gamma_{T}` is the harmonic mean of each one:

.. math:: 
   :label: NS2AC_Comp_Spread
   
   \frac{3}{\gamma_{T}}=\sum_{k}\frac{1}{\gamma_{k}}

and the double-well potential is:

.. math:: f_{dw}(\phi_{0},\phi_{1},\phi_{2})=\sum_{k=0}^{2}\frac{12}{W}\left[\frac{\gamma_{k}}{2}\phi_{k}^{2}(1-\phi_{k})^{2}\right]

The spreading coefficient of each phase is defined by a combination of
their surface tensions:

.. math::
   \begin{aligned}
   \gamma_{0} & =\sigma_{10}+\sigma_{20}-\sigma_{12}\\
   \gamma_{1} & =\sigma_{10}+\sigma_{12}-\sigma_{20}\\
   \gamma_{2} & =\sigma_{20}+\sigma_{12}-\sigma_{01}\end{aligned}

**Gravity force**

The gravity force writes:

.. math:: 
   :label: NS2AC_Comp_Gravity_Force
   
   \boldsymbol{F}_{g}=\varrho(\boldsymbol{\phi})\boldsymbol{g}
   

Closure terms
-------------

**Total density**

The total density is simply an interpolation of each bulk density:

.. math:: 
   :label: NS2AC_Comp_Total_Density
   
   \varrho(\boldsymbol{\phi})=\sum_{k}\rho_{k}\phi_{k}(\boldsymbol{x},t)
   
**Total kinematic viscosity**

The total kinematic viscosity is obtained by a harmoni mean of bulk
kinematic viscosities:

.. math::
   :label: NS2AC_Comp_Total_Viscosity
   
   \frac{1}{\vartheta(\boldsymbol{\phi})}=\sum_{k}\frac{\phi_{k}(\boldsymbol{x},t)}{\nu_{k}}


Examples of simulations with that model
---------------------------------------

**Double-Serpentine**

.. container:: sphinx-features

   .. raw:: html

      <video controls src="../../../_static/Vid_ThreePhases_Vortex_Phi1-Phi2.webm" width="500" height="370"> </video>

**Spreading lenses**

.. container:: sphinx-features

   .. raw:: html

      <video controls src="../../../_static/Vid_ThreePhases_SpreadingCapsule_vB.webm" width="600" height="420"> </video>


**Spinodal decomposition of three immiscible fluids**

.. container:: sphinx-features

   .. raw:: html

      <video controls src="../../../_static/Vid_ThreePhases_Spinodal_Test22_vD.webm" width="480" height="320"> </video>

   .. raw:: html

      <video controls src="../../../_static/Vid_ThreePhases_Spinodal_Test22_vE.webm" width="480" height="320"> </video>

**Rayleigh-Taylor and splash of three immiscible fluids**

.. container:: sphinx-features

   .. raw:: html

      <video controls src="../../../_static/Vid_ThreePhases_RayleighTaylor_Splashing.webm" width="900" height="520"> </video>


.. sectionauthor:: Alain Cartalade
   