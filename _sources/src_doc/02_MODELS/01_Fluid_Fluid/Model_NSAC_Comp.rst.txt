.. _Math-NSAC-Comp:

Model of Navier-Stokes/Conservative Allen-Cahn (CAC)/Composition
================================================================

Introduction
------------

.. admonition:: Basic model
   :class: warning

   That model is one of the most popular model of two-phase flows with interface-capturing. It is composed of incompressible Navier-Stokes (``NS``) equations coupled with the Conservative Allen-Cahn (``CAC``) equation (or levelset equation). That model is applied for simulating many classical problems such as "rising bubbles", splashing droplets", "Rayleigh-Taylor instability", etc. In LBM_Saclay, that model is implemented in the kernel ``NSAC_Comp`` where ``_Comp`` means Composition equation. The kernel ``NSAC_Comp`` is extensively used for two-phase test cases which are contained in the folder ``run_training_lbm``. The test cases of this folder are used in a training session of LBM with the Training version of LBM_Saclay.

   - :ref:`Run_Training-LBM` with that model can be performed with ``.ini`` input files of folder ``run_training_lbm``.

That model is a basis for other models which are developed in other kernels e.g. two-phase flows with surfactant, two-phase flows with phase change, two-phase flows interacting with a solid phase and three immiscible fluids:

- :ref:`Math-NSAC-Surfactant`
- :ref:`Math-NSAC-PhaseChange`
- :ref:`Math-NSAC-Comp-Solid`
- :ref:`Math-NS2AC-Comp`

Mathematical model of incompressible two-phase flows
----------------------------------------------------

The mathematical model is composed of incompressible Navier-Stokes equations coupled with the phase-field equation and the composition equation.

.. admonition:: Mathematical model
   :class: error

   **Mass balance equation**

   The mass balance writes:

   .. math::
      :label: Mass_Balance_CAC-Model
   
      \boldsymbol{\nabla}\cdot\boldsymbol{u}=0

   where :math:`\boldsymbol{u}\equiv\boldsymbol{u}(\boldsymbol{x},t)=(u_x,u_y,u_z)^T` is the fluid velocity.

   **Impulsion balance equation**

   The impulsion balance equation writes:

   .. math::
      :label: Impulsion_Balance
   
      \varrho(\phi,c)\left[\frac{\partial\boldsymbol{u}}{\partial t}+\boldsymbol{\nabla}\cdot(\boldsymbol{u}\boldsymbol{u})\right]=-\boldsymbol{\nabla}p_{h}+\boldsymbol{\nabla}\cdot\left[\eta(\phi)\left(\boldsymbol{\nabla}\boldsymbol{u}+\boldsymbol{\nabla}\boldsymbol{u}^{T}\right)\right]+\boldsymbol{F}_{tot}

   where :math:`p_{h}\equiv p_{h}(\boldsymbol{x},t)` is the hydrodynamic pressure, :math:`\varrho` is the total densiy and :math:`\eta` is the dynamic viscosity. Those quantities are obtained from the interpolation of bulk properties with the phase-field :math:`\phi`. Their expressions will be given in the subsection "Closure".

   **Phase-field equation**

   The interface is followed by an additional PDE on the phase-field:

   .. math::
      :label: CAC_Equation
   
      \frac{\partial\phi}{\partial t}+\boldsymbol{\nabla}\cdot(\boldsymbol{u}\phi)=\boldsymbol{\nabla}\cdot\left[M_{\phi}\left(\boldsymbol{\nabla}\phi-\frac{4}{W}\phi(1-\phi)\boldsymbol{n}\right)\right]+\lambda\mathscr{S}_{\phi}

   where :math:`\phi\equiv\phi(\boldsymbol{x},t)` is the phase-field, :math:`M_{\phi}` is the mobility and :math:`W` is the interface width. That equation is called "Conservative Allen-Cahn" equation (CAC). It is also encountered in the literature as the "Levelset" equation.

   **Composition equation**

   Finally, the composition equation is also considered in that model:

   .. math::
      :label: Composition_Equation
   
      \frac{\partial c}{\partial t}+\boldsymbol{\nabla}\cdot(\boldsymbol{u}c)=\boldsymbol{\nabla}\cdot\left[\mathcal{D}(\phi)\boldsymbol{\nabla}\mu_{c}\right]
      
   where :math:`c\equiv c(\boldsymbol{x},t)` is the composition, :math:`\mathcal{D}(\phi)` is the diffusion coefficient and :math:`\mu_{c}` is the chemical potential relative to the composition :math:`c`.

Force and source terms
^^^^^^^^^^^^^^^^^^^^^^

Several forces are defined in ``NSAC_Comp`` kernel.

**Total force**

The total force :math:`\boldsymbol{F}_{tot}` in Eq. :eq:`Impulsion_Balance` is defined by

.. math::
   :label: Force_Total
   
   \boldsymbol{F}_{tot}=\boldsymbol{F}_{c}+\boldsymbol{F}_{g}+\boldsymbol{F}_{M}
   
where :math:`\boldsymbol{F}_{c}` is the capillary force, :math:`\boldsymbol{F}_{g}` is the gravity force and :math:`\boldsymbol{F}_{M}` is the Marangoni force. They are detailed below.

.. container:: sphinx-features

   .. admonition:: Capillary force
      :class: hint

      The capillary force :math:`\boldsymbol{F}_{c}` is defined by

      .. math::
         :label: Force_Capillary
   
         \boldsymbol{F}_{c}=\mu_{\phi}\boldsymbol{\nabla}\phi

      where the chemical potential :math:`\mu_{\phi}` is defined by

      .. math::
         :label: pot_chem_phi
   
         \mu_{\phi}=\frac{3}{2}\sigma\left[\frac{16}{W}\phi(1-\phi)(1-2\phi)-W\boldsymbol{\nabla}^{2}\phi\right]

      :math:`\sigma` is the surface tension and :math:`W` is the interface width.

   :math:`\hspace{5mm}`
      
   .. admonition:: Marangoni force
      :class: hint

      The Marangoni force :math:`\boldsymbol{F}_{M}` is a surfacic gradient of :math:`\sigma(c)` defined by 

      .. math::
         :label: Force_Marangoni
   
         \boldsymbol{F}_{M}=\frac{3W}{2}\left[\boldsymbol{\nabla}\sigma|\boldsymbol{\nabla}\phi|^{2}-\boldsymbol{\nabla}\phi(\boldsymbol{\nabla}\phi\cdot\boldsymbol{\nabla}\sigma)\right]

      .. math::
         :label: Sigma_c
   
         \sigma(c)=\sigma_{ref}+\frac{d\sigma}{dc}(c-c_{ref})

      .. math::
         :label: ds_dc
   
         \frac{d\sigma}{dc}=\sigma_{c}<0


   .. container:: sphinx-features

      .. admonition:: Gravity force
         :class: hint

         The gravity force :math:`\boldsymbol{F}_{g}` is defined by

         .. math::
            :label: Force_Gravity
   
            \boldsymbol{F}_{g}=\varrho(\phi,c)\boldsymbol{g}

         where :math:`\varrho(\phi,c)` is an interpolation of bulk densities by Eq. :eq:`Density_Total_Surf`

**Source term of Eq.** :eq:`CAC_Equation`

In the last term of the right-hand side of Eq. :eq:`CAC_Equation`, the source term :math:`\mathscr{S}_{\phi}` can be defined for phase-change problems. An example of such a source term can be found on :ref:`Math-Dissolution` (Eq. :eq:`Source_Term_Dissolution`) and :ref:`Math-Crystal`. In that case, the :math:`\lambda` coefficient must be appropriately chosen. For two immiscible fluid flows, that coefficient is set equal to zero.

Closure relationships
^^^^^^^^^^^^^^^^^^^^^

In order to close the model, it is required to add closure relationships. In Eq. :eq:`Composition_Equation`, the flux is given by the gradient of chemical potential :math:`\mu_c` which is generalization of the classic Fick's law. The chemical potential is related to the composition :math:`c` by

.. math::
   :label: pot_chem_compos
   
   \mu_{c}=\mu_{c}^{eq}+c(\phi,\mu_{c})-\left[c_{1}^{eq}\phi+c_{0}^{eq}(1-\phi)\right]

In that equation, :math:`\mu_{c}^{eq}`, :math:`c_{0}^{eq}` and :math:`c_{1}^{eq}` are three scalar values which must be set in the input file. If all of them are zero, then the classic diffusion equation is recoved. Non-zero positive values of :math:`c_{0}^{eq}` and :math:`c_{1}^{eq}` mean that the compositions in each phase will tend to the equilibrium compositions :math:`c_{0}^{eq}` and :math:`c_{1}^{eq}` during the simulation.

The total density :math:`\varrho` is interpolated by :math:`\phi` and :math:`c`:

.. math::
   :label: Density_Total
   
   \varrho(\phi,c)=\rho_{1}(c)p(\phi)+\rho_{0}(c)(1-p(\phi))

In ``NSAC_Comp`` the bulk density can slightly vary with the composition. The interpolation is linear in :math:`c` between the initial density :math:`\rho^{ini}` and the equilibrium one :math:`\rho^{eq}`:

.. math::
   :label: Density_Bulk
   
   \rho_{\Phi}(c)=(\rho_{\Phi}^{eq}-\rho_{\Phi}^{ini})\frac{c-c_{\Phi}^{ini}}{c_{\Phi}^{eq}-c_{\Phi}^{ini}}+\rho_{\Phi}^{ini}

It is recommended to keep the variation of :math:`\Delta \rho = \rho^{ini}-\rho^{eq}` small. The index :math:`\Phi=0,1` indicates phase 0 or phase 1. The interpolation function :math:`p(\phi)` can be chosen:

.. math::
   :label: Polynom_Interpol
   
   p(\phi)=\begin{cases}
   \phi\qquad\text{or}\\
   \phi^{2}(3-2\phi)
   \end{cases}

The dynamic viscosity is interpolated by a harmonic mean formula:

.. math::
   :label: Viscosity_Total
   
   \frac{1}{\eta(\phi)}=\frac{\phi}{\eta_{1}}+\frac{1-\phi}{\eta_{0}}

Finally in the composition equation, the diffusion parameter is also
linearly interpolated:

.. math::
   :label: Diffusion_Total
   
   \mathcal{D}(\phi)=D_{1}\phi+D_{0}(1-\phi)


Alternative phase-field model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

With the kernel ``NSAC_Comp``, other phase-field equations can be simulated with appropriate options inside the input file. For example, the well-known model of Cahn-Hilliard writes:

**Cahn-Hilliard model**

.. math::
   :label: Cahn_Hilliard
   
   \frac{\partial\phi}{\partial t}+\boldsymbol{\nabla}\cdot(\boldsymbol{u}\phi)=\mathcal{M}_{\phi}\boldsymbol{\nabla}^{2}\mu_{\phi}

where the chemical potential is defined by

.. math::
   :label: Chem_pot_Cahn_Hilliard
   
   \mu_{\phi}=2H\phi(1-\phi)(1-2\phi)-\zeta\boldsymbol{\nabla}^{2}\phi

**Alternative form of conservative Allen-Cahn equation**

The counter term :math:`(4/W)\phi(1-\phi)\boldsymbol{n}` in the Conservative Allen-Cahn (CAC) Eq. :eq:`CAC_Equation` can also be put outside the divergence term and noted :math:`\mathcal{S}_{ct}`:

.. math::
   :label: CAC_2nd_Form
   
   \frac{\partial\phi}{\partial t}+\boldsymbol{\nabla}\cdot(\boldsymbol{u}\phi)=M_{\phi}\boldsymbol{\nabla}^{2}\phi\underbrace{-\boldsymbol{\nabla}\cdot\left[\frac{4}{W}\phi(1-\phi)\boldsymbol{n}\right]}_{\mathcal{S}_{ct}}
   
**Allen-Cahn equation for phase change problems**

For problems of phase change, e.g. dissolution of porous media, the phase-field equation makes appear a first term involving the derivative of double-well :math:`\mathcal{S}_{dw}` and a second term, a source term, :math:`\mathcal{S}_{st}` which is responsible for the interface displacement and proportional to a coupling coefficient :math:`\lambda`. Such a model is presented in :ref:`Math-Dissolution` where the phase-field equation writes:

.. math::
   :label: Allen_Cahn
   
   \frac{\partial\phi}{\partial t}+\boldsymbol{\nabla}\cdot(\boldsymbol{u}\phi)=M_{\phi}\boldsymbol{\nabla}^{2}\phi\underbrace{-\frac{M_{\phi}}{W^{2}}2\phi(1-\phi)(1-2\phi)}_{\mathcal{S}_{dw}}+\underbrace{\frac{\lambda M_{\phi}}{W^{2}}\mathscr{S}_{\phi}(\phi,\,\overline{\mu})}_{\mathcal{S}_{st}}
   
**General form of phase-field equation**

.. admonition:: General formulation for phase-field equation
   :class: important

   Finally, if we introduce two integers :math:`\chi_1` and :math:`\chi_2`, a general formulation of the phase-field equation writes:

   .. math::
      :label: General_Phase_Field

      \frac{\partial\phi}{\partial t}+\boldsymbol{\nabla}\cdot(\boldsymbol{u}\phi)=M_{\phi}\boldsymbol{\nabla}^{2}[\chi_{1}\mu_{\phi}+(1-\chi_{1})\phi]-(1-\chi_{1})\left[\chi_{2}\mathcal{S}_{ct}+(1-\chi_{2})\mathcal{S}_{dw}+\mathcal{S}_{st}\right]
      
   In that equation if

      - :math:`\chi_1=1` then the CH Eq. :eq:`Cahn_Hilliard` is recovered.
      - :math:`\chi_1=0` and :math:`\chi_2=1`, then the CAC Eq. :eq:`CAC_Equation` is recovered.
      - :math:`\chi_1=0` and :math:`\chi_2=0`, then the CAC Eq. :eq:`Allen_Cahn` is recovered.

In the input file of LBM_Saclay, the integers :math:`\chi_1` and :math:`\chi_2` are respectively named ``cahn_hilliard`` and ``counter_term``. Examples of ``.ini`` input files are given in the folder ``run_training_lbm``

- For Cahn-Hilliard model: ``TestCase05_Spinodal-Decomposition2D``
- For Allen-Cahn equation with phase change: ``TestCase06b_Stefan-Problem``
- For Conservative Allen-Cahn equation: all other two-phase test cases (e.g. ``TestCase09_Capillary-Wave2D``)

List of input parameters in ``.ini`` file
-----------------------------------------

1. Section ``[lbm]``

   In section ``[lbm]`` use the keyword ``problem=NSAC_Comp`` to simulate that mathematical model. Next, the sections ``[params]`` and ``[params_composition]`` must be set.

2. Section ``[params]``

   The list of parameters are summarized in Table below.

.. container:: sphinx-features

   +----------------------------------------------+--------------------------------------+---------------------------+-------------------+
   |                                              |                                      |                           |                   |
   +==============================================+======================================+===========================+===================+
   | **Math symbol**                              | **Parameter name**                   | **Equation**              | ``.ini`` **file** |
   +----------------------------------------------+--------------------------------------+---------------------------+-------------------+
   | :math:`M_{\phi}`                             | Mobility of interface                | Eq. :eq:`CAC_Equation`    | ``Mphi``          |
   +----------------------------------------------+--------------------------------------+---------------------------+-------------------+
   | :math:`W`                                    | Interface width                      | Eq. :eq:`CAC_Equation`    | ``W``             |
   +----------------------------------------------+--------------------------------------+---------------------------+-------------------+
   | :math:`\lambda`                              | Coupling parameter                   | Eq. :eq:`CAC_Equation`    | ``lambda``        |
   +----------------------------------------------+--------------------------------------+---------------------------+-------------------+
   | :math:`\rho_0`                               | Bulk density of phase 0              | Eq. :eq:`Density_Total`   | ``rho0``          |
   +----------------------------------------------+--------------------------------------+---------------------------+-------------------+
   | :math:`\rho_1`                               | Bulk density of phase 1              | Eq. :eq:`Density_Total`   | ``rho1``          |
   +----------------------------------------------+--------------------------------------+---------------------------+-------------------+
   | :math:`\nu_0`                                | Kinematic viscosity of phase 0       | Eq. :eq:`Viscosity_Total` | ``nu0``           |
   +----------------------------------------------+--------------------------------------+---------------------------+-------------------+
   | :math:`\nu_1`                                | Kinematic viscosity of phase 1       | Eq. :eq:`Viscosity_Total` | ``nu1``           |
   +----------------------------------------------+--------------------------------------+---------------------------+-------------------+
   | :math:`\sigma`                               | Surface tension                      | Eq. :eq:`pot_chem_phi`    | ``sigma``         |
   +----------------------------------------------+--------------------------------------+---------------------------+-------------------+
   | :math:`g_{\alpha}` with :math:`\alpha=x,y,z` | Gravity                              | Impulsion balance         | ``gy``            |
   +----------------------------------------------+--------------------------------------+---------------------------+-------------------+
   | :math:`D_0`                                  | Bulk diffusion of phase 0            | Eq. :eq:`Diffusion_Total` | ``rho0``          |
   +----------------------------------------------+--------------------------------------+---------------------------+-------------------+
   | :math:`D_1`                                  | Bulk diffusion of phase 1            | Eq. :eq:`Diffusion_Total` | ``rho1``          |
   +----------------------------------------------+--------------------------------------+---------------------------+-------------------+
   | :math:`\rho_{0}^{ini}`                       | Initial bulk density of phase 0      | Eq. :eq:`Density_Bulk`    | ``rho0``          |
   +----------------------------------------------+--------------------------------------+---------------------------+-------------------+
   | :math:`\rho_{0}^{eq}`                        | Equilibrium bulk density of phase 0  | Eq. :eq:`Density_Bulk`    | ``rho1``          |
   +----------------------------------------------+--------------------------------------+---------------------------+-------------------+
   | :math:`\rho_{1}^{ini}`                       | Initial bulk density of phase 0      | Eq. :eq:`Density_Bulk`    | ``rho0``          |
   +----------------------------------------------+--------------------------------------+---------------------------+-------------------+
   | :math:`\rho_{1}^{eq}`                        | Equilibrium bulk density of phase 0  | Eq. :eq:`Density_Bulk`    | ``rho1``          |
   +----------------------------------------------+--------------------------------------+---------------------------+-------------------+

3. Section ``[params_composition]``

.. container:: sphinx-features

   +------------------------+--------------------------------------+----------------------------------------------+-------------------+
   |                        |                                      |                                              |                   |
   +========================+======================================+==============================================+===================+
   | **Math symbol**        | **Parameter name**                   | **Equation**                                 | ``.ini`` **file** |
   +------------------------+--------------------------------------+----------------------------------------------+-------------------+
   | :math:`\mu^{eq}_c`     | Equilibrium chemical potential       | Eq. :eq:`pot_chem_compos`                    | ``mu_eq``         |
   +------------------------+--------------------------------------+----------------------------------------------+-------------------+
   | :math:`c_0^{ini}`      | Initial composition of phase 0       | Init cond for Eq. :eq:`Composition_Equation` | ``c0_inf``        |
   +------------------------+--------------------------------------+----------------------------------------------+-------------------+
   | :math:`c_0^{eq}`       | Equilibrium composition of phase 0   | Eq. :eq:`pot_chem_compos`                    | ``c0_co``         |
   +------------------------+--------------------------------------+----------------------------------------------+-------------------+
   | :math:`c_1^{ini}`      | Initial composition of phase 1       | Init cond for Eq. :eq:`Composition_Equation` | ``c1_inf``        |
   +------------------------+--------------------------------------+----------------------------------------------+-------------------+
   | :math:`c_1^{eq}`       | Equilibrium composition of phase 1   | Eq. :eq:`pot_chem_compos`                    | ``c1_co``         |
   +------------------------+--------------------------------------+----------------------------------------------+-------------------+

4. Section ``[params_marangoni]``

   - ``force_marangoni=``: ``1`` or ``0``
   - ``sigma_marangoni=``: positive real value (Eq. :eq:`Sigma_c`)
   - ``dsigmadcomp =``: negative real value (Eq. :eq:`ds_dc`)

5. Section ``[output]``

   In the output section ``[output]`` of ``.ini`` file, the fields to write must be indicated as a list in ``write_variables=``. For example:

   ``write_variables=vx,vy,vz,pressure,phi,composition``

   The names of fields can be found in the source file ``Index_NS_AC_Comp.h`` of directory ``LBM_Saclay_Rech-Dev/src/kernels/NSAC_Comp``.

Validation with analytical solution of Prosperetti
--------------------------------------------------

That analytical solution has been implemented in sage math (see ref [2]_)

Setup for LBM_Saclay
^^^^^^^^^^^^^^^^^^^^

The simulations with LBM_Saclay are run with kernel ``NSAC_Comp``. Even though the composition equation is solved in that kernel, the composition is not used for that test case. The collision operators are BGK for phase-field and composition equations. For Navier-Stokes equations, the MRT is used.

**Input parameters**

In ``.ini`` files, the following parameters are identical:

- For hydrodynamic the parameters are :math:`\rho_l=1`, :math:`\rho_g=0.01`, :math:`\nu_l=\nu_g=0.005`, :math:`g_y=0`, :math:`\sigma=10^{-4}`.
- For phase-field equation, they are :math:`W=5`, :math:`M_{\phi}=0.02`.


The positions of boundaries are 

- :math:`x_{min}=-64`, :math:`x_{max}=64` corresponding to :math:`L_x=128`. The conditions are periodic.
- :math:`y_{min}=0`, :math:`y_{max}=256` corresponding to :math:`L_y=256`. The conditions are bounce-back.

For following simulations :math:`L_x=128` and :math:`L_y=256` are set constant. We modify :math:`N_x` and :math:`N_y` i.e. :math:`\delta x` and :math:`\delta t`. For those comparisons, the density ratio is :math:`\rho_l/\rho_g=100`. For higher density ratios (~830) the comparisons are presented in :ref:`TwoP-Training-LBM`. The simulations ran on MANWE equipped with one GPU A6000.

- The wavelength is :math:`\lambda=L_x` and the initial amplitude :math:`a_0` is set equal to :math:`L_x/100=1.28` 

Results
^^^^^^^

**Mesh 128x256**

For that first simulation the mesh is composed of 128x256 cells corresponding to :math:`\delta x=1`. We also set :math:`\delta t=1`. The total number of time-steps is set equal to :math:`N_t=300001` (``nStepmax``) and ``nOutput=2000``. The simulation took 222.9 seconds (~3min43s). The comparison is presented on Fig. :numref:`target-Fig-Prosperetti_Mesh128x256`.

**Mesh 256x512**

For that first simulation the mesh is composed of 256x512 cells corresponding to :math:`\delta x=0.5`. We also set :math:`\delta t=0.5`. The total number of time-steps is set equal to :math:`N_t=600001` (``nStepmax``) and ``nOutput=4000``. The simulation took 1042.3 seconds (~17min22s). The comparison is presented on Fig. :numref:`target-Fig-Prosperetti_Mesh256x512`.

2085.389 s.

.. container:: sphinx-features

   .. _target-Fig-Prosperetti_Mesh128x256:

   .. figure:: ../../../src_doc/FIGS/01_FIGS_VALIDATIONS/Comparison_Prosperetti_Mesh128x256.png
      :height: 400
      :width: 500
      :scale: 95
      :align: center
   
      Comparison on mesh size 128x256 and :math:`\delta x=\delta t=1`.

   .. _target-Fig-Prosperetti_Mesh256x512:

   .. figure:: ../../../src_doc/FIGS/01_FIGS_VALIDATIONS/Comparison_Prosperetti_Mesh256x512.png
      :height: 400
      :width: 500
      :scale: 95
      :align: center
   
      Comparison on mesh size 256x512 and :math:`\delta x=\delta t=0.5`.

.. container:: sphinx-features

   .. _target-Fig-Prosperetti_CompareMesh:

   .. figure:: ../../../src_doc/FIGS/01_FIGS_VALIDATIONS/Fig_Prosperetti_CompareMesh.png
      :height: 500
      :width: 650
      :scale: 100
      :align: center
   
      Zoom for mesh sizes 64x128 (green), 128x256 (blue) and 256x512 (black) with reference (red).

As expected, the numerical solution becomes more and more accurate when the mesh size and time step diminish.


   
Examples of simulations with that model
---------------------------------------

As already mentioned, many test cases using that math model can be found in the directory ``run_training_lbm`` to  :ref:`Run_Training-LBM`. It is recommended to start running the ``.ini`` files contained in that directory. Here we present few videos of 3D simulations. Other videos can be found in :ref:`TwoP-Training-LBM`

.. raw:: html
   
   <video controls src="../../../_static/Vid3D_RT-2modes_900x900x512_Crop.webm" width="700" height="530"> </video>

.. raw:: html

   <video controls src="../../../_static/Vid3D_Taylor-Bubble_vC_Bo20.webm" width="800" height="620"> </video>


Bibliography
------------

.. [1] Andrea Prosperetti. Motion of two superposed viscous fluids. The Physics of Fluids, 24(7):1217–1223, 07 1981. URL: https://doi.org/10.1063/1.863522.

.. [2] Hoel Keraudren. Pseudo-potential method for multiphase flows using Lattice Boltzmann Methods (Simulation of Navier-Stokes-Korteweg equations). Technical Report CEA, 2023.

.. sectionauthor:: Alain Cartalade
   