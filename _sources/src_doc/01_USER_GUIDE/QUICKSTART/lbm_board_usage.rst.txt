.. _LBM-Board-Usage:

LBM Board: Editing, Run & Post-processing
=========================================

This page continues :bdg-ref-primary-line:`LBM Board: Installation & Launch <LBM-Board>`
(starting the board, the SSH tunnel, pointing it to your ``.ini`` files).

1. Pre-processing: edit your ``.ini``
-------------------------------------

.. admonition:: What the board offers for pre-processing
   :class: important

   - **Kanban view** — the ``.ini`` is displayed as columns by section
     (Config / Physique / …); the parser is **generic**: any section and
     any ``k=v`` key is read, including the keywords of new kernels under
     development (an unknown section simply appears as an « other »
     column — nothing to configure).
   - **Inline editing** — click **✎ Edit**, then click on any value to
     modify it (Enter = validate, Esc = cancel). New keys and new
     sections can be added; a reset (with double confirmation) restores
     the file on disk.
   - **Diff against a reference case** — the **⇆** button next to a file
     in the tree defines the reference; values that differ in the
     displayed case turn **amber**. Typical use: display your case, then
     pick a reference case from ``run_training_lbm/`` as reference and
     see exactly what you changed.
   - **📊 Nb adim** — computed dimensionless numbers (Re, We, Ca, Bo, Pe)
     with the formula of each line, **live**: the values are recomputed
     from the current ``.ini`` at every edit.
   - **🧮 ADIM** — build a case from reference scales (L\*, u\*, δx,
     δt, ρ\*, ν\*, …): the panel is live and cross-linked with 📊 Nb adim
     (mutually exclusive, one closes the other).
   - **📖 Éq / 📐 Domaine** — documentation of the model (equations,
     variables) and of the domain with its boundary conditions.
   - **⬇ .ini export** — downloads a copy of the file with your edits.
     The server never writes your files: it is you who replaces the
     original if you want.

2. Run a computation (▶ Run)
----------------------------

.. admonition:: Local CPU (OpenMP)
   :class: important

   Once your ``.ini`` is ready, the compiled binary
   (``build_omp/build_NSAC_Comp/src/LBM_saclay``, see section 3 of the
   :bdg-ref-primary-line:`Quick-Start <Quick-Start>`) is executed **from
   the case directory**. Recommended: run in the background so that the
   computation survives the terminal closing, with the log in
   ``lbm_run.log`` (the file followed automatically by the 📡 Monitoring
   panel):

      .. code-block:: shell

         $ cd <case directory>          # e.g. ~/run_training_lbm/TestCase01_Poiseuille_Water
         $ nohup ~/LBM_Saclay_Rech-Dev/build_omp/build_NSAC_Comp/src/LBM_saclay TestCase01_Poiseuille_Water.ini > lbm_run.log 2>&1 &

   Follow it live in another terminal: ``tail -f lbm_run.log``.
   Stop: the **■ Stop** button of the ▶ Run panel (double confirmation;
   it creates a ``LBMstop`` file in the case directory and the solver
   stops cleanly at the next time step) or ``kill <pid>`` as a last
   resort.

   The computation must run on the **same machine** as the board, and the
   case directory must be under one of the allowed bases (section 2 of
   :bdg-ref-primary-line:`Installation & Launch <LBM-Board>`).

.. admonition:: ORCUS GPU partitions (Slurm)
   :class: important

   When the board server runs on ORCUS, the ▶ Run panel adds a **🚀
   Slurm** card (the local card is greyed out, and vice versa on MANWE /
   local). **Display only**: the board generates for you the two pieces
   of the Slurm submission — the **``.slurm`` script** and the
   **``sbatch`` command** — but it **submits nothing and writes nothing**:
   you copy the script into the case directory (⧉ button), then paste the
   command in an ORCUS terminal. Two copy-pastes:

      .. code-block:: shell

         # 1) copy the generated script into the case directory (e.g. JOB_ORCUS_H100.slurm)
         # 2) submit:
         $ sbatch /absolute/path/case_directory/JOB_ORCUS_H100.slurm <your_case>.ini

   The three available partitions (1 × GPU per job): **ORCUS V100**
   (``gpuq_v100``), **ORCUS A100** (``gpuq_a100``), **ORCUS H100**
   (``gpuq_h100``); the live state of each partition (🟢/🟡/🔴, free GPU
   count) is read from ``sinfo``. Follow the job with ``squeue -u $USER``
   and cancel it with ``scancel <jobid>`` (the Slurm logs
   ``slurm_%j.out/.err`` are written in the case directory and are found
   by the 📡 Monitoring panel, like ``lbm_run.log``).

   Prerequisite: the matching build (``build_cuda_v100`` /
   ``build_cuda_a100`` / ``build_cuda_h100``) must exist in your ORCUS
   clone (see the :bdg-ref-primary-line:`ORCUS GPU compilation <Simulations-GPU>`
   pages).

3. Monitor a computation (📡 Monitoring)
----------------------------------------

The 📡 Monitoring panel observes a running computation: status, live log
(tail + progress ``nStepmax`` + ETA) and snapshots. It reads the log file
of the case (``lbm_run.log`` by default, or the Slurm logs
``slurm_%j.out/.err`` on ORCUS) — the selector lists the log files found
in the case directory.

4. Post-process the HDF5 outputs (🛠 Post-processing)
-----------------------------------------------------

.. admonition:: For laptop / desktop and clusters
   :class: important

   The 🛠 Post-processing panel analyses the ``.h5`` snapshots of the
   watched case **on the board server** (never in your browser) and
   displays the result directly in the card. The four cards are greyed
   out until the first ``.h5`` snapshot is written (``hdf5_enabled = yes``
   in ``[output]``), and stay greyed with a warning if ``h5py`` is missing
   on the server machine (section 1 of
   :bdg-ref-primary-line:`Installation & Launch <LBM-Board>`):

   - **🛡 Conservation** — relative deviation ``|S(t) − S(t₀)| / S(t₀)``
     of a variable (e.g. ``composition cB``) vs time, with a coloured
     verdict (✅ PASS / ⚠ ALERTE / ❌ ERREUR), a CSV download and the
     tool console;
   - **⏱ Time series** — values of a variable at a point vs time;
   - **📏 1D profile** — profile of a variable along a segment, CSV +
     plot;
   - **🌊 2D field** — live heatmap of a variable: the image refreshes
     itself at each new snapshot written by the computation (no click
     needed). A red banner is displayed if NaN/Inf values are detected,
     which helps locating the divergence zone.

   :octicon:`shield-check;2em;sd-text-success` **Security**: only the
   whitelisted scripts of ``post-processing/`` are allowed, the
   arguments are bounded on the server side, and the computation runs in
   a temporary directory **purged** at the end — nothing is written in
   your case directory.

.. admonition:: Command-line post-processing tools (HDF5)
   :class: important

   The same tools are available as standalone Python scripts in the folder
   ``LBM_Saclay_Rech-Dev/post-processing`` (useful to script a series of
   cases): 1D profiles along a segment, 2D slices of 3D fields, point
   time series, and conservation checks. Run them with the system Python
   (``/usr/bin/python3``), e.g. extract a 1D profile of a variable along a
   segment (grid indices, origin ``(0,0)``) and save a CSV plus a plot:

      .. code-block:: shell

         $ cd LBM_Saclay_Rech-Dev/run_training_lbm/TestCase01_Poiseuille_Water
         $ /usr/bin/python3 ../../post-processing/lbm_extract_profile_h5.py \
             myCase.h5 --var phi -P1 x1,y1 -P2 x2,y2

   List the variables available in a ``.h5`` file with the option
   ``--list``.

.. sectionauthor:: Alain Cartalade
