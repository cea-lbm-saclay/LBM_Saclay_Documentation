.. _Tuto_Force-Term:

Write a new force in Navier-Stokes solver
-----------------------------------------

We give the main stages to add a new force in the Navier-Stokes solver. You must modify three files: ``LBMScheme_NS_AC_Comp.h``, ``Index_NS_AC_Comp.h``, ``Models_NS_AC_Comp.h``

.. tab-set::

   .. tab-item:: File ``LBMScheme_NS_AC_Comp.h``

      Declare the force with ``RVect<dim> ForceMA ;``

         .. code-block:: ruby

            RVect<dim> ForceMA ;
	         if (Model.Marangoni == 1) {	
		      ForceMA      = Model.force_MA<dim>(lbmState);
	         } 
	         else if(Model.Marangoni == 0) {	
		         ForceMA[IX] = 0.0 ;
		         ForceMA[IY] = 0.0 ;
	         }

      where ``Marangoni`` is an integer which is read in the input file and defined in Model. Next each component of that new force is added in the total force ``ForceTot``

         .. code-block:: ruby

            ForceTot[IX] = (1.0 - psi)*(ForceG[IX]+ForceP[IX]+ForceTS[IX]+ForceV[IX]+ForceMA[IX]) + ForcePsolid[IX] + ForcePenal[IX];
	         ForceTot[IY] = (1.0 - psi)*(ForceG[IY]+ForceP[IY]+ForceTS[IY]+ForceV[IY]+ForceMA[IY]) + ForcePsolid[IY] + ForcePenal[IY];

      Those components can be saved for visualization with paraview

         .. code-block:: ruby

            this->set_lbm_val(IJK, IFMARAX, ForceMA[IX]);
            this->set_lbm_val(IJK, IFMARAY, ForceMA[IY]);

      where

         - ``IJK`` is the current node
         - ``IFMARAX`` and ``IFMARAY`` are indices
         - ``ForceMA[IX]`` and ``ForceMA[IY]`` are the values of each component of the Marangoni force.

   .. tab-item:: File ``Index_NS_AC_Comp.h``

      Those indices must be declared in the enumeration of file ``Index_NS_AC_Comp.h``:

         .. code-block:: ruby

            enum ComponentIndex {
            ...
               IFMARAX, /*!< Force Marangoni X */
               IFMARAY,	/*!< Force Marangoni Y */
               ...
            }

   .. tab-item:: File ``Models_NS_AC_Comp.h``

      1. Read and declare parameters of Marangoni and surfactant

         Read the parameters in the input file

            .. code-block:: ruby

               // Read parameters for Marangoni force
               Marangoni       = configMap.getInteger("params_marangoni", "marangoni_force", 0  );
	            Closure_Model   = configMap.getInteger("params_marangoni", "Closure_model"  , 0  ); //1 for logarithm, 0 for linear, default linear
	            //param for linear law
               sigma_marangoni = configMap.getFloat  ("params_marangoni", "sigma_marangoni", 0.0);
               dsigmadcomp     = configMap.getFloat  ("params_marangoni", "dsigmadcomp"    , 0.0);
	            //param for log law
               beta_log        = configMap.getFloat  ("params_marangoni","beta_log"        , 0.0);
               C_infinity      = configMap.getFloat  ("params_marangoni","C_infinity"      , 1.0); //maximum concentration

         Declare the variables

            .. code-block:: ruby

               //! Input parameters for surfactant dynamics
               real_t beta_surf,k_surf,eps_surf;
               //! Input Parameters for Marangoni force
               int Marangoni,Closure_Model;
               real_t sigma_marangoni, dsigmadcomp, beta_log, C_infinity;

      2. Define function ``force_MA<dim>(lbmState);``

         .. code-block:: ruby

            template <int dim>
            KOKKOS_INLINE_FUNCTION RVect<dim> force_MA(const LBMState &lbmState) const {
	
	         //according to Hanyang Mo et al. (2023) 
	
	         if (dim == 2) {
		         const real_t grad_phi_sqr = (SQR(lbmState[IDPHIDX])+SQR(lbmState[IDPHIDY])); //grad phi squared
		         const real_t grad_sigmax = sigma_prime(lbmState[IC])*lbmState[IDCDX]; //d(sigma)/dx = d(sigma)/dC * d(C)/dx
		         const real_t grad_sigmay = sigma_prime(lbmState[IC])*lbmState[IDCDY]; //d(sigma)/dy = d(sigma)/dC * d(C)/dy
    
		         const real_t dot_prod = lbmState[IDPHIDX]*grad_sigmax + lbmState[IDPHIDY]*grad_sigmay ;// grad sigma . grad phi 
    
		         RVect<dim> term;
		         term[IX] = 1.5*W*(grad_phi_sqr*grad_sigmax - dot_prod*lbmState[IDPHIDX]);
		         term[IY] = 1.5*W*(grad_phi_sqr*grad_sigmay - dot_prod*lbmState[IDPHIDY]);
		
		         return term;
	            }
            }

      3. Define :math:`d\sigma/dc`

         .. code-block:: ruby

            KOKKOS_INLINE_FUNCTION real_t sigma_func(real_t comp ) const {
	         if(Closure_Model == 1){
			      return sigma_marangoni*(1+beta_log*log(1.0-comp/C_infinity));
		      }
	  
	         else{
			      return sigma_marangoni + comp*dsigmadcomp;
		      }
            }

         .. code-block:: ruby

            KOKKOS_INLINE_FUNCTION real_t sigma_prime(real_t comp) const {
            if(Closure_Model == 1){
			      return -sigma_marangoni*beta_log/(C_infinity-comp);
		      }
            else{
		         return dsigmadcomp;
		      }
            }

.. sectionauthor:: Alain Cartalade
   