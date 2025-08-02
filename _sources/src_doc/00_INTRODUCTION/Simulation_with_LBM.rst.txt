.. _Videos-Gallery:

.. |br| raw:: html

   <br />

Videos gallery of simulations with LBM
======================================

We present here an overview of problems that can be simulated with the lattice Boltzmann method. First of all, many mathematical models which are implemented in LBM_Saclay involve the Navier-Stokes equations coupled with an interface-capturing equation. The models are derived from the phase-field theory and a great diversity of two-phase flows, with or without phase change can be simulated. 

Two immiscible fluids
---------------------

Several examples of two-phase simulations are presented in the folder **run_training_lbm**. A non-exhaustive list is given below:

- Rayleigh-Taylor instability
- Capillary wave
- Taylor bubble
- Rising and splashing droplets
- etc.

**Model of Navier-Stokes/Conservative Allen-Cahn (or levelset)**

The first video is the classical Rayleigh-Taylor instability between two liquid phases. The density ratio is small (3). The denser fluid is above and the lighter one is below. The mesh of computational domain is composed of 900x900x512 cells. The simulation has run 24h on 144 GPUs of supercomputer Topaze A100 (CCRT).

.. container:: sphinx-features

   .. raw:: html
   
      <video controls src="../../_static/Vid3D_RT-2modes_900x900x512_Crop.webm" width="650" height="480"> </video>

   Video: simulation of Rayleigh-Taylor instability on mesh 900x900x512


That second simulation is the classical test case of Taylor bubble inside a channel. The density ratio is 830 between both fluids. The initial condition is a cylinder for the gas phase.

.. container:: sphinx-features

   .. raw:: html

      <video controls src="../../_static/Vid3D_Taylor-Bubble_vC_Bo20.webm" width="800" height="620"> </video>

   Video: simulation of a rising Taylor bubble in a parallelepiped channel

**Model of Navier-Stokes/Cahn-Hilliard**

An alternative popular model for simulating immiscible two-phase flows, is the model coupling the Navier-Stokes equations with the Cahn-Hilliard one.

.. container:: sphinx-features

   .. raw:: html

      <video controls src="../../_static/Vid3D_Buoyancy.webm" width="800" height="620"> </video>

   Video: simulation of two rising bubbles inside a channel with NS/CH model

Two-phase flows with phase change
---------------------------------

When the phase change occurs between one liquid phase and one gas phase, the mass balance equation has to be modified to take into account the density variation. The temperature equation is solved and coupled to the phase-field equation. The mathematical model of such a model is described in reference :cite:p:`verdier_kestener_cartalade_2020`

.. container:: sphinx-features

   .. raw:: html

      <video controls src="../../_static/Vid_FilmBoiling.webm" width="600" height="500"> </video>

   Video: simulation of film boiling. The gas phase (green) is heated at bottom boundary.

Two-phase flows interacting with a solid phase
----------------------------------------------

In most of LBM simulations, when a single-phase or two-phase flow interacts with the solid, the Bounce-Back (BB) method is applied i.e. the solid is considered as a boundary condition. Even though the BB is applied for domain boundaries, when the solid is deifned inside the bulk domain, it is considered as a new phase with its phase index :math:`\psi` (see :ref:`Math-NSAC-Comp-Solid`). With that approach, simulations of non-wetting (left) and wetting (right) droplets over a surface can be simulated.

.. container:: sphinx-features

   .. raw:: html

      <video controls src="../../_static/Vid_Contact-Angle_Wetting_Surface.webm" width="800" height="500"> </video>

   Video: simulation of non-wetting (left) and wetting (right) surface

Another application of that model is the leak of a static (left) and moving (right) container. In the video below, the red color represents the solid phase, the blue color is the gas phase and orange is the liquid phase. The densuty ratio corresponds to the ratio between water and air (830 at 20°C).

.. container:: sphinx-features

   .. raw:: html
   
      <video controls src="../../_static/Vid_Container-Hole_Move-noMove.webm" width="800" height="450"> </video>

   Video: simulation of container leak in static (left) and moving (right) condition
   
Three-phase flows
-----------------

One :ref:`Math-NS2AC-Comp` is implemented in LBM_Saclay. The model requires several input parameters. In the simulation below, three immiscible fluids are initialized. A comparison is performed on the dynamic by varying the surface tension between the green phase and the magenta phase. The magenta one, above, is the lighter one whereas the two other have a density ratio of three. The surface tension between the green one and the magenta one increases from left to right.

.. container:: sphinx-features

   .. raw:: html
   
      <video controls src="../../_static/Vid3D_RT_Compare_vB-vC-vD_Publi.webm" width="780" height="460"> </video>

   Video: simulation of surface tension effect for three immiscible fluids

Solid-Liquid phase change
-------------------------

Several models of solid/liquid phase change are also implemented in LBM_Saclay. Here we present two examples: the first one for dissolution of porous media and the second one for crystal growth.

**Dissolution of porous media**

One :ref:`Math-Dissolution` is implemented in LBM_Saclay. All details of the math model and numerical schemes can be found in reference :cite:p:`boutin_verdier_cartalade_2022`. In video below in an example of dissolution of solid phase because when the initial composition reaches its thermo equilibrium.

.. container:: sphinx-features

   .. raw:: html

      <video controls src="../../_static/Vid_Dissolution_CT.webm" width="800" height="500"> </video>

   Video: dissolution of porous medium
   
**Crystal growth**

A well-known application of phase-field models is simulation of solidification and crystal growth. A basic :ref:`Math-Crystal` can be found on that link. ll details of the math model and numerical schemes can be found in reference :cite:p:`cartalade_younsi_plapp_2016`. In the simulations below, we can see how the crystal grows without (left) and with (right) fluid flows. 

.. container:: sphinx-features

   .. raw:: html

      <video controls src="../../_static/Vid3D_Crystal_100.webm" width="480" height="380"> </video>
   
   .. raw:: html

      <video controls src="../../_static/Vid3D_Crystal-Flow.webm" width="480" height="380"> </video>

   Videos: simulations of crystal growth without (left) and with (right) fluid flows

Demixing
--------

One of the most advantage of the Cahn-Hilliard model is to simulate the spinodal and the nucleation-growth regimes.

.. container:: sphinx-features

   .. raw:: html
   
      <video controls src="../../_static/Vid_SpinodalDecomp.webm" width="470" height="470"> </video>

   .. raw:: html

      <video controls src="../../_static/Vid_M3_Tps50000.webm" width="470" height="470"> </video>

   Videos: demixing in spinodal regime with Cahn-Hilliard model

.. container:: sphinx-features

   .. raw:: html

      <video controls src="../../_static/Vid_Nucleation.webm" width="470" height="470"> </video>

   .. raw:: html
   
      <video controls src="../../_static/Vid_Separation.webm" width="470" height="470"> </video>

   Videos: nucleation and growth (left) and phase separation (right)

.. sectionauthor:: Alain Cartalade