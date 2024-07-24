from file_renamer import list_folder_files;
import pytest
import os

@pytest.fixture
def setup_test_directory(tmpdir):
    """Tests listing files in a directory."""

    # Create a temporary directory with some files
    test_dir = tmpdir.mkdir("test_dir")
    test_file1 = test_dir.join("file1.txt")
    test_file2 = test_dir.join("file2.txt")
    test_file1.write("content1")
    test_file2.write("content2")
    return test_dir

def test_list_files_in_folder(setup_test_directory):
    test_dir = setup_test_directory
    files = list_folder_files(test_dir)
    assert sorted(files) == ["file1.txt", "file2.txt"]

def test_non_existent_folder():
    files = list_folder_files("nonexistent_folder")
    assert files == []


if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN", __file__])