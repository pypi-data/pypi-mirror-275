# rox-vectors



2D vector classes



## Quick start



1. Init host system with `init_host.sh`. This will build a dev image.
2. Launch in VSCode devcontainer.




## Development


1. develop and test in devcontainer (VSCode)
2. trigger ci builds by bumping version with a tag. (see `.gitlab-ci.yml`)

## Tooling

* Automation: `invoke` - run `invoke -l` to list available commands. (uses `tasks.py`)
* Verisoning : `bump2version`
* Linting and formatting : `ruff`
* Typechecking: `mypy`

## What goes where
* `src/rox_vectors` app code. `pip install .` .
* `tasks.py` automation tasks.
* `.gitlab-ci.yml` takes care of the building steps.


