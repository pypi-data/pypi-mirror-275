"""
Jabroni - Journal Abbreviations
"""
import json

from importlib.resources import files

from ._version import __version__


with open(files("jabroni").joinpath("data.json"), "rt", encoding="utf-8") as f:
    data_full_to_abbr = json.load(f)
data_abbr_to_full = {v: k for k, v in data_full_to_abbr.items()}


def get_abbr(full_title: str, errors:str = "raise") -> str:
    """Convert long journal title to short journal title.

    :param full_title: Full (long) journal title
    :param errors: How to handle situation when journal is not in database
        * ``"strict"`` will raise a KeyError
        * ``"replace"`` will replace them with ``None``
        * ``"preserve"`` will preserve the text
    :return: Abbreviated (short) journal title
    :raises KeyError: Raise if journal is not in database and ``errors`` is ``'raise'``
    """
    assert errors in {"raise", "replace", "preserve"}, (
        "`errors` must be one of 'raise', 'replace', or 'preserve'"
    )
    if errors == "raise":
        return data_full_to_abbr[full_title]
    elif errors == "replace":
        return data_full_to_abbr.get(full_title, None)
    elif errors == "preserve":
        return data_full_to_abbr.get(full_title, full_title)


def get_full(abbr_title: str, errors:str = "raise") -> str:
    """Convert short journal title to long journal title.

    :param abbr_title: Abbreviated (short) journal title
    :param errors: How to handle situation when journal is not in database
        * ``"strict"`` will raise a KeyError
        * ``"replace"`` will replace them with ``None``
        * ``"preserve"`` will preserve the text
    :return: Full (long) journal title
    :raises KeyError: Raise if journal is not in database and ``errors`` is ``'raise'``
    """
    assert errors in {"raise", "replace", "preserve"}, (
        "`errors` must be one of 'raise', 'replace', or 'preserve'"
    )
    if errors == "raise":
        return data_abbr_to_full[abbr_title]
    elif errors == "replace":
        return data_abbr_to_full.get(abbr_title, None)
    elif errors == "preserve":
        return data_abbr_to_full.get(abbr_title, abbr_title)
