# Change Log
All notable changes to this project will be documented in this file.
 
The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [1.1.4] -- 2020-09-10

### Added
- New example for the classless bot structure and manually instantiating a watcher.


### Changed
- Fixed a typo in the class-based bot example and renamed it to `subclass_bot.py` to stay in convention with
the new `classless_bot.py`. 


## [1.1.3] - 2020-08-23

### Added
- `cogwatch` will now log when a directory is modified within the `cogs_path` directory.

## [1.1.1] - 2020-08-21

### Added
- The `Watcher` class and `watch` decorator now accept a `preload`
argument. If set to True, it will detect and load all cogs on start.
If False, you have to handle your own cog loading. Defaults to False. 
***Note:** the preloading happens before the debug mode check for auto-reloads,
so you can use it as your default cog loader in production.*

### Changed
- `cogs_path` was not being read in nested path situations.
- Exceptions are no longer completely eaten.

## [1.1.0] - 2020-08-20

### Added
- The `watch()` decorator is now the preferred way to use the utility. 
You can still manually instantiate the `Watcher()` and call its `start()`
method, but the decorator does the exact same thing.
- A more thorough example is now available in the *examples/* directory.

### Changed
- Updated the Getting Started section to utilize the new `watch()`
decorator.
- The `cogs_path` argument now defaults to *'commands'*.

## [1.0.0] - 2020-08-20

Initial release!
