Get information on Graphic card for Kokkos
------------------------------------------

1. Hardware version (choose)

   - https://en.wikipedia.org/wiki/List_of_Nvidia_graphics_processing_units#RTX_Ax000_series
   - Command ``nvidia-smi --query-gpu=compute_cap --format=csv``
   - Compile https://github.com/NVIDIA/cuda-samples/tree/master/Samples/1_Utilities/deviceQuery ; execute and read info on line "CUDA Capability Major/Minor version number:"

   **Example on MANWE**

   On MANWE, the command

   .. code-block:: shell

      $ nvidia-smi --query-gpu=compute_cap --format=csv

   returns

   .. code-block:: ruby

      compute_cap
      8.6

   Next see item 2. to find out the appropriate option for Kokkos.

2. List of architectures supported by Kokkos (choose)

   - Read top file of ``external/kokkos/Makefile.kokkos``
   - https://kokkos.org/kokkos-core-wiki/keywords.html#gpu-architectures

   **Example on MANWE**

   On web page we see

   .. container:: sphinx-features

      .. table:: Example of web page
         :name: Tab-NameGPU
         :widths: 35, 15, 15, 35
         :align: center
         :width: 70%

         +---------------------------+------------------+------------------------+-------------------+
         | **NVIDIA GPUs**           | **Architecture** | **Compute capability** | **Models**        |
         +===========================+==================+========================+===================+
         |  ...                      | ...              | ...                    | ...               |
         +---------------------------+------------------+------------------------+-------------------+
         | ``Kokkos_ARCH_AMPERE86``  | Ampere           | 8.6                    | A40,A10,A16,A2    |
         +---------------------------+------------------+------------------------+-------------------+
         |  ...                      | ...              | ...                    | ...               |
         +---------------------------+------------------+------------------------+-------------------+

   We have to use the option ``Kokkos_ARCH_AMPERE86`` for ``cmake``.
     

3. Other examples

   .. container:: sphinx-features

      .. table:: Examples of cmake option
         :name: Tab-NameGPU
         :widths: 35, 15, 15, 35
         :align: center
         :width: 70%

         +---------------------------+----------+------------------+-------------------------------+
         | **Supercomputers (2024)** | **GPU**  | **Manufacturer** | **cmake option**              |
         +===========================+==========+==================+===============================+
         | Jean-Zay / Orcus          | V100     | nvidia           | ``-DKokkos_ARCH_VOLTA70=ON``  |
         +---------------------------+----------+------------------+-------------------------------+
         | Topaze / Orcus            | A100     | nvidia           | ``-DKokkos_ARCH_AMPERE80=ON`` |
         +---------------------------+----------+------------------+-------------------------------+
         | Jean-Zay / Orcus          | H100     | nvidia           | ``-DKokkos_ARCH_HOPPER90=ON`` |
         +---------------------------+----------+------------------+-------------------------------+
         | Adastra                   | MI250X   | AMD              | ``-DKokkos_ARCH_AMD_GFX90A``  |
         +---------------------------+----------+------------------+-------------------------------+
     
.. sectionauthor:: Alain Cartalade