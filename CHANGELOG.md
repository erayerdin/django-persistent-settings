# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
