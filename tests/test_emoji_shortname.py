"""
    pytest config for emoji-shortname/tests
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: Copyright 2021 by Nicholas Phair
    :license: MIT, see LICENSE for details.
"""

import pytest


@pytest.mark.sphinx(buildername="text")
def test_substitutions(app):
    app.build()
    content = (app.outdir / "index.txt").read_text()
    assert "😄" in content
    assert "🐱🐶" in content
    assert "pickle_rick" in content
