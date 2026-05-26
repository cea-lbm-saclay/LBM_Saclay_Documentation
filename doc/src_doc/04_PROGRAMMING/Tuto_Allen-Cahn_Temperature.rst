.. include:: ../Substitutions.rst

.. _Tuto-Allen-Cahn-Temperature:

Implementation of Allen-Cahn coupled with temperature for phase change problems
===============================================================================

Objective of this 2nd tutorial
------------------------------
The starting point is the kernel ``ADE_for_AC-Temp_Tutorial`` which simulates (again) the Advection-Diffusion Equation (ADE) with the lattice Boltzmann method:

.. math::
   :label: Tuto-ACT-Eq-ADE

   \frac{\partial c}{\partial t}+\boldsymbol{\nabla}\cdot(\boldsymbol{u}c)=D\boldsymbol{\nabla}^{2}c

.. admonition:: Mathematical model
   :class: error

   In this tutorial we will implement a model to simulate a phase change problem composed of two coupled PDEs, a first one for the evolution of dimensionless temperature:

   .. math::
      :label: Tuto_ACT-Eq-Temp

      \frac{\partial\theta}{\partial t}=D\boldsymbol{\nabla}^{2}\theta-\frac{\partial\phi}{\partial t}

   where :math:`\theta` is a dimensionless temperature, :math:`D` is the diffusivity parameter and :math:`\phi` the phase-field. The second equation is for the evolution of phase-field:

   .. math::
      :label: Tuto-ACT-Eq-phi

      \frac{\partial\phi}{\partial t}=M_{\phi}\boldsymbol{\nabla}^{2}\phi-\frac{16M_{\phi}}{W^{2}}\phi(1-\phi)(1-2\phi)-\frac{4D}{\mathscr{A}W^{2}}(\theta_{I}-\theta)\phi(1-\phi)

   where :math:`M_{\phi}` is the mobility parameter, :math:`W` is the interface thickness, :math:`\mathscr{A}=10/48` is known parameter and :math:`\theta_I` the temperature at interface.


.. admonition:: Objective
   :class: important

   In this tutorial we will see how to
      
   - add a new equation and all related stages (setup_collider, update, boundary conditions, etc.)
   - add source terms of Eqs. :eq:`Tuto_ACT-Eq-Temp` and :eq:`Tuto-ACT-Eq-phi`.
      
   The verification will be carried out with one analytical solution of the Stefan problem (see section 4). We will

   - compare the outputs of LBM_Saclay with an analytical solution
   - see the impact of linear and harmonic interpolation of diffusivity :math:`D(\phi)`

1. Create a new kernel for Allen-Cahn/Temperature
-------------------------------------------------

.. admonition:: Make the new kernel ``ACT`` in a new folder ``Allen-Cahn-Temp_Tutorial``
   :class: note

   That stage 1. is the same than the first tutorial on Cahn-Hilliard.

      - Copy the folder ``ADE_for_AC-Temp_Tutorial`` and rename it ``Allen-Cahn-Temp_Tutorial``
      - Modify ``_ADE`` (for Advection-Diffusion Equation) by ``_ACT`` (for Allen-Cahn/Temperature).

.. dropdown:: Details of commands
   :icon: comment

   .. admonition:: Copy the ADE kernel template and rename all files with new extension ``_ACT``
      :class: note

      - Copy and rename the folder ``ADE_for_AC-Temp_Tutorial`` which is contained in ``kernels/Templates_for_Tutorials``.

       .. dropdown:: Commands
          :icon: comment

          .. code-block:: shell

             $ cd LBM_Saclay_Rech-Dev/src/kernels
             $ cp -r Templates_for_Tutorials/ADE_for_CH-Tutorial ./Allen-Cahn-Temp_Tutorial

          .. admonition:: Remarks
             :class: important

             - Your new developments will be performed in the folder ``Cahn-Hilliard_Tutorial``
             - The folder name ``ADE_for_AC-Temp_Tutorial`` will be used for compilation

      - All files have the extension ``_ADE`` for Advection Diffusion Equation. Rename them with ``_ACT`` for Allen-Cahn Temperature.

       .. dropdown:: Commands
          :icon: comment

          .. code-block:: shell

             $ cd Cahn-Hilliard_Tutorial

             $ mv Index_ADE.h Index_ACT.h
             $ mv LBMScheme_ADE.h LBMScheme_ACT.h
             $ mv Models_ADE.h Models_ACT.h
             $ mv Problem_ADE.h Problem_ACT.h

   .. admonition:: Edit them and change strings ``_ADE`` with ``_ACT``
      :class: note

      1. Change strings ``_ADE`` with ``_ACT``

         - Open all files in your favorite editor (e.g. ``geany`` or ``codium``).
         - Search in all files the strings ``_ADE`` and replace them with ``_ACT`` (``Ctrl H`` with ``geany``).
   
      2. Change the problem name: in file ``Setup.h`` modify the problem name ``ADE`` with ``ACT``

         .. code-block:: ruby
       
            register_problem<Problem, ModelParams::Tag2Quadra>("ADE", "base");

         .. dropdown:: Modification  with ``ACT``
            :icon: comment

            .. code-block:: ruby
               :emphasize-lines: 1

               register_problem<Problem, ModelParams::Tag2Quadra>("ACT", "base");

            .. admonition:: Remark
               :class: important

               Your new problem will be named ``ACT`` inside your ``.ini`` input file i.e. in section ``[lbm]`` your problem must be:

               .. code-block:: ruby
                  :emphasize-lines: 2

                  [lbm]
                  problem=ACT



   .. admonition:: Compile your new kernel
      :class: note

      - Generate your ``makefile`` (only once)

       .. dropdown:: Commands
          :icon: comment

          .. code-block:: shell

             $ cd LBM_Saclay_Rech-Dev
             $ mkdir build_ACT
             $ cd build_ACT
             $ cmake -DKokkos_ENABLE_OPENMP=ON -DPROBLEM=Allen-Cahn-Temp_Tutorial ..

      - Compile

       .. dropdown:: Command
          :icon: comment

          .. code-block:: shell

             $ make -j 22

   .. admonition:: Run with input files of ADE
      :class: note

      - Execute your new kernel ``ACT`` of LBM_Saclay either with the simple diffusion of gaussian or with the advected gaussian in the folder ``run_training_lbm/Tutorial_Stefan``

       .. dropdown:: Commands
          :icon: comment

          Go to the directory

          .. code-block:: shell

             $ cd LBM_Saclay_Rech-Dev/run_training_lbm/Tutorial_Stefan

          Run simple diffusion of gaussian

          .. code-block:: shell

             $ ../../build_CH/src/LBM_saclay TestCase_Gaussian_ADE.ini

          Run advected gaussian

          .. code-block:: shell

             $ ../../build_CH/src/LBM_saclay TestCase_Moving-Gaussian_ADE.ini

      - Check the solutions with paraview.

2. Add a new equation in your kernel
------------------------------------

The mathematical model is composed of two coupled PDE. It is necessary to add one supplementary equation.

.. tab-set::

   .. tab-item:: File ``Problem_ACT.h``

      .. admonition:: ``Problem``
         :class: caution

         The number of equation is currently 1

          .. code-block:: ruby

             Base::nbEqs = 1;

             const int isize = params.isize;
             const int jsize = params.jsize;
             const int ksize = params.ksize;

         - Modify it for two equations

          .. dropdown:: Solution
             :icon: comment
             
             .. code-block:: ruby
                :emphasize-lines: 1

                Base::nbEqs = 2;

      .. admonition:: Function ``init_f()``
         :class: caution

         The initialization is currently performed only for one equation:

          .. code-block:: ruby

             if (params.collisionType1 == BGK) {
                  init1eq<EquationTag1, BGKCollider<dim, npop>>();
             } else if (params.collisionType1 == MRT) {
                  init1eq<EquationTag1, MRTCollider<dim, npop>>();
             }

         - Add a new block ``if`` - ``else if`` for ``EquationTag2``

          .. dropdown:: Solution
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 7,8,9,10,11

                if (params.collisionType1 == BGK) {
                  init1eq<EquationTag1, BGKCollider<dim, npop>>();
                } else if (params.collisionType1 == MRT) {
                  init1eq<EquationTag1, MRTCollider<dim, npop>>();
                }

                if (params.collisionType1 == BGK) {
                  init1eq<EquationTag2, BGKCollider<dim, npop>>();
                } else if (params.collisionType1 == MRT) {
                  init1eq<EquationTag2, MRTCollider<dim, npop>>();
                }
                
      .. admonition:: Function ``update_f()``
         :class: caution

         The update is also performed only for one equation:

          .. code-block:: ruby

             if (params.collisionType1 == BGK) {
               update1eq<EquationTag1, BGKCollider<dim, npop>>();
             } else if (params.collisionType1 == MRT) {
               update1eq<EquationTag1, MRTCollider<dim, npop>>();
             }

         - Add a new block ``if`` - ``else if`` for ``EquationTag2``

          .. dropdown:: Solution
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 7,8,9,10,11

                if (params.collisionType1 == BGK) {
                  update1eq<EquationTag1, BGKCollider<dim, npop>>();
                } else if (params.collisionType1 == MRT) {
                  update1eq<EquationTag1, MRTCollider<dim, npop>>();
                }

                if (params.collisionType1 == BGK) {
                  update1eq<EquationTag2, BGKCollider<dim, npop>>();
                } else if (params.collisionType1 == MRT) {
                  update1eq<EquationTag2, MRTCollider<dim, npop>>();
                }
                
      .. admonition:: Function ``make_boundaries()``
         :class: caution

         The update of bounday conditions is also performed for a single equation

          .. code-block:: ruby

             this->bcPerMgr.make_boundaries(scheme.f1, BOUNDARY_EQUATION_1);

         - Add a new line for ``f2`` and ``BOUNDARY_EQUATION_2``

          .. dropdown:: Solution
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 2

                this->bcPerMgr.make_boundaries(scheme.f1, BOUNDARY_EQUATION_1);
                this->bcPerMgr.make_boundaries(scheme.f2, BOUNDARY_EQUATION_2);

   .. tab-item:: File ``LBMScheme_ACT.h``

      .. admonition:: Function ``struct LBMScheme``
         :class: caution

         - Add a new tag ``tagPHI`` for ``EquationTag2``

          .. dropdown:: Solution
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 2

                EquationTag1 tagC;
                EquationTag2 tagPHI;

         - Add two empty functions called ``setup_collider`` for ``EquationTag2`` with respectively BGK and MRT collisions

          .. dropdown:: Solution
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 1,2,3,4,5,6,7,8

                KOKKOS_INLINE_FUNCTION
                void setup_collider(EquationTag2 tag, const IVect<dim>& IJK, BGK_Collider& collider) const
                {
                }

                KOKKOS_INLINE_FUNCTION
                void setup_collider(EquationTag2 tag, const IVect<dim>& IJK, MRT_Collider& collider) const
                {
             
             .. admonition:: Remark
                :class: important

                Those two functions are empty (but declared). The first one will be filled below.


      .. admonition:: Function ``make_boundary``
         :class: caution

         The boundary conditions are applied only for Advection-diffusion equation

          .. code-block:: ruby

             // ADE boundary
             if (Base::params.boundary_types[BOUNDARY_EQUATION_1][faceId] == BC_ANTI_BOUNCE_BACK) {
               real_t boundary_value = Base::params.boundary_values[BOUNDARY_CONCENTRATION][faceId];

               for (int ipop = 0; ipop < npop; ++ipop)
                  this->compute_boundary_antibounceback(tagC, faceId, IJK, ipop, boundary_value);
             }
             else if (Base::params.boundary_types[BOUNDARY_EQUATION_1][faceId] == BC_ZERO_FLUX) {
               for (int ipop = 0; ipop < npop; ++ipop)
                  this->compute_boundary_bounceback(tagC, faceId, IJK, ipop, 0.0);
             }

         - Add a new block ``if`` - ``else if`` for ``BOUNDARY_EQUATION_2`` and ``tagPHI`` with keywork ``BOUNDARY_PHASE_FIELD``

          .. dropdown:: Solution
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 1,2,3,4,5,6,7,8,9

                if (Base::params.boundary_types[BOUNDARY_EQUATION_2][faceId] == BC_ANTI_BOUNCE_BACK) {
                   real_t boundary_value = Base::params.boundary_values[BOUNDARY_PHASE_FIELD][faceId];
                   for (int ipop = 0; ipop < npop; ++ipop)
                   this->compute_boundary_antibounceback(tagPHI, faceId, IJK, ipop, boundary_value);
                }
                else if (Base::params.boundary_types[BOUNDARY_EQUATION_2][faceId] == BC_ZERO_FLUX) {
                   for (int ipop = 0; ipop < npop; ++ipop)
                   this->compute_boundary_bounceback(tagPHI, faceId, IJK, ipop, 0.0);
                }


3. Modifications inside each file for Allen-Cahn/Temperature model
------------------------------------------------------------------

.. admonition:: Advice
   :class: error

   During your implementation, it is strongly recommended to compile regularly to detect any typos. See :bdg-ref-primary-line:`Advice <Advice-During-Implementation>`


.. tab-set:: 

   .. tab-item:: File ``Index_ACT.h``

      .. admonition:: Declaration of new fields
         :class: caution

         In ``enum ComponentIndex``, only the indices for macroscopic fields such as concentration :math:`c` (``IC``) and velocity components :math:`u_x` (``IU``), :math:`u_y` (``IV``) & :math:`u_z` (``IW``) are declared:

          .. code-block:: ruby

             enum ComponentIndex {
               IU     , /*!< X velocity / momentum index */
               IV     , /*!< Y velocity / momentum index */
               IW     , /*!< Z velocity / momentum index */
               IC     , /*!< Phase field index */
               COMPONENT_SIZE /*!< invalid index, just counting number of fields */
             };

         - Replace ``IC`` by ``ITEMP`` and add the new indices for chemical potential ``IPHI`` and laplacian ``IDPHIDT``.

          .. dropdown:: Solution
             :icon: comment

             .. only:: Solutions

                .. code-block:: ruby
                   :emphasize-lines: 5,6,7

                   enum ComponentIndex {
                     IU     , /*!< X velocity / momentum index */
                     IV     , /*!< Y velocity / momentum index */
                     IW     , /*!< Z velocity / momentum index */
                     ITEMP  , /*!< Temperature index */
                     IPHI   , /*!< Phase field index */
                     IDPHIDT,	
                     COMPONENT_SIZE /*!< invalid index, just counting number of fields */
                   };

      .. admonition:: Add new outputs
         :class: caution

         In ``struct index2names`` only the strings for concentration and velocity components are written:

          .. code-block:: ruby

             map[IC ] = "comp";
             map[IU ] = "vx";
             map[IV ] = "vy";
             map[IW ] = "vz";

         - Modify for temperature and add new outputs for :math:`\phi` and :math:`\partial \phi/\partial t`.
            
          .. dropdown:: Solution
             :icon: comment

             .. only:: Solutions

                .. code-block:: ruby
                   :emphasize-lines: 1,5,6

                   map[ITEMP  ] = "temp";
                   map[IU     ] = "vx"  ;
                   map[IV     ] = "vy"  ;
                   map[IW     ] = "vz"  ;
                   map[IPHI   ] = "phi" ;
                   map[IDPHIDT] = "dphidt";

                .. admonition:: Remark
                   :class: important

                   The keywords ``temp``, ``phi``, and ``dphidt`` will be used in the ``.ini`` input file to write those fields.


   .. tab-item:: File ``Models_ACT.h``

      .. admonition:: Add specific functions for temperature equation
         :class: caution

         - Add a function ``Source_TEMP`` for the source term of temperature equation

          .. dropdown:: Solution ``Source_TEMP``
             :icon: comment

             .. only:: Solutions

               .. code-block:: ruby
                  :emphasize-lines: 1,2,3,4,5,6,7,8,9

                  // =======================================================
                  // Source term for temperature equation

                  KOKKOS_INLINE_FUNCTION
                  real_t Source_TEMP(EquationTag1 tag, const LBMState& lbmState) const
                  {
                     real_t dphidt = lbmState[IDPHIDT];
                     return -dphidt;
                  }
         
         - Modify the name of collision rate function for temperature equation

          .. dropdown:: Solution ``tau_TEMP``
             :icon: comment

             .. only:: Solutions

                .. code-block:: ruby
                   :emphasize-lines: 2

                   KOKKOS_INLINE_FUNCTION
                   real_t tau_TEMP(EquationTag1 tag, const LBMState& lbmState) const
                   {
                      real_t tau = 0.5 + (3.0 * D * dt / (dx * dx));
                      return (tau);
                   }

      .. admonition:: Add specific functions for phase-field equation
         :class: caution

         - Add a new function ``M0_PHI``

          .. dropdown:: Solution function ``M0_PHI``
             :icon: comment

             .. only:: Solutions

               .. code-block:: ruby
                  :emphasize-lines: 1,2,3,4,5,6,7
                
                  // =======================================================
                  // zero order moment for phase field
                  KOKKOS_INLINE_FUNCTION
                  real_t M0_PHI(EquationTag2 tag, const LBMState& lbmState) const
                     {
                     return lbmState[IPHI];
                  }

         - Add a new function ``M2_PHI``

          .. dropdown:: Solution function ``M2_PHI``
             :icon: comment

             .. only:: Solutions

               .. code-block:: ruby
                  :emphasize-lines: 1,2,3,4,5,6,7
                
                  // =======================================================
                  // Second order moment for phase field
                  KOKKOS_INLINE_FUNCTION
                  real_t M2_PHI(EquationTag2 tag, const LBMState& lbmState) const
                     {
                     return lbmState[IPHI];
                  }

         - Add a source term.

          .. dropdown:: Solution ``Source_PHI``
             :icon: comment

             .. only:: Solutions

                .. code-block:: ruby
                   :emphasize-lines: 1,2,3,4,5,6,7,8,9,10,11,12,13

                   // =======================================================
                   // Source term for phase field
                   KOKKOS_INLINE_FUNCTION
                   real_t Source_PHI (EquationTag2 tag, const LBMState& lbmState) const
                      {
                      real_t phi     = lbmState[IPHI];
                      real_t temp    = lbmState[ITEMP];
                      real_t tempI   = 0.0;
                      real_t Coeff_A = 10.0/48.0;
                      real_t S       = - (16.0*mobility/(W*W)) * phi * (1.0-phi) * (1-2*phi)
                                       -((4.0*D)/(Coeff_A*W*W))*(tempI-temp)*phi*(1-phi);
                      return S;
                   }

         - Add a new function ``tau_PHI`` for collision rate using the mobility :math:`M_\phi` of Allen-Cahn equation

          .. dropdown:: Solution ``tau_PHI``
             :icon: comment

             .. only:: Solutions

                .. code-block:: ruby
                   :emphasize-lines: 1,2,3,4,5,6,7

                   // =======================================================
                   // relaxation coef for LBM scheme of phase field equation
                   KOKKOS_INLINE_FUNCTION
                   real_t tau_PHI(EquationTag2 tag, const LBMState& lbmState) const
                   {
                      real_t tau = 0.5 + (3.0 * (mobility) * dt / (dx * dx));
                      return (tau);
                   }

                .. admonition:: Warning
                   :class: error

                   Don't forget to read and declare the parameter ``mobility`` in ``ModelParams``.

         - Add a new hyperbolic tangent function ``phi0`` for initial condition

          .. dropdown:: Solution ``phi0``
             :icon: comment

             .. only:: Solutions

                .. code-block:: ruby
                   :emphasize-lines: 1,2,3,4

                   // Hyperbolic tangent for g1 double-well
                   KOKKOS_INLINE_FUNCTION real_t phi0(real_t x) const {
                      return 0.5*(1.0+tanh(sign * 2.0 * x / W ));
                   }


      .. admonition:: Read and declare all parameters in ``ModelParams``
         :class: caution
      
         The Allen-Cahn equation involves three paramters: the interface thickness :math:`W` and the mobility :math:`M_\phi` and the interface temperature :math:`\theta_I`.

         - Read and declare Allen-Cahn parameters in ``ModelParams``

          .. dropdown:: Solution
             :icon: comment

             .. only:: Solutions

                .. code-block:: ruby
                   :emphasize-lines: 1,2,3,5
                
                   mobility = configMap.getFloat("params", "mobility", 1.0);
                   W        = configMap.getFloat("params", "W"       , 1.0);
                   tempI    = configMap.getFloat("params", "tempI"   , 0.0);

                   undercooling = configMap.getFloat("init", "undercooling", 0.0);

                Don't forget to declare them as ``real_t`` at the end of ``ModelParams``

                .. code-block:: ruby
                   :emphasize-lines: 1
                
                   real_t mobility, W, tempI, undercooling;

      .. admonition:: Add condition for initial condition
         :class: caution

         Currently only one condition exits for intial condition:

          .. code-block:: ruby

             if (initTypeStr == "gaussian") initType = ADE_GAUSSIAN;
         
         - Add the necessary condition for one initialization

          .. dropdown:: Solution
             :icon: comment

             .. only:: Solutions

                .. code-block:: ruby
                   :emphasize-lines: 2

                   if (initTypeStr == "gaussian") initType = ADE_GAUSSIAN;
                   else if (initTypeStr == "vertical") initType = PHASE_FIELD_INIT_VERTICAL;

                .. admonition:: Warning
                   :class: error

                   Don't forget to declare all keywords ``PHASE_FIELD_INIT_VERTICAL`` in file ``InitConditionsTypes.h``
   
   .. tab-item:: File ``LBMScheme_ACT.h``

      .. admonition:: Function ``setup_collider`` with BGK for temperature equation
         :class: caution

         The function ``setup_collider`` is written for solving Advection-Diffusion Equation. 
	
          .. code-block:: ruby

             const real_t M0     = Model.M0_TEMP(tagC, lbmState);
             const RVect<dim> uc = Model.M1_TEMP<dim>(tagC, lbmState);
             const real_t M2     = Model.M2_TEMP(tagC, lbmState);
             // ipop = 0
             collider.f[0]   = Base::get_f_val(tag, IJK, 0);
             collider.S0[0]  = 0.0 ;
             collider.feq[0] = w[0]*M0;
             // ipop > 0
             for (int ipop = 1; ipop < npop; ++ipop) {
               collider.f[ipop]   = this->get_f_val(tag, IJK, ipop);
               collider.S0[ipop]  = 0.0 ;
               collider.feq[ipop] = w[ipop] * (M2 + c_cs2 * Base::compute_scal(ipop, uc));
             }

         - Modify it for the source term.

          .. dropdown:: Solution
             :icon: comment

             .. only:: Solutions

                .. code-block:: ruby
                   :emphasize-lines: 4,6,9,14
                
                   const real_t M0     = Model.M0_TEMP(tagC, lbmState);
                   const RVect<dim> uc = Model.M1_TEMP<dim>(tagC, lbmState);
                   const real_t M2     = Model.M2_TEMP(tagC, lbmState);
                   const real_t Temp_S = Model.Source_TEMP(tagC, lbmState) ;
                   // compute collision rate
                   collider.tau = Model.tau_TEMP(tagC, lbmState);
                   // ipop = 0
                   collider.f[0]   = Base::get_f_val(tagC, IJK, 0);
                   collider.S0[0]  = dt * w[0] * Temp_S;
                   collider.feq[0] = w[0]*M0;
                   // ipop > 0
                   for (int ipop = 1; ipop < npop; ++ipop) {
                      collider.f[ipop]   = this->get_f_val(tagC, IJK, ipop);
                      collider.S0[ipop]  = dt * w[ipop] * Temp_S ;
                      collider.feq[ipop] = w[ipop] * (M2 + c_cs2 * Base::compute_scal(ipop, uc));
                   }

      .. admonition:: Function ``setup_collider`` with BGK for phase-field equation
         :class: caution

         The function ``setup_collider`` is empty. 
	
          .. code-block:: ruby

             void setup_collider(EquationTag2 tag, const IVect<dim>& IJK, BGK_Collider& collider) const
             {
             }

         - Inspired with the temperature equation, write your ``setup_collider``.

          .. dropdown:: Solution
             :icon: comment

             .. only:: Solutions

                .. code-block:: ruby
                   :emphasize-lines: 4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26
                
                   KOKKOS_INLINE_FUNCTION
                   void setup_collider(EquationTag2 tag, const IVect<dim>& IJK, BGK_Collider& collider) const
                   {
                      const real_t dt = Model.dt;
                      const real_t dx = Model.dx;
                      const real_t e2 = Model.e2;
                      const real_t c = dx / dt;
                      const real_t c_cs2 = e2 / c; // Ratio c/cs2
                      LBMState lbmState;
                      Base::template setupLBMState2<LBMState, COMPONENT_SIZE>(IJK, lbmState);
                
                      const real_t M0     = Model.M0_PHI(tagPHI, lbmState);
                      const real_t M2     = Model.M2_PHI(tagPHI, lbmState);
                      const real_t phi_S  = Model.Source_PHI(tagPHI, lbmState) ;
                      // compute collision rate
                      collider.tau = Model.tau_PHI(tagPHI, lbmState);
                      // ipop = 0
                      collider.f[0]   = Base::get_f_val(tagPHI, IJK, 0);
                      collider.S0[0]  = dt * w[0] * phi_S ;
                      collider.feq[0] = w[0]*M0;
                      // ipop > 0
                      for (int ipop = 1; ipop < npop; ++ipop) {
                         collider.f[ipop]   = this->get_f_val(tagPHI, IJK, ipop);
                         collider.S0[ipop]  = dt * w[ipop] * phi_S ;
                         collider.feq[ipop] = w[ipop] * M2;
                      }
                   }

      .. admonition:: Function ``init_macro``
         :class: caution

         After the initialization for ``ADE_GAUSSIAN``:
   
          .. code-block:: ruby

             if (Model.initType == ADE_GAUSSIAN) {
               c  = Model.ampl * exp( - ( SQR(x-Model.x0) / (2 * SQR(Model.sigmax)) + SQR(y-Model.y0) / (2 * SQR(Model.sigmay)) )) ;
               vx = Model.initVX;
               vy = Model.initVY;
             }

         - Write an initial condition corresponding to keywords ``PHASE_FIELD_INIT_VERTICAL``
	
          .. dropdown:: Solution for vertical separation
             :icon: comment

             .. only:: Solutions

                .. code-block:: ruby
                   :emphasize-lines: 1,2,3,4

                   else if (Model.initType == PHASE_FIELD_INIT_VERTICAL) {
                      xphi = x - Model.x0;
                      c    = Model.undercooling ;
                   }
                   real_t phi = Model.phi0(xphi);

         - Save in appropriate arrays

          .. dropdown:: Solution
             :icon: comment

             .. only:: Solutions

                .. code-block:: ruby
                   :emphasize-lines: 1,4
                
                   this->set_lbm_val(IJK, ITEMP, c  );
                   this->set_lbm_val(IJK, IU   , vx );
                   this->set_lbm_val(IJK, IV   , vy );
                   this->set_lbm_val(IJK, IPHI , phi);


      .. admonition:: Function ``update_macro``
         :class: caution
         
         Currently, only the concentration and the velocity are updated:

          .. code-block:: ruby

             const real_t c  = moment_c;
             const real_t vx = Model.initVX;
             const real_t vy = Model.initVY;

             this->set_lbm_val(IJK, IC , c );
             this->set_lbm_val(IJK, IU , vx);
             this->set_lbm_val(IJK, IV , vy);

         - Add for ``phi``

          .. dropdown:: Solution
             :icon: comment

             .. only:: Solutions

                .. code-block:: ruby
                   :emphasize-lines: 1,4,6

                   real_t moment_phi = 0.0;
                   for (int ipop = 0; ipop < npop; ++ipop) {
                      moment_c   += Base::get_f_val(tagC  , IJK, ipop);
                      moment_phi += Base::get_f_val(tagPHI, IJK, ipop);
                   }
                   const real_t phi  = moment_phi;
        
         - Add for ``dphidt``

          .. dropdown:: Solution
             :icon: comment
             :open:

             .. code-block:: ruby
                :emphasize-lines: 3,4,5

                LBMState lbmStatePrev;
                Base::setupLBMState(IJK, lbmStatePrev);
                // get time step
                const real_t dt = this->params.dt;
                const real_t dphidt = (phi - lbmStatePrev[IPHI])/dt;
        
         - Save in arrays

          .. dropdown:: Solution
             :icon: comment

             .. only:: Solutions

                .. code-block:: ruby
                   :emphasize-lines: 1,4,5

                   this->set_lbm_val(IJK, ITEMP  , c     );
                   this->set_lbm_val(IJK, IU     , vx    );
                   this->set_lbm_val(IJK, IV     , vy    );
                   this->set_lbm_val(IJK, IPHI   , phi   );
                   this->set_lbm_val(IJK, IDPHIDT, dphidt);
         


      .. admonition:: Function ``update_macro_grad``
         :class: note

         For that phase change model there is no need to compute additional gradient or laplacian.


   .. tab-item:: File ``InitConditionsTypes.h``

      .. admonition:: Add the keywords of initial conditions
         :class: caution

         In file ``InitConditionsTypes.h``, two keywords are currently declared:

          .. code-block:: ruby

             enum InitCondition{
	            PHASE_FIELD_INIT_UNDEFINED,
	            ADE_GAUSSIAN
             };

         Simply add after ``ADE_GAUSSIAN``, the new keyword for Allen-Cahn: ``PHASE_FIELD_INIT_VERTICAL``.

          .. dropdown:: Solution
             :icon: comment

             .. only:: Solutions

                .. code-block:: ruby
                   :emphasize-lines: 4

                   enum InitCondition{
                      PHASE_FIELD_INIT_UNDEFINED,
                      ADE_GAUSSIAN,
                      PHASE_FIELD_INIT_VERTICAL
                   };


4. Verifications of your implementation
---------------------------------------

.. tab-set::

   .. tab-item:: Solution of reference

      The LBM implementation is compared with one analytical solution of the Stefan problem. The domain is supposed to be semi-infinite :math:`]0,L]` (with :math:`L` big) with Dirichlet boundary conditions :math:`\theta(0,t)=\theta_w` and :math:`\theta(L,t)=\theta_{\infty}`. The initial condition is :math:`\theta(x,0)=\theta_{\infty}`. 

      .. admonition:: Analytical solution

         The analytical solution of this problem gives the interface position :math:`x_i(t)`, the liquid (or solid) temperature :math:`\theta_{l}(x,t)` and the gas (or liquid) temperature :math:`\theta_{g}(x,t)`. Those solutions depend on a parameter :math:`\xi` which is given by the transcendental equation.
         
         **Interface position**

         .. math::

            x_{i}(t)=2\xi\sqrt{\alpha_{l}t}

         **Liquid temperature**

         .. math::

            \theta_{l}(x,t)=\theta_{w}+(\theta_{I}-\theta_{w})\frac{\mbox{erf}(x/2\sqrt{\alpha_{l}t})}{\mbox{erf}(\xi)}

         **Gas temperature**

         .. math::

            \theta_{g}(x,t)=\theta_{\infty}+(\theta_{I}-\theta_{\infty})\frac{\mbox{erfc}(x/2\sqrt{\alpha_{g}t})}{\mbox{erfc}(\xi\sqrt{\alpha_{l}/\alpha_{g}})}

         **Transcendental equation**

         .. math::

            \frac{e^{-\xi^{2}}}{\mbox{erf}(\xi)}+\left(\frac{\alpha_{g}}{\alpha_{l}}\right)^{1/2}\frac{\theta_{I}-\theta_{\infty}}{\theta_{I}-\theta_{w}}\frac{e^{-\xi^{2}(\alpha_{l}/\alpha_{g})}}{\mbox{erfc}(\xi\sqrt{\alpha_{l}/\alpha_{g}})}=-\frac{\xi\sqrt{\pi}}{\theta_{w}}

         **Input parameters**

         - :math:`\alpha_l`, :math:`\alpha_g`: respectively diffusity of liquid and Gas
         - :math:`\theta_w`: temperature at left boundary
         - :math:`\theta_{\infty}`: temperature at right boundary and initial condition
         - :math:`\theta_I`: temperature at interface

      .. admonition:: Fortran code and analytical profile

         The analytical solution is implemented in a Fortran code. For validating our LBM implementation, the profiles of temperature for liquid (or gas) and solid (or liquid) with the position :math:`x` are given in two output files ``T_Liq_Chgt_Phase200000.dat`` and ``T_Sol_Chgt_Phase200000.dat``. Both files are in the folder ``case01``. After :math:`2\times10^5 \delta t` the temperature profile is presented on Fig. :numref:`target-Fig-Stefan-Temp-Profile` for liquid (black) and gas (blue).

         .. grid:: 2
            :gutter: 4
            :margin: 0

            .. grid-item::
               :columns: 5

               Parameters for reference profile

               - :math:`\theta_w=-0.3`
               - :math:`\theta_{\infty}=0.3`
               - :math:`\theta_I=0`
               - :math:`\alpha_l=\alpha_g=0.1`

               - :math:`L=500`: length of computational domain
               - :math:`\delta x=1`: space step
               - :math:`\delta t=1`: time step
               - :math:`x_i(0)=0`: interface position at left boundary

            .. grid-item::
               :columns: 6

               .. figure:: ../FIGS/01_FIGS_VALIDATIONS/Profile-Temp_Analytical_Stefan.png
                  :name: target-Fig-Stefan-Temp-Profile
                  :height: 350
                  :width: 500
                  :scale: 80
                  :align: center
   
                  Temperature profile at :math:`t=2\times 10^5 \delta t`.

   .. tab-item:: Make your input file

      .. admonition:: Edit your ``.ini`` input file
         :class: important

         - Set appropriate values of ``[run]`` section

          .. dropdown:: Solution
             :icon: comment

             .. only:: Solutions

                .. code-block:: ruby

                   [run]
                   lbm_name=D2Q9
                   tEnd=200001
                   nStepmax=200001
                   nOutput=20000
                   nlog=10000000
                   dt=1.0
                   adaptative_timestep=false
                   fMach=0.05

         - Set appropriate values of ``[mesh]`` section

          .. dropdown:: Solution
             :icon: comment

             .. only:: Solutions

                .. code-block:: ruby

                   [mesh]
                   nx=500
                   ny=10
                   xmin=0.0
                   xmax=500.0
                   ymin=0.0
                   ymax=10.0


         - Set appropriate values of ``[lbm]`` section

          .. dropdown:: Solution
             :icon: comment

             .. only:: Solutions

                .. code-block:: ruby

                   [lbm]
                   problem=ACT
                   model=base
                   e2=3.0
                   fcount=2

         - Set Dirichlet boundary conditions for ``[equation1]`` and ``[equation2]``.

          .. dropdown:: Solution
             :icon: comment
             :open:

             .. code-block:: ruby

                [equation1]
                boundary_type_xmin=antibounceback
                boundary_type_xmax=antibounceback
                boundary_type_ymin=periodic
                boundary_type_ymax=periodic
                collision=BGK
                
                [equation2]
                boundary_type_xmin=antibounceback
                boundary_type_xmax=antibounceback
                boundary_type_ymin=periodic
                boundary_type_ymax=periodic
                collision=BGK
                
                [phase_field_boundary]
                boundary_value_xmin=0.0
                boundary_value_xmax=1.0
                boundary_value_ymin=0.0
                boundary_value_ymax=0.0
                
                [concentration_boundary]
                boundary_value_xmin=-0.3
                boundary_value_xmax=0.3
                boundary_value_ymin=0.0
                boundary_value_ymax=0.0

         - Set the same input parameters and ``mobility=0.3`` with appropriate value of interface thickness

          .. dropdown:: Solution
             :icon: comment

             .. only:: Solutions

                .. code-block:: ruby

                   [params]
                   D=0.1
                   W=3.0
                   mobility=0.3

         - Set initial condition

          .. dropdown:: Solution
             :icon: comment

             .. only:: Solutions

                .. code-block:: ruby

                   [init]
                   init_type=vertical
                   x0=0.0
                   undercooling=0.3

         - Set outputs

          .. dropdown:: Solution
             :icon: comment

             .. only:: Solutions

                .. code-block:: ruby

                   [output]
                   write_variables=temp,vx,vy,phi
                   outputPrefix=TestCase_Stefan1
                   outputVtkAscii=no
                   vtk_enabled=yes
                   hdf5_enabled=no


      .. admonition:: Run LBM_Saclay
         :class: important

         - Run LBM_Saclay with your input datafile

   .. tab-item:: Post-process your results

      .. admonition:: Results
         :class: important

         **Generate your csv files with Paraview**

            - In paraview export one temperature profile along x-axis in ``.csv`` format (see paraview commands in :bdg-ref-primary-line:`TwoP-Training-LBM-PARTA`).
            - Alternatively, your ``.csv`` files can generated by using the ``pvpython`` command

             .. code-block:: shell

                $ path_to_pvpython/pvpython Profil-Temp.pvpy

             where ``Profil-Temp.pvpy`` is in 

         **Superpose with Gnuplot**

            - A gnuplot script ``Profil_Comparison_Analy-LBM.gnutex`` is also available in the folder

             .. code-block:: shell

                $ gnuplot Profil_Comparison_Analy-LBM.gnutex

             will generate a new file ``Profile-Temp-Stefan_LBM-Analytical.tex``

             .. code-block:: shell

                $ pdflatex Profile-Temp-Stefan_LBM-Analytical.tex

             to make the pdf file. You should obtain Fig. :numref:`target-Fig-Stefan-Temp-Profile-with-LBM`

         .. figure:: ../FIGS/01_FIGS_VALIDATIONS/Profile-Temp-Stefan_LBM-Analytical.png
            :name: target-Fig-Stefan-Temp-Profile-with-LBM
            :height: 350
            :width: 500
            :scale: 95
            :align: center
   
            Comparison between LBM and analytical solution² at :math:`t=2\times 10^5 \delta t`.

   .. tab-item:: Different diffusivities

      .. admonition:: Case :math:`D_l \neq D_g`
         :class: important

         - Modify your kernel in order to interpolate :math:`D(\phi)=(1-\phi)D_l+\phi D_g` where :math:`D_l` and :math:`D_g` are respectively the thermal diffusivity in liquid and gas.

          .. dropdown:: Solution
             :icon: comment

             .. only:: Solutions

                .. code-block:: ruby
                   :emphasize-lines: 4,5

                   KOKKOS_INLINE_FUNCTION
                   real_t tau_TEMP(EquationTag1 tag, const LBMState& lbmState) const
                   {
                      real_t phi  = lbmState[IPHI];
                      real_t Dphi = Dl*(1.0-phi)+Dg*phi ;
                      real_t tau  = 0.5 + (3.0 * Dphi * dt / (dx * dx));
                      return (tau);
                   }

                Don't forget to read and declare ``Dl`` and ``Dg``
         
         - Add necesary values of :math:`D_l` and :math:`D_g` in your the ``.ini`` input file

         - Superpose with analytical solution with  :math:`D_l=0.14` and :math:`D_g=0.014`

         - Use the harmonic interpolation for :math:`D(\phi)`
         
          .. dropdown:: Solution
             :icon: comment

             .. only:: Solutions

                .. code-block:: ruby
                   :emphasize-lines: 5

                   KOKKOS_INLINE_FUNCTION
                   real_t tau_TEMP(EquationTag1 tag, const LBMState& lbmState) const
                   {
                      real_t phi  = lbmState[IPHI];
                      real_t Dphi = 1./(phi/Dg+(1.0-phi)/Dl) ;
                      real_t tau  = 0.5 + (3.0 * Dphi * dt / (dx * dx));
                      return (tau);
                   }
             
         - Compare the impact on curves

          .. dropdown:: Solution
             :icon: comment


             .. only:: Solutions

                .. figure:: ../FIGS/01_FIGS_VALIDATIONS/Profile-Temp-Stefan_LBM-Analytical_HeterogeneousD.png
                   :name: Fig-Stefan-Temp-Profile-with-LBM-HeterogeneousD
                   :height: 350
                   :width: 500
                   :scale: 95
                   :align: center
   
                   Comparison between LBM and analytical solution at :math:`t=2\times 10^5 \delta t` for :math:`D_l=0.14` and :math:`D_g=0.014`.
   
.. sectionauthor:: Alain Cartalade
