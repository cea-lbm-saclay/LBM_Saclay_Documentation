Beamer presentation with LyX and CEA template
=============================================

Lyx must be installed on your computer and all LaTeX packages:

   .. code-block:: shell

      $ sudo apt install texlive-full


.. admonition:: For training session
   :class: error

   1. Copy in your ``/home/yourlogin`` the folder ``texmf`` contained in the directory ``/home/lbm-saclay/CONFIG/``:

    .. code-block:: shell

       $ cp -r /home/lbm-saclay/CONFIG/texmf ~/.

   2. Copy two files ``Beamer-CEA-2023.module`` and  ``beamer-easy.module`` in your directory ``~/.lyx/layouts``

    .. code-block:: shell

       $ cp -r /home/lbm-saclay/CONFIG/LyX-Layout/layouts ~/.lyx/.

   3. Reconfigure LyX:

      In ``Tools`` clic on ``Reconfigure``

