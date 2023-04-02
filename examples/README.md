# Examples

## discord.py

### subclassed_bot.py

This shows an example of a bot that subclasses the `discord.ext.commands.Bot`
client. This is my recommended way to developing your bot. You can read more on
the official documentation
[here](https://discordpy.readthedocs.io/en/latest/ext/commands/index.html).

The `commands` directory and `commands/ping.py` file show you how you would
create a working command with the bot.

### classless_bot.py

This shows how you would integrate `cogwatch` into the simpler, non-subclassed
bot.

## Other Libraries

You can check out the [integrations](/integrations) directory to see how
`cogwatch` is used in a specific library. For the most part, though, these
should be mostly the same.
