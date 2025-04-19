"""
To be homed or without a home.
"""

from typing import List
from loguru import logger as log

def check_installed_ecosystem(deep_checks: bool = False) -> List[str]:
    """
    Get a list of installed PyForged ecosystem packages.

    **NOTE:**  This is a (basically) cached function

    :param deep_checks:
    :return:
    """
    log.info("Checking for PyForged native ecosystem installations...")

    packages = [
        ("bedrocked", "Core and utility functionality WILL be limited and/or unavailable."),
        ("runecaller", "Some extensibility, events, and hooks functionality may be limited or unavailable."),
        ("essencebinder", ""),
        ("vaultkeeper", "Some storage and persistence abstraction functionality may be limited or unavailable."),
        ("wardkeeper", "Some access, authentication, and security functionality may be limited or unavailable."),
        ("flowsculptor", "Tasking, rule engines, and workflow functionality may be limited or unavailable."),
        ("hexcrafter", "Automation and intelligence functionality may be limited or unavailable."),
    ]

    results = []

    for package, warning_message in packages:
        try:
            __import__(package)
            results.append(package)
            log.debug(f"{package.upper()} package was found and installed.")
        except ImportError:
            log.debug(f"The {package.upper()} package is not installed. {warning_message}")
        except Exception as e:
            log.error(f"An error occurred while checking {package} and so was unable to determine installation status: "
                      f"\n{e}")

    if results:
        log.info(f"{len(results)} PyForged Ecosystem installations found: {results}")
    else:
        log.warning("No native PyForged ecosystem installations could be found or detected.")

    return results

if __name__ == "__main__":
    check_installed_ecosystem()