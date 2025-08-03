.. _Model_GPMixtTernary:

Model of gel maturation
^^^^^^^^^^^^^^^^^^^^^^^

The model of gel maturation is an example of phase-field model for two phases: solid and liquid and three compositions (ternary system). In section ``[lbm]``, the kernel is activated with the keyword ``problem=ternary_GP_mixt``. In the rest of this section, the mathematical model and input parameters are described for model option ``model=two_dilute``.

Mathematical model
------------------

In this model we are concerned with the diffusion of three components :math:`A`, :math:`B` and :math:`C` of compositions :math:`C_A`, :math:`C_B` and :math:`C_C`. The compositions are conserved and the following relationship holds:

.. math::
   :label: Total_Conservation
   
   C_{A}+C_{B}+C_{C}=1

**Phase-field equation**

The phase-field model is derived from the grand-potential functional with dilute assumption for composition equations. The solid phase is indicated by :math:`\phi=0` and the liquid phase by :math:`\phi=1`. The phase field equation writes:

.. math::
   :label: PF_Eq
   
   \tau\frac{\partial\phi}{\partial t}=W^{2}\boldsymbol{\nabla}^{2}\phi-\omega_{dw}^{\prime}(\phi)-\lambda p^{\prime}(\phi)\Delta\omega(\boldsymbol{\mu})
   
where :math:`\tau` is the relaxation time, :math:`W` is the interface width, :math:`\omega_{dw}^{\prime}(\phi)` is the derivative of the double-well potential with respect to :math:`\phi` which is defined by

.. math::
   :label: Double_Well
   
   \omega_{dw}(\phi)=8\phi^{2}(1-\phi)^{2}
   
:math:`\lambda` is the coupling parameter, :math:`p^{\prime}(\phi)` is the derivative of an interpolation function with respect to :math:`\phi`:
   
.. math::
   :label: Interpolation_p
   
   p(\phi)=\phi^{2}(3-2\phi)
   

and :math:`\Delta\omega(\boldsymbol{\mu})` is defined by

.. math::
   :label: Def_Delta_Omega
   
   \Delta\omega(\boldsymbol{\mu})=
   
Let us notice that the parameters :math:`\tau` can be expressed by thermodynamic properties (e.g. height of double-well and coefficient in factor of :math:`\delta\Omega/\delta\phi`). Finally in the ``.ini`` input file, the usual parameters :math:`W`, :math:`\lambda` and :math:`M_{\phi}` are set.

**Composition equations**

.. math::
   :label: Eq_Compos_A
   
   \frac{\partial C_{A}}{\partial t}=\boldsymbol{\nabla}\cdot\left[D_{A}(\phi)C_{A}\boldsymbol{\nabla}\mu_{A}\right]
   
.. math::
   :label: Eq_Compos_B
   
   \frac{\partial C_{B}}{\partial t}=\boldsymbol{\nabla}\cdot\left[D_{B}(\phi)C_{B}\boldsymbol{\nabla}\mu_{B}\right]

where for each specie, the diffusion coefficient is interpolated by the bulk coefficients of each phase (solid and liquid):

.. math::
   :label: Diffusion_Coeff
   
   D_{\alpha}(\phi)=\phi D_{\alpha}^l+(1-\phi)D_{\alpha}^s
   
for :math:`\alpha=A,B`.

The last composition is obtained by Eq. :eq:`Total_Conservation`

.. math::
   :label: Eq_Compos_C

   C_{C}=1-C_{A}-C_{B}
   
**Chemical potentials**

.. math::
   :label: Eq_ChemPot_A
   
   \mu_{A}=\log\left[\frac{C_{A}}{\phi e^{-\epsilon_{A}^{l}}+(1-\phi)e^{-\epsilon_{A}^{s}}}\right]
   
.. math::
   :label: Eq_ChemPot_B
   
   \mu_{B}=\log\left[\frac{C_{B}}{\phi e^{-\epsilon_{B}^{l}}+(1-\phi)e^{-\epsilon_{B}^{s}}}\right]


List of input parameters in ``.ini`` file
-----------------------------------------

One example of input file for that model is ``settings_ternary_instantaneous_diffusion.ini``. We describe below the content of that file where the sections ``[lbm]``, ``[params]``, ``[ccparams]`` and ``[init]`` must be wisely set.

**1. Section** ``[lbm]``

To simulate that mathematical model, put the following options in section ``[lbm]``
   
- use the keyword ``problem=ternary_GP_mixt`` 
- use the keyword ``model=two_dilute``
   

**2. Section** ``[params]``

The list of parameters are summarized in Table below.
   
   
   Phase-field parameters

   +----------------------------------------------+--------------------------------------+---------------------------+-------------------+
   |                                              |                                      |                           |                   |
   +==============================================+======================================+===========================+===================+
   | **Math symbol**                              | **Parameter name**                   | **Equation**              | ``.ini`` **file** |
   +----------------------------------------------+--------------------------------------+---------------------------+-------------------+
   | :math:`M_{\phi}`                             | Mobility of interface                | Eq. :eq:`PF_Eq`           | ``Mphi``          |
   +----------------------------------------------+--------------------------------------+---------------------------+-------------------+
   | :math:`W`                                    | Interface width                      | Eq. :eq:`PF_Eq`           | ``W``             |
   +----------------------------------------------+--------------------------------------+---------------------------+-------------------+
   | :math:`\lambda`                              | Coupling parameter                   | Eq. :eq:`PF_Eq`           | ``lambda``        |
   +----------------------------------------------+--------------------------------------+---------------------------+-------------------+   

   Diffusion parameters
   
   +---------------------------+---------------------------------------------------------+---------------------------+-------------------+
   |                           |                                                         |                           |                   |
   +===========================+=========================================================+===========================+===================+
   | **Math symbol**           | **Parameter name**                                      | **Equation**              | ``.ini`` **file** |
   +---------------------------+---------------------------------------------------------+---------------------------+-------------------+
   | :math:`\epsilon_{A}^{l}`  | Bulk energy of liquid phase for specie :math:`A`        | Eq. :eq:`Eq_ChemPot_A`    | ``elA``           |
   +---------------------------+---------------------------------------------------------+---------------------------+-------------------+
   | :math:`\epsilon_{A}^{s}`  | Bulk energy of solid phase  for specie :math:`A`        | Eq. :eq:`Eq_ChemPot_A`    | ``esA``           |
   +---------------------------+---------------------------------------------------------+---------------------------+-------------------+
   | :math:`\epsilon_{B}^{l}`  | Bulk energy of liquid phase for specie :math:`B`        | Eq. :eq:`Eq_ChemPot_B`    | ``elB``           |
   +---------------------------+---------------------------------------------------------+---------------------------+-------------------+
   | :math:`\epsilon_{B}^{s}`  | Bulk energy of solid phase  for specie :math:`B`        | Eq. :eq:`Eq_ChemPot_B`    | ``esB``           |
   +---------------------------+---------------------------------------------------------+---------------------------+-------------------+
   | :math:`\epsilon_{C}^{l}`  | Bulk energy of liquid phase for specie :math:`C`        | Eq.                       | ``elC``           |
   +---------------------------+---------------------------------------------------------+---------------------------+-------------------+
   | :math:`\epsilon_{C}^{s}`  | Bulk energy of solid phase  for specie :math:`C`        | Eq.                       | ``esC``           |
   +---------------------------+---------------------------------------------------------+---------------------------+-------------------+
   | :math:`D_{A}^l`           | Bulk diffusion of specie :math:`A` in liquid phase      | Eq. :eq:`Diffusion_Coeff` | ``DA1``           |
   +---------------------------+---------------------------------------------------------+---------------------------+-------------------+
   | :math:`D_{A}^s`           | Bulk diffusion of specie :math:`A` in solid phase       | Eq. :eq:`Diffusion_Coeff` | ``DA0``           |
   +---------------------------+---------------------------------------------------------+---------------------------+-------------------+
   | :math:`D_{B}^l`           | Bulk diffusion of specie :math:`B` in liquid phase      | Eq. :eq:`Diffusion_Coeff` | ``DB1``           |
   +---------------------------+---------------------------------------------------------+---------------------------+-------------------+
   | :math:`D_{B}^s`           | Bulk diffusion of specie :math:`B` in solid phase       | Eq. :eq:`Diffusion_Coeff` | ``DB0``           |
   +---------------------------+---------------------------------------------------------+---------------------------+-------------------+
   
**3. Section** ``[ccparams]``

``cc`` means *composantes connexes*. In this section six options can be set:

- ``use_connected_components=``: ``yes`` or ``no``
- ``print_cc_trace=``          : ``yes`` or ``no``
- ``CC_phi_threshold=``        : real value
- ``apply_virtual_volume=``    : ``yes`` or ``no``
- ``virtual_volume=``          : real value
- ``virtual_volume_boundary=`` : real value

**4. Section** ``[init]``

Example of initialization for ``init_type=perco``

- ``init_type=``: keyword. Here ``perco``
- ``initClA=``: positive real value
- ``initClB=``: positive real value
- ``initCsAA=``: positive real value
- ``initCsAB=``: positive real value
- ``initCsBA=``: positive real value
- ``initCsBB=``: positive real value

- ``read_data_phi=``: ``yes`` or ``no``
- ``file_data_phi=``: filename.dat (format i,j,k,value). See example ``init_data_perco.dat``
