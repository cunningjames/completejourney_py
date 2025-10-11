# Changelog

All notable changes to the Complete Journey Python package are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Comprehensive MkDocs documentation with cookbook examples
- Four detailed analysis notebooks (top products, shopping frequency, coupon analysis, traffic patterns)
- Enhanced API documentation with detailed examples

### Changed
- Improved docstring with comprehensive examples and dataset descriptions

## [0.0.3] - 2025-01-XX

### Added
- Modern `pyproject.toml` configuration following PEP 621 standards
- Comprehensive type hints throughout the codebase
- Enhanced test suite with 9 test cases covering all functionality
- Professional README with badges and comprehensive documentation
- Comprehensive .gitignore following Python best practices

### Changed
- **BREAKING**: Replaced deprecated `pkg_resources` with modern `importlib.resources`
- Updated Python requirement to >=3.8 (from >=3.6)
- Enhanced function docstring with detailed examples and parameter descriptions
- Modernized development workflow with black, isort, mypy integration

### Removed
- Legacy `setup.py` and `setup.cfg` files
- Deprecated `pytest-runner` dependency

### Fixed
- Eliminated deprecation warnings from `pkg_resources`
- Improved error handling and edge case coverage

## [0.0.2] - Previous Release

### Added
- Fixed missing dependency on pyarrow

### Changed
- Improved package metadata

## [0.0.1] - Initial Release

### Added
- Initial package structure with `get_data()` function
- Support for loading 8 Complete Journey datasets:
  - `transactions`: 1.47M purchase records
  - `demographics`: Household characteristics
  - `products`: Product metadata
  - `campaigns`: Marketing campaigns
  - `campaign_descriptions`: Campaign metadata
  - `promotions`: Product placement data
  - `coupons`: Coupon information
  - `coupon_redemptions`: Coupon usage records
- Parquet format for efficient data storage and loading
- Basic documentation and usage examples

### Technical Details
- Python 3.6+ support
- pandas and pyarrow dependencies
- Package data included in distribution

---

## Development Timeline

### Package Modernization (Current)

**Infrastructure Improvements:**
- ✅ Modern packaging with `pyproject.toml`
- ✅ Comprehensive type hints
- ✅ Enhanced testing (9 test cases, 100% pass rate)
- ✅ Code quality tools (black, isort, mypy, flake8)
- ✅ Future-proof resource loading

**Documentation Enhancements:**
- ✅ Professional README with badges
- ✅ Comprehensive MkDocs documentation
- ✅ Four detailed cookbook examples
- ✅ Complete API reference
- ✅ Dataset documentation following R package style

### Future Roadmap

**Version 0.1.0 - Enhanced Analysis**
- Additional analysis examples and tutorials
- Performance optimizations for large datasets
- Integration with popular visualization libraries
- Extended API for common analysis patterns

**Version 0.2.0 - Advanced Features**
- Data validation and quality checks
- Integration with statistical libraries
- Support for additional data formats
- Advanced filtering and sampling utilities

**Version 1.0.0 - Stable Release**
- Stable API with backward compatibility guarantees
- Complete documentation coverage
- Performance benchmarks
- Integration examples with major data science frameworks

## Migration Guides

### Upgrading from 0.0.2 to 0.0.3

**No breaking changes for basic usage:**
```python
# This continues to work the same way
from completejourney_py import get_data
data = get_data()
```

**New features available:**
```python
# Enhanced type hints provide better IDE support
from completejourney_py import get_data
from typing import Dict
import pandas as pd

data: Dict[str, pd.DataFrame] = get_data(["transactions", "demographics"])
```

**Development workflow improvements:**
```bash
# Modern development setup
pip install -e ".[dev]"  # Installs development dependencies

# Code quality tools now available
black completejourney_py/
isort completejourney_py/
mypy completejourney_py/
flake8 completejourney_py/
```

### Python Version Support

| Package Version | Python Versions |
|----------------|------------------|
| 0.0.1 - 0.0.2  | 3.6+ |
| 0.0.3+         | 3.8+ |
| 1.0.0+ (planned) | 3.9+ |

**Rationale for Python 3.8+ requirement:**
- Python 3.6 and 3.7 reached end-of-life
- Modern tooling assumes Python 3.8+
- Better type hint support and performance improvements
- Alignment with current data science ecosystem standards

## Contributors

- James Cunningham - Original package author
- Claude Code AI - Package modernization and documentation

## Data Attribution

This package provides Python access to the Complete Journey dataset:

**Original Data Source:**
- **Provider**: [84.51°](http://www.8451.com/area51/)
- **Original R Package**: [completejourney](https://github.com/bradleyboehmke/completejourney) by Bradley Boehmke
- **License**: Available for research and educational purposes

**Python Package:**
- **License**: MIT License
- **Repository**: [GitHub](https://github.com/jamescunningham/completejourney_py)

---

*For detailed technical changes, see the [Git commit history](https://github.com/jamescunningham/completejourney_py/commits/main).*