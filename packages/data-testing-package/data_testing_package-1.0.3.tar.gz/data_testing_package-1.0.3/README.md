# DATA-TESTING-PACKAGE

The data testing package is supported for both Unix-like and Windows OS. The purpose of this repo is to combine all methods that are commonly used for data testing into a single package. 

First, we need to create the virtual environment and install dependencies.
we will be using poetry to manage all our dependencies. 
to install poetry run `pip install poetry`

to create a virtual environment run `poetry install`

To activate virtual environment run `poetry shell`

To come out of your virtual environment run `deactivate`

More information on poetry `https://www.youtube.com/watch?v=0f3moPe_bhk`

You can find the dependencies included in the `pyproject.toml`

To publish a package using poetry: 'https://python-poetry.org/docs/repositories/#configuring-credentials'

To use the published package: Poetry add 'package-name'