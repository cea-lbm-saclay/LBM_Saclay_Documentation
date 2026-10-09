.. include:: ../Substitutions.rst

.. _Tuto-Crystal-Growth:

Implementation of a crystal growth model
========================================

Objective of this 3rd tutorial
------------------------------

The starting point is the kernel ``ACT`` of the second tutorial. That kernel will be modified here in order to simulate the growth of one crystal.

.. admonition:: Mathematical model
   :class: error

   The mathematical model is composed of one dimensionless temperature equation which writes:

   .. math::
      :label: eq-temp-crystal-growth

      \frac{\partial\theta}{\partial t}=D\boldsymbol{\nabla}^{2}\theta+\frac{1}{2}\frac{\partial\psi}{\partial t}

   The phase-field equation is slightly more complex than the previous one in the 2nd tutorial:

   .. math::
      :label: eq-phase-field-crystal-growth

      \tau_{0}{\color{red}a_{s}^{2}(\boldsymbol{n})}\frac{\partial\psi}{\partial t}=W_{0}^{2}\boldsymbol{\nabla}\cdot\left[{\color{red}a_{s}^{2}(\boldsymbol{n})}\boldsymbol{\nabla}\psi\right]+\boldsymbol{\nabla}\cdot{\color{blue}\boldsymbol{\mathcal{N}}(\boldsymbol{n})}+(1-\psi^{2})\left[\psi-\lambda\theta(1-\psi^{2})\right]

   where the anisotropy function writes:

   .. math::
      :label:

      {\color{red}a_{s}(\boldsymbol{n})}=1-3\epsilon_{s}+4\epsilon_{s}\sum_{\alpha=x,y,z}n_{\alpha}^{4}

   and the vector :math:`\boldsymbol{\mathcal{N}}` by

   .. math::
      :label:

      {\color{blue}\boldsymbol{\mathcal{N}}(\boldsymbol{n})}=W_{0}^{2}\bigl|\boldsymbol{\nabla}\psi\bigr|^{2}{\color{red}a_{s}(\boldsymbol{n})}\frac{\partial{\color{red}a_{s}(\boldsymbol{n})}}{\partial(\partial_{\alpha}\psi)}


.. admonition:: Objective
   :class: important

   Until now, only the standard BGK collider was used in our implementation. In this tutorial, we will see how to
   
   - use another LBM_Saclay collider, based on BGK (but modified) to take into account the :math:`\tau_{0}{\color{red}a_{s}^{2}(\boldsymbol{n})}` in front of the partial derivative :math:`\partial \psi/\partial t`.
   - modify the ``setup_collider`` for :math:`\boldsymbol{\nabla}\cdot{\color{blue}\boldsymbol{\mathcal{N}}(\boldsymbol{n})}`

1. Use a new collision operator for the phase-field equation in your kernel
---------------------------------------------------------------------------

Several collision operators are already implemented in ``Collision_operators.h``. The most popular are ``BGK``, ``TRT`` and ``MRT``. Here we will use a BGK operator, slightly modified and involving a non-local term. It is mainly used to take into account a time-evolving factor in front the partial derivative in time. In LBM_Saclay, that operator is called ``BGKColliderTimeFactor``.

.. tab-set::

   .. tab-item:: File ``Problem_ACT.h``

      .. admonition:: Function ``update_f()``
         :class: caution

         For ``BGK`` the update is currently

          .. code-block:: ruby

             if (params.collisionType2 == BGK) {
               update1eq<EquationTag2, BGKCollider<dim, npop>>();

         - Modify it for ``BGKColliderTimeFactor``

          .. dropdown:: Solution
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 2,3

                if (params.collisionType2 == BGK) {
                  //update1eq<EquationTag2, BGKCollider<dim, npop>>();
                  update1eq<EquationTag2, BGKColliderTimeFactor<dim,npop>>();

   .. tab-item:: File ``LBMScheme_ACT.h``

      .. admonition:: ``struct LBMScheme``
         :class: caution

         Currently only two collisions are defined

          .. code-block:: ruby

             using BGK_Collider = BGKCollider<dim, npop>;
             using MRT_Collider = MRTCollider<dim, npop>;

         - Define a new collision

          .. dropdown:: Solution
             :icon: comment
             :open:

             .. code-block:: ruby
                :emphasize-lines: 3

                using BGK_Collider = BGKCollider<dim, npop>;
                using MRT_Collider = MRTCollider<dim, npop>;
                using BGK_Collider_Time_Factor = BGKColliderTimeFactor<dim,npop>;

      .. admonition:: Add a new empty function ``setup_collider`` for ``EquationTag2`` with ``BGK_Collider_Time_Factor``
         :class: caution

          .. dropdown:: Solution
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 1-9

                // ==================================================================================================
                //
                // BGK modified for phase-field equation of crystal growth
                //
                // ==================================================================================================
                KOKKOS_INLINE_FUNCTION
                void setup_collider(EquationTag2 tag, const IVect<dim>& IJK, BGK_Collider_Time_Factor& collider) const
                {
                }

2. Modifications inside each file for implementing a crystal growth model
-------------------------------------------------------------------------

.. tab-set:: 

   .. tab-item:: File ``Index_ACT.h``

      .. admonition:: Declaration of new fields
         :class: caution

         From the previous tutorialn, in ``enum ComponentIndex``, the indices for macroscopic fields are:

          .. code-block:: ruby

             enum ComponentIndex {
               IU     , /*!< X velocity / momentum index */
               IV     , /*!< Y velocity / momentum index */
               IW     , /*!< Z velocity / momentum index */
               ITEMP  , /*!< Temperature index */
               IPHI   , /*!< Phase field index */
               IDPHIDT,	
               COMPONENT_SIZE /*!< invalid index, just counting number of fields */
             };

         - Add for components of gradient of :math:`\phi`

          .. dropdown:: Solution
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 8,9

                enum ComponentIndex {
                  IU     , /*!< X velocity / momentum index */
                  IV     , /*!< Y velocity / momentum index */
                  IW     , /*!< Z velocity / momentum index */
                  ITEMP  , /*!< Temperature index */
                  IPHI   , /*!< Phase field index */
                  IDPHIDT,
                  IDPHIDX,
                  IDPHIDY,	
                  COMPONENT_SIZE /*!< invalid index, just counting number of fields */
                };

      
   .. tab-item:: File ``Models_ACT.h``

      .. admonition:: Read and declare all parameters in ``ModelParams``
         :class: caution
      
         The Allen-Cahn equation involves three parameters: the interface thickness :math:`W` and the mobility :math:`M_\phi` and the interface temperature :math:`\theta_I`.

         - Read and declare Allen-Cahn parameters in ``ModelParams``

          .. dropdown:: Solution
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 1,2,3,4
                
                KR_W0 = configMap.getFloat("params","KR_W0",1.0);
                KR_tau0 = configMap.getFloat("params","KR_tau0",1.0);
                KR_lambda0 = configMap.getFloat("params","KR_lambda0",1.0);
                KR_eps = configMap.getFloat("params","KR_eps",1.0);

             Don't forget to declare them as ``real_t`` at the end of ``ModelParams``

             .. code-block:: ruby
                :emphasize-lines: 1
                
                real_t KR_W0, KR_tau0, KR_lambda0, KR_eps;

      .. admonition:: Add condition for initial condition
         :class: caution

         Currently only one condition exits for intial condition:

          .. code-block:: ruby

             if (initTypeStr == "gaussian") initType = ADE_GAUSSIAN;
             else if (initTypeStr == "vertical") initType = PHASE_FIELD_INIT_VERTICAL;
         
         - Add the necessary condition for one initialization

          .. dropdown:: Solution
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 3

                if (initTypeStr == "gaussian") initType = ADE_GAUSSIAN;
                else if (initTypeStr == "vertical") initType = PHASE_FIELD_INIT_VERTICAL;
                else if (initTypeStr == "sphere") initType = PHASE_FIELD_INIT_SPHERE;
   

      .. admonition:: Add specific functions for temperature equation
         :class: caution

         - Modify function ``Source_TEMP`` with factor 1/2 (be careful with the positive sign)

          .. dropdown:: Solution ``Source_TEMP``
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 8

                // =======================================================
                // Source term for temperature equation

                KOKKOS_INLINE_FUNCTION
                real_t Source_TEMP(EquationTag1 tag, const LBMState& lbmState) const
                {
                  real_t dphidt = lbmState[IDPHIDT];
                  return 0.5*dphidt;
                }

      .. admonition:: Add specific functions of crystal growth functions in the phase-field equation
         :class: caution

         - Add another source term

          .. dropdown:: Solution ``psi_st``
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 1,2,3,4,5,6,7,8,9

                // =======================================================
                // Source term for crystal growth
                KOKKOS_INLINE_FUNCTION
                real_t psi_st(EquationTag2 tag, const LBMState& lbmState) const
                {
                  real_t phi = lbmState[IPHI];
                  real_t S = (phi - KR_lambda0*(lbmState[ITEMP])*(1-phi*phi))*(1-phi*phi)/KR_tau0;
                  return S;
                }

         - Add a new function ``tau_PHI_Crystal`` for collision rate using the anaisotropy function :math:`a_s()\boldsymbol{n}`

          .. dropdown:: Solution ``tau_PHI_Crystal``
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 1,2,3,4,5,6,7,8

                // =======================================================
                // relaxation coef for LBM scheme of phase field equation
                KOKKOS_INLINE_FUNCTION
                real_t tau_PHI_Crystal(EquationTag2 tag, const LBMState& lbmState, real_t As2) const
                {
                  real_t tau = 0.5 + (3.0 * As2 * ((KR_W0*KR_W0)/KR_tau0) * dt / (dx * dx));
                  return (tau);
                }

         - Add a new hyperbolic tangent function ``phi1`` for initial condition

          .. dropdown:: Solution ``phi1``
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 1,2,3,4

                // Hyperbolic tangent for g3 double-well
                KOKKOS_INLINE_FUNCTION real_t phi1(real_t x) const {
                  return (tanh(sign * 2.0 * x / KR_W0 ));
                }

         - Add a new function ``compute_anisotropy`` for computing the anisotropy function :math:`a_s(\boldsymbol{n})`

          .. dropdown:: Solution ``compute_anisotropy``
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 1-14

                KOKKOS_INLINE_FUNCTION
                real_t compute_anisotropy(EquationTag2 tag, const LBMState& lbmState) const
                {
                  const real_t norm = sqrt( SQR(lbmState[IDPHIDX]) + SQR(lbmState[IDPHIDY]));
                  real_t As_n;
                  if(norm > 0.0){
                     real_t xx4 = SQR(lbmState[IDPHIDX])*SQR(lbmState[IDPHIDX]);
                     real_t yy4 = SQR(lbmState[IDPHIDY])*SQR(lbmState[IDPHIDY]);
                     real_t ww4 = SQR(norm)*SQR(norm);
                     As_n = 1.0 - 3.0*KR_eps + 4.0*KR_eps*(xx4+yy4)/ww4;}
                  else {
                     As_n = 1.0 - 3.0*KR_eps;}
                  return As_n;
                }

         - Add a new function ``compute_anisotropy_vector``

          .. dropdown:: Solution ``compute_anisotropy_vector``
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 1-18

                KOKKOS_INLINE_FUNCTION
                RVect2 compute_anisotropy_vector(EquationTag2 tag, const LBMState& lbmState) const
                {
                  const real_t norm = sqrt( SQR(lbmState[IDPHIDX]) + SQR(lbmState[IDPHIDY]))+NORMAL_EPSILON;
                  real_t xx = lbmState[IDPHIDX];
                  real_t yy = lbmState[IDPHIDY];
                  real_t xx4 = xx*xx*xx*xx;
                  real_t yy4 = yy*yy*yy*yy;
                  real_t ww4 = SQR(norm)*SQR(norm);
                  real_t ww6 = ww4*SQR(norm);
                  real_t As_n = 1.0 - 3.0*KR_eps + 4.0*KR_eps*(xx4+yy4)/ww4;
                  RVect2 N;
                  N[IX] = -16.0*KR_eps*xx*(yy4-SQR(xx)*SQR(yy))/ww6;
                  N[IY] = -16.0*KR_eps*yy*(xx4-SQR(yy)*SQR(xx))/ww6;
                  N[IX] *= norm*norm*As_n;
                  N[IY] *= norm*norm*As_n;
                  return N;
                }

   
   .. tab-item:: File ``LBMScheme_ACT.h``

      .. admonition:: Write a new function ``setup_collider`` with ``BGK_Collider_Time_Factor``
         :class: caution

         Fill the new ``setup_collider`` for phase-field equation

          .. dropdown:: Solution
             :icon: comment

             - Define local variables

             .. code-block:: ruby
                :emphasize-lines: 3-13
                
                KOKKOS_INLINE_FUNCTION
                void setup_collider(EquationTag2 tag, const IVect<dim>& IJK, BGK_Collider_Time_Factor& collider) const {
                  const real_t dt = Model.dt;
                  const real_t dx = Model.dx;
                  const real_t e2 = Model.e2;
                  const real_t cs2 = 1.0/e2 * SQR(dx/dt);
                  const real_t W0 = Model.KR_W0;
                  const real_t tau0 = Model.KR_tau0;
                  const real_t fact = W0*W0/tau0;

                  LBMState lbmState;
                  Base::template setupLBMState2<LBMState,COMPONENT_SIZE>(IJK, lbmState);
                  bool can_str ;
                
             - Compute moments and source term

             .. code-block:: ruby
                :emphasize-lines: 1-6
                
                const real_t M0 = Model.M0_PHI(tag, lbmState);
                const real_t As_n = Model.compute_anisotropy(tag, lbmState);
                real_t As2 = As_n*As_n;
                const RVect2 N = Model.compute_anisotropy_vector(tag, lbmState);
                
                const real_t psi_st = Model.psi_st(tag, lbmState);

             - Check neighbors for non-local term of collision

             .. code-block:: ruby
                :emphasize-lines: 1-4

                IVect<dim> IJKs;
                can_str = this->stream_alldir(IJK,IJKs,0);
                if (can_str) 	{collider.f_nonlocal[0] = this->get_f_val(tag,IJKs,0);}
                else 			{collider.f_nonlocal[0] = 0.0;}
                
             - Define all necessary inputs for collision

             .. code-block:: ruby
                :emphasize-lines: 1-18
                
                // compute collision rate
                collider.tau = Model.tau_PHI_Crystal (tag, lbmState, As2);
                // ipop = 0
                collider.f[0] = Base::get_f_val(tag,IJK,0);
                collider.S0[0] = w[0]*dt*psi_st;
                collider.feq[0] = w[0]*(M0-e2*Base::compute_scal(0,N)*(dt/dx)*fact);
                collider.factor = As2;
                
                // ipop > 0
                for (int ipop=1; ipop<npop; ++ipop) {
                  collider.f[ipop] = this->get_f_val(tag,IJK,ipop);
                  collider.S0[ipop] = dt*w[ipop]*psi_st;
                  collider.feq[ipop] = w[ipop]*(M0-e2*Base::compute_scal(ipop,N)*(dt/dx)*W0*W0/tau0);
                  can_str = this->stream_alldir(IJK,IJKs,ipop);
                  if (can_str) 	{collider.f_nonlocal[ipop] = this->get_f_val(tag,IJKs,ipop);}
                  else 			{collider.f_nonlocal[ipop] = 0.0;}
                }
                
                } // end of setup_collider for phase field equation
                //==================================================================

      
      .. admonition:: Function ``init_macro``
         :class: caution

         After the initialization for ``ADE_GAUSSIAN``:
   
          .. code-block:: ruby

             if (Model.initType == ADE_GAUSSIAN) {
               c  = Model.ampl * exp( - ( SQR(x-Model.x0) / (2 * SQR(Model.sigmax)) + SQR(y-Model.y0) / (2 * SQR(Model.sigmay)) )) ;
               vx = Model.initVX;
               vy = Model.initVY;
             }
             else if (Model.initType == PHASE_FIELD_INIT_VERTICAL) {
               xphi = x - Model.x0;
               c    = Model.undercooling ;
             }
             
             real_t phi = Model.phi0(xphi);

         - Write an initial condition corresponding to keywords ``PHASE_FIELD_INIT_SPHERE``
	
          .. dropdown:: Solution for a circle
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 1,2,3,4,5,6

                else if (Model.initType == PHASE_FIELD_INIT_SPHERE){
                  xphi = (Model.r0 - sqrt( SQR(x-Model.x0) + SQR(y-Model.y0)) );
                  c    = Model.undercooling ;
                }
                //real_t phi = Model.phi0(xphi);
                real_t psi = Model.phi1(xphi);
                

         - Save in appropriate arrays

          .. dropdown:: Solution
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 4,5
                
                this->set_lbm_val(IJK, ITEMP, c );
                this->set_lbm_val(IJK, IU   , vx);
                this->set_lbm_val(IJK, IV   , vy);
                //this->set_lbm_val(IJK,IPHI,phi);
                this->set_lbm_val(IJK,IPHI,psi);


      
      .. admonition:: Function ``update_macro_grad``
         :class: caution

         That function is currently empty

          .. code-block:: ruby

             KOKKOS_INLINE_FUNCTION
             void update_macro_grad(IVect<dim> IJK) const
             {
             }

         - Add the computation of gradient

          .. dropdown:: Solution
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 4,5,6,7

                KOKKOS_INLINE_FUNCTION
                void update_macro_grad(IVect<dim> IJK) const
                {
		            RVect<dim> gradPhi;
		            this->compute_gradient(gradPhi, IJK, IPHI, BOUNDARY_EQUATION_1);
		            this->set_lbm_val(IJK,IDPHIDX,gradPhi[IX]);
		            this->set_lbm_val(IJK,IDPHIDY,gradPhi[IY]);
                }


   .. tab-item:: File ``InitConditionsTypes.h``

      .. admonition:: Add the keywords of initial conditions
         :class: caution

         In file ``InitConditionsTypes.h``, two keywords are currently declared:

          .. code-block:: ruby

             enum InitCondition{
                PHASE_FIELD_INIT_UNDEFINED,
                ADE_GAUSSIAN,
                PHASE_FIELD_INIT_VERTICAL
             };

         Simply add after ``PHASE_FIELD_INIT_VERTICAL`` the new keyword for Allen-Cahn: ``PHASE_FIELD_INIT_SPHERE``.

          .. dropdown:: Solution
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 5

                enum InitCondition{
                  PHASE_FIELD_INIT_UNDEFINED,
                  ADE_GAUSSIAN,
                  PHASE_FIELD_INIT_VERTICAL,
                  PHASE_FIELD_INIT_SPHERE
                };


3. Verifications of your implementation
---------------------------------------

.. admonition:: Run and post-process your results
   :class: important
   
   An input file ``Crystal-Equiaxe.ini`` is given in the folder ``Tutorial03_Crystal-Growth``.
   
   - Run LBM_Saclay with that input file
   - Post-process your ``.vti`` outputs with the pvpython input file ``Video-plus-Contour.pvpy`` for paraview 5.11
      
    .. code-block:: shell
       
       $ /tmp_formation/LBM_Saclay/ParaView/ParaView-5.11.0-MPI-Linux-Python3.9-x86_64/bin/pvpython Video-plus-Contour.pvpy

    The outputs are several ``.csv`` files plus one video (``.avi`` format).

   - Run the video generated by the post-processing

    .. code-block:: shell

       $ vlc Vid-Crystal-Growth_Equiaxe.avi


   .. div:: sd-text-center

      .. raw:: html
   
         <video controls src="../../_static/Vid-Crystal-Growth_Equiaxe.webm" width="650" height="480"> </video>

      Video: simulation of 2D crystal growth

   
   - Compare the evolution of velocity tip with the steady reference.

    .. code-block:: shell

       $ python tip_velocity_contour.py

    You must obtain Fig. :numref:`Fig-Tip-Velocity-Crystal-Growth`

    .. figure:: ../FIGS/01_FIGS_VALIDATIONS/Fig_Tip-Velocity_Tuto_Crystal-Growth.png
       :name: Fig-Tip-Velocity-Crystal-Growth
       :height: 350
       :width: 500
       :scale: 95
       :align: center
   
       Comparison between LBM and reference solution of Karma-Rappel
   


.. sectionauthor:: Alain Cartalade & Capucine Méjanès
