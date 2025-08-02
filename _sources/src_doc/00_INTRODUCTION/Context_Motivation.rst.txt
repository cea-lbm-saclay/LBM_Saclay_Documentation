Observations in nuclear glass
=============================

Many phenomena of demixing are observed in nuclear glass at CEA of Marcoule. The nuclear glass is a multi-component system which is composed of twenty (or more) chemical species (or components). In this documentation, when one system is composed of two components, it will be qualified of *binary*. When it is composed of three components, it will be qualified of *ternary*. The nuclear glass is an example of multi-component system. At macroscopic scale and high temperature, the nuclear glass is usually considered as a single-phase system. However, for specific conditions of temperature and global composition, several observations show two phases, either liquid/liquid, or solid/liquid. The objective of LBM_Saclay is to model and simulate those phenomena in order to simulate them by varying the temperature and the composition of the system.

**Liquid-Liquid interface**

Demixing phenomena between two liquid phases are observed in nuclear glass such as the *nucleation and growth* (:numref:`target-Fig-Nucleation`) and *spinodal decomposition* (:numref:`target-Fig-Spinodal`). Those phenomena occur at high temperature when the temperature is below a critical temperature (see next section).

.. container:: sphinx-features

   .. _target-Fig-Nucleation:

   .. figure:: ../FIGS/02_FIGS_OBSERVATIONS/Nucleation-Growth.png
      :class: align-center
      :height: 600
      :width: 300
      :scale: 50

      Nucleation and growth (S. Schuller ISEC/DPME, 2013)

   .. _target-Fig-Spinodal:

   .. figure:: ../FIGS/02_FIGS_OBSERVATIONS/SpinodalDecomposition.png
      :class: align-center
      :height: 600
      :width: 400
      :scale: 50

      Spinodal decomposition (D. Bouttes, PhD 2015)

**Solid-Liquid interface**

When the temperature is lowered, a phase solid/liquid change occurs for some species and .*crystal growth* (:numref:`target-Fig-CrystalGrowth`), is observed. Various gemetric shapes are observed. Finally at lower temperature, when glass and water are in contact, a phenomenon of  *gel maturation* (:numref:`target-Fig-Maturation`) is observed.

.. container:: sphinx-features

   .. _target-Fig-CrystalGrowth:

   .. figure:: ../FIGS/02_FIGS_OBSERVATIONS/MEB-Cristaux.png
      :class: align-center
      :height: 400
      :width: 600
      :scale: 50

      Crystal growth (E. Régnier, ISEC/DPME 2011)

   .. _target-Fig-Maturation:

   .. figure:: ../FIGS/02_FIGS_OBSERVATIONS/Maturation-Gel.png
      :class: align-center
      :height: 400
      :width: 600
      :scale: 50

      Maturation of gels (S. Gin, ISEC/DPME 2015)

Thermodynamics
==============

Those phenomena occur because they depend on the thermodynamic and they make appear an interface which separates two or several phases. The thermodynamics of a binary system is sketched on :numref:`target-Fig-BinaryPhaseDiagram`. On that figure, when the temperature :math:`T` is above a critical temperature :math:`T>T_c`, we observe only one phase. But when the temperature is below that critical temperature :math:`T<T_c`, we observe two phases, provided that the point of composition :math:`C` and temperature :math:`T` is within the red curve (binodal line). The demixing can occur into two different regimes: when the composition is inside the black line (spinodal line) the *spinodal* regime is observed, whereas the *nucleation and growth* regime is observed in other cases.

For three components, the phase diagram is much more complicated. It is represented by the Gibbs triangle (:numref:`target-Fig-GibbsTriangle`) where the green lines are the conodes. On that figure, the miscibility gap is the area where the observations confirm the presence of two phases (blue dots).

.. container:: sphinx-features

   .. _target-Fig-BinaryPhaseDiagram:

   .. figure:: ../FIGS/03_FIGS_THERMO/PhaseDiagram.png
      :class: align-center
      :height: 600
      :width: 700
      :scale: 50

      Thermodynamics of phase separation

   .. _target-Fig-GibbsTriangle:

   .. figure:: ../FIGS/03_FIGS_THERMO/GibbsTriangle.png
      :class: align-center
      :height: 600
      :width: 900
      :scale: 50

      Phase diagram of :math:`SiO_2-Na_2O-MoO_3` (S. Bordier, PhD 2015)

.. sectionauthor:: Alain Cartalade