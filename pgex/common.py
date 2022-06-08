"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.

Defines a few globally used variables.
"""

import pathlib

PGEX_DIR = pathlib.Path(__file__).parent
EXAMPLES_DIR = PGEX_DIR / "examples"
PGEX_EXAMPLES = [i.name for i in EXAMPLES_DIR.iterdir()]
