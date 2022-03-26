<h1 align="center">Cog Watch</h1>
    
<div align="center">
  <strong><i>Automatic hot-reloading for your discord.py command files.</i></strong>
  <br>
  <br>
  
  <a href="https://pypi.org/project/cogwatch">
    <img src="https://img.shields.io/pypi/v/cogwatch?color=0073B7&label=Latest&style=for-the-badge" alt="Version" />
  </a>
  
  <a href="https://python.org">
    <img src="https://img.shields.io/pypi/pyversions/cogwatch?color=0073B7&style=for-the-badge" alt="Python Version" />
  </a>
</div>
<br>

`cogwatch` is a utility that you can plug into your `discord.py` bot that will watch your command
files directory *(cogs)* and automatically reload them as you modify or move them around in
real-time. No more reloading your bot / command yourself every time you edit an embed just to make
sure it looks perfect!

## Features

- Automatically reloads commands in real-time as you edit them *(no !reload <cmdName> needed)*.
- Can handle the loading of all your commands on start-up *(no boilerplate)*.

## Getting Started

You can install the library with `pip install cogwatch`.

Import the `watch` decorator and apply it to your `on_ready` method and let the magic take effect.

See the [examples](https://github.com/robertwayne/cogwatch/tree/master/examples) directory for more
details, as well as an example on how to use the `cog` concept in `dpymenus` if you are unfamiliar
with it.

```python
import asyncio
from discord.ext import commands
from cogwatch import watch


class ExampleBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!')

    @watch(path='commands')
    async def on_ready(self):
        print('Bot ready.')

    async def on_message(self, message):
        if message.author.bot:
            return

        await self.process_commands(message)


async def main():
    client = ExampleBot()
    await client.start('YOUR_TOKEN_GOES_HERE')

if __name__ == '__main__':
    asyncio.run(main())
```

## Configuration

You can pass any of these values to the decorator:

`path='commands'`: Root name of the cogs directory; cogwatch will only watch within this directory -- recursively.

`debug`: Whether to run the bot only when the Python **\_\_debug\_\_** flag is True. Defaults to True.

`loop`: Custom event loop. Defaults to the current running event loop.

`default_logger`: Whether to use the default logger *(to sys.stdout)* or not. Defaults to True.

`preload`: Whether to detect and load all found cogs on start. Defaults to False.

`colors`: Whether to use colorized terminal outputs or not. Defaults to True.

**NOTE:** `cogwatch` will only run if the **\_\_debug\_\_** flag is set on Python. You can read more
about that [here](https://docs.python.org/3/library/constants.html). In short, unless you run Python
with the *-O* flag from your command line, **\_\_debug\_\_** will be **True**. If you just want to
bypass this feature, pass in `debug=False` and it won't matter if the flag is enabled or not.

## Logging

By default, the utility has a logger configured so users can get output to the console. You can
disable this by passing in `default_logger=False`. If you want to hook into the logger -- for
example, to pipe your output to another terminal or `tail` a file -- you can set up a custom logger
like so:

```python
import logging
import sys

watch_log = logging.getLogger('cogwatch')
watch_log.setLevel(logging.INFO)
watch_handler = logging.StreamHandler(sys.stdout)
watch_handler.setFormatter(logging.Formatter('[%(name)s] %(message)s'))
watch_log.addHandler(watch_handler)
```
