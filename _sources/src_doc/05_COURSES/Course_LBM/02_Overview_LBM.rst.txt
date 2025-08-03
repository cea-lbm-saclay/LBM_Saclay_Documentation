.. _Basic-LBM:

Overview of Lattice Boltzmann Methods
=====================================

This part is a quick introduction to the Lattice Boltzmann Method.  More details on the origin and the theoretical aspects of the method can be found in reference [1]_.

More details of numerical methods that are implemented in LBM_Saclay will be found in the pages below.

.. _Overview-LBM:

Continuous Boltzmann equation
-----------------------------

At mesoscopic level, a collection of particles can be described by a distribution function of particles :math:`f(\boldsymbol{x},\boldsymbol{c},t)` which is a function of position :math:`\boldsymbol{x}`, microscopic speeds :math:`\boldsymbol{c}` and time :math:`t`. Its evolution in time and space obeys to the continuous Boltzmann equation:

.. math::
   :label: Boltzmann_Eq
   
   \frac{\partial f}{\partial t}+\boldsymbol{c}\cdot\boldsymbol{\nabla}f+\boldsymbol{F}\cdot\boldsymbol{\nabla}_{\boldsymbol{c}}f=\Omega(f,f^{eq})\label{eq:Boltzmann_Eq}

which is a transport equation where :math:`\boldsymbol{F}` is the external force and :math:`\Omega(f,f^{eq})` is the collision operator that relaxes the distribution function :math:`f` toward an equilibrium :math:`f^{eq}`. For the classical Batnaghar-Gross-Krook (**BGK**) approximation, that collision operator simply writes:

.. math::
   :label: BGK_Operator
   
    \Omega(f,f^{eq})\sim-\frac{1}{\lambda}\left[f-f^{eq}\right]

where :math:`\lambda` is the collision time. Eq. :eq:`Boltzmann_Eq`, computes the evolution of the distribution function :math:`f` in space and time. The macrosopic quantities such as the density :math:`\rho`, impulsion :math:`\rho\boldsymbol{u}` and energy :math:`\rho\varepsilon` can be derived from that distribution function by integration over the velocity space:

.. math::

   \begin{aligned}
   \rho & =\int fd\boldsymbol{c}\\
   \rho\boldsymbol{u} & =\int f\boldsymbol{c}d\boldsymbol{c}\\
   \rho\varepsilon & =\frac{1}{2}\int(\boldsymbol{c}-\boldsymbol{u})^{2}fd\boldsymbol{c}\end{aligned}

Those macroscopic quantities are called the moments of the distribution function :math:`f(\boldsymbol{x},\boldsymbol{c},t)`.

For more details on the origin of the Boltzmann equation and the physical interpretation of distribution function see reference [2]_.

Discretization of velocity space
--------------------------------

Eq. :eq:`Boltzmann_Eq` must be discretized for :math:`\boldsymbol{x}`, :math:`\boldsymbol{c}` and :math:`t`. After discretization of the velocity space with a finite number of speeds, :math:`\boldsymbol{c}` becomes :math:`\boldsymbol{c}_i` where :math:`i` is the index of velocity varying between :math:`0` and the total number of speeds :math:`N`. The discrete distribution function :math:`f(\boldsymbol{x},\boldsymbol{c}_i,t)` is noted :math:`f_i(\boldsymbol{x},t)`.

**Discrete velocity space**

The discrete velocity is related to them time-step :math:`\delta t` and space-step of spatial discretization :math:`\delta x` by

.. math::
   :label: Discrete_Speeds
   
   \boldsymbol{c}_i = \frac{\delta x}{\delta t}\boldsymbol{e}_i

where :math:`\boldsymbol{e}_i` are the moving directions. A representation of that discretization is presented on Fig. 1. On that example, for one position :math:`\boldsymbol{x}` and time :math:`t`, the distribution function :math:`f` represents a collection of particles of different velocities. After discretization of :math:`\boldsymbol{c}`, only five speeds are kept on that example: right-direction (blue), upward-direction (red), left-direction (green), downward-direction (orange) and non-moving direction (black).

.. figure:: ../../FIGS/FIGS_LBM/DiscreteSpeeds.png
   :height: 320
   :width: 450
   :scale: 100
   :align: center
   
   Fig. 1: Principle of discrete velocity space and discrete distribution function :math:`f_i`

After discretization in space the lattice is a superposition of one standard mesh with the discrete velocity space. If the dimension of space is 2 and the number of total discrete speeds is 5, the lattice name D2Q5 is presented on Fig. 2.

.. figure:: ../../FIGS/FIGS_LBM/Mesh-Lattice.png
   :height: 300
   :width: 500
   :scale: 100
   :align: center
   
   Fig. 2: Example of lattice D2Q5 after discretization of :math:`\boldsymbol{x}` and :math:`\boldsymbol{c}`.

**Lattices**

Many lattices exist in LBM. The most popular lattices are D2Q9 for two-dimensional simulations, and D3Q15, D3Q19 and D3Q27 for three-dimensional simulations. Let us mention that for simulations problems involving only diffusion, the minimal lattices D2Q5 and D3Q7 can be sufficient. In LBM_Saclay, one supplementary lattice is available: D3Q27.

.. admonition:: Two-dimensional lattices: D2Q5 (left) and D2Q9 (right)

   .. container:: sphinx-features

      .. _target-Fig-D2Q5:

      .. figure:: ../../FIGS/FIGS_LBM/Lattice_D2Q5.png
         :height: 250
         :width: 250
         :align: center
      
      .. _target-Fig-D2Q9:

      .. figure:: ../../FIGS/FIGS_LBM/Lattice_D2Q9.png
         :height: 250
         :width: 250
         :align: center
      
   For lattice D2Q5, the five moving vectors are defined by 
   
   .. math::
      :label: Def_D2Q5
      
      \boldsymbol{e}_{0}=\left(\begin{array}{c}
      0\\
      0
      \end{array}\right),\quad\boldsymbol{e}_{1}=\left(\begin{array}{c}
      1\\
      0
      \end{array}\right),\quad\boldsymbol{e}_{2}=\left(\begin{array}{c}
      0\\
      1
      \end{array}\right),\quad\boldsymbol{e}_{3}=\left(\begin{array}{c}
      -1\\
      0
      \end{array}\right),\quad\boldsymbol{e}_{4}=\left(\begin{array}{c}
      0\\
      -1
      \end{array}\right)

   For D2Q9, the four diagonal moving vectors are added:

   .. math::
      :label: Def_D2Q9
      
      \boldsymbol{e}_{5}=\left(\begin{array}{c}
      1\\
      1
      \end{array}\right),\quad\boldsymbol{e}_{6}=\left(\begin{array}{c}
      -1\\
      1
      \end{array}\right),\quad\boldsymbol{e}_{7}=\left(\begin{array}{c}
      -1\\
      -1
      \end{array}\right),\quad\boldsymbol{e}_{8}=\left(\begin{array}{c}
      1\\
      -1
      \end{array}\right)

   
.. admonition:: Three-dimensional lattices
   
   .. container:: sphinx-features

      .. _target-Fig-D3Q7:

      .. figure:: ../../FIGS/FIGS_LBM/D3Q7.png
         :height: 200
         :width: 240
         :align: center

         Lattice D3Q7

      .. _target-Fig-D3Q15:

      .. figure:: ../../FIGS/FIGS_LBM/D3Q15.png
         :height: 200
         :width: 240
         :align: center

         Lattice D3Q15
      
      .. _target-Fig-D3Q19:

      .. figure:: ../../FIGS/FIGS_LBM/D3Q19.png
         :height: 200
         :width: 240
         :align: center

         Lattice D3Q19
      

Lattice Boltzmann Equation (LBE)
--------------------------------

Once the Boltzmann equation is discretized in space and time the following Lattice Boltzmann Equation (**LBE**) is obtained:

.. math::
   :label: LBE
   
   f_{i}(\boldsymbol{x}+\boldsymbol{c}_{i}\delta t,t+\delta t)=f_{i}(\boldsymbol{x},t)-\frac{1}{\tau}\left[f_{i}(\boldsymbol{x},t)-f_{i}^{eq}(\boldsymbol{x},t)\right]

where :math:`\delta t` is the time step and the second term of the right-hand side is the discrete BGK collision operator. The coefficient of proportionnality :math:`\tau` is the collision rate which is related to the collision time by

.. math::
   :label: Def_Tau
   
   \tau=\frac{\lambda}{\delta t}

The right-hand side represents the collision stage and it is often noted

.. math::
   :label: Def_Collision
   
   f_{i}^{\star}(\boldsymbol{x},t)=f_{i}(\boldsymbol{x},t)-\frac{1}{\tau}\left[f_{i}(\boldsymbol{x},t)-f_{i}^{eq}(\boldsymbol{x},t)\right]
   

The expression of the equilibrium distribution function :math:`f_i^{eq}` depends on the physical problem to simulate.

Equilibrium distribution function
---------------------------------

**For low Mach version of Navier-Stokes equations**

For example for low Mach version of Navier-Stokes equations:

.. math::
   :label: Feq_NS
   
   f_{i}^{eq}(\boldsymbol{x},t)=w_{i}\rho\left[1+\frac{\boldsymbol{c}_{i}\cdot\boldsymbol{u}}{c_{s}^{2}}+\frac{(\boldsymbol{c}_{i}\cdot\boldsymbol{u})^{2}}{2c_{s}^{4}}-\frac{\boldsymbol{u}\cdot\boldsymbol{u}}{2c_{s}^{2}}\right]
   
where the coefficient :math:`c_{s}`, called the sound speed, is defined by

.. math::
   :label: Def_Cs
   
   c_{s}=\frac{1}{\sqrt{3}}\frac{\delta x}{\delta t}
   
and :math:`w_{i}` are weights which depend on the lattice considered.

**For Advection-Diffusion Equation (ADE)**

.. math::
   :label: Feq_ADE
   
   f_{i}^{eq}(\boldsymbol{x},t)=w_{i}T\left[1+\frac{\boldsymbol{u}\cdot\boldsymbol{c}_{i}}{c_{s}^{2}}\right]

Explicit algorithm
------------------

The algorithm is extremely simple and it can be summarized into three main stages:

#. Collision: :math:`f_{i}(\boldsymbol{x},t)\rightarrow f_{i}^{\star}(\boldsymbol{x},t)` (right-hand side of Eq. :eq:`LBE`)

#. Streaming: :math:`f_{i}^{\star}(\boldsymbol{x},t)\rightarrow f_{i}(\boldsymbol{x}+\boldsymbol{c}_{i}\delta t,t+\delta t)` (left-hand side)

#. Update the density and impulsion

.. math::
   :label: Def_Moment_O0
   
   \rho(\boldsymbol{x},t)=\sum_{i}f_{i}(\boldsymbol{x},t)
   
.. math::
   :label: Def_Moment_O1
   
   \rho(\boldsymbol{x},t)\boldsymbol{u}(\boldsymbol{x},t)=\sum_{i}f_{i}(\boldsymbol{x},t)\boldsymbol{c}_{i}

.. admonition:: Algorithm
   :class: hint

   Finally, once the lattice is defined, the Navier-Stokes solver using the lattice Boltzmann method consists in a succession of collision and streaming:

   .. math::
      :label: LBE_Overview
   
      f_{i}(\boldsymbol{x}+\boldsymbol{c}_{i}\delta t,t+\delta t)=f_{i}(\boldsymbol{x},t)-\frac{1}{\tau}\left[f_{i}(\boldsymbol{x},t)-f_{i}^{eq}(\boldsymbol{x},t)\right]

   where the equilibrium distribution function is defined by

   .. math::
      :label: Feq_NS-Overview-LBM
   
      f_{i}^{eq}(\boldsymbol{x},t)=w_{i}\rho\left[1+\frac{\boldsymbol{c}_{i}\cdot\boldsymbol{u}}{c_{s}^{2}}+\frac{(\boldsymbol{c}_{i}\cdot\boldsymbol{u})^{2}}{2c_{s}^{4}}-\frac{\boldsymbol{u}\cdot\boldsymbol{u}}{2c_{s}^{2}}\right]

   Once those two stages are performed, the density and impulsion are updated with the relationships:

   .. math::
      :label: Update_Moment_O0
   
      \rho(\boldsymbol{x},t)=\sum_{i}f_{i}(\boldsymbol{x},t)
   
   .. math::
      :label: Update_Moment_O1
   
      \rho(\boldsymbol{x},t)\boldsymbol{u}(\boldsymbol{x},t)=\sum_{i}f_{i}(\boldsymbol{x},t)\boldsymbol{c}_{i}



Chapman-Enskog expansion
------------------------

The link between the discrete Boltzmann equation with the macroscopic Navier-Stokes equations is performed with a mathematical procedure of asymptotic expansions called the Chapman-Enskog expansion. Details of those expansions can be founds in the link below.

.. toctree::
   :maxdepth: 1

   ./05_Chapman-Enskog.rst

The starting point is the algorithm Eq. :eq:`LBE` -- :eq:`Update_Moment_O1`. Once the Chapman-Enskog expansion is performed, the procedure recovers the following macroscopic equations:

.. admonition:: Equivalent macroscopic PDE with the condition :math:`\bigl|\boldsymbol{u}\bigr|\ll c_{s}`
   :class: error
   
   .. math::
      :label: Mass_Balance_LowMac
   
      \partial_{t}\rho+\boldsymbol{\nabla}\cdot(\rho\boldsymbol{u})=0

   for the mass balance equation, and

   .. math::
      :label: Impulsion_Balance_LowMach
   
      \partial_{t}(\rho\boldsymbol{u})+\boldsymbol{\nabla}\cdot(\rho\boldsymbol{u}\boldsymbol{u})=-\boldsymbol{\nabla}p+\boldsymbol{\nabla}\cdot\left[\rho\nu(\boldsymbol{\nabla}\boldsymbol{u}+(\boldsymbol{\nabla}\boldsymbol{u})^{T})\right]+\mathcal{O}(\rho u^{3})

   where the pressure is given by the law of perfect gas :math:`p=\rho c_{s}^{2}` and the kinematic viscosity :math:`\nu` is related to the relaxation rate :math:`\tau` by :math:`\nu=(\tau-1/2)c_{s}^{2}\delta t`.

Variable change in LBE with a source term
-----------------------------------------

.. toctree::
   :maxdepth: 1

   ./04_Variable_Change.rst

Bibliography
------------

.. [1] Krüger T., H. Kusumaatmaja, A. Kuzmin, O. Shardt, G. Silva, E. Viggen, The Lattice Boltzmann Method: Principles and Practice, Graduate Texts in Physics, Springer, 2016.

.. [2] Bird G.A., Molecular Gas Dynamics and the Direct Simulation of Gas Flows, Oxford Engineering Science Series, 1994.
