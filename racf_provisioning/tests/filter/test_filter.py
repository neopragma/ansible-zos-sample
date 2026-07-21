import importlib.util
from pathlib import Path


def load_filter_module():

    path = (
        Path(__file__).parents[2]
        / "filter_plugins"
        / "racf.py"
    )

    spec = importlib.util.spec_from_file_location(
        "racf_filter",
        path,
    )

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return module


def test_filter_exports_racf_provision():

    module = load_filter_module()

    filters = module.FilterModule().filters()

    assert "racf_provision" in filters
