# This file is used for calling scripts through the poetry CLI.

from subprocess import CalledProcessError, run

libraries = [
    'discord-py',
    'discord.py-message-components',
    'disnake',
    'nextcord',
    'py-cord',
]


def is_installed(library: str) -> bool:
    """Checks to see if a library is installed."""
    try:
        run(['poetry', 'show', library, '--quiet'], check=True)
    except CalledProcessError:
        return False
    else:
        return True


def reset_environment(library: str):
    """Removes all libraries from the poetry environment."""
    print('Resetting test environment...')

    for installed_library in libraries:
        if library == installed_library:
            continue

        run(['poetry', 'remove', installed_library, '--quiet'])

    if not is_installed(library):
        run(['poetry', 'add', library, '--dev', '--quiet'])


def fmt():
    """Runs black on the project source directory. Uses the config defined in `pyproject.toml`."""
    run(['black', 'cogwatch/', 'integrations/', 'examples', 'tests', './'])


def discord4py():
    """Runs the discord.py-message-components integration test."""
    reset_environment('discord.py-message-components')
    run(['poetry', 'run', 'python', 'integrations/discord4py/main.py'])


def discordpy():
    """Runs the discord.py integration test."""
    reset_environment('discord-py')
    run(['poetry', 'run', 'python', 'integrations/discord-py/main.py'])


def disnake():
    """Runs the disnake integration test."""
    reset_environment('disnake')
    run(['poetry', 'run', 'python', 'integrations/disnake/main.py'])


def nextcord():
    """Runs the nextcord integration test."""
    reset_environment('nextcord')
    run(['poetry', 'run', 'python', 'integrations/nextcord/main.py'])


def pycord():
    """Runs the py-cord integration test."""
    reset_environment('py-cord')
    run(['poetry', 'run', 'python', 'integrations/py-cord/main.py'])
