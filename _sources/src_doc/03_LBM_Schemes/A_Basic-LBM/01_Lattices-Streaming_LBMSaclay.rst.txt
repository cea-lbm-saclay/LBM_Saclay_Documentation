.. _Def-Lattices:

Lattices and streaming
----------------------

After discretization of the continuous Boltzmann Equation, the Lattice Boltzmann Equation (LBE) writes

.. math::
   :label: LBE_OmegaColl
   
   f_{i}(\boldsymbol{x}+\boldsymbol{c}_{i}\delta t,t+\delta t)=f_{i}(\boldsymbol{x},t)+\Omega_{i}^{\iota}(f_{i},f_{i}^{eq})+\mathcal{F}_i

where :math:`f_i` is the distribution function, :math:`\Omega_i^{\iota}(f_{i},f_{i}^{eq})` is the collision operator and :math:`\mathcal{F}_i` is the microscopic forcing term. The right-hand side is called the collision stage which is local and explicit. The algorithm is splitted into two main stages: the collision stage and the streaming stage. After the collision, the values are set in the function :math:`f_i^{\star}`:

.. math::
   :label: Collision_Stage
   
   f_i^{\star}(\boldsymbol{x},t)=f_{i}(\boldsymbol{x},t)+\Omega_{i}^{\iota}(f_{i},f_{i}^{eq})+\mathcal{F}_i
   
Once the collision is performed, the streaming stage writes:

.. math::
   :label: Streaming_Stage
   
   f_{i}(\boldsymbol{x}+\boldsymbol{c}_{i}\delta t,t+\delta t)=f_i^{\star}(\boldsymbol{x},t)

Definition of lattices
^^^^^^^^^^^^^^^^^^^^^^

.. important::

   All lattices are defined in the C++ file ``src/LBM_Base_Functor.cpp``. In that file, all 2D or 3D lattices are defined by several functions which implement the weights :math:`w_i`, the moving directions :math:`\boldsymbol{e}_i`, their opposite directions :math:`\boldsymbol{e}_\bar{i}`, the matrix :math:`\boldsymbol{M}` of change of basis and its inverse :math:`\boldsymbol{M}^{-1}`.
   
In the source file ``src/LBM_Base_Functor.cpp``, the functions are:

- ``LBM_Weights``: defines the weights :math:`w_i` in ``w``
- ``LBM_speeds``: defines the moving directions :math:`\boldsymbol{e}_i` in ``E``
- ``LBM_speeds_opposite``: defines the opposite moving directions :math:`\boldsymbol{e}_\bar{i}` in ``Ebar``
- ``Matrix``: defined the matrix :math:`\boldsymbol{M}` and :math:`\boldsymbol{M}^{-1}` for MRT collision in ``M`` and ``Minv``

The index :math:`i=0,...,N_{pop}` where :math:`N_{pop}` depends on the lattice. The elements lattices :math:`w_i`, :math:`\boldsymbol{e}_i`, :math:`\boldsymbol{e}_\bar{i}` and :math:`\boldsymbol{M}` are defined for

- D2Q5
- D2Q9
- D3Q7
- D3Q15
- D3Q19
- D3Q27

The inverse matrix :math:`\boldsymbol{M}^{-1}` is defined only for D2Q9 and D3Q27.


Streaming in LBM_Saclay
^^^^^^^^^^^^^^^^^^^^^^^

The streaming stage occurs after the collision and writes:

.. math::
   :label: Streaming
   
   f_i(\boldsymbol{x}+\boldsymbol{c}_i\delta t,t+\delta t)=f_i^{\star}(\boldsymbol{x},t)
   
where, for one particular direction :math:`i`, the value of the distribution function at position :math:`\boldsymbol{x}` after the collison stage :math:`f_i^{\star}(\boldsymbol{x},t)` is moved to the neighboring node :math:`\boldsymbol{x}+\boldsymbol{c}_i\delta t` at time :math:`t+\delta t`.

.. important::

   The streaming stage in LBM_Saclay is written in the C++ function ``stream`` in the file ``src/kernels/LBMSchemeBase.h``.
   

Definitions of C++ functions
""""""""""""""""""""""""""""

The ``stream`` function splits the streaming into two different functions: the first one, ``stream_alldir``, checks if the displacement is possible and the second one, ``set_ftmp_val``, sets the value of post-collision.

.. code-block:: ruby
   
   template <typename Collider>
   KOKKOS_INLINE_FUNCTION void stream(IVect<dim> IJK,
                                     const Collider &collider) const {
      IVect<dim> IJKs;
      bool can_str;
      for (int ipop = 0; ipop < npop; ++ipop) {
         can_str = stream_alldir(IJK, IJKs, ipop);
         if (can_str) {
            set_ftmp_val(IJKs, ipop, collider.collide(ipop));
         }
      }
   }

An example of function ``stream_alldir`` in 2D is

.. code-block:: ruby
   
   KOKKOS_INLINE_FUNCTION bool stream_alldir(const IVect2 &IJK, IVect2 &IJKs,
                                            int ipop) const {
      const int i = IJK[IX];
      const int j = IJK[IY];
      const int ip = lattice.E[ipop][IX];
      const int jp = lattice.E[ipop][IY];
      IJKs[IX] = i + ip;
      IJKs[IY] = j + jp;
      return (IJKs[IX] >= 0 and IJKs[IX] < params.isize and IJKs[IY] >= 0 and
            IJKs[IY] < params.jsize);
   }
   
Let us notice that the current node is set in the 2D/3D vector ``IJK`` whereas the neighboring node is set in the 2D/3D vector ``IJKs`` (``s`` for stream). Once the stream is checked possible for all directions, the values of post-collision are set with the C++ function ``set_ftmp_val``:

.. code-block:: ruby

   KOKKOS_INLINE_FUNCTION void set_ftmp_val(const IVect2 ijk, int ipop,
                                           real_t val) const {
      f_tmp(ijk[0], ijk[1], ipop) = val;
   }

where the values of :math:`f_i^{\star}` are stored in ``collider.collide(ipop)`` and set in ``f_tmp``. Let us notice again that the neighboring node ``IJKs`` is put in argument.

Call of C++ function ``stream``
"""""""""""""""""""""""""""""""

.. important::
   
   The function ``stream`` is called in the functor ``void operator()`` with first argument ``const TagUpdate`` in the file ``src/kernels/FunctorSheme.h``.

For example, the 2D functor writes:

.. code-block:: ruby

   KOKKOS_INLINE_FUNCTION void operator()(const TagUpdate, const typename std::enable_if<dim_ == 2, int>::type& index) const
    {
        IVect2 IJK = index2coord(index, isize, jsize);

        if (is_in_bounds(IJK)) {
            // compute feq and source terms
            Collider collider = Collider(lattice);
            scheme.setup_collider(tag, IJK, collider);
            // collide and stream
            scheme.stream(IJK, collider);
        }
    }
    
.. sectionauthor:: Alain Cartalade
   