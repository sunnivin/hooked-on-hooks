## Usage

To run the example code

    $ poetry shell
    (demo-py3.12)$ poetry install
    (demo-py3.12)$ python demo/pre_commit_magic_needed.py 4

## Develop

We use `pre-commit` for standardizing our coding format before your are allowed to push into the `main`-branch. You need to enable the hooks before first time usage

    (demo-py3.12)$ pre-commit install

You can override the run with the `--no-verify` option after a commit message

    (demo-py3.12)$$ git add .
    (demo-py3.12)$$ git commit -m "my message" --no-verify

Running pre-commit hooks on one file which is not committed

    (demo-py3.12)$$ pre-commit run --files <PATH/TO/FILE>
