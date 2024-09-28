from __future__ import annotations

from pathlib import Path

import pytest

from feefifofum.utils.file_utils import get_file_paths


class TestGetFilePaths:
    """Tests for get_file_paths()."""

    @pytest.fixture
    def mock_file_paths(self, tmp_path: Path) -> dict[str, Path]:
        """
        Fixture to set up temporary file structure with text and non-text files and nested directories.

        :param tmp_path: Pytest fixture for creating a temporary directory
        :return: Mapping of descriptive keys to file paths.
        """
        mock_file_paths = {
            'text_file': tmp_path / 'text_file.txt',
            'nested_text_file_1': tmp_path / 'subdirectory_1' / 'nested_text_file.txt',
            'nested_text_file_2': tmp_path / 'subdirectory_1' / 'subdirectory_2' / 'nested_text_file_2.txt',
            'non_text_file': tmp_path / 'non_text_file.md',
            'nested_non_text_file': tmp_path / 'subdirectory_1' / 'nested_non_text_file.md',
        }

        for path in mock_file_paths.values():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.touch()

        return mock_file_paths

    def test_file_paths_matching_extension(self, mock_file_paths: dict[str, Path]) -> None:
        """Tests for input file paths to be returned when their extension matches."""
        input_paths = [
            mock_file_paths['text_file'],
            mock_file_paths['nested_text_file_1'],
            mock_file_paths['nested_text_file_2'],
        ]

        assert set(get_file_paths(input_paths, file_extension='.txt')) == set(input_paths)

    def test_file_paths_different_extension(self, mock_file_paths: dict[str, Path]) -> None:
        """Tests for no file paths to be returned when files exist but extension doesn't match."""
        input_paths = [mock_file_paths['non_text_file'], mock_file_paths['nested_non_text_file']]

        assert get_file_paths(input_paths, file_extension='.txt') == []

    def test_file_paths_no_matching_extension(self, mock_file_paths: dict[str, Path]) -> None:
        """Tests for no file paths to be returned when no files exist with matching extension."""
        input_paths = list(mock_file_paths.values())  # All files
        assert get_file_paths(input_paths, '.pdf') == []

    def test_file_paths_non_existent_paths(self) -> None:
        """Tests for no file paths to be returned when file path doesn't exist."""
        assert get_file_paths([Path('non_existent_file.txt')], '.txt') == []

    def test_single_directory_matching_extension(self, mock_file_paths: dict[str, Path]) -> None:
        """Tests for file paths to be returned when root directory contains files with matching extension."""
        input_path_directory = mock_file_paths['text_file'].parent

        expected_paths = [
            mock_file_paths['text_file'],
            mock_file_paths['nested_text_file_1'],
            mock_file_paths['nested_text_file_2'],
        ]

        assert set(get_file_paths([input_path_directory], file_extension='.txt')) == set(expected_paths)

    def test_multiple_directories_matching_extension(self, mock_file_paths: dict[str, Path]) -> None:
        """Tests for file paths to be returned when multiple directories containing files with matching extension."""
        expected_paths = [
            mock_file_paths['text_file'],
            mock_file_paths['nested_text_file_1'],
            mock_file_paths['nested_text_file_2'],
        ]

        input_path_directories = [file_path.parent for file_path in expected_paths]

        assert set(get_file_paths(input_path_directories, file_extension='.txt')) == set(expected_paths)

    def test_directory_different_extension(self, mock_file_paths: dict[str, Path]) -> None:
        """Tests for no file paths to be returned when files exist but extension doesn't match."""
        input_paths = [mock_file_paths['non_text_file'], mock_file_paths['nested_non_text_file']]

        assert get_file_paths(input_paths, file_extension='.txt') == []

    def test_directory_no_matching_extension(self, mock_file_paths: dict[str, Path]) -> None:
        """Tests for no file paths to be returned when directory has no files that exist with matching extension."""
        input_path_directory = mock_file_paths['text_file'].parent
        assert get_file_paths([input_path_directory], file_extension='.pdf') == []

    def test_directory_non_existent_paths(self) -> None:
        """Test for no file paths to be returned when directory doesn't exist."""
        assert get_file_paths([Path('non/existent/path')], '.txt') == []

    def test_file_path_and_directory_matching_extension(self, mock_file_paths: dict[str, Path]) -> None:
        """Tests for file paths to be returned when file paths and directories are passed with matching extension."""
        input_paths = [
            mock_file_paths['text_file'],  # File path
            mock_file_paths['nested_text_file_2'].parent,  # Directory path
        ]
        expected_paths = [mock_file_paths['text_file'], mock_file_paths['nested_text_file_2']]

        assert set(get_file_paths(input_paths, file_extension='.txt')) == set(expected_paths)
