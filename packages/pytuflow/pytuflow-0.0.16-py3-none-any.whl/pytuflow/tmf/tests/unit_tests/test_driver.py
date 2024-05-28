from pathlib import Path

import pytest

from tmf.tuflow_model_files.db.drivers.driver import DatabaseDriver
from tmf.tuflow_model_files.db.drivers.csv import CsvDatabaseDriver


def test_driver_init_error():
    with pytest.raises(TypeError):
        DatabaseDriver()

    with pytest.raises(TypeError):
        DatabaseDriver(1)


def test_driver_init_csv():
    p = Path(__file__).parent / 'csv_database.csv'
    with p.open('w') as f:
        f.write('a,b,c\n1,2,3')
    try:
        driver = DatabaseDriver(p)
        assert isinstance(driver, CsvDatabaseDriver)
    except Exception as e:
        raise e
    finally:
        p.unlink()


def test_driver_init_csv_2():
    p = Path(__file__).parent / 'csv_database.txt'
    with p.open('w') as f:
        f.write('a,b,c\n1,2,3')
    try:
        driver = DatabaseDriver(p)
        assert isinstance(driver, CsvDatabaseDriver)
    except Exception as e:
        raise e
    finally:
        p.unlink()


def test_driver_init_csv_3():
    p = Path(__file__).parent / 'csv_database.csv'
    driver = DatabaseDriver(p)
    assert isinstance(driver, CsvDatabaseDriver)


def test_driver_init_not_csv():
    p = Path(__file__).parent / 'csv_database.txt'
    with p.open('wb') as f:
        f.write(b'\x00\x01\x02')
    try:
        with pytest.raises(ValueError):
            DatabaseDriver(p)
    except Exception as e:
        raise e
    finally:
        p.unlink()


def test_driver_init_not_csv_2():
    p = Path(__file__).parent / 'csv_database.txt'
    with p.open('w') as f:
        f.write('a\tb\tc\n1\t2\t3')
    try:
        with pytest.raises(ValueError):
            DatabaseDriver(p)
    except Exception as e:
        raise e
    finally:
        p.unlink()


def test_driver_init_csv_fail():
    p = Path(__file__).parent / 'csv_database.txt'
    with p.open('w') as f:
        f.write('\n')
    try:
        with pytest.raises(ValueError):
            DatabaseDriver(p)
    except Exception as e:
        raise e
    finally:
        p.unlink()


def test_driver_load():
    p = Path(__file__).parent / 'csv_database.csv'
    with p.open('w') as f:
        f.write('a,b,c\n1,2,3')
    try:
        driver = DatabaseDriver(p)
        df = driver.load(p, 0, 0)
        assert df.shape == (1, 2)
    except Exception as e:
        raise e
    finally:
        p.unlink()

