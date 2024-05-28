from pathlib import Path

from tmf.tuflow_model_files.dataclasses.file import is_file_binary


def test_is_file_binary():
    p = Path(__file__).parent / 'test_binary.dat'
    with p.open('wb') as f:
        f.write(b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f')
    try:
        assert is_file_binary(p)
    except Exception as e:
        raise e
    finally:
        p.unlink()


def test_file_is_not_binary():
    p = Path(__file__).parent / 'test_binary.txt'
    with p.open('w') as f:
        f.write('Hello World!')
    try:
        assert not is_file_binary(p)
    except Exception as e:
        raise e
    finally:
        p.unlink()
