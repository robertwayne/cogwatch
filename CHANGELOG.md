# Change Log
All notable changes to this project will be documented in this file.
 
The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [2.1.0] -- 2021-15-02

### Added
- The subclassed bot can now be run via a poetry script `poetry run example`.
- The `examples` directory now includes a sample command directory & cog file to 
  demonstrate the expected tree and code structure. (#9)
- Added python-dotenv to dev-dependencies for passing in bot tokens to examples.


## [2.0.0] -- 2021-30-01

### Changed
- **BREAKING**: The `cogs_path` parameter is now just `path`. This was done for simplicity and to
  closer match the general naming convention.
- Updated `watchgod` dependency to latest version for performance improvements.

## [1.1.8] -- 2020-12-14

### Changed
- Fixed path manipulation bug that caused issues between POSIX and Windows systems. Paths
  are now handled platform-agnostic with the `os` module. Added tests for regressions. (#6)

## [1.1.6 -- 1.1.7] -- 2020-12-02

### Changed
- Fixed a bug where nested project structures would break internal path resolution.
- A `ValueError` will now be raised if the user uses invalid input delimiters on
the `cogs_path` parameter.

### Added
- Migrated to the Poetry package & dependency manager.
- New dev dependency for testing: `pytest`.
- Included several test cases on `get_dotted_cog_path` and `get_cog_name`
ensuring they are returning usable values.

### Removed
- Removed setup.py, requirements.txt, build.ps1 in favor of the Poetry ecosystem.

## [1.1.5] -- 2020-09-16

### Changed
- Fixed a bug where the watcher would spam errors if the specified cog directory did not exist.
- The watcher will additionally track changes to the command directory name. The watcher will 
will seek for a matching directory name in the background and restart itself once found *(this includes
reloading all cogs within that directory, if not loaded)*.
- Refactored some internal code.

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
