from pathlib import Path

import pytest

from tmf.tuflow_model_files.utils.context import Context
from tmf.tuflow_model_files.db._db_run_state import DatabaseRunState
from tmf.tuflow_model_files.db.bc_dbase import BCDatabase
from tmf.tuflow_model_files.db._db_build_state import DatabaseBuildState
from tmf.tuflow_model_files.dataclasses.event import EventDatabase, Event


def test_db_ctx_init():
    p = Path(__file__).parent / 'bc_dbase.csv'
    with p.open('w') as f:
        f.write('Name,Source,Column 1,Column 2,Add Col 1,Mult Col 2,Add Col 2,Column 3,Column 4\n'
                'FC01,<<ARI>><<DUR>>_001.csv,inflow_time_hr,inflow_<<TP>>,,,,,\n'
                'FC02,,,<<WATER_LEVEL>>,,,,,')
    with (Path(__file__).parent / '100y2h_001.csv').open('w') as f:
        f.write(
            'inflow_time_hr,inflow_TP01\n0.000,0\n0.083,0.84\n0.167,3.31\n0.250,4.6\n0.333,7.03\n0.417,12.39\n0.500,22.63')
    try:
        db = BCDatabase(p)
        ctx = Context([], {'ARI': '100y', 'DUR': '2h', 'TP': 'TP01', 'WATER_LEVEL': 15.5})
        db_ctx = DatabaseRunState(db, ctx, None)
        assert isinstance(db_ctx, DatabaseRunState)
        assert db_ctx._df.loc['FC01'].tolist()[:3] == ['100y2h_001.csv', 'inflow_time_hr', 'inflow_TP01']
        assert db_ctx._df.loc['FC02'].iloc[2] == 15.5
    except Exception as e:
        raise e
    finally:
        p.unlink()
        (Path(__file__).parent / '100y2h_001.csv').unlink()


def test_bc_database_get_files_simple():
    p = Path(__file__).parent / 'bc_dbase.csv'
    file1 = Path(__file__).parent / '100yr2hr_001.csv'
    file2 = Path(__file__).parent / '100yr2hr_002.csv'
    with p.open('w') as f:
        f.write('Name,Source,Column 1,Column 2,Add Col 1,Mult Col 2,Add Col 2,Column 3,Column 4\n'
                'FC01,100yr2hr_001.csv,inflow_time_hr,inflow_FC01,,,,,\n'
                'FC02,100yr2hr_001.csv,inflow_time_hr,inflow_FC02,,,,,\n'
                'FC03,100yr2hr_002.csv,inflow_time_hr,inflow_FC03,,,,,\n')
    with file1.open('w') as f:
        f.write(
            'inflow_time_hr,inflow_FC01,inflow_FC02\n0.000,0,0\n0.083,0.84,1.5\n0.167,3.31,6.2\n0.250,4.6,8\n0.333,7.03,12\n0.417,12.39,15\n0.500,22.63,50')
    with file2.open('w') as f:
        f.write(
            'inflow_time_hr,inflow_FC04,inflow_FC03\n0.000,0,0\n0.083,0.1,5\n0.167,0.5,10\n0.250,2,15\n0.333,5,20\n0.417,7.5,25\n0.500,10.5,30')
    try:
        db = BCDatabase(p)
        files = db.get_files()
        assert sorted(files) == sorted([file1, file2])
    except Exception as e:
        raise e
    finally:
        p.unlink()
        file1.unlink()
        file2.unlink()


def test_bc_database_get_files():
    p = Path(__file__).parent / 'bc_dbase.csv'
    file1 = Path(__file__).parent / '100yr2hr_001.csv'
    file2 = Path(__file__).parent / '100yr1hr_001.csv'
    file3 = Path(__file__).parent / '100yr3hr_001.csv'
    file4 = Path(__file__).parent / '50yr2hr_001.csv'
    file5 = Path(__file__).parent / '50yr1hr_001.csv'
    file6 = Path(__file__).parent / '50yr3hr_001.csv'
    file7 = Path(__file__).parent / '20yr2hr_001.csv'
    file8 = Path(__file__).parent / '20yr1hr_001.csv'
    file9 = Path(__file__).parent / '20yr3hr_001.csv'
    with p.open('w') as f:
        f.write('Name,Source,Column 1,Column 2,Add Col 1,Mult Col 2,Add Col 2,Column 3,Column 4\n'
                'FC01,_event1__event2__001.csv,inflow_time_hr,inflow_FC01,,,,,\n'
                'FC02,,,15.5,,,,,')
    with file1.open('w') as f:
        f.write(
            'inflow_time_hr,inflow_FC01\n0.000,0\n0.083,0.84\n0.167,3.31\n0.250,4.6\n0.333,7.03\n0.417,12.39\n0.500,22.63')
    with file2.open('w') as f:
        f.write(
            'inflow_time_hr,inflow_FC01\n0.000,0\n0.083,0.84\n0.167,3.31\n0.250,4.6\n0.333,7.03\n0.417,12.39\n0.500,22.63')
    with file3.open('w') as f:
        f.write(
            'inflow_time_hr,inflow_FC01\n0.000,0\n0.083,0.84\n0.167,3.31\n0.250,4.6\n0.333,7.03\n0.417,12.39\n0.500,22.63')
    with file4.open('w') as f:
        f.write(
            'inflow_time_hr,inflow_FC01\n0.000,0\n0.083,0.84\n0.167,3.31\n0.250,4.6\n0.333,7.03\n0.417,12.39\n0.500,22.63')
    with file5.open('w') as f:
        f.write(
            'inflow_time_hr,inflow_FC01\n0.000,0\n0.083,0.84\n0.167,3.31\n0.250,4.6\n0.333,7.03\n0.417,12.39\n0.500,22.63')
    with file6.open('w') as f:
        f.write(
            'inflow_time_hr,inflow_FC01\n0.000,0\n0.083,0.84\n0.167,3.31\n0.250,4.6\n0.333,7.03\n0.417,12.39\n0.500,22.63')
    with file7.open('w') as f:
        f.write(
            'inflow_time_hr,inflow_FC01\n0.000,0\n0.083,0.84\n0.167,3.31\n0.250,4.6\n0.333,7.03\n0.417,12.39\n0.500,22.63')
    with file8.open('w') as f:
        f.write(
            'inflow_time_hr,inflow_FC01\n0.000,0\n0.083,0.84\n0.167,3.31\n0.250,4.6\n0.333,7.03\n0.417,12.39\n0.500,22.63')
    with file9.open('w') as f:
        f.write(
            'inflow_time_hr,inflow_FC01\n0.000,0\n0.083,0.84\n0.167,3.31\n0.250,4.6\n0.333,7.03\n0.417,12.39\n0.500,22.63')
    try:
        db = BCDatabase(p)
        event_db = EventDatabase(
            {'Q100': Event('Q100', '_event1_', '100yr'),
             'Q50': Event('Q50', '_event1_', '50yr'),
             'Q20': Event('Q20', '_event1_', '20yr'),
             '1hr': Event('1hr', '_event2_', '1hr'),
             '2hr': Event('2hr', '_event2_', '2hr'),
             '3hr': Event('3hr', '_event2_', '3hr')})
        ctx = Context(['e1', 'Q100', 'e2', '2hr'])
        ctx.load_events(event_db)
        db_ctx = db.context(context=ctx)
        files = db_ctx.get_files()
        assert files == [file1]
        ctx = Context(['e1', 'Q50', 'e2', '3hr'])
        ctx.load_events(event_db)
        db_ctx = db.context(context=ctx)
        files = db_ctx.get_files()
        assert files == [file6]
    except Exception as e:
        raise e
    finally:
        p.unlink()
        file1.unlink()
        file2.unlink()
        file3.unlink()
        file4.unlink()
        file5.unlink()
        file6.unlink()
        file7.unlink()
        file8.unlink()
        file9.unlink()


def test_bc_dbase_repr():
    bc_dbase = BCDatabase('bc_dbase.csv')
    ctx = bc_dbase.context()
    assert repr(ctx) == '<BCDatabaseContext> bc_dbase.csv (not found)'


def test_bc_dbase_repr2():
    bc_dbase = BCDatabase()
    ctx = bc_dbase.context()
    assert repr(ctx) == '<DatabaseContext> (empty)'


def test_bc_dbase_repr3():
    file = Path(__file__).parent / 'bc_dbase.csv'
    with file.open('w') as f:
        f.write('Name,Source,Column 1,Column 2,Add Col 1,Mult Col 2,Add Col 2,Column 3,Column 4\n'
                'FC01,_event1__event2__001.csv,inflow_time_hr,inflow_FC01,,,,,\n'
                'FC02,,,15.5,,,,,')
    try:
        bc_dbase = BCDatabase(file)
        ctx = bc_dbase.context()
        assert repr(ctx) == '<BCDatabaseContext> bc_dbase.csv'
    except Exception as e:
        raise e
    finally:
        file.unlink()


def test_bc_dbase_get_files_empty():
    bc_dbase = BCDatabase('bc_dbase.csv')
    ctx = bc_dbase.context()
    assert ctx.get_files() == []


def test_bc_dbase_get_files_empty2():
    bc_dbase = BCDatabase()
    ctx = bc_dbase.context()
    assert ctx.get_files() == []


def test_bc_dbase_values_empty():
    bc_dbase = BCDatabase('bc_dbase.csv')
    ctx = bc_dbase.context()
    with pytest.raises(ValueError):
        ctx.value('FC01')
    assert 'FC01' not in ctx


def test_bc_dbase_values_empty2():
    bc_dbase = BCDatabase()
    ctx = bc_dbase.context()
    with pytest.raises(ValueError):
        ctx.value('FC01')
    assert 'FC01' not in ctx


def test_bc_dbase_value_key_error():
    file = Path(__file__).parent / 'bc_dbase.csv'
    with file.open('w') as f:
        f.write('Name,Source,Column 1,Column 2,Add Col 1,Mult Col 2,Add Col 2,Column 3,Column 4\n'
                'FC01,_event1__event2__001.csv,inflow_time_hr,inflow_FC01,,,,,\n'
                'FC02,,,15.5,,,,,')
    try:
        bc_dbase = BCDatabase(file)
        ctx = bc_dbase.context()
        assert 'FC03' not in ctx
        assert 'FC03' not in bc_dbase
        with pytest.raises(KeyError):
            ctx.value('FC03')
    except Exception as e:
        raise e
    finally:
        file.unlink()
