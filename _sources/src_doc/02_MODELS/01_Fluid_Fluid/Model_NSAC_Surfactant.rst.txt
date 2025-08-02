.. _Math-NSAC-Surfactant:

Model of Navier-Stokes/CAC with surfactant
==========================================

We detail here the model of two-phase flows with surfactant. Compared to the kernel ``NSAC_Comp``, the equations of mass balance, impulsion balance and levelset are identical. The modification appears in the composition equation.

Mathematical model of two-phase with surfactant
-----------------------------------------------

The mathematical model is composed of incompressible Navier-Stokes equations coupled with the phase-field equation and the composition equation. Compared to the ``NSAC_Comp`` kernel, the composition equation is modified with a counter term to impose an equilibrium profile at the interface. The model writes as follows.
   
**Mass balance equation**

The mass balance writes:

.. math::
   :label: Mass_Balance_Surf
   
   \boldsymbol{\nabla}\cdot\boldsymbol{u}=0

where :math:`\boldsymbol{u}\equiv\boldsymbol{u}(\boldsymbol{x},t)=(u_x,u_y,u_z)^T` is the fluid velocity.

**Impulsion balance equation**

The impulsion balance equation writes:

.. math::
   :label: Impulsion_Balance_Surf
   
   \varrho(\phi,c)\left[\frac{\partial\boldsymbol{u}}{\partial t}+\boldsymbol{\nabla}\cdot(\boldsymbol{u}\boldsymbol{u})\right]=-\boldsymbol{\nabla}p_{h}+\boldsymbol{\nabla}\cdot\left[\eta(\phi)\left(\boldsymbol{\nabla}\boldsymbol{u}+\boldsymbol{\nabla}\boldsymbol{u}^{T}\right)\right]+\boldsymbol{F}_{tot}

where :math:`p_{h}\equiv p_{h}(\boldsymbol{x},t)` is the hydrodynamic pressure, :math:`\varrho` is the total densiy and :math:`\eta` is the dynamic viscosity. Those quantities are obtained from the interpolation of bulk properties with the phase-field :math:`\phi`. Their expressions will be given in the subsection "Closure".

**Phase-field equation**

The interface is followed by an additional PDE on the phase-field:

.. math::
   :label: CAC_Equation_Surf
   
   \frac{\partial\phi}{\partial t}+\boldsymbol{\nabla}\cdot(\boldsymbol{u}\phi)=\boldsymbol{\nabla}\cdot\left[M_{\phi}\left(\boldsymbol{\nabla}\phi-\frac{4}{W}\phi(1-\phi)\boldsymbol{n}_{\phi}\right)\right]

where :math:`\phi\equiv\phi(\boldsymbol{x},t)` is the phase-field, :math:`M_{\phi}` is the mobility and :math:`W` is the interface width. That equation is called "Conservative Allen-Cahn" equation (CAC). It is also encountered in the literature as the "Levelset" equation.

.. admonition:: Composition equation
   :class: important

   Finally, the composition equation is also considered in that model:

   .. math::
      :label: Composition_Equation_Surf
   
      \frac{\partial c}{\partial t}+\boldsymbol{\nabla}\cdot\left(c\boldsymbol{u}\right)=\boldsymbol{\nabla}\cdot\left[M_{c}\left(\boldsymbol{\nabla} c-c(1-c)\mathcal{P}(\phi)\boldsymbol{n}_{\phi}\right)\right]
      
   where :math:`c\equiv c(\boldsymbol{x},t)` is the composition, :math:`M_c` is the diffusion coefficient and :math:`\mathcal{P}(\phi)` is an interpolation polynom defined by

   .. math::
      :label: Polynom_Surf

      \mathcal{P}(\phi)=\beta\frac{4}{W}\phi(1-\phi)\left(1-2\phi\right)\left[\frac{k}{2}+\frac{16}{W²}\epsilon(1-\phi)\phi\right]

   where :math:`\beta`, :math:`k`, and :math:`\epsilon` are three coefficients which control the composition height at the interface.

Force and source terms
^^^^^^^^^^^^^^^^^^^^^^

The forces are still the same than those defined in ``NSAC_Comp`` kernel.

**Total force**

The total force :math:`\boldsymbol{F}_{tot}` in Eq. :eq:`Impulsion_Balance_Surf` is defined by

.. math::
   :label: Force_Total_Surf
   
   \boldsymbol{F}_{tot}=\boldsymbol{F}_{c}+\boldsymbol{F}_{g}+\boldsymbol{F}_{M}
   
where :math:`\boldsymbol{F}_{c}` is the capillary force, :math:`\boldsymbol{F}_{g}` is the gravity force and :math:`\boldsymbol{F}_{M}` is the Marangoni force. They are detailed below.

**Capillary force** :math:`\boldsymbol{F}_{c}`

The capillary force defined by

.. math::
   :label: Force_Capillary_Surf
   
   \boldsymbol{F}_{c}=\mu_{\phi}\boldsymbol{\nabla}\phi

where the chemical potential :math:`\mu_{\phi}` is defined by

.. math::
   :label: pot_chem_phi_Surf
   
   \mu_{\phi}=\frac{3}{2}\textcolor{red}{\sigma(c)}\left[\frac{16}{W}\phi(1-\phi)(1-2\phi)-W\boldsymbol{\nabla}^{2}\phi\right]

where :math:`W` is the interface width and :math:`\textcolor{red}{\sigma(c)}` is the surface tension varying with composition :math:`c`. Two phenomenological laws are given below.

**The gravity force** :math:`\boldsymbol{F}_{g}`

The gravity force is defined by

.. math::
   :label: Force_Gravity_Surf
   
   \boldsymbol{F}_{g}=\varrho(\phi,c)\boldsymbol{g}
      
**Marangoni force** :math:`\boldsymbol{F}_{M}`

The Marangoni force is defined by

.. math::
   :label: Force_Marangoni_Surf
   
   \boldsymbol{F}_{M}=\frac{3W}{2}\left[\boldsymbol{\nabla}\textcolor{red}{\sigma(c)}|\boldsymbol{\nabla}\phi|^{2}-\boldsymbol{\nabla}\phi(\boldsymbol{\nabla}\phi\cdot\boldsymbol{\nabla}\textcolor{red}{\sigma(c)})\right]
   
   
**Source term of Eq.** :eq:`CAC_Equation_Surf`

In the last term of the righ-hand side of Eq. :eq:`CAC_Equation_Surf`, the source term :math:`\mathscr{S}_{\phi}` can be defined for phase-change problems. In that case, the :math:`\lambda` coefficient must be appropriately chosen. For two immiscible fluid flows, that coefficient is set equal to zero.

.. admonition:: Phenomenological laws for surface tension
   :class: hint

   Two models are implemented to modify the surface tension :math:`\sigma (c)` with composition :math:`c`. The first one writes:

   .. math::
      :label: Sigma_c_Surf
   
      \sigma(c)=\sigma_{ref}+\frac{d\sigma}{dc}(c-c_{ref})

   In that case we need to set the option ``Closure_Model=0`` and ``disgmadcomp`` is used in the ``.ini`` file:

   .. math::
      :label: ds_dc_Surf
   
      \frac{d\sigma}{dc}=\sigma_{c}<0

   For simulations of two-phase with surfactant, another law between the surface tension and the composition is used:

   .. math::
      :label: sigma_Surf

      \sigma=\sigma_{0}\left(1+\gamma ln\left(1-c\right)\right)

   in that case, option ``Closure_Model=1`` must be set and the coefficient :math:`\gamma` is named ``beta_log`` in .ini file and :math:`\sigma_{0}` are two coefficients to be indicated inside the ``.ini`` file.

Closure relationships
^^^^^^^^^^^^^^^^^^^^^

In order to close the model, it is required to add closure relationships. The total density :math:`\varrho` is interpolated by :math:`\phi` and :math:`c`:

.. math::
   :label: Density_Total_Surf
   
   \varrho(\phi,c)=\rho_{1}(c)p(\phi)+\rho_{0}(c)(1-p(\phi))

where each bulk density :math:`\rho_{\Phi}` is linearly interpolated by :math:`c`:

.. math::
   :label: Density_Bulk_Surf
   
   \rho_{\Phi}(c)=(\rho_{\Phi}^{eq}-\rho_{\Phi}^{ini})\frac{c-c_{\Phi}^{ini}}{c_{\Phi}^{eq}-c_{\Phi}^{ini}}+\rho_{\Phi}^{ini}


The index :math:`\Phi=0,1` indicates phase 0 or phase 1. The interpolation function :math:`p(\phi)` can be chosen:

.. math::
   :label: Polynom_Interpol_Surf
   
   p(\phi)=\begin{cases}
   \phi\qquad\text{or}\\
   \phi^{2}(3-2\phi)
   \end{cases}

The dynamic viscosity is interpolated by a harmonic mean formula:

.. math::
   :label: Viscosity_Total_Surf
   
   \frac{1}{\eta(\phi)}=\frac{\phi}{\eta_{1}}+\frac{1-\phi}{\eta_{0}}

Finally in the composition equation, the diffusion parameter is also
linearly interpolated:

.. math::
   :label: Diffusion_Total_Surf
   
   \mathcal{D}(\phi)=D_{1}\phi+D_{0}(1-\phi)


List of input parameters in ``.ini`` file
-----------------------------------------

1. Section ``[lbm]``

   In section ``[lbm]`` use the keyword ``problem=NSAC_Comp`` to simulate that mathematical model. Next, the sections ``[params]`` and ``[params_composition]`` must be set.

2. Section ``[params]``

   The list of parameters are summarized in Table below.

.. container:: sphinx-features

   +----------------------------------------------+--------------------------------------+----------------------------------+-------------------+
   |                                              |                                      |                                  |                   |
   +==============================================+======================================+==================================+===================+
   | **Math symbol**                              | **Parameter name**                   | **Equation**                     | ``.ini`` **file** |
   +----------------------------------------------+--------------------------------------+----------------------------------+-------------------+
   | :math:`M_{\phi}`                             | Mobility of interface                | Eq. :eq:`CAC_Equation_Surf`      | ``Mphi``          |
   +----------------------------------------------+--------------------------------------+----------------------------------+-------------------+
   | :math:`W`                                    | Interface width                      | Eq. :eq:`CAC_Equation_Surf`      | ``W``             |
   +----------------------------------------------+--------------------------------------+----------------------------------+-------------------+
   | :math:`\lambda`                              | Coupling parameter                   | Eq. :eq:`CAC_Equation_Surf`      | ``lambda``        |
   +----------------------------------------------+--------------------------------------+----------------------------------+-------------------+
   | :math:`\rho_0`                               | Bulk density of phase 0              | Eq. :eq:`Density_Total_Surf`     | ``rho0``          |
   +----------------------------------------------+--------------------------------------+----------------------------------+-------------------+
   | :math:`\rho_1`                               | Bulk density of phase 1              | Eq. :eq:`Density_Total_Surf`     | ``rho1``          |
   +----------------------------------------------+--------------------------------------+----------------------------------+-------------------+
   | :math:`\nu_0`                                | Kinematic viscosity of phase 0       | Eq. :eq:`Viscosity_Total_Surf`   | ``nu0``           |
   +----------------------------------------------+--------------------------------------+----------------------------------+-------------------+
   | :math:`\nu_1`                                | Kinematic viscosity of phase 1       | Eq. :eq:`Viscosity_Total_Surf`   | ``nu1``           |
   +----------------------------------------------+--------------------------------------+----------------------------------+-------------------+
   | :math:`\sigma`                               | Surface tension                      | Eq. :eq:`pot_chem_phi_Surf`      | ``sigma``         |
   +----------------------------------------------+--------------------------------------+----------------------------------+-------------------+
   | :math:`g_{\alpha}` with :math:`\alpha=x,y,z` | Gravity                              | Eq. :eq:`Impulsion_Balance_Surf` | ``gy``            |
   +----------------------------------------------+--------------------------------------+----------------------------------+-------------------+
   | :math:`D_0`                                  | Bulk diffusion of phase 0            | Eq. :eq:`Diffusion_Total_Surf`   | ``rho0``          |
   +----------------------------------------------+--------------------------------------+----------------------------------+-------------------+
   | :math:`D_1`                                  | Bulk diffusion of phase 1            | Eq. :eq:`Diffusion_Total_Surf`   | ``rho1``          |
   +----------------------------------------------+--------------------------------------+----------------------------------+-------------------+
   | :math:`\rho_{0}^{ini}`                       | Initial bulk density of phase 0      | Eq. :eq:`Density_Bulk_Surf`      | ``rho0``          |
   +----------------------------------------------+--------------------------------------+----------------------------------+-------------------+
   | :math:`\rho_{0}^{eq}`                        | Equilibrium bulk density of phase 0  | Eq. :eq:`Density_Bulk_Surf`      | ``rho1``          |
   +----------------------------------------------+--------------------------------------+----------------------------------+-------------------+
   | :math:`\rho_{1}^{ini}`                       | Initial bulk density of phase 0      | Eq. :eq:`Density_Bulk_Surf`      | ``rho0``          |
   +----------------------------------------------+--------------------------------------+----------------------------------+-------------------+
   | :math:`\rho_{1}^{eq}`                        | Equilibrium bulk density of phase 0  | Eq. :eq:`Density_Bulk_Surf`      | ``rho1``          |
   +----------------------------------------------+--------------------------------------+----------------------------------+-------------------+

3. Section ``[params_composition]``

.. container:: sphinx-features

   +------------------------+--------------------------------------+---------------------------------------------------+-------------------+
   |                        |                                      |                                                   |                   |
   +========================+======================================+===================================================+===================+
   | **Math symbol**        | **Parameter name**                   | **Equation**                                      | ``.ini`` **file** |
   +------------------------+--------------------------------------+---------------------------------------------------+-------------------+
   | :math:`k`              | Equilibrium chemical potential       | Eq. :eq:`Polynom_Surf`                            | ``k_surf``        |
   +------------------------+--------------------------------------+---------------------------------------------------+-------------------+
   | :math:`\epsilon`       | Initial composition of phase 0       | Eq. :eq:`Polynom_Surf`                            | ``eps_surf``      |
   +------------------------+--------------------------------------+---------------------------------------------------+-------------------+
   | :math:`\beta`          | Equilibrium composition of phase 0   | Eq. :eq:`Polynom_Surf`                            | ``beta_surf``     |
   +------------------------+--------------------------------------+---------------------------------------------------+-------------------+
   | :math:`c_b`            | Initial bulk composition             | Init cond for Eq. :eq:`Composition_Equation_Surf` | ``c0_co``         |
   +------------------------+--------------------------------------+---------------------------------------------------+-------------------+

4. Section ``[params_marangoni]``

   - ``force_marangoni=``: ``1`` or ``0``
   - ``sigma_marangoni=``: positive real value (Eq. :eq:`Sigma_c_Surf`)
   - ``dsigmadcomp =``: negative real value (Eq. :eq:`ds_dc_Surf`)

5. Section ``[output]``

   In the output section ``[output]`` of ``.ini`` file, the fields to write must be indicated as a list in ``write_variables=``. For example:

   ``write_variables=vx,vy,vz,pressure,phi,composition``

   The names of fields can be found in the source file ``Index_NS_AC_Comp.h`` of directory ``LBM_Saclay_Rech-Dev/src/kernels/NSAC_Comp``.

   
Validation with analytical solutions
------------------------------------

**Solution** :math:`\phi^{eq}(x)`

In one dimension the analytical solution writes (ref rapport Simon) :math:`\phi^{eq}` for the standard hyperbolic tangent solution

.. math::
   :label: Phi_eq

   \phi^{eq}(x)=0.5[1+\tanh(2x/W)]

**Solution** :math:`c^{analy}(x)` for :math:`c_b^{0}=c_b^{1}`

For composition

.. math::
   :label: Analytical_Surf

   c^{analy}(x)=\frac{c_{b}}{c_{b}+exp(-G(\phi^{eq}))}

where :math:`c_b` is the initial bulk composition which is assumed identical in each bulk: :math:`c_b^{0}=c_b^{1}=c_b` and :math:`G(\phi)` is defined by

.. math::
   :label: G_phi

   G(\phi^{eq})=\beta\left(\frac{8\epsilon}{W^{2}}\phi^{eq}(1-\phi^{eq})+\frac{k}{2}\right)\phi^{eq}(1-\phi^{eq})

.. container:: sphinx-features

   .. _target-Fig-Surfactant-Phi-Analytical:
   
   .. figure:: ../../FIGS/01_FIGS_VALIDATIONS/Surfactant_Phi-Analytical.png
      :figclass: align-center
      :align: center
      :height: 450
      :width: 700
      :scale: 60 %

      Comparison of :math:`\phi`

   .. _target-Fig-Surfactant-C-Analytical:
   
   .. figure:: ../../FIGS/01_FIGS_VALIDATIONS/Surfactant-C-Analytical.png
      :figclass: align-center
      :align: center
      :height: 450
      :width: 700
      :scale: 60 %

      Comparison of :math:`c`

**Solution** :math:`c^{analy}(x)` for :math:`c_b^{0}\neq c_b^{1}`

.. math::
   :label: Surfactant-Asymm-AnalySol-C

   c^{analytical}(x)=\frac{c_{b}^{0}}{c_{b}^{1}+exp\left\{ \beta\phi(1-\phi)\left[\frac{8\epsilon}{W^{2}}\phi(1-\phi)+\frac{k}{2}\right]\textcolor{red}{-2\beta\gamma\phi}\right\} }


.. _target-Fig-Surfactant-C-Analytical:
   
   .. figure:: ../../FIGS/01_FIGS_VALIDATIONS/Surfactant-DeltaC-Analytical.png
      :figclass: align-center
      :align: center
      :height: 450
      :width: 700
      :scale: 60 %

      Comparison of :math:`c`

.. admonition:: In run_training_lbm
   :class: warning

   Those analytical solutions can be run in folders ``Analytical_Profile1`` and ``Analytical_Profile2`` of directory ``TestCase19_Surfactant``. The post-processing used version 5.12 of paraview.

Examples of simulations with that model
---------------------------------------

**Rising bubble and falling droplet**

.. container:: sphinx-features

   .. raw:: html

      <video controls src="../../../_static/Vid_Surfactant_Rising-Bubble.webm" width="450" height="310"> </video>

   .. raw:: html

      <video controls src="../../../_static/Vid_Surfactant_Falling-Droplet.webm" width="450" height="310"> </video>


**Rayleigh-Taylor instability and droplets coalescence**

.. container:: sphinx-features

   .. raw:: html

      <video controls src="../../../_static/Vid_Surfactant_Rayleigh-Taylor.webm" width="450" height="310"> </video>

   .. raw:: html

      <video controls src="../../../_static/Vid_Surfactant_Droplet-Coalescence.webm" width="450" height="310"> </video>

.. sectionauthor:: Alain Cartalade
   