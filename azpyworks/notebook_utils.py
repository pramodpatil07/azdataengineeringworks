import sys
from pathlib import Path
from typing import Any


def ensure_python_path(package_root: str) -> None:
    """Ensure the Python package root is available on sys.path."""
    root_path = str(Path(package_root).resolve())
    if root_path not in sys.path:
        sys.path.insert(0, root_path)


def display_dataframe(df: Any, max_rows: int = 20) -> None:
    """Display a pandas or Spark DataFrame in notebook-friendly form."""
    try:
        from pandas import DataFrame
    except ImportError:
        DataFrame = None

    if DataFrame is not None and isinstance(df, DataFrame):
        print(df.head(max_rows).to_markdown(index=False))
        return

    if hasattr(df, "show"):
        df.show(truncate=False, n=max_rows)
        return

    print(df)
