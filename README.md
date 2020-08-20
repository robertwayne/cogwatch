# cogwatch

*Automatic hot-reloading for your discord.py command files.*

`cogwatch` is a utility that you can plug into your `discord.py` bot that will watch your command files directory *(cogs)* 
and automatically reload them as you modify or move them around in real-time. No more manually reloading commands with 
other commands, or *(worse)* restarting your bot, every time you edit that embed!

`cogwatch` recursively checks from the given directory and will not load files which are not `discord.py` cogs, nor will it
load code which would otherwise cause a syntax error. It uses the builtin extension methods which do a great job at
ensuring your commands stay loaded even if you save a change which would otherwise not run.

### Tables of Contents
+ [Getting Started](#getting-started)
+ [Logging](#logging)


### Getting Started
You can install the library with `pip install cogwatch`.

You can import and start the bot anywhere you want, as long as you have access to your initialized bot class. The
`on_ready` method makes a good, generic location. The first two arguments are *required*. The first is your bot instance.
 The second is the name of the directory where your command files exist. All other arguments are optional.

```python
from cogwatch import Watcher

async def on_ready(self):
    cw = Watcher(self, 'commands', debug=False, loop=None, default_logger=True)
    await cw.start()
```

By default the library will use the running event loop. If you wish to pass in a specific loop, you can do so with the
`loop=None` parameter.

**NOTE:** `cogwatch` will only run if the **\_\_debug\_\_** flag is set on Python. You can read more about that 
[here](https://docs.python.org/3/library/constants.html). In short, unless you run Python with the *-O* flag from
your command line, **\_\_debug\_\_** will be **True**. If you just want to bypass this feature, pass in `debug=False` and
it won't matter if the flag is enabled or not. *This is a development tool. You should not run it on production.*

### Logging
By default the library has a logger enabled so users can get output to the console. You can disable this by
passing in `default_logger=False`. If you want to hook into the logger -- for example, to pipe your output to another
terminal or `tail` a file -- you can set up a custom logger like so:

```python
import logging
import sys

watch_log = logging.getLogger(__name__)
watch_log.setLevel(logging.INFO)
watch_handler = logging.StreamHandler(sys.stdout)
watch_handler.setFormatter(logging.Formatter('[%(name)s] %(message)s'))
watch_log.addHandler(watch_handler)
```
