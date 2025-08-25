.. _Input-File:

Description of LBM_Saclay input file
====================================

.. important::

    The LBM_Saclay input file is a text file which must have a suffix name ``.ini``.
    
    Several examples of input files are given in the folder ``settings``. To :ref:`Run_Training-LBM`, we recommend to start practicing with the input files of folder ``run_training_lbm`` which give examples of such input files for classical two-phase simulations.

The parameters of input file are gathered in **sections**, their names must be put in brackets.

List of section names: ``[section name]``
----------------------------------------

We distinguish **Generic sections** for input parameters relative to execution (``[run]``), mesh, mpi processes, mathematical problem to simulate and outputs. The **Problem-dependent sections** contain input paramaters depending on the mathematical model to be solved. Finally, several other sections can be turn on for specific models in **Optional sections**.

**Generic sections**

- ``[run]``: lattice name (e.g. ``D2Q9`` or ``D3Q27``) and time management (e.g. :math:`\delta t`)
- ``[mesh]``: number of nodes :math:`n_x`, :math:`n_y`, :math:`n_z`, and positions of domain in :math:`\boldsymbol{x}_{min}` and :math:`\boldsymbol{x}_{max}` where :math:`\boldsymbol{x}=(x,y,z)^T`.
- ``[mpi]``: number of mpi processes :math:`m_x`, :math:`m_y`, :math:`m_z`
- ``[lbm]``: name of problem solved and number of distribution functions
- ``[output]``: information for output files

**Problem-dependent sections**

- ``[equationN]`` where ``N`` is the equation index: boundary conditions and collision operator for equation ``N``
- ``[MRT_NS]``: values of the collision rates for the Multiple-Relaxation-Times collision operator
- ``[init]``: initial conditions for every equation. Depending on problem: :math:`\phi`, :math:`p_h`, :math:`\boldsymbol{u}`, etc.
- ``[params]``: values of parameter for the mathematical model
- ``[params_composition]``: values of parameters for the composition equation

**Optional sections**

- ``[init_solid]``: initial condition for the solid phase :math:`\psi`
- ``[move_solid]``: parameters for a moving solid phase
- ``[contact_angle]``: parameters for contact angles

Those sections are not described here. For details see :ref:`Math-NSAC-Comp-Solid`.


Sections Part I: generic sections
---------------------------------

``[run]``
^^^^^^^^^
- ``lbm_name=``: lattice name. Value: ``D2Q9``, ``D3Q15``, ``D3Q19``, ``D3Q27``
- ``tEnd=``: final time of simulation where ``tEnd`` is a real
- ``nStepmax=``: total numer of time-iterations where ``nStepmax`` is an integer
- ``nOutput=``: output file every ``nOutput`` where ``nOutput`` is an integer
- ``nlog=``: output log file every ``nlog`` where ``nlog`` is an integer
- ``dt=``: time discretization (:math:`\delta t`) where ``dt`` is a real

``[mesh]``
^^^^^^^^^^

Number of nodes

- ``nx=``: number of nodes in :math:`x`-direction. Integer.
- ``ny=``: number of nodes in :math:`y`-direction. Integer.
- ``nz=``: number of nodes in :math:`z`-direction. Integer.

Positions of domain

- ``xmin=``: position of :math:`x_{min}`. Real. May be negative
- ``xmax=``: position of :math:`x_{max}`. Real. Must be greater than :math:`x_{min}`.
- ``ymin=``: position of :math:`y_{min}`. Real. May be negative
- ``ymax=``: position of :math:`y_{max}`. Real. Must be greater than :math:`y_{min}`.
- ``ymin=``: position of :math:`z_{min}`. Real. May be negative
- ``ymax=``: position of :math:`z_{max}`. Real. Must be greater than :math:`z_{min}`.

Boundary conditions

- ``boundary_type_xmin=``: global value for :math:`x_{min}` boundary condition
- ``boundary_type_xmax=``: global value for :math:`x_{max}` boundary condition
- ``boundary_type_ymin=``: global value for :math:`y_{min}` boundary condition
- ``boundary_type_ymax=``: global value for :math:`y_{max}` boundary condition
- ``boundary_type_zmin=``: global value for :math:`z_{min}` boundary condition
- ``boundary_type_zmax=``: global value for :math:`z_{max}` boundary condition

``[lbm]``
^^^^^^^^^

- ``problem=``: name of kernel. Keyword (e.g. ``NSAC_Comp`` for :ref:`Math-NSAC-Comp` or ``NSK``)
- ``model=``: type of model for the problem (.e.g. ``base`` or ``sansGamma`` for ``NSAC_Comp`` kernel)
- ``e2=3.0``: do not change.
- ``fcount=``: number of distribution functions used in the kernel. Kernel dependent (e.g. ``3`` for ``NSAC_Comp`` kernel)

Example

.. admonition:: For training session
    :class: error

    Open one input file with ``gedit``, e.g. ``TestCase10_Rayleigh-Plateau_Sigma1.ini``:

     .. code-block:: shell
      
        $ cd run_training_lbm/TestCase10_Rayleigh-Plateau2D/Sigma1
        $ gedit TestCase10_Rayleigh-Plateau_Sigma1.ini&

    returns

     .. code-block:: ruby

        [run]
        lbm_name=D2Q9
        tEnd=9999000.0
        nStepmax=500001.0
        nOutput=2000
        nlog=50000
        dt=1.0

        [mesh]
        nx=256
        ny=512
        xmin=-128.0
        xmax=128.0
        ymin=0.0
        ymax=512.0

        #choices are "periodic"/"zero_flux"/"antibounceback"
        boundary_type_ymin=zero_flux
        boundary_type_ymax=zero_flux
        boundary_type_xmin=periodic
        boundary_type_xmax=periodic

        [lbm]
        problem=NSAC_Comp
        #model in {base,sansGamma}
        model=base
        e2=3.0
        fcount=3

        ...

    The ``...`` means that other input parameters have to be set in the input file. The list of parameters depends on the mathematical problem (number of equations, initial conditions and paramters) that is simulated. Here the problem name is ``NSAC_Comp`` corresponding to the mathematical :ref:`Math-NSAC-Comp`.


``[mpi]``
^^^^^^^^^

- ``mx=``: number of mpi processes in :math:`x`-direction. Integer.
- ``my=``: number of mpi processes in :math:`y`-direction. Integer.
- ``mz=``: number of mpi processes in :math:`z`-direction. Integer.


.. admonition:: Example
   :class: hint

    .. code-block:: ruby

        [mesh]
        nx=128
        ny=128
        nz=384

        xmin=-64.0
        xmax=64.0
        ymin=-64.0
        ymax=64.0
        zmin=0.0
        zmax=1536.0

        [mpi]
        mx=1
        my=1
        mz=4

    means that the whole computational domain is defined by

    - :math:`\boldsymbol{x}_{1}=(-64,-64,0)`, :math:`\boldsymbol{x}_{2}=(+64,-64,0)`, :math:`\boldsymbol{x}_{3}=(+64,+64,0)`, :math:`\boldsymbol{x}_{4}=(-64,+64,0)`
    - :math:`\boldsymbol{x}_{5}=(-64,-64,1536)`, :math:`\boldsymbol{x}_{6}=(+64,-64,1536)`, :math:`\boldsymbol{x}_{7}=(+64,+64,1536)`, :math:`\boldsymbol{x}_{8}=(-64,+64,1536)`

    The whole domain is decomposed into 4 MPI processes (e.g. 4 graphic cards) in :math:`z`-direction. Each graphic card will handle one subdomain of mesh size indicated in section ``[mesh]``: ``nx=128``, ``ny=128`` and ``nz=384``.

    The total number of computational cells is :math:`N_x=n_x\times m_x`, :math:`N_y=n_y\times m_y`, :math:`N_z=n_z\times m_z`. In that example: ``128x128x1536``.


``[output]``
^^^^^^^^^^^^

- ``write_variables``: list of scalar fields to write in the output files. Keywords.
- ``outputPrefix=``: prefix name for output files. Keywords.
- ``vtk_enabled=``: vtk format for output files (``yes``, ``no``)
- ``hdf5_enabled=``: hdf5 format for output files (``yes``, ``no``)

   +----------------+-------------------------------------+----------------------------------------------------------+
   |                |                                     |                                                          |
   +================+=====================================+==========================================================+
   | **Extension**  | **Description**                     | **Command**                                              |
   +----------------+-------------------------------------+----------------------------------------------------------+
   | ``.vti``       | Format vtk                          | open .vti files in paraview                              |
   +----------------+-------------------------------------+----------------------------------------------------------+
   | ``.h5``        | Format HDF5                         |                                                          |
   +----------------+-------------------------------------+----------------------------------------------------------+
   | ``.xmf``       | Contains list of ``.h5`` file names | open ``.xmf`` file in paraview for visu of ``.h5`` files |
   +----------------+-------------------------------------+----------------------------------------------------------+

For example, the following options

 .. code-block:: ruby

    [output]
    write_variables=vx,vy,rho,phi,composition,pressure
    outputPrefix=TestCase10_Rayleigh-Plateau_Sigma1
    vtk_enabled=no
    hdf5_enabled=yes

means that the output files will have a HDF5 format (extension ``.h5``) with a prefix name ``TestCase10_Rayleigh-Plateau_Sigma1``. The following fields could post-processed with paraview: velocity components :math:`u_x` and :math:`u_y`, density :math:`\rho`, phase-field :math:`\phi`, composition :math:`c` and pressure :math:`p_h`.

Sections Part II: problem-dependent sections
--------------------------------------------

The sections below depend on the mathematical problem simulated: if we want to simulate 3 PDEs, then we need to set for every PDE 1) Boudary conditions and type of collision, 2) Initial conditions and 3) parameter values.

``[equationN]``
^^^^^^^^^^^^^^^

- ``N``: equation number
- ``boundary_type_ymin=``: type of boudary condition for :math:`y_{min}`. Keyword.
- ``boundary_type_ymax=``: type of boudary condition for :math:`y_{max}`. Keyword.
- ``boundary_type_xmin=``: type of boudary condition for :math:`x_{min}`. Keyword.
- ``boundary_type_xmax=``: type of boudary condition for :math:`x_{max}`. Keyword.
- ``collision=``: type of collision for that equation. Keyword.

Example for 3 PDEs, the first PDE is the phase-field, the second one is the Navier-Stokes and the third one is the composition:

    .. code-block:: ruby

        [equation1]
        boundary_type_ymin=zero_flux
        boundary_type_ymax=zero_flux
        boundary_type_xmin=periodic
        boundary_type_xmax=periodic
        collision=BGK

        [equation2]
        boundary_type_ymin=zero_flux
        boundary_type_ymax=zero_flux
        boundary_type_xmin=periodic
        boundary_type_xmax=periodic
        collision=MRT

        [equation3]
        boundary_type_ymin=zero_flux
        boundary_type_ymax=zero_flux
        boundary_type_xmin=periodic
        boundary_type_xmax=periodic
        collision=BGK

    Here the BGK collision operator (``collision=BGK``) is used for phase-field equation (``[equation1]``) and composition equation (``[equation3]``). MRT (``collision=MRT``) is used for Navier-Stokes equations (``[equation2]``).

``[MRT_NS]``
^^^^^^^^^^^^

If the keyword for ``collision`` is ``MRT``, then it is required to add one supplementary section for relaxation collision rates. Example for ``[equation2]``

    .. code-block:: ruby

        [MRT_NS]
        tau0=0.2
        tau1=0.2
        tau2=0.2
        tau3=0.2
        tau4=0.2
        tau5=0.2
        tau6=0.2
        tau7=-1.0
        tau8=-1.0

For phase-field and composition equations, the section names are ``[MRT_AC]`` and ``[MRT_COMP]``.

``[params]``
^^^^^^^^^^^^
In order to set appropriate parameters in this section, is is recommended to start with an existing file in the database ``run_training_lbm``. All values must be dimensionless.

- ``W=``: interface width :math:`W`. Real.
- ``Mphi=``: interface mobility :math:`M_{\phi}`. Real.
- ``counter_term=``: counter term :math:`4M_{\phi}\phi(1-\phi)/W` in the phase-field equation ? yes: ``1.0``, no: ``0.0``
- ``rho0=``: density value of phase 0. Real.
- ``rho1=``: density value of phase 1. Real.
- ``nu0=``: kinetic viscosity value of phase 0. Real.
- ``nu1=``: kinetic viscosity value of phase 1. Real.
- ``sigma=``: surface tension between phases 0 and 1. Real.
- ``gy=``: value of gravity in :math:`y`-direction. Use alternatively ``gx=`` or ``gz=``. Real.
- ``gamma=``: 
- ``lambda=``: coupling parameter in the phase-field equation for phase-change problems. Real.
- ``PF_advec=``: unused.
- ``D0=``: diffusion coefficient in phase 0. Real.
- ``D1=``: diffusion coefficient in phase 1. Real.

For problems where densities are interpolated by composition

- ``rho0_ini=``: initial value of density (phase 0) with :math:`c`. Positive real.
- ``rho0_eq=``: equilibrium value of density (phase 0) with :math:`c`. Positive real.
- ``rho1_ini=``: initial value of density (phase 1) with :math:`c`. Positive real.
- ``rho1_eq=``: equilibrium value of density (phase 1) with :math:`c`. Positive real.

``[params_compos]``
^^^^^^^^^^^^^^^^^^^

- ``mu_eq=0.0``: equilibrium value of chemical potential. Real.
- ``c0_inf=0.02``: initial composition of phase 0. Positive real.
- ``c0_co=0.15``: equilibrium (or coexistence) composition of phase 0. Positive real.
- ``c1_inf=0.15``: initial composition of phase 1. Positive real.
- ``c1_co=0.6``: equilibrium (or coexistence) composition of phase 1. Positive real.

``[init]``
^^^^^^^^^^

- ``init_type=``:
- ``amplitude=``:
- ``hauteur=``:
- ``nombre_onde=``:
- ``longueur_onde=``:
- ``initVX=``:
- ``initVY=``:

.. sectionauthor:: Alain Cartalade
    