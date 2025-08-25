.. _Math-NSAC-Comp-Solid:

Model of Navier-Stokes/Allen-Cahn/Composition interacting with a solid phase
============================================================================

The previous :ref:`Math-NSAC-Comp` is extended here to interact with a solid phase which is described by a new function noted :math:`\psi`. In the input file, the problem name ``NSAC_Comp`` remains unchanged. The new function is taken into account through new sections and options in the input file.

Mathematical model
------------------

As already said, in this model we introduce of a new field :math:`\psi\equiv\psi(\boldsymbol{x},t)` for solid phase. :math:`\phi` is the phase-field of the first fluid phase, whereas :math:`\varphi` is the phase-field of the second fluid phase. In that model :math:`\psi` is defined by its initial condition and evolves with a PDE, :math:`\phi` is defined by its initial condition and evolves with a PDE and :math:`\varphi` is obtained by the closure relationship:

.. math::
   :label: Closure
   
   \varphi(\boldsymbol{x},t)=1-\phi(\boldsymbol{x},t)-\psi(\boldsymbol{x},t)
   
.. admonition:: Mathematical model
   :class: error

   **Mass balance equation**

   The mass balance equation writes:

   .. math::
      :label: Mass_Balance_Psi
   
      \boldsymbol{\nabla}\cdot\boldsymbol{v}=-\boldsymbol{u}_{s}\cdot\boldsymbol{\nabla}\psi
   
   where the fluid velocity is noted :math:`\boldsymbol{u}` and a variable change is introduced :math:`\boldsymbol{v}=(1-\psi)\boldsymbol{u}`. In the solid phase :math:`\psi=1` and :math:`\boldsymbol{v}=\boldsymbol{0}`. In the right-hand side, :math:`\boldsymbol{u}_{s}` is the velocity of the solid phase which must be known and imposed as input parameter.

   **Impulsion balance equation**

   The impulsion balance equation writes:

   .. math::
      :label: Impulsion_Balance_Psi
   
      \varrho\left[\frac{\partial\boldsymbol{v}}{\partial t}+\boldsymbol{\nabla}\cdot(\boldsymbol{v}\boldsymbol{u})\right]=-(1-\psi)\boldsymbol{\nabla}p_{h}+\boldsymbol{\nabla}\cdot\left[\eta\left(\boldsymbol{\nabla}\boldsymbol{v}+(\boldsymbol{\nabla}\boldsymbol{v})^{T}\right)\right]+(1-\psi)\boldsymbol{F}_{tot}
   
   If :math:`\psi=1`, all terms of this equation cancel.

   **Phase-field equation**

   The phase-field equation is modified to take into account the both fields :math:`\psi` and :math:`\varphi`:

   .. math::
      :label: Phi_Equation
   
      \frac{\partial\phi}{\partial t}+\boldsymbol{\nabla}\cdot(\boldsymbol{u}\phi)=\boldsymbol{\nabla}\cdot\left\{ M_{\phi}\left[\boldsymbol{\nabla}\phi-\frac{4}{W_{\phi}}\phi(1-\phi)\boldsymbol{n}_{\phi}+\boldsymbol{\mathscr{L}}(\phi,\varphi,\psi)\right]\right\}

   In right-hand side of Eq. :eq:`Phi_Equation`, a Lagrange multiplier :math:`\boldsymbol{\mathscr{L}}` is introduced to impose the constrainst :eq:`Closure`. Its expression is:

   .. math::
      :label: Lagrange_Mult
   
      \boldsymbol{\mathscr{L}}(\phi,\varphi,\psi)=\frac{1}{2}\left[\frac{4}{W_{\psi}}\psi(1-\psi)\boldsymbol{n}_{\psi}+\frac{4}{W_{\phi}}\phi(1-\phi)\boldsymbol{n}_{\phi}+\frac{4}{W_{\varphi}}\varphi(1-\varphi)\boldsymbol{n}_{\varphi}\right]

   For every phase-field, the unit normal vector of the interface is defined by

   .. math::
      :label: Normal
   
      \boldsymbol{n}_{f}=\frac{\boldsymbol{\nabla}f}{\bigl|\boldsymbol{\nabla}f\bigr|}

   where :math:`f=\psi,\phi,\varphi`.

   **Solid phase transport equation**
   
   Finally the evolution equation on :math:`\psi` is a standard advection equation:

   .. math::
      :label: Psi_Equation
   
      \frac{\partial\psi}{\partial t}+\boldsymbol{u}_{s}\cdot\boldsymbol{\nabla}\psi=0
   
   Let us mention that the composition equation remains unchanged in that version of model. Integration of :math:`\psi`: in that equation could be done in future work.


Force terms
^^^^^^^^^^^

.. admonition:: Force terms
   :class: caution

   .. grid:: 2
      :gutter: 4
      :margin: 3 3 0 5

      .. grid-item-card:: Total force

         The total force term :math:`\boldsymbol{F}_{tot}` is the sum of two forces: the capillary force :math:`\boldsymbol{F}_{c}` and the gravity force :math:`\boldsymbol{F}_{g}`.

         .. math::
            :label: Total_Force_Solid

            \boldsymbol{F}_{tot} = \boldsymbol{F}_{c} + \boldsymbol{F}_{g}


      .. grid-item-card:: Gravity force

         The gravity force is defined by

         .. math::
            :label: Force_Gravity
   
            \boldsymbol{F}_{g}=\varrho(\boldsymbol{\phi})\boldsymbol{g}

         where :math:`\boldsymbol{\phi}=(\phi_{0},\phi_{1},\phi_{2})` and we have introduced the notations :math:`\phi_{0}\equiv\varphi`, :math:`\phi_{1}\equiv\phi` and :math:`\phi_{2}\equiv\psi`.


   .. grid:: 2
      :gutter: 4
      :margin: 3 3 0 5

      .. grid-item-card:: Capillary force
   
         .. math::
            :label: Force_Capillary
   
            \boldsymbol{F}_{c}=\mu_{\phi}\boldsymbol{\nabla}\phi+\mu_{\varphi}\boldsymbol{\nabla}\varphi+\mu_{\psi}\boldsymbol{\nabla}\psi
   
         The first term of the righ-hand side corresponds to the capillary force between fluid 1 (:math:`\phi`) and fluid 2 (:math:`\varphi`) which involves the surface tension :math:`\sigma_{12}`. The second term corresponds to the capillary force between fluid 1 (:math:`\phi`) and solid (:math:`\psi`) which involves the surface tension :math:`\sigma_{1s}`. Finally, the last term corresponds to the capillary force between fluid 2 (:math:`\phi`) and solid (:math:`\psi`) which involves the surface tension :math:`\sigma_{2s}`.
   

      .. grid-item-card:: Chemical potentials
      
         With the notations of gravity force, the chemical potentials write

         .. math::
            :label: Chemical-Potential_Solid
   
            \mu_{\phi_{k}}(\boldsymbol{x},t)=\frac{4\gamma_{T}}{W}\sum_{\ell\neq k}\left[\frac{1}{\gamma_{\ell}}\left(\frac{\partial f_{dw}}{\partial\phi_{k}}-\frac{\partial f_{dw}}{\partial\phi_{\ell}}\right)\right]-\frac{3}{4}W\gamma_{k}\boldsymbol{\nabla}^{2}\phi_{k}


Closure relationships
^^^^^^^^^^^^^^^^^^^^^

.. math::
   :label: Density_Total
   
   \varrho=\phi\rho_1+\varphi\rho_2+\psi\rho_{s}

where :math:`\rho_1` is the bulk density of first fluid phase, :math:`\rho_2` is the bulk density of second fluid phase, and :math:`\rho_s` is the solid density. The total viscosity :math:`\eta` is interpolated only with bulk properties of fluid phases:

.. math::
   :label: Viscosity_Total
   
   \frac{1}{\eta}=\frac{\phi}{\eta_1}+\frac{(1-\phi)}{\eta_2}
   
The harmonic mean is used.
   

List of input parameters in ``.ini`` file
-----------------------------------------

**Section** ``[init_solid]``

   In ``.ini`` file, this section is necessary for initialization of funtion :math:`\psi`. Option ``solid_phase`` must be set equal to ``1`` to activate the solid phase:
   
   - ``solid_phase=1``
   
   Three other parameters are required in the model:
   
   - ``W_sol=``: interface width of solid phase
   - ``rho_sol=``: solid density
   - ``Mphi_sol=``: interface mobility of solid phase
   
   .. warning::
      Even though it is possible to set different values, it is highly recommended to set identical values for solid phase and fluid phase interface properties: :math:`W_{\psi}=W_{\phi}=W_{\varphi}` and :math:`M_{\psi}=M_{\phi}=M_{\varphi}`. In practice, the same parameter value must be set for ``W`` and ``W_sol`` and ``Mphi`` and ``Mphi_sol``.
   
   Next several parameters dependent of the initialization must set:
   
   - ``init_solid_type=``: keyword of solid initial condition
   
   If ``init_solid_type=container_hole``, then the following parameters are required
   
   - ``x0_gl=``
   - ``y0_gl=``
   - ``width_gl=``
   - ``height_gl=``
   - ``thickness_gl=``
   - ``h_glass=``
   - ``length_hole_gl=``
   
   Other examples of initial conditions for :math:`\psi` can be found inside folder ``run_training_lbm``.

**Section** ``[move_solid]``
   
   In ``.ini`` file, this section is necessary for indicating how the solid phase moves. More particularly the parameters of this section are necessary for :math:`\boldsymbol{u}_s` in Eq. :eq:`Psi_Equation`.
   
   - ``move_solid_type=``: keyword to indicate what sort of displacement is imposed.
   
   If ``move_solid_type=``
   
**Section** ``[contact_angle]``

   In ``.ini`` file, this section is necessary for calculating the three surface tension forces. By default, only the capillary forcce between both fluid phases is computed. If ``contact_angle=1``, then the two last forces of Eq. :eq:`Force_Capillary` are also computed.
   
   - ``contact_angle=1``
   
   If that option is equal to ``1``, then the values of surface tension between fluid 1 and solid :math:`\sigma_{1s}` and between fluid 2 and solid :math:`\sigma_{2s}` have to be set:
   
   - ``sigma_phi1_solid=``: positive real value
   - ``sigma_phi2_solid=``: positive real value

Examples of simulations with that model
---------------------------------------

Several examples are available in the folder ``run_training_lbm`` to practice two-phase flows interacting with a solid phase: see :ref:`TwoP-Solid-Training-LBM`.

.. sectionauthor:: Alain Cartalade
   