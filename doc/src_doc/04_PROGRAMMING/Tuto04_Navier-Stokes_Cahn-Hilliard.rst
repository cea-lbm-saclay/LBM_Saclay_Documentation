.. include:: ../Substitutions.rst

.. _Tuto-Navier-Stokes_Cahn-Hilliard:

Implementation of a Navier-Stokes/Cahn-Hilliard model 
=====================================================

Objective of this 4th tutorial
------------------------------

The objective is to implement in LBM_Saclay, the Navier-Stokes/Cahn-Hilliard model. The starting point is the kernel ``CH`` implemented in the first tutorial. It will be extended here with the Navier-Stokes (NS) equations and renamed ``NSCH``.

.. admonition:: Mathematical model
   :class: error
   
   The model summarized in :bdg-ref-primary-line:`Summary of Navier-Stokes/phase-field model <Summary-NS-PF-model>` composed of incompressible Navier-Stokes equations Eqs. :eq:`TwoPhase_MassBalance` - :eq:`Chem_Pot_TwoPhase`  coupled with a Cahn-Hilliard equation Eq. :eq:`CH_Eq_TwoPhase`. Two forces appear in that model: 1) the capillary force defined by Eq. :eq:`Proof-Equiv-Surface-Tension_NSAC` :math:`\boldsymbol{F}_c=\mu_{\phi}\boldsymbol{\nabla}\phi` and 2) the gravity force defined by :math:`\boldsymbol{F}_g=\varrho\boldsymbol{g}`.

.. admonition:: Objective
   :class: important

   In this tutorial, we will see how to
   
   - add a new equation (like tuto 2)
   - add a MRT collision operator for LBM relative to NS equations
   - add external force terms :math:`\boldsymbol{F}_c` and :math:`\boldsymbol{F}_g`

1. Create a new kernel ``NSCH``
-------------------------------

.. admonition:: Create a new kernel ``NSCH``
   :class: note

   You can refer to Tuto 1 & 2 where all commands have been presented in detail:

   1. Copy your kernel ``CH`` and rename it ``NSCH_Tutorial`` in directory ``LBM_Saclay_Rech-Dev/src/kernels/``
   2. Go to your new folder ``NSCH_Tutorial`` and replace all files with extension ``_CH`` by ``_NSCH``
   3. Edit your files and replace ``_CH`` with ``_NSCH``
   4. In file ``Setup.h`` replace the problem name ``CH`` by ``NSCH``
   5. Create your ``Makefile`` with option ``-DPROBLEM=NSCH_Tutorial`` and compile


2. Add a new equation in your kernel ``NSCH``
---------------------------------------------

The mathematical model is currently composed of one Cahn-Hilliard equation. It is necessary to add one supplementary equation.

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

         - Add a new block ``if`` - ``else if`` for ``collisionType2`` & ``EquationTag2``

          .. dropdown:: Solution
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 7,8,9,10,11

                if (params.collisionType1 == BGK) {
                  init1eq<EquationTag1, BGKCollider<dim, npop>>();
                } else if (params.collisionType1 == MRT) {
                  init1eq<EquationTag1, MRTCollider<dim, npop>>();
                }

                if (params.collisionType2 == BGK) {
                  init1eq<EquationTag2, BGKCollider<dim, npop>>();
                } else if (params.collisionType2 == MRT) {
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

         - Add a new block ``if`` - ``else if`` for ``collisionType2`` & ``EquationTag2``

          .. dropdown:: Solution
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 7-11

                if (params.collisionType1 == BGK) {
                  update1eq<EquationTag1, BGKCollider<dim, npop>>();
                } else if (params.collisionType1 == MRT) {
                  update1eq<EquationTag1, MRTCollider<dim, npop>>();
                }

                if (params.collisionType2 == BGK) {
                  update1eq<EquationTag2, BGKCollider<dim, npop>>();
                } else if (params.collisionType2 == MRT) {
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

         - Add a new tag ``tagNS`` for ``EquationTag2``

          .. dropdown:: Solution
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 2

                EquationTag1 tagC;
                EquationTag2 tagNS;

         - Add two empty functions called ``setup_collider`` for ``EquationTag2`` with respectively BGK and MRT collisions

          .. dropdown:: Solution
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 1-8

                KOKKOS_INLINE_FUNCTION
                void setup_collider(EquationTag2 tag, const IVect<dim>& IJK, BGK_Collider& collider) const
                {
                }

                KOKKOS_INLINE_FUNCTION
                void setup_collider(EquationTag2 tag, const IVect<dim>& IJK, MRT_Collider& collider) const
                {
             
             .. admonition:: Remark
                :class: important

                Those two functions are empty (but declared). The second one will be filled below.


      .. admonition:: Function ``make_boundary``
         :class: caution

         The boundary conditions are applied only for Cahn-Hilliard equation

          .. code-block:: ruby

             // phi boundary
             if (Base::params.boundary_types[BOUNDARY_EQUATION_1][faceId] == BC_ANTI_BOUNCE_BACK) {
               real_t boundary_value = Base::params.boundary_values[BOUNDARY_CONCENTRATION][faceId];

               for (int ipop = 0; ipop < npop; ++ipop)
                  this->compute_boundary_antibounceback(tagC, faceId, IJK, ipop, boundary_value);
             }
             else if (Base::params.boundary_types[BOUNDARY_EQUATION_1][faceId] == BC_ZERO_FLUX) {
               for (int ipop = 0; ipop < npop; ++ipop)
                  this->compute_boundary_bounceback(tagNS, faceId, IJK, ipop, 0.0);
             }

         - Add a new block ``if`` - ``else if`` for ``BOUNDARY_EQUATION_2`` and ``tagNS`` with keyword ``BOUNDARY_PRESSURE``

          .. dropdown:: Solution
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 1-12

                if (Base::params.boundary_types[BOUNDARY_EQUATION_2][faceId] == BC_ANTI_BOUNCE_BACK) {
                  real_t boundary_value = this->params.boundary_values[BOUNDARY_PRESSURE][faceId];
                  for (int ipop = 0; ipop < npop; ++ipop) {
                     this->compute_boundary_antibounceback(tagNS, faceId, IJK, ipop, boundary_value);
                  }
                }
                
                else if (Base::params.boundary_types[BOUNDARY_EQUATION_2][faceId] == BC_ZERO_FLUX) {
                  for (int ipop = 0; ipop < npop; ++ipop)
                     this->compute_boundary_bounceback(tagNS, faceId, IJK, ipop, 0.0);
                  }
                }

3. Modifications inside each file of ``NSCH``
---------------------------------------------

.. tab-set:: 

   .. tab-item:: File ``Index_NSCH.h``

      .. admonition:: Declaration of new fields

         In ``enum ComponentIndex``, only the indices relative to Cahn-Hilliard model are declared:

          .. code-block:: ruby

             enum ComponentIndex {
               IU     , /*!< X velocity / momentum index */
               IV     , /*!< Y velocity / momentum index */
               IW     , /*!< Z velocity / momentum index */
               IC     , /*!< Phase field index */
               IMU    , /*!< Chemical potential */
               ILAPLAC,     /*!< Laplacien of Phase field */
               COMPONENT_SIZE /*!< invalid index, just counting number of fields */
             };

         - Complete the list with hydrodynamics indices density :math:`\varrho`, hydrodynamic pressure :math:`p_h`, gradient :math:`\boldsymbol{\nabla}\phi`, gradient :math:`\boldsymbol{\nabla}\varrho` and total force :math:`\boldsymbol{F}_{tot}`.

          .. dropdown:: Solution
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 5,8-18

                enum ComponentIndex {
                  IU     , /*!< X velocity / momentum index */
                  IV     , /*!< Y velocity / momentum index */
                  IW     , /*!< Z velocity / momentum index */
                  IPHI   , /*!< Phase field index */
                  IMU    , /*!< Chemical potential */
                  ILAPLAC,     /*!< Laplacien of Phase field */
                  ID,
                  IP,
                  DPHIDX,
                  DPHIDY,
                  DPHIDZ,
                  DRHODX,
                  DRHODY,
                  DRHODZ,
                  IFX,           /*!< Force Navier Stokes X */
                  IFY,           /*!< Force Navier Stokes Y */
                  IFZ,           /*!< Force Navier Stokes Z */
                  COMPONENT_SIZE /*!< invalid index, just counting number of fields */
                };

      .. admonition:: Add new outputs

         In ``struct index2names`` only the strings for Cahn-Hilliard model are written:

          .. code-block:: ruby

             map[IC ] = "comp";
             map[IU ] = "vx";
             map[IV ] = "vy";
             map[IW ] = "vz";
             map[IMU] = "mu";

         - Add a new outputs for density and pressure (and more if wanted).
            
          .. dropdown:: Solution
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 6-7

                map[IPHI] = "phi";
                map[IU  ] = "vx";
                map[IV  ] = "vy";
                map[IW  ] = "vz";
                map[IMU ] = "mu";
                map[ID  ] = "rho";
                map[IP  ] = "pressure";


   .. tab-item:: File ``Models_NSCH.h``

      .. admonition:: Read and declare Navier-Stokes parameters in ``ModelParams``
      
         The Navier-Stokes equations involve several parameters: the kinematic viscosity :math:`\nu_1` of fluid 1 (respectively :math:`\nu_2` of fluid 2), the density :math:`\rho_1` (:math:`\rho_2`). The surface tension :math:`\sigma` has already been read as input paramater for Cahn-Hilliard equation. Also read the components of gravity :math:`\boldsymbol{g}=(g_x,g_y,g_z)` (``gx``, ``gy``, ``gz``)

         - Read and declare the Navier-Stokes parameters in ``ModelParams``

          .. dropdown:: Solution
             :icon: comment

             Read parameters in input file:

             .. code-block:: ruby
                :emphasize-lines: 1-7

                rho0 = configMap.getFloat("params", "rho0", 1.0);
                rho1 = configMap.getFloat("params", "rho1", 1.0);
                nu0  = configMap.getFloat("params", "nu0" , 1.0);
                nu1  = configMap.getFloat("params", "nu1" , 1.0);
                gx   = configMap.getFloat("params", "gx"  , 0.0);
                gy   = configMap.getFloat("params", "gy"  , 0.0);
                gz   = configMap.getFloat("params", "gz"  , 0.0);

         - Declare them as ``real_t`` at the end of ``ModelParams``

          .. dropdown:: Solution
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 1
                
                real_t rho0, rho1, nu0, nu1, gx, gy, gz;

      .. admonition:: Add specific functions for Navier-Stokes

         - Add a new harmonic function ``tau_NS`` for relaxation rate :math:`\tau_{NS}`

          .. dropdown:: Solution ``tau_NS``
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 1-10

                // =======================================================
                // relaxation coef for LBM scheme
                //
                KOKKOS_INLINE_FUNCTION
                real_t tau_NS(const LBMState &lbmState) const {
                  const real_t phi = lbmState[IPHI];
                  const real_t nu  = nu0 * nu1 / (((1.0 - phi) * nu1) + ((phi)*nu0));
                  real_t tau = 0.5 + (e2 * nu * dt / SQR(dx));
                  return (tau);
                }

         - Add a new function ``interpol_rho`` for linear interpolation of density :math:`\varrho=\rho_1\phi+\rho_2(1-\phi)`

          .. dropdown:: Solution ``interpol_rho``
             :icon: comment

              .. code-block:: ruby
                :emphasize-lines: 1-3
                
                KOKKOS_INLINE_FUNCTION real_t interpol_rho (real_t phi) const {
                  return rho1*phi + rho2*(1.0 - phi);
                }

         - Add a new function ``force_P`` for pressure force :math:`\boldsymbol{F}_p=-p_h/\varrho(\phi)\boldsymbol{\nabla}\varrho`

          .. dropdown:: Solution ``force_P``
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 1-20

                // ===============================================================================================================
                // Pressure term for NS. Correction term because of p* formulation inside the eq dist function
                // ===============================================================================================================
                template <int dim>
                KOKKOS_INLINE_FUNCTION RVect<dim> force_P (const LBMState &lbmState) const {
                  RVect<dim> gradrho;
                  gradrho[IX] = lbmState[IDRHODX];
                  gradrho[IY] = lbmState[IDRHODY];
                  if (dim == 3) {
                     gradrho[IZ] = lbmState[IDRHODZ];
                  }
                  const real_t scal = lbmState[IP] / lbmState[ID];
                  RVect<dim> term;
                  term[IX] = -scal * gradrho[IX];
                  term[IY] = -scal * gradrho[IY];
                  if (dim == 3) {
                     term[IZ] = -scal * gradrho[IZ];
                  }
                  return term;
                }

         - Add a new function ``force_G`` for gravity force :math:`\boldsymbol{F}_g=\varrho\boldsymbol{g}`

          .. dropdown:: Solution ``force_G``
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 1-13

                // ===============================================================================================================
                // Body term for NS: gravity
                //
                template <int dim>
                KOKKOS_INLINE_FUNCTION RVect<dim> force_G(const LBMState &lbmState) const {
                  RVect<dim> term;
                  term[IX] = gx * lbmState[ID];
                  term[IY] = gy * lbmState[ID];
                  if (dim == 3) {
                     term[IZ] = gz * lbmState[ID];
                  }
                  return term;
                }
         
         - Add a new function ``force_TS`` for surface tension force :math:`\mu_{\phi}\boldsymbol{\nabla}\phi`

          .. dropdown:: Solution ``force_TS``
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 1-13

                // ===============================================================================================================
                // Surface tension liquid/gas for NS
                //
                template <int dim>
                KOKKOS_INLINE_FUNCTION RVect<dim> force_TS(const LBMState &lbmState) const {
                  const real_t tension = sigma * 1.5 / W * (g_prime(lbmState[IPHI]) - SQR(W) * lbmState[ILAPLAPHI]);
                  RVect<dim> term;
                  term[IX] = tension * lbmState[IDPHIDX];
                  term[IY] = tension * lbmState[IDPHIDY];
                  if (dim == 3) {
                     term[IZ] = tension * lbmState[IDPHIDZ];
                  }
                  return term;
                }

   .. tab-item:: File ``LBMScheme_NSCH.h``

      .. admonition:: Function ``setup_collider`` with BGK

         - From stage 2, the function ``setup_collider`` is currently empty. It must be filled to simulate Navier-Stokes equations.

          .. dropdown:: Solution
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 3-60

                KOKKOS_INLINE_FUNCTION
                void setup_collider(EquationTag2 tag, const IVect<dim> &IJK, BGK_Collider &collider) const {
                  // Paramètres pour la simulation
                  const real_t dx = Model.dx;
                  const real_t dt = Model.dt;
                  const real_t c = dx / dt;
                  const real_t cs2 = SQR(c) / Model.e2;
                  // Stockage des anciennes grandeurs macroscopiques
                  LBMState lbmState;
                  Base::template setupLBMState2<LBMState, COMPONENT_SIZE>(IJK, lbmState);
                
                  // Calcul du tau de collision
                  collider.tau = Model.tau_NS(lbmState);
                
                  // Equilibrium without force term
                  FState GAMMA;
                  if (dim == 2) {
                     real_t scalUU = SQR(lbmState[IU]) + SQR(lbmState[IV]);
                     for (int ipop = 0; ipop < npop; ++ipop) {
                        real_t scalUC = c * Base::compute_scal(ipop, lbmState[IU], lbmState[IV]);
                        GAMMA[ipop] = scalUC / cs2 + 0.5 * SQR(scalUC) / SQR(cs2) - 0.5 * scalUU / cs2;
                        real_t feqbar = w[ipop] * (lbmState[IP] / (cs2 * lbmState[ID]) + GAMMA[ipop]);
                        collider.feq[ipop] = feqbar;
                        collider.f[ipop] = Base::get_f_val(tag, IJK, ipop);
                     }
                
                     // Computation of force terms defined in models
                     RVect<dim> ForceTS = Model.force_TS<dim>(lbmState);
                     RVect<dim> ForceG = Model.force_G<dim>(lbmState);
                     RVect<dim> ForceP = Model.force_P<dim>(lbmState);
                
                     // Computation of viscous force
                     RVect<dim> ForceV;
                     const real_t nu = Model.nu0 * Model.nu1 / (((1.0 - lbmState[IPHI]) * Model.nu1) + ((lbmState[IPHI]) * Model.nu0));
                     real_t coeffV = - nu / (cs2 * dt * collider.tau);
                     ForceV[IX] = 0.0;
                     ForceV[IY] = 0.0;
                     for (int alpha = 0; alpha < npop; ++alpha) {
                        ForceV[IX] += E[alpha][IX] * E[alpha][IX] * lbmState[IDRHODX] * (collider.f[alpha] - collider.feq[alpha]) +
                                      E[alpha][IX] * E[alpha][IY] * lbmState[IDRHODY] * (collider.f[alpha] - collider.feq[alpha]);
                        ForceV[IY] += E[alpha][IY] * E[alpha][IX] * lbmState[IDRHODX] * (collider.f[alpha] - collider.feq[alpha]) +
                                      E[alpha][IY] * E[alpha][IY] * lbmState[IDRHODY] * (collider.f[alpha] - collider.feq[alpha]);
                     }
                     ForceV[IX] = coeffV * ForceV[IX];
                     ForceV[IY] = coeffV * ForceV[IY];
                
                     // Calcul et enregistrement du terme source total
                     RVect<dim> ForceTot;
                     ForceTot[IX] = ForceG[IX] + ForceP[IX] + ForceTS[IX] + ForceV[IX];
                     ForceTot[IY] = ForceG[IY] + ForceP[IY] + ForceTS[IY] + ForceV[IY];
                
                     this->set_lbm_val(IJK, IFX, ForceTot[IX]);
                     this->set_lbm_val(IJK, IFY, ForceTot[IY]);
                
                     // Add force term in equilibrium
                     for (int ipop = 0; ipop < npop; ++ipop) {
                        collider.S0[ipop] = dx * w[ipop] / (lbmState[ID] * cs2) * Base::compute_scal(ipop, ForceTot[IX], ForceTot[IY]);
                        collider.feq[ipop] = collider.feq[ipop] - 0.5 * (collider.S0[ipop]);
                     }
                  }
                } // end of setup_collider for composition equation


      .. admonition:: Function ``update_macro``

         - Update necessary fields

          .. dropdown:: Solution
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 1-25
                
                real_t moment_phi = 0.0;
                real_t moment_P   = 0.0;
                real_t moment_VX  = 0.0;
                real_t moment_VY  = 0.0;
                for (int ipop = 0; ipop < npop; ++ipop) {
                  moment_phi += Base::get_f_val(tagPHI, IJK, ipop);
                  moment_P   += Base::get_f_val(tagNS, IJK, ipop);
                  moment_VX  += Base::get_f_val(tagNS, IJK, ipop) * E[ipop][IX];
                  moment_VY  += Base::get_f_val(tagNS, IJK, ipop) * E[ipop][IY];
                }
                // Update phi
                const real_t phi  = moment_phi

                // Update mu
                const real_t mu = Model.M2(tagC, lbmStatePrev);

                // Update pressure p_h
                const real_t rho = Model.interpol_rho(phi) ;
                const real_t P   = moment_P * (rho*cs2) ;

                // Update VX and VY
                const real_t ForceNSX = lbmStatePrev[IFX];
                const real_t ForceNSY = lbmStatePrev[IFY];
                real_t VX = moment_VX + 0.5 * dt * ForceNSX / rho;
                real_t VY = moment_VY + 0.5 * dt * ForceNSY / rho;

         - Save in appropriate arrays

          .. dropdown:: Solution
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 1-6

                this->set_lbm_val(IJK, IPHI , phi);
                this->set_lbm_val(IJK, ID   , rho);
                this->set_lbm_val(IJK, IP   , P  );
                this->set_lbm_val(IJK, IU   , VX );
                this->set_lbm_val(IJK, IV   , VY );
                this->set_lbm_val(IJK, IMU  , mu );


      .. admonition:: Function ``update_macro_grad``

         Currently the function contains the laplacian computation for chemical potential.
         
          .. code-block:: ruby

             .. code-block:: ruby
                :emphasize-lines: 3,4
                
                KOKKOS_INLINE_FUNCTION
                void update_macro_grad(IVect<dim> IJK) const {
                  real_t laplace_c = Base::compute_laplacian(IJK, IC, BOUNDARY_EQUATION_1);
                  Base::set_lbm_val(IJK, ILAPLAC, laplace_c);
                }
         
         - Add computation of gradients

          .. dropdown:: Solution
             :icon: comment

             .. code-block:: ruby
                :emphasize-lines: 6-16

                KOKKOS_INLINE_FUNCTION
                void update_macro_grad(IVect<dim> IJK) const {
		            real_t laplace_c = Base::compute_laplacian(IJK, IC, BOUNDARY_EQUATION_1);
		            Base::set_lbm_val(IJK, ILAPLAC, laplace_c);

                  RVect<dim> gradPhi;
                  this->compute_gradient(gradPhi, IJK, IPHI, BOUNDARY_EQUATION_1);
                  this->set_lbm_val(IJK, IDPHIDX, gradPhi[IX]);
                  this->set_lbm_val(IJK, IDPHIDY, gradPhi[IY]);
                  if (dim == 3) this->set_lbm_val(IJK, IDPHIDZ, gradPhi[IZ]);

                  RVect<dim> gradRho;
                  this->compute_gradient(gradRho, IJK, ID, BOUNDARY_EQUATION_2);
                  this->set_lbm_val(IJK, IDRHODX, gradRho[IX]);
                  this->set_lbm_val(IJK, IDRHODY, gradRho[IY]);
                  if (dim == 3) this->set_lbm_val(IJK, IDRHODZ, gradRho[IZ]);
                }



4. Verification of your implementation
--------------------------------------

.. sectionauthor:: Alain Cartalade
