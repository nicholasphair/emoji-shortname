[![Build Status](https://github.com/nicholasphair/emoji-shortname/actions/workflows/build.yml/badge.svg?branch=main)](https://github.com/nicholasphair/emoji-shortname/actions/workflows/build.yml)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)


# emoji-shortname
Replace emoji short names with their corresponding emojis.

## Overview
The short names we are familiar with (e.g. the ones used on sites like GitHub)
are not inline with the [CLDR short names][1] defined in the Unicode standard.
This makes mapping short codes to emojis a bit of a challenge. So, I punt on
this issue, and defer to the [emoji package][2] created by [Taehoon Kim and Kevin Wurster][3].
Their wonderful library does the heavy lifting.  

This extension amounts to a find-and-replace. Find the short name, replace it with the
appropriate emoji. It works with both `Markdown` and `reStructuredText`.

## Details
Emojis are added to documents by sandwiching their short names between colons.
For example, `:smile:` resolves to :smile:. This syntax conflicts with
the way you provide options to directives in Sphinx. And, since the extension
ties into the [source-read hook][4], those directives are yet to be resolved.
As such, if an option shares the same name as an emoji short code, the option
will be replaced by the emoji. Though I am unaware of any case where this happens,
be aware that it is a possibility.

## Development
The project is managed with [poetry][5].  

To contribute to `emoji-shortname`, first [install poetry][6]. Once installed,
fetch the project dependencies with `poetry install`. From here, you can
iterate on the code and run the unit tests with `poetry run tox pyproject.toml`

## Usage
Simply install the package with your manager of choice (e.g. poetry, pip, etc)
and then add the extension to your sphinx `config.py`.
```python
extensions = ["emoji_shortname"]
```

[1]: https://unicode.org/emoji/charts/full-emoji-list.html
[2]: https://github.com/carpedm20/emoji/
[3]: https://github.com/carpedm20/emoji/blob/master/LICENSE.txt
[4]: https://www.sphinx-doc.org/en/master/extdev/appapi.html#event-source-read
[5]: https://python-poetry.org/
[6]: https://python-poetry.org/docs/#installation
