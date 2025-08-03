.. |br| raw:: html

   <br />

.. _Law-Similarity:

Law of similarity: application on Poiseuille flow
=================================================

To start practicing with input parameters without physical dimension, we recommmend to run the classical test case of Poiseuille flow which is contained in folder ``run_training_lbm``. The law of similarity is applied to derive dimensionless parameters from physical parameters in SI units. In the case of Poiseuille flow, Reynolds number is used to derive dimensionless parameters.

The analytical solution of Poiseuille flow is

.. math::
   :label: Poiseuille

   u_{x}(y)=u_{max}\left(1-\frac{4y^{2}}{L^{2}}\right)

where :math:`u_{max}=gL^{2}/8\nu`. If we consider water properties inside a channel of width :math:`L`

.. container:: sphinx-features

   +---------------------+--------------------+------------------------------+----------------+
   | **Parameter**       | **Math symbol**    | **Value**                    | **Dimension**  |
   +=====================+====================+==============================+================+
   | Gravity             | :math:`g`          | :math:`9.81\cong10`          | m/s2           |
   +---------------------+--------------------+------------------------------+----------------+
   | Density             | :math:`\rho_w`     | :math:`998.29\cong1000`      | kg/m3          |
   +---------------------+--------------------+------------------------------+----------------+
   | Kinematic viscosity | :math:`\nu`        | :math:`10^{-6}`              | m2/s           |
   +---------------------+--------------------+------------------------------+----------------+
   | Width               | :math:`L`          | :math:`10^{-3}`              | m              |
   +---------------------+--------------------+------------------------------+----------------+

it is possible to compute the maximum velocity :math:`u_{max}`

.. math::
   :label: u_max_poiseuille

   u_{max}=\frac{gL^{2}}{8\nu}=1.25\text{ m.s}^{-1}

and the Reynolds number Re:

.. math::
   :label: Re_mas_poiseuille

   \text{Re}=\frac{u_{max}L}{\nu}=1250

.. figure:: ../../FIGS/01_FIGS_VALIDATIONS/Poiseuille.png
      :name: Analy-Poiseuille
      :figclass: align-center
      :align: center
      :height: 400
      :width: 500
      :scale: 80 %
      
      Poiseuille flow inside a channel

In what follows, we present four different ways to set one characteristic length and one characteristic time to derive all dimensionless parameters.

First choice of parameters: :math:`\delta x_1` and :math:`\tau`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If we set (initial guess) :math:`\delta x_1=5 \times 10^{-5}` m and :math:`\tau=0.6`, then we derive the other parameters

.. math::

   L_{1}^{\star}=\frac{L}{\delta x_{1}}=20

where :math:`L_1^{\star}` is the dimensionless width of domain, obtained from the space-step :math:`\delta x_1`. It is equivalent to the total number of nodes :math:`N_y`.

The kinematic viscosity is linked to the collision rate:

.. math::

   \nu_{1}^{\star}=\frac{1}{3}(\tau-0.5)=0.03333

We can derive the time step:

.. math::

   \delta t=\frac{1}{3}(\tau-0.5)\frac{\delta x_{1}^{2}}{\nu}=8.33\times10^{-5}

.. admonition:: Unstable simulation
   :class: warning

   For a given Re number :math:`\text{Re}=u_{max}^{\star}L^{\star}/\nu^{\star}=1250`, the maximum dimensionless velocity is:

   .. math::

      u_{max}^{\star}=\frac{\nu^{\star}\text{Re}}{L^{\star}}=2.08

   That value is greater than :math:`\color{red}{u_{max}^{\star}}{\color{red}{\gg0.4}}` so that the simulation will be unstable.

Second choice of parameters: :math:`L^{\star}` and :math:`\nu^{\star}`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From the previous set of parameters, one solution to keep the simulation stable is to set :math:`L^{\star}` and :math:`\nu^{\star}` such that :math:`u_{max}^{\star}/10=0.208`. To achieve that, for a given Reynolds number, it is sufficient to multiply by five the dimensionless width :math:`L_{1}^{\star}\times5` and divide by two the kinematic viscosity :math:`\nu_{1}^{\star}/2`.

- :math:`L^{\star}=L_{1}^{\star}\times5=100`, means that the number of nodes is :math:`N_y=100`. We can derive the space-step by:

   .. math::
      :label: dx_Poiseuille

      \delta x=\frac{L}{L^{\star}}=10^{-5}

- The target value of dimensionless kinematic viscosity is

   .. math::
      :label: nu_Poiseuille

      \nu^{\star}=\frac{\nu_1^{\star}}{2}=0.016667
   
 We can derive the collision rate which is linked to kinematic viscosity by :math:`\tau^{\star}=3\nu^{\star}+0.5=0.55`.

- We can derive the time step, for example here with the kinematic viscosity:

   .. math::
      :label: dt_Poiseuille

      \delta t=\frac{1}{3}(\tau-0.5)\frac{\delta x^{2}}{\nu}=1.6667\times10^{-6}

- Finally, the dimensionless gravity :math:`g^{\star}` is obtained from the physical value of gravity and the factor of conversion :math:`C_g=\delta x/\delta t^2` (see Eq. :eq:`C_U_nu_g_p`):

   .. math::
      :label: Gravity_Poiseuille

      g^{\star}=g\frac{\delta t^{2}}{\delta x}=2.777\times10^{-6}

 The simulation is accurate because :math:`u_{max}^{\star}<0.3` and stable because :math:`u_{max}^{\star}<0.4`.

.. admonition:: Parameters of input file
   :class: hint

   For test case ``TestCase02_Poiseuille_Water`` of folder ``run_training_lbm``, those values are set in the ``.ini`` input file. The main parameters are presented below:

   .. container:: sphinx-features

      .. code-block:: ruby

         [run]
         dt=1

         [mesh]
         ny=100
         ymin=-50
         ymax=50

         [params]
         rho0=1
         rho1=1
         nu0=0.01666666666666668
         nu1=0.01666666666666668
         gx=2.777777777777784e-06

      - ``dt=1`` means that :math:`\delta t^{\star}=1`
      - The number of nodes :math:`N_y` in :math:`y`-direction is ``ny=100``
      - The width of domain (:math:`L^{\star}`) is ``ymax-ymin=100`` meaning that :math:`\delta x^{\star}=L^{\star}/N_y=1`
      - The value of kinematic viscosities ``nu0`` and ``nu1`` are given by Eq. :eq:`nu_Poiseuille`
      - The dimensionless gravity is given by Eq. :eq:`Gravity_Poiseuille`
      
         Once the simulation is complete, use :math:`\delta x` defined by Eq. :eq:`dx_Poiseuille`, :math:`\delta t` defined by |Br|
         Eq. :eq:`dt_Poiseuille`, and the density to calculate the conversion factors Eqs. :eq:`C_U_nu_g_p`. |Br|
         Use those conversion factors to obtain the results with physical dimensions. |Br|
         A python script ``Post-Pro_Poiseuille_Water_CompareAnaly.py`` is available  |Br|
         in the folder to compare numerical and analytical solutions.

.. admonition:: For LBM training session
   :class: error

   Those stages are written in a python script:

    .. code-block:: shell
       
        $ cd TestCase02_Poiseuille_Water
        $ python Pre-Pro_Poiseuille.py

.. admonition:: For training session
   :class: error

    .. code-block:: shell
       
        $ gedit TestCase02_Poiseuille_Water&

   Check that the numerical parameters of your input file correspond to the output of python script.


The methodology is described in the jupyter notebook ``Validation-Sheet_Poiseuille_Similarity_Water.ipynb``. The input parameters of ``TestCase02_Poiseuille_Water.ini`` are dimensionless.

.. code-block:: shell
   
   $ cd run_training_lbm/TestCase02_Poiseuille_Water
   $ jupyter notebook Validation-Sheet_Poiseuille_Similarity_Water.ipynb

Third choice of parameters: :math:`u_{max}^{\star}` and :math:`\tau`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As unit of length and time, it is also possible to set :math:`u_{max}^{\star}=0.1<0.4` and :math:`\tau=0.8>052`. The simulation will be stable and accurate. In order to derive the other parameters, we use the first one to calculate de conversion factor of velocity:

.. math::

   C_{u}=\frac{u_{max}}{u_{max}^{\star}}=12.5=\frac{\delta x}{\delta t}

Newt we use the relaxation rate for deriving the dimensionless kinematic viscosity:

.. math::

   \nu^{\star}=\frac{1}{3}(\tau-0.5)=0.1

and the conversion factor of :math:`\nu`:

.. math::

   C_{\nu}=\frac{\nu}{\nu^{\star}}=10^{-5}=\frac{\delta x^{2}}{\delta t}

The dimensionless width (or number of nodes) is derived from the Reynolds number 

.. math::

   L^{\star}=\frac{\text{Re}\nu^{\star}}{u_{max}^{\star}}=1250

.. admonition:: Remark
   :class: warning

   That set of initial parameters requires a discretization with 1250 nodes. The simulation won't be efficient.

The ratio between both conversion factors allows deriving the space-step

.. math::

   \delta x=\frac{C_{\nu}}{C_{u}}=8\times10^{-7}\quad{\color{gray}(\text{check }=L/L^{\star})}

Finally, :math:`\delta t` can be obtained

.. math::

   \delta t=\frac{\delta x}{C_{u}}=6.4\times10^{-8}\quad{\color{gray}(\text{check }\nu=\nu^{\star}\delta x^{2}/\delta t)}

as well as :math:`g^{\star}`:

.. math::

   g^{\star}=g\frac{\delta t^{2}}{\delta x}=5.12\times10^{-8}

Fourth choice of parameters: :math:`u_{max}^{\star}` and :math:`L^{\star}`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Another choice of parameters is possible. Set for instance :math:`L^{\star}=5\times 10^{2}` and :math:`u_{max}^{\star}=0.1<0.4`. In that case, we can derive the missing parameters as follows:

.. math::

   \delta x=\frac{L}{L^{\star}}=2\times10^{-6}

.. math::

   C_{u}=\frac{u_{max}}{u_{max}^{\star}}=12.5=\frac{\delta x}{\delta t}

.. math::

   \delta t=\frac{\delta x}{C_{u}}=1.6\times10^{-7}

.. math::

   \nu^{\star}=\frac{u_{max}^{\star}L^{\star}}{\text{Re}}=0.04\quad{\color{gray}(\text{check }\nu=\nu^{\star}\delta x^{2}/\delta t)}

.. math::

   \tau=3\nu^{\star}+0.5=0.62\;({\color{red}>0.55})

.. math::

   g^{\star}=g\frac{\delta t^{2}}{\delta x}=1.28\times10^{-7}

Conclusion
----------

.. admonition:: Conclusion
   :class: hint

   On that simple Poiseuille flow, we see that several ways are possible to set two initial parameters and derive all others. For other configurations and types of flows, those choices depend on the system and phenomenology to be simulated. The example was given here for a single-phase flow. For two-phase flows, one example is detailed in :ref:`Similarity-Two-Phases`. To help users to set dimensionless parameters, several python scripts are available in the test cases of ``run_training_lbm``. A description of one of them is done in :ref:`Similarity-Two-Phases`.
