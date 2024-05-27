"""Support executing the CLI by doing `python -m peglib`."""
from __future__ import annotations

from peglib.cli import cli

if __name__ == "__main__":
    raise SystemExit(cli())
