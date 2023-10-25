## Usage

To run the example code

    hooked-on-hooks/demo$ $ poetry shell
    (demo-py3.12)hooked-on-hooks/demo$ poetry install
    (demo-py3.12)hooked-on-hooks/demo$ python demo/pre_commit_magic_needed.py 4

Follow the steps in the develop guide and see how the formatting is chaging. Even though the code ran!

## Develop

We use `pre-commit` for standardizing our coding format. You need to enable the hooks before first time usage

    (demo-py3.12)hooked-on-hooks/demo$ pre-commit install

Now the pre-commit hooks will run automatically each time you try to do a commit

    (demo-py3.12)hooked-on-hooks/demo$ git add .
    (demo-py3.12)hooked-on-hooks/demo$ git commit -m "my message"

You can override the run with the `--no-verify` option after a commit message

    (demo-py3.12)hooked-on-hooks/demo$ git add .
    (demo-py3.12)hooked-on-hooks/demo$ git commit -m "my message" --no-verify

Running pre-commit hooks on one file without committing

    (demo-py3.12)hooked-on-hooks/demo$ pre-commit run --files <PATH/TO/FILE>
