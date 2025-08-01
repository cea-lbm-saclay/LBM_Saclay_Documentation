.. _Similarity-Two-Phases:

Law of similarity: practice on Rayleigh-Taylor instability
-----------------------------------------

The Rayleigh-Taylor test case can be found in folder

.. admonition:: For training session
   :class: error
   
    .. code-block:: shell

       $ cd run_training_lbm/TestCase08_Rayleigh-Taylor2D

For that test case, we set :math:`\rho_h^{\star}=3` (heavy fluid), :math:`\rho_l^{\star}=3` (light fluid), the domain width :math:`L^{\star}=128`, :math:`\delta x^{\star}=1` and :math:`\delta t^{\star}=1`. 

.. admonition:: For training session
   :class: error

   The file ``Pre-Pro_InputParam_Rayleigh-Taylor.py`` is a python script that derives all dimensionless parameters. The command

    .. code-block:: shell

       $ python Pre-Pro_InputParam_Rayleigh-Taylor.py

returns

.. code-block:: ruby

   ###############################################################################
   ###############################################################################
   ###                      NUMERICAL VALUES FOR LBM_Saclay                    ###
   ###                        TEST CASE: RAYLEIGH-TAYLOR                       ###
   ###############################################################################
   ###############################################################################
 
   # INPUT PARAMETERS (ADIM)
   rhoH =  3
   rhoL =  1
   At   =  0.5
   L    =  128
   Nx   =  128

The characteristic numbers are :math:`\text{Re}=3000`,  :math:`\text{Pe}=1000`,  :math:`\text{Ca}=0.26` and one chacteristic time of instability :math:`t_c^{\star}=16000`.

.. code-block:: ruby

   # TARGET ADIM NB
   Re =  3000
   Pe =  1000
   Ca =  0.26
   # CHARACTERISTIC TIME OF SIMULATION
   Tcar =  16000

We derive successively

- Atwood number:

.. math::
   :label: Atwood-Nb

   \text{At}=\frac{\rho_h^{\star}-\rho_l^{\star}}{\rho_h^{\star}+\rho_l^{\star}}=0.5

- gravity

.. math::
   :label: g_RT2D

   g^{\star}=\frac{L}{t_c^{\star}\times \text{At}}=10^{-6}

- kinematic viscosity

.. math::
   :label: nu_RT2D

   \nu^{\star}=\frac{L^{\star}\sqrt{g^{\star}L^{\star}}}{\text{Re}}

- Surface tension

.. math::
   :label: sigma_RT2D

   \sigma^{\star}=\frac{\rho_h \nu^{\star} \sqrt{g^{\star}L^{\star}}}{\text{Ca}}

- Mobility of interface

.. math::
   :label: Mobility_Interface

   M_{\phi}=\frac{L^{\star}\sqrt{g^{\star}L^{\star}}}{\text{Pe}}

.. code-block:: ruby

   # DERIVATION OF INPUT PARAMETERS
   g     =  1e-06 (derived from L, Tcar and At)
   M     =  0.0014481546878700492 (derived from Pe)
   nu    =  0.0004827182292900164 (derived from Re)
   sigma =  6.30153846153846e-05 (derived from Ca)
   lc    =  5.613171323564987 Capillary length
   W     =  4.0
 
   ###############################################################################
   ###############################################################################
   ###########################        END         ################################
   ###############################################################################
   ###############################################################################

Those output values are set in the ``.ini`` file for LBM_Saclay. For example, we see inside file ``TestCase08_Rayleigh-Taylor_Spike-Bubble.ini``, first in section ``[mesh]``

.. code-block:: ruby

   [mesh]
   nx=128
   ny=512
   xmin=-64
   xmax=64

Second in section ``[params]``

.. code-block:: ruby

   [params]
   W=4
   Mphi=0.0014481546878700492
   counter_term=1.0
   rho0=1.0
   rho1=3.0
   nu0=0.0004827182292900164
   nu1=0.0004827182292900164
   PF_advec=1.0
   gy=-1e-06
   sigma=6.30153846153846e-05

Practice on rising bubble
^^^^^^^^^^^^^^^^^^^^^^^^^
One example of using dimensionless numbers is presented in the folder ``TestCase11_Rising-Bubble2D`` of directory ``run_training_lbm``. 

.. code-block:: shell

   $ cd LBM_Saclay/run_training_lbm/TestCase11_Rising-Bubble2D

In that folder the file ``Pre-Pro_InputParam_Rising-Bubble_Water-Air.py`` is a python script which derives dimensionless parameters for two-phase flows. The physical properties are those of water and air (see table :ref:`Tab-Water-Air`). That script can be executed with the command

.. code-block:: shell

   $ python Pre-Pro_InputParam_Rising-Bubble_Water-Air.py

For pedagogical reasons, the result of that command is separated here into several parts for adding comments. In the first part, the values of parameters are reminded in SI units

.. code-block:: ruby

   ###############################################################################
   ###############################################################################
   ###                      NUMERICAL VALUES FOR LBM_Saclay                    ###
   ###                    TEST CASE: RISING BUBBLE (Water-Air)                 ###
   ###############################################################################
   ###############################################################################
 
   #############################################
   #           1. INPUT PARAMETERS             #
   #############################################
 
   # PHYSICAL PROPERTIES (SI)
   Density   water        :   rho_l =  998.29 kg/m3
   Viscosity water        :   nu_l  =  1.0034e-06 m2/s
   Density   air          :   rho_a =  1.204 kg/m3
   Viscosity air          :   nu_a  =  1.56e-05 m2/s
   Surface tension        :   sigma =  0.0728 N/m
   Gravity                :   g     =  9.81 m/s2

With those values, the density ratio :math:`\rho_l/\rho_a`, the viscosity ratio :math:`\nu_l/\nu_a`, the density difference  :math:`\rho_l-\rho_a`, the dynamic viscosities  :math:`\eta_l`, :math:`\eta_a` and its ratio :math:`\eta_l/\eta_a` can be calculated:

.. code-block:: ruby

   # DERIVED PROPERTIES
   Density   ratio        :   rho_l/rho_a     =  829.1445182724252
   Viscosity ratio        :   nu_l / nu_a     =  0.06432051282051282  = 1/ 15.54713972493522
   DeltaRho               :   rho_l-rho_a     =  997.086
   Dynamic viscosity water:   Visc_Dyn_l      =  0.001001684186
   Dynamic viscosity air  :   Visc_Dyn_a      =  1.8782399999999998e-05
   Dynamic viscosity ratio:   Visc_l / Visc_a =  53.33100061759946

For Poiseuille flow, the characteristic length was the domain width :math:`L`. Here, it is the diameter :math:`D` of the bubble and its value is supposed to be equal to ``D=2mm``. The characteristic velocity ``Uref`` is derived:

.. code-block:: ruby

   # HYPOTHESES FOR RISING BUBBLE (ADAPT FOR OTHER TEST CASE)
   Hypothesis: Uref=sqrt(g*D) where g=9.81m/s2 and D the droplet diameter
   For D =  0.002 m then:
   Uref  = sqrt(gD)                   =  0.14007141035914503 m/s

Finally, the numbers of Reynolds (``Re``), Bond (``Bo``) and Morton (``Mo``) can be computed:

.. code-block:: ruby

   # COMPUTATION OF REYNOLDS, BOND, AND MORTON NUMBERS
   Re    = Uref*D/nu_l                              =  279.1935626054316
   Bo    = g*DeltaRho * D**2  / sigma               =  0.537440310989011
   Mo    = g*DeltaRho * eta^4 / (rho_l^2 * sigma^3) =  2.5610456286997475e-11

In that first part, all values have physical units. In the second part, we derive the dimensionless parameters by setting one length of reference (here the radius :math:`R^{\star}`), one parameter for time (here the collision rate :math:`\tau_l^{\star}`) and the reference density is the water density :math:`\rho_{ref}=\rho_l`:

.. code-block:: ruby

   ###############################################################################
   ###############################################################################
 
   #############################################
   #           2. ADIM PARAMETERS              #
   #############################################
 
   # We set Rstar, rho_ref, tau_l_star
   # The reference density is rho_l
   Rayon adim             : Rstar      =  37.5
   Collision rate of water: tau_l_star =  0.51

All other dimensionless parameters can be derived by using :math:`R^{\star}`, :math:`\tau_l^{\star}`, :math:`\rho_l` and the dimensionless numbers (Re, Bo Mo). See the order to derive the parameters and the relationships inside the python script.

The first dimensionless parameters are :math:`\rho_l^{\star}=1`, :math:`\rho_a^{\star}=\rho_a/\rho_l` and :math:`\Delta \rho^{\star}` is straightforward. Next, the space step is :math:`\delta x= R/R^{\star}`, and the length :math:`L^{\star}=L/\delta x`. As :math:`\tau_l^{\star}` is set, we can compute :math:`nu_l^{\star}` by:

.. math::

   \nu_l^{\star}=\frac{1}{3}(\tau_l^{\star}-0.5)

The (dimensionless) surface tension and gravity are obtained with Bond and Morton numbers. After some algebra, we obtain for surface tension

.. math::

   \sigma^{\star}=\sqrt{\frac{\text{Bo}\rho_l^{\star}\nu_l^{\star4}}{\text{Mo}\Delta \rho^{\star}D^{\star2}\rho_l^{\star}}}

and for gravity

.. math::

   g^{\star}=\frac{\sigma^{\star}\text{Bo}}{\Delta \rho^{\star}D^{\star2}}

The time step is derived with gravity and its factor of conversion :math:`C_g`:

.. math::

   \delta t=\sqrt{g^{\star}\frac{\delta x}{g}}

At last, we can calculate the dimensionless relxation rate of air :math:`\tau_a^{\star}=0.5+3.0\nu_a\delta t/\delta x^2`, and its dimensionless kinematic viscosity :math:`\nu_a^{\star}=(1/3)(\tau_a^{\star}-0.5)`. Finally the dimensionless parameters are

We give here only the results:

.. code-block:: ruby

   # DERIVED DIMENSIONLESS VALUES
   dx            = 2.6666666666666667e-05
   Lstar         = 400.0
   rho_l_star    = 1.0
   rho_a_star    = 0.0012060623666469664
   DeltaRho_star = 0.998793937633353
   nu_l_star     = 0.003333333333333336 (derived from tau_l_star)
   Sigma_star    = 0.021474088528285768 (derived from Bo & Mo)
   gstar         = 2.0542181048108674e-06 (derived with Bo & Sigma_star)
   dt            = 2.3630512390059374e-06
   tau_a_star    = 0.6555183096670782
   Uref_star     = 0.012412346992443252

Once all dimensionless parameters are derived, we can check that the procedure and the values are correct by using the ':math:`\star`' values and the appropriate factors of conversion (see :ref:`Law-Similarity`)

.. code-block:: ruby

   ###############################################################################
   ###############################################################################
 
   #############################################
   #           3. VERIFICATION                 #
   #############################################
 
   # VERIFICATIONS OF DIMENSIONLESS VALUES WITH 'star', dx, dt et rho_ref
 
   Use of
   dx      =  2.6666666666666667e-05
   dt      =  2.3630512390059374e-06
   rho_ref =  998.29
 
   SIMILARITY OF DIMENSIONLESS PARAMETERS
   L_verif     (m)     = Lstar * dx                         = 0.010666666666666666
   g_verif     (m/s2)  = gstar * dx / dt2                   = 9.809999999999999
   R_verif     (m)     = Rstar * dx                         = 0.001
   rho_l_verif (kg/m3) = rho_l_star * rho_ref               = 998.29
   rho_a_verif (kg/m3) = rho_a_star * rho_ref               = 1.204
   nu_l_verif  (m2/s)  = nu_l_star  * dx2 / dt              = 1.0030973223278534e-06
   nu_a_verif  (m2/s)  = nu_a_star  * dx2 / dt              = 1.56e-05
   Sigma_verif (N/m)   = Sigma_star * rho_ref * dx3 / (dt2) = 0.07279999999999999
   Uref_verif  (m/s)   = Uref_star  * dx / dt               = 0.14007141035914503

Finally, a summary is given of values to use in LBM_Saclay input file.

.. code-block:: ruby

   ###############################################################################
   ###############################################################################
   # EXAMPLE OF INPUT VALUES FOR LBM_Saclay
   [run]
   dt    = 1.0
   [mesh]
   nx    = 400
   ny    = 800
   xmin  = 0.0
   xmax  = 400.0
   ymin  = 0.0
   ymax  = 800.0
   [params]
   rho0  = 0.0012060623666469664
   rho1  = 1.0
   nu0   = 0.051839436555692744
   nu1   = 0.003333333333333336
   gy    = -2.0542181048108674e-06
   sigma = 0.021474088528285768
   [init]
   rayon = 37.5
 
   ###############################################################################
   ###############################################################################
   ###########################        END         ################################
   ###############################################################################
   ###############################################################################
