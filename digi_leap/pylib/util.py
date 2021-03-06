"""Misc. utilities."""

import regex


class DotDict(dict):
    """Allow dot.notation access to dictionary items"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


def shorten(text):
    """Collapse whitespace in a string."""
    return ' '.join(text.split())


def flatten(nested):
    """Flatten an arbitrarily nested list."""
    flat = []
    nested = nested if isinstance(nested, (list, tuple, set)) else [nested]
    for item in nested:
        if hasattr(item, '__iter__'):
            flat.extend(flatten(item))
        else:
            flat.append(item)
    return flat


def squash(values):
    """Squash a list to a single value is its length is one."""
    return values if len(values) != 1 else values[0]


def as_list(values):
    """Convert values to a list."""
    return values if isinstance(values, (list, tuple, set)) else [values]
