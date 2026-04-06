Beamer presentation with LyX and CEA template
=============================================

Lyx and all LaTeX packages must be installed on your computer:

   .. code-block:: shell

      $ sudo apt install lyx
      $ sudo apt install texlive-full


.. admonition:: Configuration for using CEA Beamer template with LyX

   1. Copy in your ``/home/yourlogin`` the folder ``texmf`` contained in the directory ``/home/lbm-saclay/INTERN-START/``:

    .. code-block:: shell

       $ cp -r /home/lbm-saclay/INTERN-START/texmf ~/.

   2. Copy two files ``Beamer-CEA-2023.module`` and  ``beamer-easy.module`` in your directory ``~/.lyx/layouts``

    .. code-block:: shell

       $ cp -r /home/lbm-saclay/INTERN-START/LyX-Layout/layouts ~/.lyx/.

   3. Reconfigure LyX:

      In ``Tools`` clic on ``Reconfigure``

.. admonition:: Make your presentation
   :class: error

   To make your own presentation, follow the LyX file example ``Template-LyX-Presentation.lyx`` given in the directory ``/home/lbm-saclay/INTERN-START/Template-LyX-Presentation/``

