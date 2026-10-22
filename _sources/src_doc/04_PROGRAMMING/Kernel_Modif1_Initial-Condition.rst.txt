.. _Tuto_Initial-Conditions:

Write a new initial condition inside a kernel
---------------------------------------------

The purpose is to implement one initial condition for the phase-field :math:`\phi` such as it represents a circular (2D) or spherical (3D) bubble at the beginning of the simulation. We need to implement the following equation:

.. math::
   :label: Init_sphere

   \phi(\boldsymbol{x},0)=\frac{1}{2}\left[1+\tanh\left(\frac{2(r_0-d_{0})}{W}\right)\right]

where :math:`r_0` is bubble radius and the distance :math:`d_0` is defined by

.. math::
   :label: dist

   d_{0}=\sqrt{(x-x_{0})^{2}+(y-y_{0})^{2}+(z-z_{0})^{2}}

where :math:`\boldsymbol{x}_0=(x_0,y_0,z_0)` is the center position of the bubble and :math:`\boldsymbol{x}=(x,y,z)` is one particular node on the mesh.

Implement your initial condition
""""""""""""""""""""""""""""""""

You must modify three files which are in the folder: ``Models_NS_AC_Comp.h``, ``LBMScheme_NS_AC_Comp.h`` and ``LBM_enums.h``.

.. tab-set::

   .. tab-item:: File ``Models_NS_AC_Comp.h``

      Edit the file with command:

         .. code-block:: shell

            $ cd LBM_Saclay_Rech-Dev/src/kernels/NSAC_Comp
            $ geany Models_NS_AC_Comp.h

      1. Read the input parameters

         In this file, the input parameters :math:`r_0`, :math:`x_0,y_0,z_0` must be read from the ``.ini`` file. Add e.g. between lines 97 and 206

         .. code-block:: ruby

            ModelParams(const ConfigMap &configMap, LBMParams params) {
            ...
            ...
            x0 = configMap.getFloat  ("init", "x0", 0.0);
            y0 = configMap.getFloat  ("init", "y0", 0.0);
            z0 = configMap.getFloat  ("init", "z0", 0.0);
            r0 = configMap.getFloat  ("init", "r0", 0.2);

         The first line means that ``x0`` must be read as a real in section ``[init]``. If the line does not exist in the input file, then its value is ``0``.

      2. Declare them (between lines 309 and 341)

         .. code-block:: ruby

            ModelParams(const ConfigMap &configMap, LBMParams params) {
            ...
            ...

            real_t x0, y0, z0, r0 ;

      3. Add a new keyword for that initial condition (e.g. between lines 234 and 271)

         .. code-block:: ruby

            else if (initTypeStr == "sphere")
               initType = PHASE_FIELD_INIT_SPHERE;

         The keyword ``sphere`` has to appear in the ``.ini`` file. The keyword ``PHASE_FIELD_INIT_SPHERE`` must be added in the list of enumerations (see below file ``LBM_enums.h``).

      4. Definition of hyperbolic tangent function (line 349)

         .. code-block:: ruby

            KOKKOS_INLINE_FUNCTION real_t phi0(real_t x) const {
               return 0.5 * (1 + tanh(sign * 2.0 * x / W));
            }

         The function ``phi0`` implements the hyperbolic tangent function. It is defined in class ``Model``.

   .. tab-item:: File ``LBMScheme_NS_AC_Comp.h``

      Eq. :eq:`Init_sphere` is implemented in file ``LBMScheme_NS_AC_Comp.h``:

         .. code-block:: shell

            $ cd LBM_Saclay_Rech-Dev/src/kernels/NSAC_Comp
            $ geany LBMScheme_NS_AC_Comp.h

      1. The initializations of macroscopic fields are performed in the function (line 1024):

         .. code-block:: JSON

            KOKKOS_INLINE_FUNCTION
            void init_macro(IVect<dim> IJK, RANDOM_POOL::generator_type rand_gen) const {
               ...
            }

         In that function, the following lines implement :math:`r_0-d_0` for 2D or 3D cases:

         .. code-block:: ruby

            else if (Model.initType == PHASE_FIELD_INIT_SPHERE) {
	         if (dim == 2) {
	            xphi = (Model.r0 - sqrt(SQR(x - Model.x0) + SQR(y - Model.y0)));
	         }
	         else if (dim == 3) {
	            xphi = (Model.r0 - sqrt(SQR(x - Model.x0) + SQR(y - Model.y0) + SQR(z - Model.z0)));
	         }
	            xc = xphi ;
	         }

      2. Once :math:`r_0-d_0` is defined (``xphi``), the hyperbolic tangent function is applied (line 1420)

         .. code-block:: ruby

            phi = Model.phi0(xphi);

   .. tab-item:: File ``LBM_enums.h``

      Edit file ``LBM_enums.h``

      .. code-block:: shell

         $ cd LBM_Saclay_Rech-Dev/src
         $ geany LBM_enums.h

      1. Add the keyword ``PHASE_FIELD_INIT_SPHERE`` in the list of enumeration (line 111)

         .. code-block:: ruby

            enum PhaseFieldInit {
               ...

               PHASE_FIELD_INIT_SPHERE,

Compile, modify your ``.ini`` file and check
""""""""""""""""""""""""""""""""""""""""""""


.. sectionauthor:: Alain Cartalade
   