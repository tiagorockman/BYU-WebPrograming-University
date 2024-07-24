from file_renamer import list_folder_selection_files;
import pytest
import os

@pytest.fixture
def setup_test_directory(tmp_path):
    test_dir = tmp_path / "test_dir"
    test_dir.mkdir()
    (test_dir / "file1.txt").write_text("content of file1")
    (test_dir / "file2.txt").write_text("content of file2")
    sub_dir = test_dir / "sub_dir"
    sub_dir.mkdir()
    (sub_dir / "file3.txt").write_text("content of file3")
    return test_dir

def test_list_files_in_folder(setup_test_directory):
    test_dir = setup_test_directory
    files = list_folder_selection_files(test_dir)
    assert sorted(files) == ["file1.txt", "file2.txt"]

def test_list_files_in_empty_folder(tmp_path):
    empty_dir = tmp_path / "empty_dir"
    empty_dir.mkdir()
    files = list_folder_selection_files(empty_dir)
    assert files == []

def test_list_files_in_non_existent_folder():
    files = list_folder_selection_files("non_existent_folder")
    assert files == []

def test_list_files_in_folder_with_special_chars(tmp_path):
    special_dir = tmp_path / r"folder_with_\t_special_chars"
    special_dir.mkdir()
    (special_dir / "file1.txt").write_text("content of file1")
    (special_dir / "file2.txt").write_text("content of file2")
    files = list_folder_selection_files(special_dir)
    assert sorted(files) == ["file1.txt", "file2.txt"]


if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN", __file__])