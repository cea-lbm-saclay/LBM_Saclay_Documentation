.. LBM_Saclay documentation master file, created by
   sphinx-quickstart on Fri Oct 11 13:14:51 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. raw:: html

    <style> .red {color:red} </style>

.. role:: red

.. raw:: html

    <style> .blue {color:blue} </style>

.. role:: blue

.. raw:: html

    <style> .green {color:green} </style>

.. role:: green

Contribution guidelines
***********************

On your computer
----------------

#. Install sphinx on your computer

    .. code-block:: shell

       $ sphinx-build --version
       $ pip install sphinxcontrib-bibtex
   
   
    - Sphinx doc see: https://www.sphinx-doc.org/en/master/usage/index.html
    - Math with Sphinx see: https://sphinx-rtd-trial.readthedocs.io/en/latest/ext/math.html
    - BibTeX with Sphinx https://pypi.org/project/sphinxcontrib-bibtex/

#. The source files (``.rst`` files) of LBM_Saclay documentation are in directory ``/home/lbm-saclay/LBM_Saclay_Doc/src_doc/``

#. Compile

    .. code-block:: shell

        $ cd LBM_Saclay_Doc 
        $ make html

#. Open in google-chrome

    .. code-block:: shell

        $ google-chrome /home/lbm-saclay/LBM_Saclay_Doc/_build/html/index.html&

Write your doc
--------------

#. Write your ``.rst`` files

    The main file is ``index.rst`` in the folder ``LBM_Saclay_Doc``. All other ``.rst`` files are contained in ``src_doc``. Edit them, add new ``.rst`` files, compile and visualize your modifications.

#. Write your ``.tex`` files

    Write your documentation directly in LaTeX or with LyX and export it in ``.tex`` format. Next, convert your ``.tex`` files into ``.rst`` files with ``pandoc``:

    .. code-block:: shell

        $ pandoc filename.tex -o filename.rst

    .. warning::
    
        - UTF8 format is required for pandoc. For LyX users, Go to Document > Settings, select the section "Language". Under “Encoding”, select “Other: Unicode (utf8)”.
        - pandoc is not a miraculous converter, the generated ``.rst`` file will require some modification.

#. Convert your videos to ``.webm`` format

    .. code-block:: shell

        $ ffmpeg -i "videoname.avi" -c:v libvpx -b:v 2000k -pix_fmt yuva420p -auto-alt-ref 0 "videoname.webm"
    
    and put them in folder ``LBM_Saclay_Doc/_static/``


Push your improvements
----------------------
