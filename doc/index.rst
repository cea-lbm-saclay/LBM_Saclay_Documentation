.. LBM_Saclay documentation master file, created by
   sphinx-quickstart on Fri Oct 11 13:14:51 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. include:: ./src_doc/Substitutions.rst

.. _main-index:

###########################################################
Welcome to LBM_Saclay's documentation (last update |today|)
###########################################################

.. .. cssclass:: sphinx-tagline

.. admonition:: :mediumbold:`LBM_Saclay`

   .. .. container:: sphinx-features

   .. figure:: src_doc/FIGS/Logos_LBM_Saclay/Logo_LBM_Saclay.png
      :class: align-left
      :height: 300
      :width: 280
      :scale: 40
   
   LBM_Saclay is a Computational Fluid Dynamics (CFD) code based on the **Lattice Boltzmann Methods** (:math:`\mathcal{LBM}`). It is developed and maintained at STMF/LDEL laboratory from **CEA/Saclay**. Its main purpose is to simulate Multi-Phase and Multi-Component flows with interface-capturing models derived from the **phase-field theory**. You can run LBM_Saclay either on your own deskop or on supercomputers equipped with a **multi-GPU** partition (High Performance Computing). You will find in this documentation all you need to compile and run your first simulation either on CPU or on GPU. You will also find details on mathematical models, numerical schemes implemented in the code, and tutorials to develop your own models. The code is open source and can be downloaded on :bdg-link-success-line:`Codev-Tuleap repository <https://codev-tuleap.cea.fr/projects/lbmsaclay/>`. For that purpose, follow the instructions on :bdg-ref-primary-line:`Get access to the git repository <Get-Access-Repository>`.

.. admonition:: :mediumbold:`Video gallery`
   :class: important
      
   The combination of *phase-field models* with *LBM* and *GPU* is a very efficient approach for simulating multi-phase and multi-component flows. To illustrate what can be simulated, several videos are presented in different parts of this documentation. An overview can be found on :bdg-ref-primary-line:`Videos-Gallery`. 2D simulations with LBM_Saclay are presented in :bdg-ref-primary-line:`TwoP-Training-LBM-PARTB`. Applications of :bdg-ref-primary-line:`Math-Models` are illustrated with videos.

.. admonition:: :mediumbold:`Links for direct access`

   .. grid:: 2
      :gutter: 4
      :margin: 3 3 0 5

      .. grid-item-card:: For visitors
         :columns: 4

         .. button-ref:: Videos-Gallery
            :color: primary
            :shadow:

            Video gallery

         .. button-ref:: Math-Models
            :color: primary
            :shadow:

            Mathematical models

         .. button-ref:: LBM-Saclay-Schemes
            :color: primary
            :shadow:

            Lattice Boltzmann schemes

      .. grid-item-card:: For users
         :columns: 4

         .. button-ref:: Quick-Start
            :color: primary
            :shadow:

            Quick start

         .. button-ref:: Run_Training-LBM
            :color: primary
            :shadow:

            Practice of two-phase flows

         .. button-ref:: Set-Own-Parameters
            :color: primary
            :shadow:

            Set your own parameters

      .. grid-item-card:: For developers
         :columns: 4

         .. button-link:: https://codev-tuleap.cea.fr/projects/lbmsaclay/
            :color: success
            :shadow:

            codev-tuleap repository

         .. button-ref:: Tutorials
            :color: primary
            :shadow:

            Tutorials for developers

         .. button-ref:: Contribute-Documentation
            :color: primary
            :shadow:

            Guidelines for documentation



****************
**Introduction**
****************
   
.. tab-set::

   .. tab-item:: Context and motivations

      .. admonition:: :mediumbold:`Context and motivations`

         Two-phase flows, and more generally Multi-Phase and Multi-Component flows (MPMC), are involved in many physical phenomena such as *spinodal decomposition*, *nucleation and growth*, *coalescence and breakup* of droplets, *rising bubbles* & *falling droplets*, *Marangoni flows*, *Rayleigh-Taylor instability*, *surfactants*, *Ostwald ripening* and so on. Those phenomena occur in the daily life as well as in industrial problems. The first example described in :bdg-ref-primary-line:`Nuclear-Glass` is the *nuclear glass* which is used to confine radioactive wastes. We can also mention the *corium* in the context of severe accident of nuclear core reactors, *microfluidics* and *flow and transport in porous media*. Some of them are purely problems of fluid dynamics (rising bubbles or Rayleigh-Taylor instability). But others require a coupling between Navier-Stokes equations and thermodynamics.

   .. tab-item:: Mathematical models

      .. admonition:: :mediumbold:`Mathematical models: phase-field theory`
   
         To be thermodynamically-consistent and capture the interface between phases, we use the **phase-field theory** (see :bdg-ref-primary-line:`Basic-Concepts-Phase-Field-Theory`) to derive the mathematical phase-field models (:math:`\varphi`-models).

         - For hydrodynamic phenomena of two immiscible fluids such as *Rayleigh-Taylor instability*, *rising bubbles*, *splashing droplets*, *capillary wave* etc., the interface is captured by the Conservative Allen-Cahn model (or *conservative levelset equation*) which is coupled with the incompressible Navier-Stokes equations.
   
         - For thermodynamic phenomena such as *spinodal decomposition*, *Ostwald ripening*, *solid-liquid* phase change, the mathematical models are derived from the phase-field theory (:math:`\varphi`-theory). Those models can be coupled with hydrodynamic equations in their incompressible formulation, or low Mach formulation (see :bdg-ref-primary-line:`Model_NSK_Course`).

         .. only:: titania
   
            - A complete presentation can be found in :bdg-link-warning-line:`CEA INSTN Course of two-phase flows with phase-field models <file:///home/lbm-saclay/PDF/COURS-SORBONNE_UM5MEE32_CFD-DIPHASIQUE_PARTIE2_CARTALADE.pdf>`. In this course, basic of thermodynamics, free energy functional, derivation of constitutive laws, and all proofs of equivalence between potential form and conservative forms of surface tension force, etc.

   .. tab-item:: Lattice Boltzmann Methods

      .. admonition:: :mediumbold:`Numerical schemes: Lattice Boltzmann Methods and C++ implementation`

         The *Lattice Boltzmann Equation* (LBE) is one discretization (among other) of the continuous Boltzmann equation in the kinetic theory of gases (see :bdg-ref-primary-line:`Basic-LBM`). The Lattice Boltzmann Methods (**LBM**) are a set of numerical methods, based on that LBE, used as solver of Navier-Stokes equations and other conservative Partial Derivative Equations (PDEs). It is an alternative method to classical approaches for CFD such as finite element or finite volume methods. Its main advantage is to simulate simply different versions of Navier-Stokes equations (incompressible and low Mach formulations) and run efficiently on supercomputers. In this documentation, the section :bdg-ref-primary-line:`LBM-Saclay-Schemes` describes the LB methods which are implemented in LBM_Saclay.
         LBM is a powerful method which is very efficient on Graphics Processing Units (GPUs). LBM_Saclay developers program neither in ``cuda`` (for Nvidia GPUs) nor ``opencl`` but in C++ standard language. With a simple modification of ``cmake`` options, the code can be compiled either on CPU architectures or on GPU devices (see :bdg-ref-primary-line:`Quick-Start`). The Kokkos library is used for the portability of LBM_Saclay. You will find in :bdg-ref-primary-line:`Guidelines` what you need to implement your own initial conditions or source terms. Tutorials are also under progress for more advanced programmers who wish to develop new kernels with new ``setup_collider`` functions.

   .. tab-item:: Simulations

      .. admonition:: :mediumbold:`Simulations: Multi-Phase and Multi-Component flows`

         LBM_Saclay can simulate Multi-Phase and Multi-Component (**MPMC**) flows such as *binary demixing*, *buyoancy and coalescence of bubbles*, *Rayleigh-Taylor instability*, *liquid-gas phase change*, etc. A quick look of those phenomena is presented on :numref:`target-Fig-Approach`. Other examples are given in each subsection of :bdg-ref-primary-line:`Math-Models` which describe the PDEs of each model and their closure relationships. The phase-field models that are implemented in LBM_Saclay, are based on different forms of Cahn-Hilliard and Allen-Cahn equations which are modified and adapted to problems to simulate e.g. *crystal growth*, *dissolution of porous media*, *liquid-vapor phase change*, etc.
      
   .. tab-item:: ToC

      .. admonition:: :mediumbold:`Table of content`

         .. dropdown:: Table of Content of this introduction
            :icon: comment
            :open:

            .. toctree::
               :maxdepth: 1

               src_doc/00_INTRODUCTION/Simulation_with_LBM.rst
               src_doc/00_INTRODUCTION/Context_Motivation.rst
               src_doc/00_INTRODUCTION/TEAM/Team_Presentation.rst
               src_doc/00_INTRODUCTION/TEAM/List-Of-Publications.rst
               src_doc/00_INTRODUCTION/contribute.rst


.. _target-Fig-Approach:
   
.. figure:: ./src_doc/FIGS/Overview_Approach.png
   :name: the-lpn-logo
   :alt: The Li-Pro.Net logo.
   :figclass: align-center
   :align: center
   :height: 460
   :width: 920
   :scale: 100 %
      
   Examples of two-phase flows simulated with LBM

.. admonition:: :mediumbold:`LBM_Saclay workforce`

   .. figure:: src_doc/FIGS/Logos_LBM_Saclay/Logo-Workforce_LBM_Saclay.png
      :class: align-left
      :height: 300
      :width: 300
      :scale: 40

   Many CEA collaborators have contributed to the development and validation of LBM_Saclay: P. Kestener, W. Verdier, T. Boutin, E. Stavropoulos-Vasilakis, H. de Gieter, C. Méjanès, T. Duez, H. Keraudren, C. Elharti, S. Dupuy, C. Bardet, S. Cappe, A. Genty, A. Laurens, P. Chavasse-Frétaz, Y. Janson, B. Peiffert, C. Renard, A. Cartalade.

   - :bdg-ref-primary-line:`TeamPresentation`
   - :bdg-ref-primary-line:`List-Of-Publications-with-LBM`


*****************
**Documentation**
*****************
      
.. admonition:: :mediumbold:`Content of this documentation`
   :class: error

   .. figure:: src_doc/FIGS/Logos_LBM_Saclay/Logo_LBM_Saclay_DOC.png
      :class: align-left
      :height: 300
      :width: 300
      :scale: 50
   
   The purpose of this documentation is to establish the link between parameters of input datafiles with mathematical models and numerical schemes. After a short description of :bdg-ref-primary-line:`PARTI`, the two-phase and multi-phase models are detailed in :bdg-ref-primary-line:`Math-Models`. Next, the numerical schemes of those models are described in :bdg-ref-primary-line:`LBM-Saclay-Schemes`. The following section, :bdg-ref-primary-line:`Guidelines`, is aimed at scientists who wish to implement their own models or add new equations. Finally, the last part :bdg-ref-primary-line:`PART-V-Course-Reminders` contains introductions on *basic fluid dynamics*, *lattice Boltzmann methods* and *phase-field theory*.
   
   **Contribute to this documentation**
   
   You will find here :bdg-ref-primary-line:`Contribute-Documentation` all you need to correct and add new sections of this documentation.

   
************************
**PART I: User's guide**
************************

.. admonition:: :mediumbold:`User's guide`
   :class: caution

   .. toctree::
      :maxdepth: 2
   
      src_doc/01_USER_GUIDE/TOC_User-Guide.rst

********************************
**PART II: Mathematical models**
********************************

.. admonition:: :mediumbold:`Mathematical models in LBM_Saclay`
   :class: caution

   .. toctree::
      :maxdepth: 3
   
      src_doc/02_MODELS/models.rst

***************************************
**PART III: Lattice Boltzmann schemes**
***************************************

.. admonition:: :mediumbold:`Lattice Boltzmann schemes in LBM_Saclay`
   :class: caution

   .. toctree::
      :maxdepth: 3
   
      src_doc/03_LBM_Schemes/TOC_LBM_Schemes.rst

**************************************************
**PART IV: Guidelines for developers & Tutorials**
**************************************************

.. admonition:: :mediumbold:`Guidelines for developers`
   :class: caution

   .. toctree::
      :maxdepth: 2
   
      src_doc/04_PROGRAMMING/TOC_Guidelines.rst

.. admonition:: :mediumbold:`Tutorials for developers`
   :class: caution

   .. toctree::
      :maxdepth: 2
   
      src_doc/04_PROGRAMMING/TOC_Tutorials.rst

.. _PART-V-Course-Reminders:

*********************************************
**PART V: Reminders of fundamental concepts**
*********************************************

.. admonition:: :mediumbold:`Lattice Boltzmann Methods`
   :class: hint

   .. toctree::
      :maxdepth: 2
   
      src_doc/05_COURSES/Course_LBM/TOC_LBM_Course.rst

.. admonition:: :mediumbold:`Phase-field (or diffuse interface) theory`
   :class: hint
   
   .. toctree::
      :maxdepth: 2

      src_doc/05_COURSES/Course_PF/TOC_Phase-Field.rst

   .. toctree::
      :maxdepth: 2

      src_doc/05_COURSES/Thermo-PhaseTransition/TOC_PhaseField_For_PhaseTransition.rst


.. admonition:: :mediumbold:`Appendices`
   :class: note

   .. toctree::
      :maxdepth: 2

      ./src_doc/05_COURSES/Course_Fluid_Dyn/TOC_Fluid-Dyn.rst
      ./src_doc/05_COURSES/Course_Intro-Two-Phase/TOC_Two-Phase_Intro.rst
   

.. sectionauthor:: Alain Cartalade
   