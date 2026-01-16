# All changes will be tracked here

Based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)

## [0.2.2] - 2026-01-15

## Fixed

- Return value instead of node in `last_value` property
- Correct `__repr__` to use `self.next` safely

### Tests
- Add parameterized case for empty stack in `Stack.push`

## [0.2.1] - 2026-01-14

### Added

- Added `pytest` module to requirements.txt
- Updated `README.md` content with:
  - installation steps
  - how to run tests
  - project license

## [0.2.0] - 2026-01-14

### Added

- Implemented class Stack with:
  - `push()` method
  - `last_value` @property
  - `length` @property
- Unit tests for each of these functions
- Exposed `Stack` class in public API

## [0.1.1] - 2026-01-14

### Fixed

- Fixed format issues inside `pyproject.toml`
- Added quotes in version string inside `pyproject.toml`

## [0.1.0] - 2026-01-14

### Added

- Basic project structure.