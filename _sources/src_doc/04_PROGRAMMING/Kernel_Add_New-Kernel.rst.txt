.. _Tuto_New-Directory:

Copy and rename directory and files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. First copy and rename the directory ``NSAC_Comp`` with the new name ``MPwSLphC``:

   .. code-block:: shell

      $ cd LBM_Saclay_Rech-Dev/src/kernels
      $ cp -r NSAC_Comp MPwSLphC

2. Next, rename four files which are contained inside the new directory:

   .. code-block:: shell

      $ cd MPwSLphC
      $ mv Index_NS_AC_Comp.h Index_MPwSLphC.h
      $ mv LBMScheme_NS_AC_Comp.h LBMScheme_MPwSLphC.h
      $ mv Models_NS_AC_Comp.h Models_MPwSLphC.h
      $ mv Problem_NS_AC_Comp.h Problem_MPwSLphC.h

3. Once it is done, edit file ``Setup.h`` with your favorite text editor (here example with ``geany``):

   .. code-block:: shell

      $ geany Setup.h&

   Modify the names with the new kernel name. Below, the new lines are highlighted after the old ones:

   .. code-block:: ruby
      :emphasize-lines: 3,4,7,11,12,16,20,21,27,31
      :linenos:

      #ifndef SETUP_NSAC_COMP_H_
      #define SETUP_NSAC_COMP_H_
      #ifndef SETUP_MPWSLPHC_H_
      #define SETUP_MPWSLPHC_H_

      #include "Problem_NS_AC_Comp.h"
      #include "Problem_MPwSLphC.h"

      namespace PBM_NS_AC_Compo {
      struct pbm_registerer_NSAC_comp
      namespace PBM_MPwSLphC {
      struct pbm_registerer_MPwSLphC

      {
         pbm_registerer_NSAC_comp()
         pbm_registerer_MPwSLphC()
         {
            register_problem<Problem, ModelParams::TagCompo>("NSAC_Comp", "base");
            register_problem<Problem, ModelParams::TagSansGamma>("NSAC_Comp", "sansGamma");
            register_problem<Problem, ModelParams::TagCompo>("MPwSLphC", "base");
            register_problem<Problem, ModelParams::TagSansGamma>("MPwSLphC", "sansGamma");
         };

      };

      static pbm_registerer_NSAC_comp registerer_NSAC_comp;
      static pbm_registerer_MPwSLphC registerer_MPwSLphC;
      }

      #endif //SETUP_NSAC_COMP_H_
      #endif //SETUP_MPWSLPHC_H_

4. Modification of file ``Problem_MPwSLphC.h``

   .. code-block:: ruby
      :emphasize-lines: 3,4,7,10
      :linenos:

      #ifndef PROBLEM_NS_AC_C_H_
      #define PROBLEM_NS_AC_C_H_
      #ifndef PROBLEM_MPWSLPHC_H_
      #define PROBLEM_MPWSLPHC_H_

      #include "LBMScheme_NS_AC_Comp.h"
      #include "LBMScheme_MPwSLphC.h"

      namespace PBM_NS_AC_Compo {
      namespace PBM_MPwSLphC {

5. Modification file ``Models_MPwSLphC.h``

   .. code-block:: ruby
      :emphasize-lines: 3,4,7,10
      :linenos:

      #ifndef MODELS_NS_AC_C_H_
      #define MODELS_NS_AC_C_H_
      #ifndef MODELS_MPWSLPHC_H_
      #define MODELS_MPWSLPHC_H_

      #include "Index_NS_AC_Comp.h"
      #include "Index_MPwSLphC.h"

      namespace PBM_NS_AC_Compo {
      namespace PBM_MPwSLphC {

6. Modification file ``LBMScheme_MPwSLphC.h``

   .. code-block:: ruby
      :emphasize-lines: 3,4,7,10
      :linenos:

      #ifndef LBMSCHEME_NS_AC_C_H_
      #define LBMSCHEME_NS_AC_C_H_
      #ifndef LBMSCHEME_MPWSLPHC_H_
      #define LBMSCHEME_MPWSLPHC_H_

      #include "Models_NS_AC_Comp.h"
      #include "Models_MPwSLphC.h"

      namespace PBM_NS_AC_Compo {
      namespace PBM_MPwSLphC {


7. Modification file ``Index_MPwSLphC.h``

   .. code-block:: ruby
      :emphasize-lines: 3,4,7
      :linenos:

      #ifndef INDEX_NS_AC_C_H_
      #define INDEX_NS_AC_C_H_
      #ifndef INDEX_MPWSLPHC_H_
      #define INDEX_MPWSLPHC_H_

      namespace PBM_NS_AC_Compo {
      namespace PBM_MPwSLphC {

8. Compilation

   .. code-block:: shell

      $ cmake -DKokkos_ENABLE_OPENMP=ON -DUSE_HDF5=ON -DPROBLEM=MPwSLphC ..
      $ make -j 22

.. sectionauthor:: Alain Cartalade
   