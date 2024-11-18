import pytest
from pyreachx.config import AnalyzerConfig

def test_config_from_dict():
    config_data = {
        'exclude_patterns': ['tests/.*', '.*\\.pyc']
    }
    config = AnalyzerConfig.from_dict(config_data)
    assert len(config.exclude_patterns) == 2

def test_invalid_config():
    config_data = {
        'exclude_patterns': ['*invalid[' ]  # Invalid regex pattern
    }
    with pytest.raises(ValueError):
        AnalyzerConfig.from_dict(config_data)

def test_config_merge():
    base_config = AnalyzerConfig.from_dict({"exclude_patterns": [".*\\.py$"]})
    override_config = AnalyzerConfig.from_dict({"exclude_patterns": [".*\\.txt$"]})
    merged = base_config.merge(override_config)
    # Extract pattern strings from compiled regex patterns
    merged_patterns = [pattern.pattern for pattern in merged.exclude_patterns]
    assert set(merged_patterns) == {".*\\.py$", ".*\\.txt$"}