from pathlib import Path

import pytest

from feefifofum.main import format_feature_file
from feefifofum.utils.file_utils import read_file_lines

ROOT_DIR = Path(__file__).resolve().parent


class TestFormatFeatureFile:
    """Tests for format_feature_file()."""

    test_data = [
        ('full_file_input.feature', 'full_file_expected.feature'),
        ('text_only_input.feature', 'text_only_expected.feature'),
    ]

    @pytest.mark.parametrize('input_file, expected_file', test_data)
    def test_format_feature_file(self, input_file: str, expected_file: str) -> None:
        """Tests format_feature_file by running all transformations."""
        file_path_input = ROOT_DIR / 'data' / input_file
        file_path_expected = ROOT_DIR / 'data' / expected_file

        file_lines_input = read_file_lines(file_path_input)
        formatted_output = format_feature_file(file_lines_input)

        formatted_expected = read_file_lines(file_path_expected)

        assert formatted_output == formatted_expected
