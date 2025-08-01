Methodology to set your own parameters in input file
====================================================

For new LBM users, it is recommended to start with the test cases of folder ``run_training_lbm``, because several examples are given to set dimensionless parameters inside the input file of LBM_Saclay. You will find python scripts to help users to convert parameters given in S.I. units into dimensionless parameters.

How to set dimensionless parameters
-----------------------------------

Most of two-phase test cases of that folder use physical properties of water and air (see first Table below) expressed in lattice units. Those lattice units (lu) are derived by setting the reference length as :math:`\delta x`, the reference time as :math:`\delta t`, the reference mass as :math:`\rho`.

Other parameters such as gravity, surface tension, etc. are derived by using the dimensionless characteristic numbers which control the flows (Reynolds, Bond, Weber, Morton, etc.), i.e. by applying the :ref:`Law-Similarity`.

Law of similarity for single-phase
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Most of the time, in LBM publications, the input parameters are dimensionless and the results are presented in *Lattice Units*. The dimensionless parameters are obtained by setting one length of reference :math:`\ell_{ref}`, one time of reference :math:`t_{ref}` and one mass of reference :math:`\rho_{ref}`. The other parameters are derived by applying the **law of similarity**. In this section the procedure is reminded to set dimensionless parameters in the input file of LBM_Saclay.

In LBM_Saclay, the choice is left to users if they want to work with parameters with physical units or not. Nevertheless, one important stability criterion must be kept in mind for LBM simulations: the fluid velocity magnitude :math:`|\boldsymbol{u}|` has to be lower than the sound speed :math:`c_s=(1/\sqrt3)\delta x/\delta t` where :math:`\delta x` is the spatial discretization and :math:`\delta t` is the time-step of time discretization. If the velocity is to close or greater than :math:`c_s`, the simulation will be unstable.

.. admonition:: Law of similarity

   Two incompressible flows are dynamically similar if they have the same Reynolds number and geometry. With different words, the results of two simulations will be the same provided that the Reynolds number and the geometry are identical:

   .. math::
      :label: Re_similarity

      \text{Re}=\frac{\bigl|\boldsymbol{u}\bigr|L}{\nu}=\frac{\bigl|\boldsymbol{u}_{sim}\bigr|L_{sim}}{\nu_{sim}}

   where :math:`u`, :math:`L` and :math:`\nu` have physical dimensions, whereas :math:`u_{sim}`, :math:`L_{sim}` and :math:`\nu_{sim}` are dimensionless quantities obtained from references of length :math:`\ell_{ref}`, of time :math:`t_{ref}` and mass :math:`\rho_{ref}`.

.. admonition:: Coefficients of conversion

   To convert the results without dimensions to results with physical dimensions, it is necessary to convert them with coefficients of conversion. They are obtained with :math:`\ell_{ref}`, of time :math:`t_{ref}` and :math:`\rho_{ref}`:

   .. math::
      :label: conversion

      \underbrace{C_{u}=\frac{\ell_{ref}}{t_{ref}}}_{\text{Velocity}},\qquad\underbrace{C_{\nu}=\frac{\ell_{ref}^{2}}{t_{ref}}}_{\text{Viscosity}},\qquad\underbrace{C_{g}=\frac{\ell_{ref}}{t_{ref}^{2}}}_{\text{Gravity}},\qquad\underbrace{C_{p}=\frac{C_{\rho}\ell_{ref}^{2}}{t_{ref}^{2}}}_{\text{Pressure}}

.. admonition:: For LBM: lattice units (l.u.)
   :class: hint

   The lattice units correspond to the case :math:`\ell_{ref}=\delta x` and :math:`t_{ref}=\delta t`:

   .. math::
      :label: dxdt_star

      \delta x^{\star}=\frac{\delta x}{\delta x}=1,\qquad\delta t^{\star}=\frac{\delta t}{\delta t}=1

   The reference density is one of the two bulk densities, e.g. the greater one: :math:`\rho_{ref}=\rho_l` where the index :math:`l` stands for liquid.

   .. math::
      :label: rho_star

      \rho_l^{\star}=\frac{\rho_l}{\rho_{ref}}=1,\qquad\rho_g^{\star}=\frac{\rho_g}{\rho_{ref}}

   In that case, the factors of conversion Eq. :eq:`conversion` between dimensionless results of simulations and quantities with physical dimension are:

   .. math::
      :label: C_U_nu_g_p

      C_{u}=\frac{\delta x}{\delta t},\qquad C_{\nu}=\frac{\delta x^{2}}{\delta t},\qquad C_{g}=\frac{\delta x}{\delta t^{2}},\qquad C_{p}=\rho_{ref}\frac{\delta x^{2}}{\delta t^{2}},\qquad C_{\sigma}=\rho_{ref}\frac{\delta x^{3}}{\delta t^{2}}

   With those factors, the remaining dimensionless quantities can be derived:

   .. math::
      :label: Quantities_star

      L^{\star}=\frac{L}{\delta x},\qquad u^{\star}=\frac{u}{C_{u}},\qquad\nu^{\star}=\frac{\nu}{C_{\nu}},\qquad g^{\star}=\frac{g}{C_{g}},\qquad \sigma^{\star}=\frac{\sigma}{C_{\sigma}}

   The Reynolds number is

   .. math::
      :label:

      \text{Re}=\frac{u^{\star}L^{\star}}{\nu^{\star}}

.. admonition:: For training session: law of similarity applied to Poiseuille flow
   :class: error

   The law of similarity is applied on Poiseuille flow.

   .. toctree::
      :maxdepth: 1

      ./LawOfSimilarity_Poiseuille.rst

Law of similarity for two-phase
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In :ref:`Law-Similarity`, the procedure has been described to derive the dimensionless parameters to set in the input file. The example was given on the single-phase fluid flow: the Poiseuille flow. Here we present the methodology for two-phase flows on two examples: "Rayleigh-Taylor instability" and an "air bubble rising inside a channel filled of water". For two-phase with interface-tracking, there is an additional parameter to set: the surface tension between both phases. In this Section, we first remind the standard dimensionless number for two-phase flows involving that new parameter. Next we describe the methodology to set dimensionless paramaters.

Dimensionless numbers for two-phase
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When the gravity is taken into account in simulations, another dimensionless number can be used: the Froude number compares one characteristic velocity :math:`U_c` to the characteristic velocity due to gravity :math:`g` in a domain of width :math:`L`: :math:`U_g=\sqrt{gL}`

.. container:: sphinx-features

   .. admonition:: Reynolds number 
      
      .. math::

         \text{Re}=\frac{U_cL}{\nu}

   .. math::

      \hspace{3mm}

   .. admonition:: Froude number
      
      .. math::

         \text{Fr}=\frac{U_c}{\sqrt{gL}}

For two-phase, there is a new parameter, the surface tension :math:`\sigma` which a property of the interface between both phases. That new parameter is involved in three new dimensionless numbers which compare the surface tension force with forces of gravity (Bond number), of viscosity (Capillary number), and inertia (Weber number). For a two-phase problem, one simulation must respect those dimensionless number in order to simulate the same underlying physics.

The competition between surface tension and gravity is given by the Bond number (Bo) or Eötvös (Eo). It can be defined as the ratio of hydrostatic pressure difference :math:`\Delta p_h` over the capillary pressure difference :math:`\Delta p_c`. It can also be defined as the ratio of :math:`L^2` over the capillary length :math:`\ell_c^2=\sigma/\rho g`

.. container:: sphinx-features

   .. admonition:: Bond number 
      
      .. math::

         \text{Bo}=\frac{\Delta p_{h}}{\Delta p_{c}}=\frac{\rho g(2R)}{2\sigma/R}=\frac{\rho gR^{2}}{\sigma}

   .. math::

      \hspace{3mm}

   .. admonition:: Weber number 
      
      .. math::

         \text{We}=\frac{\rho U^{2}L}{\sigma}

   .. math::

      \hspace{3mm}

   .. admonition:: Capilary number 
      
      .. math::

         \text{Ca}=\frac{\text{We}}{\text{Re}}=\frac{\rho U^{2}L/\sigma}{UL/\nu}=\frac{\eta U}{\sigma}

The Weber number compares the kinetic energy and the energy of interface (surface tension). The capillary number compare dynamic viscosity with surface tension. Finally, a commonly used dimensionless number for shapes of bubbles is the Morton (Mo) number. It can be defined from We, Fr and Re and make appear in the same number the gravity :math:`g`, the dynamic viscosity :math:`\eta` and the surface tension :math:`\sigma`. 

.. container:: sphinx-features

   .. admonition:: Morton number 
      
      .. math::

         \text{Mo}=\frac{\text{We}^{3}}{\text{Fr}^{2}\text{Re}^{4}}=\frac{gL\left(\rho U^{2}L/\sigma\right)^{3}}{U^{2}(\rho UL/\eta)^{4}}=\frac{g\eta^{4}}{\rho\sigma^{3}}


.. admonition:: For training session: practice with Rayleigh-Taylor instability
   :class: error

   Application of law of similarity for two-phase is presented on the Rayleigh-Taylor instability.

   .. toctree::
      :maxdepth: 1

      ./LawOfSimilarity_Two_Phase.rst

Recipes for stability and accuracy
----------------------------------

Once the Chapman-Enskog expansion is performed, the Navier-Stokes equations are recovered provided that :math:`|\boldsymbol{u}|<c_s` where :math:`c_s=\delta x/(\delta t \sqrt{3})`, :math:`\delta x` is the space-step and :math:`\delta t` is the time step. In lattice unit :math:`\delta x^{\star}=\delta t^{\star}=1`, that condition means that the maximum dimensionless velocity :math:`|\boldsymbol{u}_{max}^{\star}|` has to be lower than

.. math::
   :label: Stability_Cond

   |\boldsymbol{u}_{max}^{\star}| < \frac{1}{\sqrt{3}}\approx 0.577

for lattices D2Q9, D3Q15, D3Q19 and D3Q27. For one-dimensional lattice D1Q3 that condition is :math:`|\boldsymbol{u}_{max}^{\star}| < \sqrt{2/3}\approx 0.816`.

Another stability condition involves the collision rate :math:`\tau` in the BGK collision operator. That coefficient is directly related to the kinematic viscosity by :math:`\nu=(1/3)(\tau-0.5)c_s^2\delta t`. The relaxation rate must be strictly greater than 0.5.

.. container:: sphinx-features

   .. admonition:: Stability conditions
      :class: hint

      Two main conditions have to be respected:

      - :math:`|\boldsymbol{u}_{max}^{\star}| < \frac{1}{\sqrt{3}}\approx 0.577`
      - :math:`\tau > 0.5`

   .. math::

      \hspace{3mm}

   .. admonition:: Accuracy
      :class: hint

      For accurate simulations

      - :math:`|\boldsymbol{u}_{max}^{\star}| < 0.01 - 0.3`
      - :math:`\tau` not much larger than unity
      - :math:`\delta x` and :math:`\delta t` sufficiently fine

Alternative collision operators
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The recipes of stability are given for the simplest one, the BGK operator. For two-phase flows with high denstiy ratio, alternative collision such as ``TRT`` and ``MRT`` exist in the literature and are available in LBM_Saclay. For those operators, one additional parameter for TRT controls the stability and accuracy. For MRT many other can affect stability and accuracy.

.. sectionauthor:: Alain Cartalade
   