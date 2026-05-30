.. _Contribute-Documentation:

Contribution guidelines for this documentation
**********************************************

Install Sphinx on your computer
-------------------------------

.. admonition:: Install Sphinx on your computer

    .. dropdown:: Ubuntu 22.04

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

    .. dropdown:: Ubuntu 24.04
        :open:

        On ubuntu 24.04, if ``pip`` command does not work, follow, the instructions below:

         .. code-block:: shell

            $ mkdir -p ~/.venvs
            $ python3 -m venv ~/.venvs/sphinx
            $ ~/.venvs/sphinx/bin/python -m pip install git+https://github.com/sphinx-doc/sphinx
            $ ~/.venvs/sphinx/bin/python -m pip install sphinx-design
            $ ~/.venvs/sphinx/bin/python -m pip install myst-parser
            $ ~/.venvs/sphinx/bin/python -m pip install sphinx_rtd_theme
            $ ~/.venvs/sphinx/bin/python -m pip install sphinxcontrib-bibtex
            $ ~/.venvs/sphinx/bin/python -m pip install sphinx-pdf-generate

        Add in your ``.bashrc`` file the path to Sphinx

         .. code-block:: shell

            export PATH=~/.venvs/sphinx/bin:$PATH

        Check your version of Sphinx :

         .. code-block:: shell

            $ sphinx-build --version

Get the source files of LBM_Saclay's documentation
--------------------------------------------------

.. admonition:: Get source files of LBM_Saclay's documentation

    Get the source files 

        .. code-block:: shell

            $ git clone git@github.com:cea-lbm-saclay/LBM_Saclay_Documentation.git

    Go to the directory ``doc``

        .. code-block:: shell

            $ cd LBM_Saclay_Documentation/doc

    Add the directory path of your local Sphinx in the configuration file ``conf.py``:

        .. code-block:: ruby

            sys.path.insert(0, os.path.abspath('~/.venvs/sphinx/lib/python3.12/site-packages'))

.. admonition:: Generate the html pages on your local computer

    The main file is ``index.rst`` in the directory ``LBM_Saclay_Documentation/doc``. All other source files (``.rst`` files) of LBM_Saclay documentation are the in directory ``LBM_Saclay_Documentation/doc/src_doc/``.

    Compile

        .. code-block:: shell

            $ cd LBM_Saclay_Documentation/doc
            $ make html

    Open in google-chrome

        .. code-block:: shell

            $ google-chrome ~/LBM_Saclay_Documentation/doc/_build/html/index.html&

Write your documentation
------------------------

.. admonition:: Write your documentation
    :class: error
    
    **Write your** ``.rst`` **files**

    The main file is ``index.rst`` in the folder ``LBM_Saclay_Documentation/doc``. All other ``.rst`` files are contained in ``src_doc``. Edit them, add new ``.rst`` files, compile and visualize your modifications (``make html``).

    - To write your  ``.rst`` files see :bdg-link-success-line:`Sphinx doc <https://www.sphinx-doc.org/en/master/usage/index.html>`
    - To write equations with Sphinx see :bdg-link-success-line:`Math with Sphinx <https://sphinx-rtd-trial.readthedocs.io/en/latest/ext/math.html>`
    - For references see :bdg-link-success-line:`BibTeX with Sphinx <https://pypi.org/project/sphinxcontrib-bibtex/>`
    - For badges, buttons and icons, see :bdg-link-success-line:`Sphinx design <https://sphinx-design.readthedocs.io/en/latest/index.html>`

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
    
    and put them in folder ``LBM_Saclay_Documentation/doc/_static/``


Push your improvements
----------------------

If your modifications are brought on the GitHub version, don't forget to create a new branch and push your addings (see :bdg-ref-primary:`Git-Commands`).

.. sectionauthor:: Alain Cartalade
    