"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.

Runs black and isort on all project files, makes sure each file has the license
doc header
"""

import os
import sys
from pathlib import Path

import pkg_resources

# the leading and trailing newlines are significant here, don't remove
LICENCE_HEADER = """
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""

HEADER_TEXT = '"""' + LICENCE_HEADER

INSTALLED_PACKAGES = {i.key for i in pkg_resources.working_set}
REQUIRED_PACKAGES = {"black", "isort"}

missing_pkg_cnt = 0
for package in REQUIRED_PACKAGES:
    if package not in INSTALLED_PACKAGES:
        print(f"{package} is not installed.")
        missing_pkg_cnt += 1

if missing_pkg_cnt:
    sys.exit(
        f"{missing_pkg_cnt} packages are missing."
        if missing_pkg_cnt != 1
        else "1 package is missing."
    )


def check_header_string(path: Path = Path()):
    """
    Checks each python file recursively under the specified 'path' directory
    (by default it is the current working directory).
    Appends a license header at the start of the file if missing.
    """
    for file in path.rglob("*.py"):
        file_data = file.read_text().lstrip()
        if file_data.startswith(HEADER_TEXT):
            continue

        if file_data.startswith('"""'):
            file.write_text(HEADER_TEXT + file_data[3:])
        else:
            file.write_text(f'{HEADER_TEXT}"""\n\n{file_data}')

        print(f"Added license header doc-string to {file}")


check_header_string()
os.system("black .")
os.system("isort .")
