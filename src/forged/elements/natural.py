"""
Native imports
"""
from forged.unsorted import check_installed_ecosystem
from forged.core.logged import logger as log

is_installed = check_installed_ecosystem()
total = 0

for package in is_installed:
    total += 1
    try:
        pkg_module = __import__(package)
        log.success(f"Successfully imported '{package}' package.")
        pkg_module.forge()
    except ImportError as e:
        log.error(f"Failed to import '{package}': {e}")
    except Exception as e:
        log.error(f"An unexpected error occurred while importing '{package}': {e}")

if total > 0:
    log.success(f"{total} packages from the PyForged ecosystem were imported.")

