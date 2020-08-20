# cogwatch

*Automatic hot-reloading for discord.py command files.*

`cogwatch` is a utility that you can plug into your discord.py bot *(or run as a stand-alone CLI script)* that will
watch your command files directory *(cogs)* and automatically reload them as you modify or move them around in real-time.
No more manually reloading commands with other commands, or *(worse)* restarting your bot, every time you edit that embed!

<br>

### Tables of Contents
+ [Getting Started](#getting-started)
+ [CLI Stand-Alone](#cli-stand-alone)
+ [Logging](#logging)


### Getting Started
*Please note that `cogwatch` is a development tool. You should not run it on production.*

You can install the library with `pip install cogwatch`.

You can import and start the bot anywhere you want, as long as you have access to your initialized bot class. The
`on_ready` method makes a good, generic location.

```python
from cogwatch import Watcher

async def on_ready(self):
    cw = Watcher(self, 'commands', debug=False, loop=None)
    await cw.start()
```
