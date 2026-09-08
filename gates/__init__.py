"""
Gates Master Package
Organized into:
- gates.auth (6 Auth Gates)
- gates.charge (16 Charge Gates)
- gates.mass (6 Mass Checkers)
"""
from importlib import import_module

__all__ = ["auth", "charge", "mass"]


def __getattr__(name):
    if name in __all__:
        return import_module(f".{name}", __name__)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
