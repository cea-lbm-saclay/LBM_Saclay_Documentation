.. _Analytical-Solutions-Two-Phase:

Analytical solutions for two-phase
==================================

Laplace's law
-------------

.. figure:: ../../FIGS/01_FIGS_VALIDATIONS/Laplace-Law.png
   :class: align-left
   :height: 180
   :width: 200
   :scale: 80

The difference between the pressure inside the droplet :math:`P_{in}` and the pressure outside :math:`P_{out}` is equal to

.. math::
   :label: Laplace-Law

   \underbrace{P_{in}-P_{out}}_{\Delta P}=\frac{\sigma}{R}

where :math:`\sigma` is the surface tension and :math:`R` is the droplet radius.

Analytical solution of double-Poiseuille flow
---------------------------------------------

.. math::
   :label: 

   u_{x}(y)=\begin{cases}
      \frac{Gh^{2}}{2\eta_{A}}\left[-\left(\frac{y}{h}\right)^{2}-\frac{y}{h}\left(\frac{\eta_{A}-\eta_{B}}{\eta_{A}+\eta_{B}}\right)+\frac{2\eta_{A}}{\eta_{A}+\eta_{B}}\right] & \mbox{if }0\leq y\leq h\\
      \frac{Gh^{2}}{2\eta_{B}}\left[-\left(\frac{y}{h}\right)^{2}-\frac{y}{h}\left(\frac{\eta_{A}-\eta_{B}}{\eta_{A}+\eta_{B}}\right)+\frac{2\eta_{B}}{\eta_{A}+\eta_{B}}\right] & \mbox{if }-h\leq y\leq0
   \end{cases}

.. _Analytical-Solution-Capillary-Wave-Prosperetti:

Analytical solution of Prosperetti for capillary wave
-----------------------------------------------------

The example of such a study is given by the test case of capillary wave. For that test case, an analytical solution exists [2]_. The objective is to study the influence of mesh on the solution accuracy. The amplitude is

.. math::
   :label: Sol_Prosperetti

   a(t)=\frac{4(1-4\beta)\nu^{2}k^{4}}{8(1-4\beta)\nu^{2}k^{4}+\omega_{0}^{2}}a_{0}\text{erfc}(\nu k^{2}t)^{1/2}+\sum_{i=1}^{4}\frac{z_{i}}{Z_{i}}\left(\frac{\omega_{0}^{2}a_{0}}{z_{i}^{2}-\nu k^{2}}-u_{0}\right)\times\exp[(z_{i}^{2}-\nu k^{2})t]\text{erfc}(z_{i}t^{1/2})

where :math:`\nu` is the kinematic viscosity which is identical for both fluids, :math:`k` is the wave number which is related to the wavelength :math:`\lambda` by :math:`k=2\pi/\lambda`. The coefficient :math:`\beta` is defined by the liquid :math:`\rho_l` and gas :math:`\rho_g` densities:

.. math::
   :label: Def_beta_prosperetti

   \beta=\frac{\rho_{l}\rho_{g}}{(\rho_{l}+\rho_{g})^{2}}

:math:`\omega_0` is the inviscid natural frequency given by

.. math::
   :label: Natural_Freq_Prosperetti

   \omega_{0}=\frac{\rho_{l}-\rho_{g}}{\rho_{l}+\rho_{g}}gk+\frac{\sigma k^{3}}{\rho_{l}+\rho_{g}}

where :math:`g` is the gravity. In the following verifications :math:`g=0`. The :math:`z_i`'s are the four roots of the algebric equation

.. math::
   :label: Eq_zi

   z^{4}-4\beta(k^{2}\nu)^{1/2}z^{3}+2(1-6\beta)k^{2}\nu z^{2}+4(1-3\beta)(k^{2}\nu)^{3/2}z+(1-4\beta)\nu^{2}k^{4}+\omega_{0}^{2}=0

and 

.. math::
   :label: Def_Z1

   Z_{1}=(z_{2}-z_{1})(z_{3}-z_{1})(z_{4}-z_{1})

