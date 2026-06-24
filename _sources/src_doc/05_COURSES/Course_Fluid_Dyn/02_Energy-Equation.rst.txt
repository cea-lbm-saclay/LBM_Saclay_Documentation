.. _Reminder-Energy-Equation:

Energy balance equation
=======================

Formulation with total energy
-----------------------------

This section is a summary of [1]_ (section VI.3 p. 119) and reminds the derivation of energy equation. The total energy which is contained inside a volume :math:`V` is:

.. math::
   :label: eq:Total_energy_Heat-Course

   \int_{V}\rho(e+\frac{1}{2}u^{2})dV

where :math:`e` is the internal energy and :math:`\rho u^{2}/2` is the kinetic energy of fluid. From first principle of thermodynamics, the time-variation of that energy is equal to the work of forces and the heat quantity exchanged between the system and the external medium:

.. math::
   :label: eq:Variation_Total-energy_Heat-Course

   \frac{d}{dt}\int_{V}\rho(e+\frac{1}{2}u^{2})dV=\dot{W}+\dot{Q}

where :math:`\dot{W}` is the work per time unit of non-conservative forces such as the volumic force and stress force applied at the surface
of volume :math:`V`:

.. math::
   :label: eq:Work

   \dot{W}=\int_{V}\rho\boldsymbol{g}\cdot\boldsymbol{u}dV+\int_{A}\boldsymbol{t}(\boldsymbol{n})\cdot\boldsymbol{u}dA

and :math:`\dot{Q}` is the heat which is exchanged from the external to the system. Without source term, it is given by the heat flux by
conduction :math:`\boldsymbol{q}`:

.. math::
   :label: eq:Def_Heat
   
   \dot{Q}=-\int_{A}\boldsymbol{q}\cdot\boldsymbol{n}dA

.. math::
   :label: 
   
   \frac{d}{dt}\int_{V}\rho(e+\frac{1}{2}u^{2})dV=\int_{V}\rho\boldsymbol{g}\cdot\boldsymbol{u}dV+\int_{A}\boldsymbol{t}(\boldsymbol{n})\cdot\boldsymbol{u}dA-\int_{A}\boldsymbol{q}\cdot\boldsymbol{n}dA

Once again we use the Reynolds’ transport theorem for the left-hand side
and we transform both surfacic integral of right-hand side into volumic
ones with Green-Ostrogradsky’s theorem:

.. math::
   :label: 
   
   \int_{V}\left\{ \frac{\partial}{\partial t}\left[\rho(e+\frac{1}{2}u^{2})\right]+\boldsymbol{\nabla}\cdot\rho\boldsymbol{u}(e+\frac{1}{2}u^{2})\right\} dV=\int_{V}\rho\boldsymbol{g}\cdot\boldsymbol{u}dV+\int_{V}\left[-\boldsymbol{\nabla}\cdot(p\boldsymbol{u})+\boldsymbol{\nabla}\cdot(\overline{\overline{\boldsymbol{\tau}}}\cdot\boldsymbol{u})\right]dV+\int_{V}\boldsymbol{\nabla}\cdot\boldsymbol{q}dV

The volume is arbitray, hence

.. math::
   :label: eq:Balance-Energy_Heat-Course

   \frac{\partial}{\partial t}\left[\rho(e+\frac{1}{2}u^{2})\right]+\boldsymbol{\nabla}\cdot\left[\rho(e+\frac{1}{2}u^{2})\boldsymbol{u}\right]=-\boldsymbol{\nabla}\cdot(p^{eos}\boldsymbol{u})+\boldsymbol{\nabla}\cdot(\overline{\overline{\boldsymbol{\tau}}}\cdot\boldsymbol{u})-\boldsymbol{\nabla}\cdot\boldsymbol{q}+\rho\boldsymbol{g}\cdot\boldsymbol{u}

Alternative formulations
------------------------

**Formulation with internal energy**

.. math::
   :label: eq:Internal-energy_Heat-Course

   \frac{\partial(\rho e)}{\partial t}+\boldsymbol{\nabla}\cdot\left[\rho e\boldsymbol{u}\right]=-\boldsymbol{\nabla}\cdot\boldsymbol{q}-p^{eos}\boldsymbol{\nabla}\cdot\boldsymbol{u}+\overline{\overline{\boldsymbol{\tau}}}:\boldsymbol{\nabla}\boldsymbol{u}

**Formulation with total enthalpy**

.. math::
   :label: eq:Total-Enthalpy_Heat-Course

   \frac{\partial}{\partial t}\left[\rho(h+\frac{1}{2}u^{2})\right]+\boldsymbol{\nabla}\cdot\left[\rho(h+\frac{1}{2}u^{2})\boldsymbol{u}\right]=-\boldsymbol{\nabla}\cdot\boldsymbol{q}+\frac{\partial p^{eos}}{\partial t}+\boldsymbol{\nabla}\cdot(\overline{\overline{\boldsymbol{\tau}}}\cdot\boldsymbol{u})+\rho\boldsymbol{g}\cdot\boldsymbol{u}

**Formulation with enthalpy**

.. math::
   :label: eq:Enthalpy_Heat-Course
   
   \frac{\partial(\rho h)}{\partial t}+\boldsymbol{\nabla}\cdot(\rho h\boldsymbol{u})=-\boldsymbol{\nabla}\cdot\boldsymbol{q}+\overline{\overline{\boldsymbol{\tau}}}:\boldsymbol{\nabla}\boldsymbol{u}+\frac{dp^{eos}}{dt}

**Formulation with entropy**

.. math::
   :label: eq:Entropy_Heat-Course

   T\left[\frac{\partial(\rho s)}{\partial t}+\boldsymbol{\nabla}\cdot(\rho s\boldsymbol{u})\right]=-\boldsymbol{\nabla}\cdot\boldsymbol{q}+\overline{\overline{\boldsymbol{\tau}}}:\boldsymbol{\nabla}\boldsymbol{u}

**Formulation with temperature and** :math:`c_p`

.. math::
   :label: eq:Temp-Cv_Heat-Course
   
   \frac{\partial(\rho c_{p}T)}{\partial t}+\boldsymbol{\nabla}\cdot(\rho c_{p}T\boldsymbol{u})=-\boldsymbol{\nabla}\cdot\boldsymbol{q}-T\left(\frac{\partial\ln\rho}{\partial\ln T}\right)_{\rho}\frac{dp}{dt}+\overline{\overline{\boldsymbol{\tau}}}:\boldsymbol{\nabla}\boldsymbol{u}+\rho T\frac{dc_{p}}{dt}

**Formulation with temperature and** :math:`c_v`

.. math::
   :label: eq:Temp-Cp_Heat-Course
   
   \frac{\partial(\rho c_{v}T)}{\partial t}+\boldsymbol{\nabla}\cdot(\rho c_{v}T\boldsymbol{u})=-\boldsymbol{\nabla}\cdot\boldsymbol{q}-T\left(\frac{\partial p}{\partial T}\right)_{\rho}\boldsymbol{\nabla}\cdot\boldsymbol{u}+\overline{\overline{\boldsymbol{\tau}}}:\boldsymbol{\nabla}\boldsymbol{u}+\rho T\frac{dc_{v}}{dt}












Bibliography
------------

.. [1] Candel S., Mécanique des fluides, 2e édition, Dunod, 2001.
