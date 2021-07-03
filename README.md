# Demo
Demonstrating Some Python Features and Documentation Examples.

## Requirements
- Python 3.7+
- [pipenv](https://pipenv.pypa.io/en/latest/install/#installing-pipenv): python dependency manager
- [pdoc](https://pdoc.dev/): automatically generates code documentation from docstrings
- [pylint](https://www.pylint.org): helps maintain code quality

## Developers

### Setup
1. Clone this repo.
2. Create a virtual environment with Python 3.7+. I use pyenv, if you use conda it's `conda create --name demo python=3.7`
3. I use pipenv (You can install via `pip install pipenv`) to manage my python dependencies. If you use pipenv, you'll see a Pipfile available for you to run: `pipenv install --dev` in the directory containing the Pipfile (i.e. the top-level directory of this repo)
4. Launch the environment with `pipenv shell`
5. Navigate to the `src` directory and run "run_pipeline.py": `python run_pipeline.py`

## Making Updates
1. Please ensure you have properly commented your code and added docstrings!
2. Run pylint and don't move forward until your code has a rating above 8.5: `pylint src`
3. Update the documentation and code documentation: `pdoc --html src --output-dir docs`
4. Make a local commit with a descriptive message
5. Push to remote! 
