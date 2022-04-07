import pytest
from functions import openFile

def test_open_file_success(capsys):
    openFile("testing.txt")

    stdout, stderr = capsys.readouterr()

    assert stdout.strip() == "File opened."

def test_open_file_nonexistent():
    with pytest.raises(FileNotFoundError):
        openFile("nonexistant.txt")

@pytest.mark.parametrize("filename", [123, [], {}])
def test_open_file_bad_input(filename):
    with pytest.raises((TypeError)):
        openFile(filename)