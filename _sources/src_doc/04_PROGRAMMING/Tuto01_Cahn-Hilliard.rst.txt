.. include:: ../Substitutions.rst

.. _Tuto-Cahn-Hilliard:

Implementation of a Cahn-Hilliard model
=======================================

Objective of this 1st tutorial
------------------------------

The objective of this tutorial is to implement a kernel to simulate the Cahn-Hilliard equation (Eq. :eq:`CH_Eq_TwoPhase` with chemical potential defined by Eq. :eq:`Chem_Pot_TwoPhase`). The starting point is the kernel ``ADE_for_CH-Tutorial`` which simulates the Advection-Diffusion Equation (ADE) with the lattice Boltzmann method. This tutorial provides all code lines to write in each file for simulating three test cases with the Cahn-Hilliard model: serpentine, spinodal decomposition and nucleation. The verification tests will be carried out with the input files (``.ini``) contained in the folder ``Tutorial01_Cahn-Hilliard/`` in ``run_training_lbm``.

It is assumed that you have already downloaded ``LBM_Saclay_Rech-Dev`` and you are working on your own branch (see :bdg-ref-primary-line:`Git-Commands`).

1. Create a new kernel ``CH`` for Cahn-Hilliard
-----------------------------------------------

.. admonition:: Copy the ADE kernel template and rename all files with new extension ``_CH``
   :class: caution

   - Copy the folder ``ADE_for_CH-Tutorial`` which is contained in ``kernels/Templates_for_Tutorials``, and rename it ``Cahn-Hilliard_Tutorial`` in the folder ``kernels``

    .. dropdown:: Commands
       :icon: comment

       .. code-block:: shell

          $ cd LBM_Saclay_Rech-Dev/src/kernels
          $ cp -r Templates_for_Tutorials/ADE_for_CH-Tutorial ./Cahn-Hilliard_Tutorial

       .. admonition:: Remarks
          :class: important

          - Your new developments will be performed in the folder ``Cahn-Hilliard_Tutorial``
          - The folder name ``Cahn-Hilliard_Tutorial`` will be used for compilation

   - All files have the extension ``_ADE`` for Advection Diffusion Equation. Rename them with ``_CH`` for Cahn-Hilliard.

    .. dropdown:: Commands
       :icon: comment

       .. code-block:: shell

          $ cd Cahn-Hilliard_Tutorial

          $ mv Index_ADE.h Index_CH.h
          $ mv LBMScheme_ADE.h LBMScheme_CH.h
          $ mv Models_ADE.h Models_CH.h
          $ mv Problem_ADE.h Problem_CH.h

.. admonition:: Edit them and change strings ``_ADE`` with ``_CH``
   :class: caution

   1. Change strings ``_ADE`` with ``_CH``

      - Open all files in your favorite editor (e.g. ``geany`` or ``codium``).
      - Search in all files the strings ``_ADE`` and replace them with ``_CH`` (``Ctrl H`` with ``geany``).
   
   2. Change the problem name: in file ``Setup.h`` modify the problem name ``ADE`` with ``CH``

      .. code-block:: ruby
       
         register_problem<Problem, ModelParams::Tag2Quadra>("ADE", "base");

      .. dropdown:: Modification  with ``CH``
         :icon: comment

         .. code-block:: ruby
            :emphasize-lines: 1

            register_problem<Problem, ModelParams::Tag2Quadra>("CH", "base");

         .. admonition:: Remark
            :class: important

            Your new problem will be named ``CH`` inside your ``.ini`` input file i.e. in section ``[lbm]`` your problem must be:

            .. code-block:: ruby
               :emphasize-lines: 2

               [lbm]
               problem=CH



.. admonition:: Compile your new kernel
   :class: caution

   - Generate your ``makefile`` (only once)

    .. dropdown:: Commands
       :icon: comment

       .. code-block:: shell

          $ cd LBM_Saclay_Rech-Dev
          $ mkdir build_CH
          $ cd build_CH
          $ cmake -DKokkos_ENABLE_OPENMP=ON -DUSE_HDF5=ON -DPROBLEM=Cahn-Hilliard_Tutorial ..

   - Compile

    .. dropdown:: Command
       :icon: comment

       .. code-block:: shell

          $ make -j 22

.. admonition:: Run with input files of ADE
   :class: caution

   - Execute your new kernel ``CH`` of LBM_Saclay either with the simple diffusion of gaussian or with the advected gaussian in the folder ``run_training_lbm/Tutorial01_Cahn-Hilliard``

    .. dropdown:: Commands
       :icon: comment

       Go to the directory

         .. code-block:: shell

            $ cd LBM_Saclay_Rech-Dev/run_training_lbm/Tutorial01_Cahn-Hilliard

       Run simple diffusion of gaussian

         .. code-block:: shell

            $ ../../build_CH/src/LBM_saclay TestCase_Gaussian_ADE.ini

       Run advected gaussian

         .. code-block:: shell

            $ ../../build_CH/src/LBM_saclay TestCase_Moving-Gaussian_ADE.ini

   - Check the solutions with paraview.

.. _Advice-During-Implementation:

2. Modifications inside each file of ``CH``
-------------------------------------------

.. admonition:: Advice
   :class: error

   During your implementation, it is strongly recommended to compile regularly (``make`` or ``make -j 22``) to detect any typos.

   For compilation errors, it is useful to write the terminal outputs inside a file e.g. ``compil.log``:

    .. code-block:: shell

       $ make -j 22 2>&1 | tee compil.log

   or alternatively ``compil2.log``

    .. code-block:: shell

       $ make VERBOSE=1 2>&1 | tee compil2.log


.. tab-set:: 

   .. tab-item:: File ``Index_CH.h``

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

         - Add the new indices for chemical potential ``IMU`` and laplacian ``ILAPLAC``.

          .. dropdown:: Solution
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 6,7

                enum ComponentIndex {
                  IU     , /*!< X velocity / momentum index */
                  IV     , /*!< Y velocity / momentum index */
                  IW     , /*!< Z velocity / momentum index */
                  IC     , /*!< Phase field index */
                  IMU    , /*!< Chemical potential */
                  ILAPLAC,     /*!< Laplacien of Phase field */
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

         - Add a new output for chemical potential.
            
          .. dropdown:: Solution
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 5

                map[IC ] = "comp";
                map[IU ] = "vx";
                map[IV ] = "vy";
                map[IW ] = "vz";
                map[IMU] = "mu";

             .. admonition:: Remark
                :class: important

                The keyword ``mu`` will be used in the ``.ini`` input file to write the chemical potential.


   .. tab-item:: File ``Models_CH.h``

      .. admonition:: Read and declare Cahn-Hilliard parameters in ``ModelParams``
         :class: caution

         The Cahn-Hillard equation involves three parameters: the surface tension :math:`\sigma`, the interface thickness :math:`W` and the mobility :math:`\mathcal{M}_\phi`.

         - Read and declare Cahn-Hilliard parameters in ``ModelParams``

          .. dropdown:: Solution
             :icon: comment

             Read parameters in input file:

             .. code-block:: ruby
                :emphasize-lines: 1,2,3

                mobility = configMap.getFloat("params", "mobility", 1.0);
                W        = configMap.getFloat("params", "W"       , 1.0);
                sigma    = configMap.getFloat("params", "sigma"   , 1.0);

             Don't forget to declare them as ``real_t`` at the end of ``ModelParams``

             .. code-block:: ruby
                :emphasize-lines: 1
                
                real_t mobility, W, sigma;

      .. admonition:: Add specific functions for Cahn-Hilliard
         :class: caution

         - Add a new function for derivative of double-well ``g_prime`` defined by the first term inside the bracket of Eq. :eq:`Chem_Pot_TwoPhase`.

          .. dropdown:: Solution ``g_prime``
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 1-5

                // =======================================================
                // Derivative of double-well
                KOKKOS_INLINE_FUNCTION real_t g_prime(real_t c) const {
                  return 16.0 * c * (1.0 - c) * (1.0 - 2.0 * c);
                }

         - Add a new function ``M2`` to compute the chemical potential :math:`\mu` (``MU``) defined by Eq. :eq:`Chem_Pot_TwoPhase`

          .. dropdown:: Solution function ``M2``
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 1-7
                
                // =======================================================
                // second order moment of feq
                KOKKOS_INLINE_FUNCTION
                  real_t M2(EquationTag1 tag, const LBMState &lbmState) const {
                  const real_t mu = sigma*1.5/W * (g_prime(lbmState[IC])-SQR(W)* lbmState[ILAPLAC]);
                  return mu;
                }

             .. admonition:: Remarks
                :class: important

                - ``IC`` & ``ILAPLAC`` have been declared in ``Index_CH.h``.
                - The parameters ``sigma`` (surface tension :math:`\sigma`) and ``W`` (interface thickness :math:`W`) have been read and declared inside ``ModelParams`` (previous box).
                - The new function ``g_prime`` has been defined just above


         - Add a new function ``tauM`` for collision rate using the mobility :math:`\mathcal{M}_\phi` of Cahn-Hilliard equation

          .. dropdown:: Solution ``tauM``
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 1-7

                // =======================================================
                // relaxation coef for LBM scheme of phase field equation
                KOKKOS_INLINE_FUNCTION
                  real_t tauM (EquationTag1 tag, const LBMState &lbmState) const {
                  real_t tau = 0.5 + (e2 * mobility * dt / SQR(dx));
                  return (tau);
                }

             .. admonition:: Remark
                :class: important

                - The parameter ``mobility`` has been read and declared in ``ModelParams``.

                - You could have used the parameter ``D`` as the mobility coefficient. In that case, that new function is useless. But take care, especially if a future coupling with a transport equation is planned.

         - Add the standard hyperbolic tangent function ``phi0`` defined by Eq. :eq:`Hyperbolic_Tangent_Solution_Course` (for initial condition)

          .. dropdown:: Solution ``phi0``
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 1,2,3,4,5

                // ================================================
                // Hyperbolic tangent solution
                KOKKOS_INLINE_FUNCTION real_t phi0(real_t x) const {
                  return 0.5 * (1 + tanh(sign * 2.0 * x / W));
                }

             .. admonition:: Remark
                :class: important

                ``sign`` will take the values ``+1`` or ``-1`` in the input datafile ``.ini`` for initialize ``1`` inside or outside the bubble.

      
      .. admonition:: Add conditions and keywords for several initial conditions
         :class: caution

         Currently only one condition exits for intial condition:

          .. code-block:: ruby

             if (initTypeStr == "gaussian") initType = ADE_GAUSSIAN;
         
         - Add the necessary conditions for three Cahn-Hilliard initializations

          .. dropdown:: Solution
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 2,3,4

                if (initTypeStr == "gaussian") initType = ADE_GAUSSIAN;
                else if (initTypeStr == "serpentine") initType = SERPENTINE;
                else if (initTypeStr == "random") initType = RANDOM_SPINODAL;
                else if (initTypeStr == "nucleation") initType = RANDOM_NUCLEATION;

             .. admonition:: Warning
                :class: error

                Don't forget to declare all keywords ``SERPENTINE``, ``RANDOM_SPINODAL`` and ``RANDOM_NUCLEATION`` in file ``InitConditionsTypes.h``
   
   .. tab-item:: File ``LBMScheme_CH.h``

      .. admonition:: Function ``setup_collider`` with BGK
         :class: caution

         The function ``setup_collider`` is written for solving Advection-Diffusion Equation. It must be modified for solving Cahn-Hilliard equation.

         - First, the 2nd order moment, is currently :math:`c` 

          .. code-block:: ruby

             const real_t M0 = Model.MomentM0(tag, lbmState);
             const RVect<dim> uc = Model.MomentM1<dim>(tag, lbmState);
             const real_t M2 = Model.MomentM2(tag, lbmState);
    
          Modify the call of function to compute :math:`\mu` instead of :math:`c`
         
          .. dropdown:: Solution
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 1,2

                //const real_t M2     = Model.MomentM2(tag, lbmState);
                const real_t MU = Model.M2(tag, lbmState);

         - Next, the appropriate function must be called for collision rate to take into account the mobility :math:`\mathcal{M}_\phi`

          .. code-block:: ruby

		       // compute collision rate
             collider.tau = Model.tau(tag, lbmState);

          .. dropdown:: Solution
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 1
             
                collider.tau = Model.tauM(tag, lbmState);

            

         - Finally, the equilibrium distribution function is currently written for ADE (lines 4 & 10)
	
          .. code-block:: ruby
             :linenos:
             
             // ipop = 0
             collider.f[0]   = Base::get_f_val(tag, IJK, 0);
             collider.S0[0]  = 0.0 ;
             collider.feq[0] = w[0]*M0;
             
             // ipop > 0
             for (int ipop = 1; ipop < npop; ++ipop) {
               collider.f[ipop]   = this->get_f_val(tag, IJK, ipop);
               collider.S0[ipop]  = 0.0 ;
               collider.feq[ipop] = w[ipop] * (M2 + c_cs2 * Base::compute_scal(ipop, uc));

         - Modify it to take into account :math:`c` (moment 0) and :math:`\mu` (moment 2) (see SMEMaG course)

          .. dropdown:: Solution
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 4,9
                :linenos:
                
                // ipop = 0
                collider.f[0]   = Base::get_f_val(tag, IJK, 0);
                collider.S0[0]  = 0.0 ;
                collider.feq[0] = M0 - 3.0*MU*(1 - w[0]);
                // ipop > 0
                for (int ipop = 1; ipop < npop; ++ipop) {
                  collider.f[ipop]   = this->get_f_val(tag, IJK, ipop);
                  collider.S0[ipop]  = 0.0 ;
                  collider.feq[ipop] = 3.0*MU*w[ipop] + w[ipop] * c_cs2 * Base::compute_scal(ipop, uc);

      .. admonition:: Function ``init_macro``
         :class: caution

         Only one initial condition exists for ADE with ``ADE_GAUSSIAN``:
   
          .. code-block:: ruby

             if (Model.initType == ADE_GAUSSIAN) {
	      c  = Model.ampl * exp( - ( SQR(x-Model.x0) / (2 * SQR(Model.sigmax)) + SQR(y-Model.y0) / (2 * SQR(Model.sigmay)) )) ;
	      vx = Model.initVX;
	      vy = Model.initVY;
            }

         - Write three initial conditions corresponding to keywords ``SERPENTINE``, ``RANDOM_SPINODAL`` and ``RANDOM_NUCLEATION``
	
          .. dropdown:: Solution for serpentine
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 1-7
                
                else if (Model.initType == SERPENTINE) {
                  const real_t pi = M_PI;
                  xphi  = (Model.r0 - sqrt(SQR(x - Model.x0) + SQR(y - Model.y0)));
                  c     = Model.phi0(xphi) ;
                  vx    = - pi*Model.U0 * cos(pi*((x/Model.L)-0.5)) * sin(pi*((y/Model.L)-0.5));
                  vy    =   pi*Model.U0 * sin(pi*((x/Model.L)-0.5)) * cos(pi*((y/Model.L)-0.5));
                }

             .. admonition:: Warning
                :class: error

                At line ``c = Model.phi0(xphi) ;`` the position ``xphi`` is "regularized" with the hyperbolic tangent function ``phi0``. Don't forget to define it in ``Models_CH.h``.

          .. dropdown:: Solution for spinodal
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 1-3
                
                else if (Model.initType == RANDOM_SPINODAL) {
                  c = rand_gen.drand();
                }

          .. dropdown:: Solution for nucleation
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 1-10
                
                else if (Model.initType == RANDOM_NUCLEATION) {
                  if (IJK[IX] % Model.valModuloX || IJK[IY] % Model.valModuloY ) {
                     c = 0.2 ;
                  }
                else {
                  real_t r    = 0.0;
                  r = rand_gen.drand();
                  c = (9.0+r)/10.0 ;
                  }
                }

             .. admonition:: Remark
                :class: important

                Both integers ``valModuloX`` and ``valModuloY`` have already been declared in file ``Models_CH``.

      .. admonition:: Function ``update_macro``
         :class: caution

         Currently, only the concentration and the velocity are updated:

          .. code-block:: ruby
            
             const real_t c  = moment_c;
             const real_t vx = Model.initVX;
             const real_t vy = Model.initVY;
             
             this->set_lbm_val(IJK, IC , c );
             this->set_lbm_val(IJK, IU , vx );
             this->set_lbm_val(IJK, IV , vy );

         Add for chemical potential and add a condition for velocity of ``SERPENTINE`` option

          .. dropdown:: Solution
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 3,4,5,6,7,8,9,10,15
                
                const real_t c  = moment_c;
                
                real_t vx = Model.initVX;
                real_t vy = Model.initVY;
                const real_t mu = Model.M2(tagC, lbmStatePrev);
                if (Model.initType == SERPENTINE) {
                  const real_t pi = M_PI;
                  vx    = - pi*Model.U0 * cos(pi*((x/Model.L)-0.5)) * sin(pi*((y/Model.L)-0.5));
                  vy    =   pi*Model.U0 * sin(pi*((x/Model.L)-0.5)) * cos(pi*((y/Model.L)-0.5));
                }
                
                this->set_lbm_val(IJK, IC , c );
                this->set_lbm_val(IJK, IU , vx );
                this->set_lbm_val(IJK, IV , vy );
                this->set_lbm_val(IJK, IMU, mu);
      
      .. admonition:: Function ``update_macro_grad``
         :class: caution

         Currently the function is empty because for ADE, there is no need to compute additional gradients or laplacian with the LB method.
         
          .. code-block:: ruby

             KOKKOS_INLINE_FUNCTION
             void update_macro_grad(IVect<dim> IJK) const {
		
             }
         
         This is not the case for Cahn-Hilliard equation because a laplacian is involved in the definition of chemical potential. Add the computation of laplacian.

          .. dropdown:: Solution
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 3,4

                KOKKOS_INLINE_FUNCTION
                void update_macro_grad(IVect<dim> IJK) const {
		            real_t laplace_c = Base::compute_laplacian(IJK, IC, BOUNDARY_EQUATION_1);
		            Base::set_lbm_val(IJK, ILAPLAC, laplace_c);
                }


   .. tab-item:: File ``InitConditionsTypes.h``

      .. admonition:: Add the keywords of initial conditions
         :class: caution
         
         In file ``InitConditionsTypes.h``, two keywords are currently declared:

          .. code-block:: ruby

             enum InitCondition{
	             PHASE_FIELD_INIT_UNDEFINED,
	             ADE_GAUSSIAN
             };

         - Add the three new keywords for Cahn-Hilliard: ``SERPENTINE``, ``RANDOM_SPINODAL`` and ``RANDOM_NUCLEATION``.

          .. dropdown:: Solution
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 4,5,6

                enum InitCondition{
                   PHASE_FIELD_INIT_UNDEFINED,
                   ADE_GAUSSIAN,
                   RANDOM_SPINODAL,
                   RANDOM_NUCLEATION,
                   SERPENTINE
                };

   

3. Verifications of your implementation
---------------------------------------

Three ``.ini`` input files are available in the directory ``Tutorial01_Cahn-Hilliard`` to check your implementation for each initial condition:

   - ``Tuto-CH_Test01-Serpentine.ini``
   - ``Tuto-CH_Test02-Spinodal.ini``
   - ``Tuto-CH_Test03-Nucleation.ini``

It is recommended to start with ``Tuto-CH_Test01-Serpentine.ini`` because comparisons can be done with ``csv`` files contained in the folder ``Contours_CAC``.

.. tab-set::

   .. tab-item:: Serpentine

      .. admonition:: Run ``Tuto-CH_Test01-Serpentine.ini``
         :class: important

         - Run ``Tuto-CH_Test01-Serpentine.ini``

          .. dropdown:: Commands
             :icon: comment

             Go to the appropriate folder

             .. code-block:: shell

                $ cd run_training_lbm/Tutorial01_Cahn-Hilliard
   
             and run LBM_Saclay

             .. code-block:: shell

                $ ../../build_CH/src/LBM_saclay Tuto-CH_Test01-Serpentine.ini

         - Once the simulations is over, post-process your results with paraview.

          Open paraview (e.g. version 5.11) and compare the contours from Cahn-Hilliard ``.vti`` files and ``csv`` files of subfolder ``Contours_CAC``.
   
          .. dropdown:: Commands for contours
             :icon: comment

             - Open all ``.vti`` files and select ``comp``
             - ``Ctrl space`` and ``Cell Data to Point Data`` and ``Apply``
             - Clic on ``contour`` and select field ``comp`` with value ``0.5`` and ``Apply``

          .. dropdown:: Commands for csv files
             :icon: comment

             - Open ``csv`` files (choose option ``CSV Reader``) + ``OK`` + ``Apply``
             - Crtl space + ``Table To Points`` + select ``Points:0`` for X Column and ``Points:2`` for Y Column
             - Play with ``Point Size`` in section ``Styling``

   .. tab-item:: Spinodal

      .. admonition:: Run & post-process
         :class: important

         - Run Spinodal decomposition: ``Tuto-CH_Test02-Spinodal.ini``
         - Make a video with paraview (version 5.11)
    
          .. code-block:: shell
             
             $ path-to-pvpython/pvpython Make-Movie-Spinodal_PV511.pvpy

         - You must obtain the video below

         .. div:: sd-text-center

            .. raw:: html
   
               <video controls src="../../_static/Movie-Spinodal.webm" width="650" height="480"> </video>

            Video: simulation of spinodal decomposition

   .. tab-item:: Nucleation

      .. admonition:: Run & post-process
         :class: important

         - Run Nucleation: ``Tuto-CH_Test03-Nucleation.ini``
         - Make a video with paraview (version 5.11)

          .. code-block:: shell

             $ path-to-pvpython/pvpython Make-Movie-Nucleation_PV511.pvpy

         - You must obtain the video below

         .. div:: sd-text-center

            .. raw:: html
   
               <video controls src="../../_static/Movie-Nucleation.webm" width="650" height="480"> </video>

            Video: simulation of spinodal decomposition

4. From Cahn-Hilliard toward Conservative Allen-Cahn model
----------------------------------------------------------

Modificatons inside three files
"""""""""""""""""""""""""""""""

.. admonition:: Mathematical model & LBM scheme
   :class: error

   - Now we want to simulate the conservative Allen-Cahn model Eq. :eq:`CAC_Course`.
   - The LBM scheme is the second method in :bdg-ref-primary-line:`LBM scheme <LBMScheme-for-CAC>`

.. tab-set::

   .. tab-item:: File ``Index_CH.h``

      .. admonition:: Declaration of new fields
         :class: caution

         - In ``enum ComponentIndex``, add new indices ``IDPHIDX`` and ``IDPHIDY``

          .. dropdown:: Solution
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 8,9
                
                enum ComponentIndex {
                  IU     , /*!< X velocity / momentum index */
                  IV     , /*!< Y velocity / momentum index */
                  IW     , /*!< Z velocity / momentum index */
                  IC     , /*!< Phase field index */
                  IMU    , /*!< Chemical potential */
                  ILAPLAC,     /*!< Laplacien of Phase field */
                  IDPHIDX,       /*!< Grad X of Phase field */
                  IDPHIDY,       /*!< Grad Y of Phase field */
                  COMPONENT_SIZE /*!< invalid index, just counting number of fields */
                };

   .. tab-item:: File ``Models_CH.h``

      .. admonition:: ``struct ModelParams``
         :class: caution

         - Add a new constant value :math:`\epsilon=10^{-16}` for computation of normal vector :math:`\boldsymbol{n}`

          .. dropdown:: Solution
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 2

                using LBMState = typename Kokkos::Array<real_t, COMPONENT_SIZE>;
                static constexpr real_t NORMAL_EPSILON = 1.0e-16;


         - Read and declare a new flag (real) ``counter_term`` for CAC model. If ``counter_term=0`` then the Cahn-Hilliard model will be simulated. Else If ``counter_term=1``, the CAC model will be solved.

          .. dropdown:: Solution
             :icon: comment

             - Read

              .. code-block:: ruby
                 :emphasize-lines: 1

                 counter_term = configMap.getFloat("params","counter_term",0.0);

             - Declare

              .. code-block:: ruby
                 :emphasize-lines: 1

                 real_t counter_term;
             

             
      .. admonition:: Add specific functions for CAC
         :class: caution

         - Add a function ``Source_CT`` for counter term :math:`(4/W)M_{\phi}\phi(1-\phi)\boldsymbol{n}`

          .. dropdown:: Solution ``Source_CT``
             :icon: comment
             
             .. code-block:: ruby
                :emphasize-lines: 1-12
                
                // =======================================================
                // Source term for counter term of phase field equation
                KOKKOS_INLINE_FUNCTION
                RVect2 Source_CT (EquationTag1 tag, const LBMState& lbmState) const
                {
                  const real_t norm = sqrt( SQR(lbmState[IDPHIDX]) + SQR(lbmState[IDPHIDY]))+NORMAL_EPSILON;
                  real_t force_ct = Mphi * 4.0*lbmState[IPHI]*(1.0-lbmState[IPHI])/ W / norm;
                  RVect2 term;
                  term[IX] = force_ct * lbmState[IDPHIDX];
                  term[IY] = force_ct * lbmState[IDPHIDY];
                  return term;
                }

         - Rename the second order function for CH ``M2_CH`` and add a new one ``M2_CAC`` for CAC

          .. dropdown:: Solutions ``M2_CAC`` and ``M2_CH``
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 1-6, 11
                
                // =======================================================
                // Second order moment of feq for CAC model
                KOKKOS_INLINE_FUNCTION
                real_t M2_CAC(EquationTag1 tag, const LBMState &lbmState) const {
                  return lbmState[IC];
                }
                
                // =======================================================
                // second order moment of feq for CH model
                KOKKOS_INLINE_FUNCTION
                real_t M2_CH(EquationTag1 tag, const LBMState &lbmState) const {
                  const real_t mu = sigma * 1.5 / W * (g_prime(lbmState[IC]) - SQR(W) * lbmState[ILAPLAC]);
                  return mu;
                }

             

   .. tab-item:: File ``LBMScheme_CH.h``

      .. admonition:: Function ``setup_collider``
         :class: caution

         - Add ``if`` - ``else if`` with ``counter_term`` for Cahn-Hilliard or Conservative Allen-Cahn

          .. dropdown:: Solution
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 4,7,23,24,25

                LBMState lbmState;
                Base::template setupLBMState2<LBMState, COMPONENT_SIZE>(IJK, lbmState);
                
                if (Model.counter_term == 0.0) {
                  const real_t comp   = Model.M0(tag, lbmState);
                  const RVect<dim> uc = Model.M1<dim>(tag, lbmState);
                  const real_t MU     = Model.M2_CH(tag, lbmState);
                  
                  // compute collision rate
                  collider.tau = Model.tau(tag, lbmState);
                  
                  // ipop = 0
                  collider.f[0]   = Base::get_f_val(tag, IJK, 0);
                  collider.S0[0]  = 0.0 ;
                  collider.feq[0] = comp -3.0*MU*(1 - w[0]);
                  
                  // ipop > 0
                  for (int ipop = 1; ipop < npop; ++ipop) {
                     collider.f[ipop]   = this->get_f_val(tag, IJK, ipop);
                     collider.S0[ipop]  = 0.0 ;
                     collider.feq[ipop] = 3.0*MU*w[ipop] + w[ipop] * c_cs2 * Base::compute_scal(ipop, uc);
                  }
                }
                else if (Model.counter_term == 1.0) {
                }

         - The second part ``else if`` is empty. Add the necessary code lines to solve CAC model

          .. dropdown:: Solution
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 2-14

                else if (Model.counter_term == 1.0) {
                  const real_t     M0   = Model.M0(tag, lbmState);
                  const RVect<dim> M1   = Model.M1<dim>(tag, lbmState);
                  const real_t     M2   = Model.M2_CAC(tag, lbmState);
                  const RVect2     G_ct = Model.Source_CT(tag, lbmState);		
                     
                  // compute collision rate
                  collider.tau = Model.tau(tag, lbmState);
                  real_t staudx = 1.0/((collider.tau-0.5)*dx/e2);
                  for (int ipop=0; ipop<npop; ++ipop) {
                     collider.f[ipop  ] = this->get_f_val(tag,IJK,ipop);
                     collider.S0[ipop ] = w[ipop] * dt * staudx * Base::compute_scal(ipop,G_ct);
                     collider.feq[ipop] = w[ipop] * (M2 + c_cs2 * Base::compute_scal(ipop, M1) ) - 0.5 * (collider.S0[ipop]);
                  }
                }

      .. admonition:: Function ``update_macro_grad``
         :class: caution

         - Update gradient computation for :math:`\boldsymbol{n}=\boldsymbol{\nabla}\phi/|\boldsymbol{\nabla}\phi|`

          .. dropdown:: Solution
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 9-12

                // =============================================================
                // Update gradients of macrosopic variables
                KOKKOS_INLINE_FUNCTION
                void update_macro_grad(IVect<dim> IJK) const
                {
                  real_t laplace_c = Base::compute_laplacian(IJK, IC, BOUNDARY_EQUATION_1);
                  Base::set_lbm_val(IJK, ILAPLAC, laplace_c);
                  
                  RVect<dim> gradPhi;
                  this->compute_gradient(gradPhi, IJK, IC, BOUNDARY_EQUATION_1);
                  this->set_lbm_val(IJK, IDPHIDX, gradPhi[IX]);
                  this->set_lbm_val(IJK, IDPHIDY, gradPhi[IY]);
                }

Verifications of your implementation
""""""""""""""""""""""""""""""""""""

.. admonition:: Verification of your implementation
   :class: important

   - Run your CAC model with the input file ``Tuto-CH_Test04_CAC_Serpentine.ini`` which is contained in the folder ``run_training_lbm/Tutorial01_Cahn-Hilliard``
   - Compare your contours with those in the subfolder ``Contours_CAC``


5. Push your developments on Codev-Tuleap
-----------------------------------------

.. admonition:: Save your developments on ``codev-tuleap.cea.fr``
   :class: hint

   Once your verifications are carried out, save only your implementation (not your output ``.vti`` files). See commands on :bdg-ref-primary-line:`Push-Implementation`




.. sectionauthor:: Alain Cartalade