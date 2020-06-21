# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [v0.2.1] - 2020-06-21
### Added
 - `rine` parameter to `var` tag which defines what to render if `Variable` does
 not exist.

## [v0.2.0] - 2020-06-21
### Changed
 - Fixed `management.commands` in `setup.py`.

## [v0.1.5a1] - 2019-12-27
### Added
 - A `ForeignKey` named `user` for model `User` to model `Variable`

## [v0.1.4a1] - 2019-12-26
### Added
 - `getvar` command
 - `setvar` command
 - `delvar` command

## [v0.1.3a2] - 2019-12-16
### Added
 - Python 3.8 support.

## [v0.1.3a1] - 2019-12-15
### Added
 - `_PickleField` to be used with `value` field of `Variable`. Uses `pickle`.

### Changed
 - Replaced `value_binary` with `value` in `Variable` model

### Removed
 - `value_binary` field from `Variable` model

## [v0.1.2a1] - 2019-12-12
### Changed
 - `var` is optimized for assignment in template

## [v0.1.1a1] - 2019-12-12
### Added
 - Added `rit` (render if true) to `var` template tag.
 - Added `rif` (render if false) to `var` template tag.
 - Added `rin` (render if none) to `var` template tag.

### Changed
 - `get_var` tag has changed its name to `var`.
 - Now `update` method of `Variable`'s `QuerySet` supports `value` kwarg.
 - `Variable` now has a default primary key implementation.

## [v0.1.0a2] - 2019-12-08
Initial second release.

## [v0.1.0a1] - 2019-12-08
Initial release.
