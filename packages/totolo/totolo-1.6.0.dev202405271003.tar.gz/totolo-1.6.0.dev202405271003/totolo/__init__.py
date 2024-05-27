"""
The Python interface to themeontology.org.
"""

__version__ = "1.6.0.dev202405271003"

from totolo.api import TORemote, empty, files

remote = TORemote()

__ALL__ = [
    empty,
    files,
    remote,
]
