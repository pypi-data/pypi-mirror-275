import os, sys

PACKAGE_NAME = "pypi-wukunhuan"
PACKAGE_PATH = os.path.dirname(__file__)
PACKAGE_VERSION = "0.1.0"
COMMAND_NAME = "pypi"
EXECUTABLE_PATH = os.path.dirname(sys.executable)

PYPI_PACKAGE_NAME_PLACEHOLDER = "<PyPI package name>"
PYPI_LICENSE_CHOICES = {
    "MIT": "https://opensource.org/licenses/MIT",
    "Apache": "https://www.apache.org/licenses/LICENSE-2.0",
    "GPL": "https://www.gnu.org/licenses/gpl-3.0.en.html",
    "BSD": "https://opensource.org/licenses/BSD-3-Clause",
    "CreativeCommons": "https://creativecommons.org/licenses/",
    "Mozilla": "https://www.mozilla.org/en-US/MPL/",
    "Eclipse": "https://www.eclipse.org/legal/epl-2.0/",
    "LGPL": "https://www.gnu.org/licenses/lgpl-3.0.en.html",
    "AGPL": "https://www.gnu.org/licenses/agpl-3.0.en.html",
    "ISC": "https://opensource.org/licenses/ISC",
    "zlib": "https://opensource.org/licenses/Zlib",
}

CYAN='\033[0;36m'
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'
