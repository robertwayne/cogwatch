# This file is used for calling scripts through the poetry CLI.

from subprocess import run


def fmt():
    """Runs black on the project source directory. Uses the config defined in `pyproject.toml`."""
    run(['black', 'cogwatch/', 'examples', 'tests'])
