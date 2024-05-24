=============
CompChemUtils
=============

CompChemUtils is a set of tools for computational chemistry workflows.

Requirements
============

* Python_ 3.10 or later
* Click_ (package for command line interfaces)
* NumPy_ (N-dimensional array package)
* SciPy_ (library for scientific computing)
* ASE_ (tools for atomistic simulations)

.. _Python: https://www.python.org
.. _Click: https://click.palletsprojects.com/en/8.1.x/
.. _NumPy: https://numpy.org
.. _SciPy: https://scipy.org
.. _ASE: https://wiki.fysik.dtu.dk/ase/index.html

Installation
============

::

    $ pip install comp-chem-utils

or, if you use poetry::

    $ poetry add comp-chem-utils

You can also install the in-development version with::

    $ pip install git+ssh://git@gitlab.com:ugognw/python-comp-chem-utils.git

or, similarly::

    $ poetry add git+ssh://git@gitlab.com:ugognw/python-comp-chem-utils.git


Documentation
=============


https://python-comp-chem-utils.readthedocs.io/en/latest


Testing
===========

To run all the tests run::

    $ nox

Note, to combine the coverage data from all the nox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            nox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append nox


Examples
========

Determine whether a water molecule is symmetric with respect to a 180 degree rotation about its secondary orientation axis.

>>> from ase.build import molecule
>>> from ccu.structure.axisfinder import find_secondary_axis
>>> from ccu.structure.symmetry import Rotation, RotationSymmetry
>>> h2o = molecule('H2O')
>>> axis = find_secondary_axis(h2o)
>>> r = Rotation(180, axis)
>>> sym = RotationSymmetry(r)
>>> sym.check_symmetry(h2o)
True

Retrieve reaction intermediates for the two-electron CO2 reduction reaction.

>>> from ccu.adsorption.adsorbates import get_adsorbate
>>> cooh = get_adsorbate('COOH_CIS')
>>> cooh.positions
array([[ 0.        ,  0.        ,  0.        ],
       [ 0.98582255, -0.68771934,  0.        ],
       [ 0.        ,  1.343     ,  0.        ],
       [ 0.93293074,  1.61580804,  0.        ]])
>>> ocho =  get_adsorbate('OCHO')
>>> ocho.positions
array([[ 0.        ,  0.        ,  0.        ],
       [ 1.16307212, -0.6715    ,  0.        ],
       [ 0.        ,  1.343     ,  0.        ],
       [-0.95002987, -0.5485    ,  0.        ]])

Place adsorbates on a surface (namely, "Cu-THQ.traj") while considering the symmetry of the adsorbate and the adsorption sites.::

    $ ccu adsorption place-adsorbate CO Cu-THQ.traj orientations/


Enable Shell Completion
=======================

Add this to your ~/.bashrc:::

    eval "$(_CCU_COMPLETE=bash_source ccu)"

Add this to ~/.zshrc:::

    eval "$(_CCU_COMPLETE=zsh_source ccu)"

Add this to ~/.config/fish/completions/ccu.fish:::

    eval (env _CCU_COMPLETE=fish_source ccu)
