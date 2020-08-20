# Change Log
All notable changes to this project will be documented in this file.
 
The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [1.1.0] - 2020-08-20

### Added
- The `watch()` decorator is now the preferred way to use the utility. 
You can still manually instantiate the `Watcher()` and call its `start()`
method, but the decorator does the exact same thing.
- A more thorough example is now available in the *examples/* directory.

### Changed
- Updated the Getting Started section to utilize the new `watch()`
decorator.
- The `cogs_path` kwarg now defaults to *'commands'*.

## [1.0.0] - 2020-08-20

Initial release!
