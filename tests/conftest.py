import pytest
import os
from pathlib import Path


@pytest.fixture
def sample_project_path():
    return Path(__file__).parent / "fixtures" / "sample_project"


@pytest.fixture
def sample_config():
    return {
        "exclude_patterns": ["**/test_*.py"],
        "ignore_decorators": ["@property"],
        "confidence_threshold": 0.8,
    }


@pytest.fixture
def create_temp_python_file(tmp_path):
    def _create_file(content: str) -> Path:
        file_path = tmp_path / "test_file.py"
        file_path.write_text(content)
        return file_path

    return _create_file
