from pathlib import Path

from feefifofum.main import format_feature_file
from feefifofum.utils.file_utils import read_file_lines


ROOT_DIR = Path(__file__).resolve().parent


def test_format_feature_file() -> None:
    """Tests format_feature_file by running all transformations."""
    file_path_input = ROOT_DIR / 'data' / 'example_input.feature'
    file_path_expected = ROOT_DIR / 'data' / 'example_expected.feature'

    file_lines_input = read_file_lines(file_path_input)
    formatted_output = format_feature_file(file_lines_input)

    formatted_expected = read_file_lines(file_path_expected)

    assert formatted_output == formatted_expected
