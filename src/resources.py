"""Helpers for locating files shipped with the application."""

from pathlib import Path
import sys


def resource_path(*parts: str) -> Path:
    """Return a resource path both in development and in a PyInstaller build."""
    base_dir = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent))
    return base_dir.joinpath(*parts)
