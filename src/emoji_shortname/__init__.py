"""
    sphinxcontrib.emoji-shortname
    ~~~~~~~~~~~~~~~~~~~~~~

    Replace emoji short names with their corresponding emojis.

    :copyright: Copyright 2021 by Nicholas Phair
    :license: MIT, see LICENSE for details.
"""
try:
    import importlib.metadata as metadata
except ImportError:
    import importlib_metadata as metadata


import re

import emoji

__version__ = metadata.version("emoji-shortname")

SHORTNAME_REGEX = re.compile(r":(\w+):", re.IGNORECASE)


def setup(app):
    app.connect("source-read", to_unicode)
    return {"version": __version__, "parallel_read_safe": True}


def to_unicode(app, docname, source):
    emojized = SHORTNAME_REGEX.sub(
        lambda m: emoji.emojize(m.group(0), use_aliases=True), source[0]
    )
    source[0] = emojized
