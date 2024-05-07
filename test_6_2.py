import pytest

def merge_and_write(file1_path, file2_path, output_file_path):
    try:
        with open(file1_path, 'r') as file1:
            data1 = file1.read().strip()

        with open(file2_path, 'r') as file2:
            data2 = file2.read().strip()

        merged_data = data1 + ' ' + data2

        with open(output_file_path, 'w') as output_file:
            output_file.write(merged_data)

        with open(output_file_path, 'r') as output_file:
            data = output_file.read()
        return data
    except FileNotFoundError:
        return "Один из файлов не найден"

@pytest.fixture
def files(tmpdir):
    file1_path = tmpdir.join("file1.txt")
    file2_path = tmpdir.join("file2.txt")
    output_file_path = tmpdir.join("output.txt")
    file1_path.write("Hello")
    file2_path.write("Python")
    return file1_path, file2_path, output_file_path

def test_merge_and_write(files):
    file1_path, file2_path, output_file_path = files
    merged_data = "Hello Python"

    result = merge_and_write(file1_path, file2_path, output_file_path)

    assert result == merged_data
    assert output_file_path.read() == merged_data

def test_fail(files):
    file1_path, file2_path, output_file_path = files
    assert merge_and_write(file1_path, 'test_file.txt', output_file_path) == "Один из файлов не найден"
    assert merge_and_write('test_file.txt', file2_path, output_file_path) == "Один из файлов не найден"
    assert merge_and_write('test_file1.txt', 'test_file2.txt', output_file_path) == "Один из файлов не найден"