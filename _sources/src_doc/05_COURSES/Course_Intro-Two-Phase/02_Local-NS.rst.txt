.. _Local-Instantaneous-NS:

Local and instantaneous Navier-Stokes equations
===============================================

Two-fluid formulation without phase-change
------------------------------------------

That section is a summary of [1]_ (section 3.2 page 205). We consider a control volume :numref:`Fig-Volume-Control` with two fluids of index 1 and 2 seprated by one interface. The volume of each fluid is :math:`V_k` with :math:`k=1,2`, the surrounding surface is noted :math:`A_k` and the surface of separation is :math:`A_i` where the index :math:`i` means *interface*.

.. _Fig-Volume-Control:
   
.. figure:: ../../FIGS/04_FIGS_COURSES/Two-Phase_Volume-Control.png
   :figclass: align-center
   :align: center
   :height: 220
   :width: 500
   :scale: 100 %

   Control volume of two-phase flows

Mass balance
""""""""""""
The mass balance for each fluid writes

.. math::

   \begin{aligned}
      \frac{\partial\rho_{1}}{\partial t}+\boldsymbol{\nabla}\cdot(\rho_{1}\boldsymbol{u}_{1}) & =0\\
      \frac{\partial\rho_{2}}{\partial t}+\boldsymbol{\nabla}\cdot(\rho_{2}\boldsymbol{u}_{2}) & =0
   \end{aligned}

In more compact form with index :math:`k=1,2` for fluid 1 and fluid 2:

.. math::
   
   \boxed{\frac{\partial\rho_{k}}{\partial t}+\boldsymbol{\nabla}\cdot(\rho_{k}\boldsymbol{u}_{k})=0}

The local and instantaneous equation at interface writes:

.. math::
   :label: eq:Mass-Balance_Interface_TwoPhase-Course

   \rho_{1}(\boldsymbol{u}_{1}-\boldsymbol{u}_{i})\cdot\boldsymbol{n}_{1}=\rho_{2}(\boldsymbol{u}_{2}-\boldsymbol{u}_{i})\cdot\boldsymbol{n}_{2}=0

It expresses the mass balance through the interface. It is common to set:

.. math:: \dot{m}_{k}:=\rho_{k}(\boldsymbol{u}_{k}-\boldsymbol{u}_{i})\cdot\boldsymbol{n}_{k}

where :math:`\dot{m}_{k}` is the local mass flux of phase :math:`k`
which goes out the domain occupied by phase :math:`k` at one point of
the interface. With that quantity Eq.
:eq:`eq:Mass-Balance_Interface_TwoPhase-Course` writes:

.. math:: \dot{m}_{1}+\dot{m}_{2}=0

.. math::

   \begin{aligned}
      (\boldsymbol{u}_{1}-\boldsymbol{u}_{i})\cdot\boldsymbol{n}_{1} & =0\\
      (\boldsymbol{u}_{2}-\boldsymbol{u}_{i})\cdot\boldsymbol{n}_{2} & =0
   \end{aligned}

.. math::
   
   \boldsymbol{u}_{1}\cdot\boldsymbol{n}_{1}+\boldsymbol{u}_{2}\cdot\boldsymbol{n}_{2}=0

If we assume that both fluids do not slip, then the tangential
velocities are identical :math:`\boldsymbol{u}_{1}^{t}=\boldsymbol{u}_{2}^{t}` and

.. math::
   
   \boxed{\boldsymbol{u}_{1}=\boldsymbol{u}_{2}}

Without phase change and no-slip of both fluids, the velocity of each
phase is identical.

Impulsion balance with surface tension
""""""""""""""""""""""""""""""""""""""

The impulsion balance for each bulk phase writes:

.. math::
   
   \boxed{\frac{\partial(\rho_{k}\boldsymbol{u}_{k})}{\partial t}+\boldsymbol{\nabla}\cdot(\rho_{k}\boldsymbol{u}_{k}\boldsymbol{u}_{k})=\boldsymbol{\nabla}\cdot\overline{\overline{\boldsymbol{T}}}_{k}+\rho_{k}\boldsymbol{g}}

where :math:`\overline{\overline{\boldsymbol{T}}}_{k}` is the stress tensor which is defined by Eq. :eq:`eq:Decomposition-Stress-Tensor-NS-Course` for each phase :math:`k`. At interface, the impulsion balance through an element of interface writes

.. math::

   \begin{aligned}
      \frac{d}{dt}\int_{V_{1}}\rho_{1}\boldsymbol{u}_{1}dV+\frac{d}{dt}\int_{V_{2}}\rho_{2}\boldsymbol{u}_{2}dV & =-\int_{A_{1}}\rho_{1}\boldsymbol{u}_{1}(\boldsymbol{u}_{1}\cdot\boldsymbol{n}_{1})dA-\int_{A_{2}}\rho_{2}\boldsymbol{u}_{2}(\boldsymbol{u}_{2}\cdot\boldsymbol{n}_{2})dA+\int_{V_{1}}\rho_{1}\boldsymbol{F}dV+\int_{V_{2}}\rho_{2}\boldsymbol{F}dV\\
      & \qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad+\int_{A_{1}}\boldsymbol{n}_{1}\cdot\overline{\overline{\boldsymbol{T}}}_{1}dA+\int_{A_{1}}\boldsymbol{n}_{1}\cdot\overline{\overline{\boldsymbol{T}}}_{1}dA+\oint_{C}\sigma\boldsymbol{n}_{i}dC
   \end{aligned}

where :math:`\sigma` is the surface tension and
:math:`\boldsymbol{n}_{i}` is the unit normal vector of :math:`C` and
directed toward outside the volume :math:`V`. The impulsion balance the
local instantaneous relation at interface:

.. math::
   
   \dot{m}_{1}\boldsymbol{u}_{1}+\dot{m}_{2}\boldsymbol{u}_{2}-\boldsymbol{n}_{1}\cdot\overline{\overline{\boldsymbol{T}}}_{1}-\boldsymbol{n}_{2}\cdot\overline{\overline{\boldsymbol{T}}}_{2}+\underbrace{\frac{d\sigma}{ds}\boldsymbol{t}}_{\text{Marangoni term}}-\underbrace{\frac{\sigma}{R}\boldsymbol{n}_{1}}_{\text{Young-Laplace term}}=0

where :math:`s` is the curvilinear coordinate at interface, :math:`\boldsymbol{t}` is the tangential unit vector at interface and
:math:`R` is the curvature radius. The term :math:`d\sigma/ds` is related to Marangoni effects due to variation of surface tension with
temperature or concentration at interface. The term :math:`\sigma\boldsymbol{n}_{1}/R` is the Young-Laplace term. In static case, we obtain:

.. math::
   :label: Laplace-Law_TwoPhase-Course
   
   \boxed{P_{1}-P_{2}=\frac{\sigma}{R}}


One-fluid formulation for incompressible fluids
-----------------------------------------------

In one-fluid formulation, there are only one mean velocity :math:`\boldsymbol{u}` and one mean pressure for two fluids of bulk densities :math:`\rho_1` and :math:`\rho_2` and dynamic viscosity :math:`\eta_1` and :math:`\eta_2`. We must introduce a new numerical quantity to track the interface and respect the jump conditions.


Bibliography
------------

.. [1] Delhaye J.M., Thermohydraulique des réacteurs, Collection Génie Atomique, INSTN, EDP Sciences, 2008.

.. [2] Andrea Prosperetti. Motion of two superposed viscous fluids. The Physics of Fluids, 24(7):1217–1223, 07 1981. URL: https://doi.org/10.1063/1.863522.

