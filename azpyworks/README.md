# azpyworks

Shared Python utilities for Databricks notebook workflows in this repository.

## Purpose

- Provide common Python classes and helpers for notebook development.
- Store Python-specific configuration examples and notebook utilities.
- Support Python notebooks in addition to the existing Scala/Spark modules.

## Usage

In a Databricks notebook or local Python session, add the module root to `sys.path` and import the package:

```python
import sys
sys.path.append("/Workspace/Repos/<your-repo-path>/azpyworks")

from azpyworks import load_config, display_dataframe

config = load_config("/Workspace/Repos/<your-repo-path>/azpyworks/configs/sample_config.json")
print(config)
```

## Example notebook

A ready-to-run example notebook is available at:

- `azpyworks/examples/azpyworks_example.ipynb`

It demonstrates loading `azpyworks`, reading the sample JSON config, and displaying a DataFrame.

## Structure

- `azpyworks/config.py` - configuration loading helpers
- `azpyworks/notebook_utils.py` - notebook utility helpers
- `azpyworks/configs/` - sample configuration files
