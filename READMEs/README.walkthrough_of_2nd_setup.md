# 2nd walkthrough

## TLDR - walking through how to set up a Python project

Here is how you can setup some files and folders on your computer to start playing around with Python. This time we will incorporate...

- python-poetry (aka Poetry)  *only works with Python 3.7+.
  - for doing package management, package isolation, and script support with an API similar to NPM or bundler
- pytest (test runner) *only works with Python 3.7+.
  - pytest : Python :: jest : Node.js :: rspec : Ruby
- pytest-cov
  - a code coverage reporter - much like Instabul for Node.js or simplecov for Ruby
- add a linter called black `https://black.readthedocs.io/en/stable/`
  - for auto-formatting code like Prettier for Node.js or Rubocop for Ruby
- auto-reloading support via nodemon `https://nodemon.io/`
  - for auto-restarting our project when we change code
- and test debugging support with VSCode
  - an awesome tool for troubleshooting buggy code

### Python

```.sh
python3 --version # 3.10.9 -> 3.10.x
python3 -m pip --version # 22.3.1
```

#### create a tag

### Install Poetry - I installed 1.3.1

```.sh
curl -sSL https://install.python-poetry.org | python3 -
export PATH="/Users/a/.local/bin:$PATH"
poetry --version
poetry completions bash >> ~/.bash_completion
poetry init # will walkthrough initializing poetry integration
```

delete `requirements.txt` as pyproject.toml keeps the record of 3rd party dependencies now

#### create a tag after creating pyproject.toml

### test adding dependencies with poetry

```.sh
poetry add pandas matplotlib # this is like `npm i <PACKAGE_NAME>` or `bundle install <GEM_NAME>`
```

### How to activate/deactivate the virtualenv with poetry

Activate: `poetry shell` - SHIFT + COMMAND + P is VSCode shortcut to check interpreter version
Deactivate: `exit`

#### create a tag before configuring pyproject.toml

### Switched up package name in pyproject.toml because long prompt bothered me

```.toml
[tool.poetry]
name = "venv"
```

### Changed `included` package name to be src in pyproject.toml

```.toml
[tool.poetry]
packages = [{include = "src"}]
```

```.sh
mkdir src
touch src/__init__.py
```

### here's how to install packages from the project dependency list in the pyproject.toml

`poetry install` # this is like `npm install` or `bundle install`

### smoke test main.py

- poetry run python main.py

#### create a tag after smoke testing main.py

### create a script

```.toml
[tool.poetry.scripts]
main = "src:main" # like the `scripts` key in package.json files
```

### populate src folder

- aka move `main.py` to src module

```__init__.py
from . import main # like exporting code out of modules with index.js or index.ts
```

### run script

- poetry run main

#### create a tag after creating a script

## Create a basic test setup

```.sh
poetry add pytest --group dev
poetry add pytest-cov --group dev
poetry install --with dev # how to install dev group packages from the project dependency list in the pyproject.toml
mkdir tests
touch tests/test_example.py
```

### How to write tests with PyTest

any file beginning with `test_` and any function inside of said file beginning with the name `test_` will be scanned for assertions whose results will be reported by PyTest

```test_example.py
def inc(x):
    return x + 1

def dec(x):
    return x - 1

def test_inc():
    assert inc(3) == 4
    assert inc(5) == 6

def test_dec():
    assert dec(5) == 4
```

poetry run pytest
poetry run pytest --cov=src tests/

#### create a tag after running tests

### add the code formatter called black - `https://black.readthedocs.io/en/stable/`

- poetry add black --group dev
- run `poetry shell` and then launch VSCode for virtualenv to be recognized and VSCode to find `black` package
- SHIFT + COMMAND + P is VSCode shortcut to check interpreter version and make sure it is the same version managed by python-poetry
- create `settings.json` file

and add the following to `<PROJECT_ROOT>/.vscode/settings.json`

```.json
{
    "python.analysis.typeCheckingMode": "basic",
    "python.analysis.autoImportCompletions": true,
    "[python]": {
        "editor.formatOnSave": true,
    },
    "python.formatting.provider": "black",
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": false,
    "python.analysis.extraPaths": [
        "."
    ],
    "files.exclude": {
        "**/.git": true
    }
}
```

#### create a tag setting up black

### auto-reloading support via nodemon - `https://nodemon.io/`

- npm init -y
- npm i -D nodemon
- add node_modules to .gitignore
- add the following scripts into the `package.json` file with the following content for the `scripts` key

```.json
"scripts": {
    "test": "nodemon --watch '**/*' -e py --exec poetry run pytest",
    "coverage": "poetry run pytest --cov=src tests/",
    "dev": "nodemon --watch '**/*' -e py --exec poetry run main"
},
```

#### create a tag after adding nodemon

### and finally test debugging support with VSCode

The Python debugger seems to have great integration with debugging with VSCode!

## Next Steps

Now you can take this project and use it to solve many problems you might come across. I will now take it further and develop it into an app for creating Algorand smart contracts. I will do this in another video and we will see how well this development setup fares!
