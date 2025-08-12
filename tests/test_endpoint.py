from duden_webscraper.endpoint import Endpoint
import pytest

@pytest.mark.parametrize(
    "attr, expected_prefix",
    [("DICTIONARY_SEARCH", "/"), ("ORTHOGRAPHY", "/")]
)
def test_paths_start_with_slash(attr, expected_prefix):
    assert getattr(Endpoint, attr).startswith(expected_prefix)
