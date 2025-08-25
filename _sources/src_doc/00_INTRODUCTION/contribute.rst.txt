Contribution guidelines
***********************

Install Sphinx on your computer
-------------------------------

.. admonition:: Install Sphinx

    Install sphinx on your computer (see https://www.sphinx-doc.org/en/master/usage/installation.html) and check the version:

        .. code-block:: shell

            $ sphinx-build --version

    Install PyPI packages

        .. code-block:: shell
            
            $ pip install sphinx-design
            $ pip install myst-parser
            $ pip install sphinx_rtd_theme
            $ pip install sphinxcontrib-bibtex
            $ pip install sphinx-pdf-generate

    On ubuntu 24.04, if ``pip`` command does not work, follow, the instructions below:

        .. code-block:: shell

            $ mkdir -p ~/.venvs
            $ python3 -m venv ~/.venvs/sphinx
            $ ~/.venvs/sphinx/bin/python -m pip install sphinx-design
            $ ~/.venvs/sphinx/bin/python -m pip install myst-parser
            $ ~/.venvs/sphinx/bin/python -m pip install sphinx_rtd_theme
            $ ~/.venvs/sphinx/bin/python -m pip install sphinxcontrib-bibtex
            $ ~/.venvs/sphinx/bin/python -m pip install sphinx-pdf-generate

    And add the path of directory in ``conf.py``:

        .. code-block:: ruby

            sys.path.insert(0, os.path.abspath('~/.venvs/sphinx/lib/python3.12/site-packages'))


.. admonition:: Generate the html pages

    The main file is ``index.rst`` in the directory ``/home/lbm-saclay/LBM_Saclay_Documentation/``. All other source files (``.rst`` files) of LBM_Saclay documentation are the in directory ``/home/lbm-saclay/LBM_Saclay_Documentation/src_doc/``.

    Compile

        .. code-block:: shell

            $ cd LBM_Saclay_Documentation
            $ make html

    Open in google-chrome

        .. code-block:: shell

            $ google-chrome /home/lbm-saclay/LBM_Saclay_Documentation/_build/html/index.html&

Write your documentation
------------------------

.. admonition:: Write your documentation
    :class: error
    
    **Write your** ``.rst`` **files**

    The main file is ``index.rst`` in the folder ``LBM_Saclay_Documentation``. All other ``.rst`` files are contained in ``src_doc``. Edit them, add new ``.rst`` files, compile and visualize your modifications.

    - Sphinx doc see: https://www.sphinx-doc.org/en/master/usage/index.html
    - Math with Sphinx see: https://sphinx-rtd-trial.readthedocs.io/en/latest/ext/math.html
    - BibTeX with Sphinx https://pypi.org/project/sphinxcontrib-bibtex/
    - Sphinx desing: https://sphinx-design.readthedocs.io/en/latest/index.html

    **Write your** ``.tex`` **files**

    Write your documentation directly in LaTeX or with LyX and export it in ``.tex`` format. Next, convert your ``.tex`` files into ``.rst`` files with ``pandoc``:

        .. code-block:: shell

            $ pandoc filename.tex -o filename.rst

    .. grid:: 1

        .. grid-item-card:: Warning with pandoc
    
            - UTF8 format is required for pandoc. For LyX users, Go to Document > Settings, select the section "Language". Under “Encoding”, select “Other: Unicode (utf8)”.
            - pandoc is not a miraculous converter, the generated ``.rst`` file will require some modification.

    **Convert your videos to** ``.webm`` **format**

        .. code-block:: shell

            $ ffmpeg -i "videoname.avi" -c:v libvpx -b:v 2000k -pix_fmt yuva420p -auto-alt-ref 0 "videoname.webm"
    
    and put them in folder ``LBM_Saclay_Doc/_static/``


Push your improvements
----------------------

If your modifications are brought on the GitHub version, don't forget to create a new branch and push your addings.