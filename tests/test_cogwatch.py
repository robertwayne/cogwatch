import pytest

from cogwatch import Watcher


class ClientMock:
    pass


def test_get_dotted_cog_path():
    c = ClientMock()

    # test the default path
    default_watcher = Watcher(c)
    path = default_watcher.get_dotted_cog_path("/usr/example_bot/commands/cmd.py")

    # test a nested path with duplicate names
    options_watcher = Watcher(c, path="example_bot/commands")
    nested_path = options_watcher.get_dotted_cog_path("/usr/example_bot/example_bot/commands/cmd.py")

    # test deeper nests
    options_watcher.path = "example_bot/even/deeper/commands"
    deep_nested_path = options_watcher.get_dotted_cog_path("/usr/example_bot/example_bot/even/deeper/commands/cmd.py")

    assert path == "commands"
    assert nested_path == "example_bot.commands"
    assert deep_nested_path == "example_bot.even.deeper.commands"


def test_get_dotted_cog_path_input():
    c = ClientMock()
    default_watcher = Watcher(c)

    # test invalid input backslash
    with pytest.raises(ValueError):
        default_watcher.path = r"example_bot\commands"
        default_watcher.get_dotted_cog_path(r"E:\Examples\example_bot\example_bot\commands\cmd.py")

    # test invalid input dotted
    with pytest.raises(ValueError):
        default_watcher.path = "example_bot.commands"
        default_watcher.get_dotted_cog_path(r"E:\Examples\example_bot\example_bot\commands\cmd.py")


def test_get_cog_name():
    c = ClientMock()
    default_watcher = Watcher(c)

    path = "/usr/example_bot/commands/cmd.py"
    cog = default_watcher.get_cog_name(path)

    assert cog == "cmd"
