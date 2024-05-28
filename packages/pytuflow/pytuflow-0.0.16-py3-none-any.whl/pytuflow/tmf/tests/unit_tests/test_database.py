from pathlib import Path

import pytest

from tmf.tuflow_model_files.dataclasses.inputs import Inputs
from tmf.tuflow_model_files.db.bc_dbase import BCDatabase
from tmf.tuflow_model_files.db._db_build_state import DatabaseBuildState
from tmf.tuflow_model_files.dataclasses.event import EventDatabase, Event
from tmf.tuflow_model_files.dataclasses.scope import Scope, ScopeList
from tmf.tuflow_model_files.utils.context import Context
from tmf.tuflow_model_files.utils.commands import Command
from tmf.tuflow_model_files.inp._inp_build_state import InputBuildState
from tmf.tuflow_model_files.utils.settings import Settings


def test_database_init_empty():
    db = DatabaseBuildState()
    assert db._path is None
    assert db._driver is None


def test_database_init_error():
    with pytest.raises(TypeError):
        DatabaseBuildState(1)


def test_database_init():
    p = Path(__file__).parent / 'csv_database.csv'
    with p.open('w') as f:
        f.write('a,b,c\n1,2,3')
    try:
        with pytest.raises(NotImplementedError):
            db = DatabaseBuildState(p.resolve())
            assert db._driver is not None
            assert db._df is not None
            assert db._scopes == [Scope('GLOBAL', '')]
    except Exception as e:
        raise e
    finally:
        p.unlink()


def test_database_load():
    p = Path(__file__).parent / 'csv_database.csv'
    with p.open('w') as f:
        f.write('a,b,c\n1,2,3')
    try:
        with pytest.raises(NotImplementedError):
            db = DatabaseBuildState()
            db.load(p)
            assert db._driver is not None
            assert db._df is not None
    except Exception as e:
        raise e
    finally:
        p.unlink()


def test_database_scope():
    p = Path(__file__).parent / 'csv_database.csv'
    with p.open('w') as f:
        f.write('Name,Source,Column 1,Column 2,Add Col 1,Mult Col 2,Add Col 2,Column 3,Column 4\n'
                '<<NAME>>,<<~e~>>_001.csv,inflow_time_hr,inflow_<<NAME>>,,,,,')
    try:
        with pytest.raises(NotImplementedError):
            db = DatabaseBuildState(p)
            assert db._scopes == [Scope('EVENT', '<<~e~>>'), Scope('VARIABLE', 'NAME')]
    except Exception as e:
        raise e
    finally:
        p.unlink()


def test_bc_database_init():
    p = Path(__file__).parent / 'bc_dbase.csv'
    with p.open('w') as f:
        f.write('Name,Source,Column 1,Column 2,Add Col 1,Mult Col 2,Add Col 2,Column 3,Column 4\n'
                '<<NAME>>,<<~e~>>_001.csv,inflow_time_hr,inflow_<<NAME>>,,,,,')
    with (Path(__file__).parent / 'EG001_001.csv').open('w') as f:
        f.write('inflow_time_hr,inflow_FC01\n0.000,0\n0.083,0.84\n0.167,3.31\n0.250,4.6\n0.333,7.03\n0.417,12.39\n0.500,22.63')
    try:
        db = BCDatabase(p)
        assert list(db._index_to_scopes.values())[0] == [Scope('VARIABLE', '<<NAME>>'), Scope('EVENT', '<<~e~>>')]
        assert list(db._file_to_scope.values()) == [[Scope('EVENT', 'EG001')]]
        assert db.index_to_file('<<NAME>>') == [Path(__file__).parent / 'EG001_001.csv']
    except Exception as e:
        raise e
    finally:
        p.unlink()
        (Path(__file__).parent / 'EG001_001.csv').unlink()


def test_bc_database_scope_resolve():
    p = Path(__file__).parent / 'bc_dbase.csv'
    with p.open('w') as f:
        f.write('Name,Source,Column 1,Column 2,Add Col 1,Mult Col 2,Add Col 2,Column 3,Column 4\n'
                '<<NAME>>,<<~e1~>><<~e2~>>_001.csv,inflow_time_hr,inflow_<<NAME>>,,,,,')
    with (Path(__file__).parent / '100y2h_001.csv').open('w') as f:
        f.write(
            'inflow_time_hr,inflow_FC01\n0.000,0\n0.083,0.84\n0.167,3.31\n0.250,4.6\n0.333,7.03\n0.417,12.39\n0.500,22.63')
    try:
        db = BCDatabase(p)
        assert list(db._file_to_scope.values()) == [[Scope('EVENT', '<<~e1~>>'), Scope('EVENT', '<<~e2~>>')]]
        db.figure_out_file_scopes([Scope('EVENT', '100y'), Scope('EVENT', '2h')])
        assert list(db._file_to_scope.values()) == [[Scope('EVENT', '100y'), Scope('EVENT', '2h')]]
    except Exception as e:
        raise e
    finally:
        p.unlink()
        (Path(__file__).parent / '100y2h_001.csv').unlink()


def test_database_init_not_implemented_error():
    p = Path(__file__).parent / 'bc_dbase.csv'
    with p.open('w') as f:
        f.write('Name,Source,Column 1,Column 2,Add Col 1,Mult Col 2,Add Col 2,Column 3,Column 4\n'
                '<<NAME>>,<<~e1~>><<~e2~>>_001.csv,inflow_time_hr,inflow_<<NAME>>,,,,,')
    try:
        with pytest.raises(NotImplementedError):
            db = DatabaseBuildState(p)
    except Exception as e:
        raise e
    finally:
        p.unlink()


def test_database_get_files_not_implemented_error():
    p = Path(__file__).parent / 'bc_dbase.csv'
    with p.open('w') as f:
        f.write('Name,Source,Column 1,Column 2,Add Col 1,Mult Col 2,Add Col 2,Column 3,Column 4\n'
                '<<NAME>>,<<~e1~>><<~e2~>>_001.csv,inflow_time_hr,inflow_<<NAME>>,,,,,')
    try:
        with pytest.raises(NotImplementedError):
            db = DatabaseBuildState()
            db._get_files()
    except Exception as e:
        raise e
    finally:
        p.unlink()


def test_database_file_scopes_not_implemented_error():
    p = Path(__file__).parent / 'bc_dbase.csv'
    with p.open('w') as f:
        f.write('Name,Source,Column 1,Column 2,Add Col 1,Mult Col 2,Add Col 2,Column 3,Column 4\n'
                '<<NAME>>,<<~e1~>><<~e2~>>_001.csv,inflow_time_hr,inflow_<<NAME>>,,,,,')
    try:
        with pytest.raises(NotImplementedError):
            db = DatabaseBuildState()
            db._file_scopes()
    except Exception as e:
        raise e
    finally:
        p.unlink()


def test_database_resolve_scopes_not_implemented_error():
    p = Path(__file__).parent / 'bc_dbase.csv'
    with p.open('w') as f:
        f.write('Name,Source,Column 1,Column 2,Add Col 1,Mult Col 2,Add Col 2,Column 3,Column 4\n'
                '<<NAME>>,<<~e1~>><<~e2~>>_001.csv,inflow_time_hr,inflow_<<NAME>>,,,,,')
    try:
        with pytest.raises(NotImplementedError):
            db = DatabaseBuildState()
            db.figure_out_file_scopes([])
    except Exception as e:
        raise e
    finally:
        p.unlink()


def test_database_empty_get_files():
    p = Path(__file__).parent / 'bc_dbase.csv'
    with p.open('w') as f:
        f.write('Name,Source,Column 1,Column 2,Add Col 1,Mult Col 2,Add Col 2,Column 3,Column 4\n'
                'FC01,<<~e1~>><<~e2~>>_001.csv,inflow_time_hr,inflow_<<NAME>>,,,,,')
    with (Path(__file__).parent / '100y2h_001.csv').open('w') as f:
        f.write(
            'inflow_time_hr,inflow_FC01\n0.000,0\n0.083,0.84\n0.167,3.31\n0.250,4.6\n0.333,7.03\n0.417,12.39\n0.500,22.63')
    try:
        db = BCDatabase()
        db._get_files()
        assert db.index_to_file('FC01') == []
    except Exception as e:
        raise e
    finally:
        p.unlink()
        (Path(__file__).parent / '100y2h_001.csv').unlink()


def test_database_empty_resolve_scopes():
    p = Path(__file__).parent / 'bc_dbase.csv'
    with p.open('w') as f:
        f.write('Name,Source,Column 1,Column 2,Add Col 1,Mult Col 2,Add Col 2,Column 3,Column 4\n'
                'FC01,<<~e1~>><<~e2~>>_001.csv,inflow_time_hr,inflow_<<NAME>>,,,,,')
    with (Path(__file__).parent / '100y2h_001.csv').open('w') as f:
        f.write(
            'inflow_time_hr,inflow_FC01\n0.000,0\n0.083,0.84\n0.167,3.31\n0.250,4.6\n0.333,7.03\n0.417,12.39\n0.500,22.63')
    try:
        db = BCDatabase()
        db.figure_out_file_scopes([Scope('EVENT', '100y'), Scope('EVENT', '2h')])
        assert db._file_to_scope == {}
    except Exception as e:
        raise e
    finally:
        p.unlink()
        (Path(__file__).parent / '100y2h_001.csv').unlink()


def test_bc_database_get_item():
    p = Path(__file__).parent / 'bc_dbase.csv'
    with p.open('w') as f:
        f.write('Name,Source,Column 1,Column 2,Add Col 1,Mult Col 2,Add Col 2,Column 3,Column 4\n'
                'FC01,<<~e1~>><<~e2~>>_001.csv,inflow_time_hr,inflow_FC01,,,,,')
    try:
        db = BCDatabase(p)
        assert db['FC01'].tolist()[:3] == ['<<~e1~>><<~e2~>>_001.csv', 'inflow_time_hr', 'inflow_FC01']
    except Exception as e:
        raise e
    finally:
        p.unlink()


def test_bc_database_extract_value_no_scope():
    p = Path(__file__).parent / 'bc_dbase.csv'
    with p.open('w') as f:
        f.write('Name,Source,Column 1,Column 2,Add Col 1,Mult Col 2,Add Col 2,Column 3,Column 4\n'
                'FC01,100y2h_001.csv,inflow_time_hr,inflow_FC01,,,,,\n'
                'FC02,,,15.5,,,,,')
    with (Path(__file__).parent / '100y2h_001.csv').open('w') as f:
        f.write(
            'inflow_time_hr,inflow_FC01\n0.000,0\n0.083,0.84\n0.167,3.31\n0.250,4.6\n0.333,7.03\n0.417,12.39\n0.500,22.63')
    try:
        db = BCDatabase(p)
        db_ctx = db.context()
        qt = db_ctx.value('FC01')
        assert qt.iloc[:,0].tolist()[:3] == [0.0, 0.083, 0.167]
        assert qt.iloc[:,1].tolist()[:3] == [0.0, 0.84, 3.31]
        wl = db_ctx.value('FC02')
        assert wl == 15.5
    except Exception as e:
        raise e
    finally:
        p.unlink()
        (Path(__file__).parent / '100y2h_001.csv').unlink()


def test_bc_database_extract_value_no_scope_2():
    p = Path(__file__).parent / 'bc_dbase.csv'
    with p.open('w') as f:
        f.write('Name,Source,Column 1,Column 2,Add Col 1,Mult Col 2,Add Col 2,Column 3,Column 4\n'
                'FC01,100y2h_001.csv,inflow_time_hr,inflow_FC01,,,,,\n'
                'FC02,,,15.5,,,,,')
    with (Path(__file__).parent / '100y2h_001.csv').open('w') as f:
        f.write(
            'inflow_time_hr,inflow_FC01\n0.000,0\n0.083,0.84\n0.167,3.31\n0.250,4.6\n0.333,7.03\n0.417,12.39\n0.500,22.63')
    try:
        db = BCDatabase(p)
        qt = db.value('FC01')
        assert qt.iloc[:,0].tolist()[:3] == [0.0, 0.083, 0.167]
        assert qt.iloc[:,1].tolist()[:3] == [0.0, 0.84, 3.31]
        wl = db.value('FC02')
        assert wl == 15.5
    except Exception as e:
        raise e
    finally:
        p.unlink()
        (Path(__file__).parent / '100y2h_001.csv').unlink()


def test_bc_database_extract_value_context_req():
    p = Path(__file__).parent / 'bc_dbase.csv'
    with p.open('w') as f:
        f.write('Name,Source,Column 1,Column 2,Add Col 1,Mult Col 2,Add Col 2,Column 3,Column 4\n'
                'FC01,<<~e1~>><<~e2~>>_001.csv,inflow_time_hr,inflow_<<TP>>,,,,,\n'
                'FC02,,,<<WATER_LEVEL>>,,,,,')
    with (Path(__file__).parent / '100y2h_001.csv').open('w') as f:
        f.write(
            'inflow_time_hr,inflow_TP01\n0.000,0\n0.083,0.84\n0.167,3.31\n0.250,4.6\n0.333,7.03\n0.417,12.39\n0.500,22.63')
    try:
        ctx = Context(['s1', 'EXG', 's2', '5m', 'e1', '100y', 'e2', '2h'], {'TP': 'TP01', 'WATER_LEVEL': '15.5'})
        db = BCDatabase(p)
        db_ctx = db.context(context=ctx)
        qt = db_ctx.value('FC01')
        assert qt.iloc[:,0].tolist()[:3] == [0.0, 0.083, 0.167]
        assert qt.iloc[:,1].tolist()[:3] == [0.0, 0.84, 3.31]
        wl = db_ctx.value('FC02')
        assert wl == 15.5
    except Exception as e:
        raise e
    finally:
        p.unlink()
        (Path(__file__).parent / '100y2h_001.csv').unlink()


def test_bc_database_extract_value_multiple():
    p = Path(__file__).parent / 'bc_dbase.csv'
    with p.open('w') as f:
        f.write('Name,Source,Column 1,Column 2,Add Col 1,Mult Col 2,Add Col 2,Column 3,Column 4\n'
                'FC01,_event1__event2__001.csv,inflow_time_hr,inflow__TP_,,,,,\n'
                'FC02,,,<<WATER_LEVEL>>,,,,,')
    with (Path(__file__).parent / '100yr2hr_001.csv').open('w') as f:
        f.write(
            'inflow_time_hr,inflow_TP01,inflow_TP02\n0.000,0,0\n0.083,0.84,1.5\n0.167,3.31,6.2\n0.250,4.6,8\n0.333,7.03,12\n0.417,12.39,15\n0.500,22.63,50')
    with (Path(__file__).parent / '100yr1hr_001.csv').open('w') as f:
        f.write(
            'inflow_time_hr,inflow_TP01,inflow_TP02\n0.000,0,0\n0.083,0.1,5\n0.167,0.5,10\n0.250,2,15\n0.333,5,20\n0.417,7.5,25\n0.500,10.5,30')
    try:
        events = {'e1': ['Q100'], 'e2': ['1hr', '2hr'], 'e3': ['TP01', 'TP02']}
        event_db = EventDatabase({'Q100': Event('Q100', '_event1_', '100yr'), 'Q50': Event('Q50', '_event1_', '50yr'),
                                 '1hr': Event('1hr', '_event2_', '1hr'), '2hr': Event('2hr', '_event2_', '2hr'),
                                 'TP01': Event('TP01', '_TP_', 'TP01'), 'TP02': Event('TP02', '_TP_', 'TP02')})
        db = BCDatabase(p)
        qt = db.value('FC01', event_groups=events, event_db=event_db, variables={'WATER_LEVEL': '15.5'})
        assert len(qt) == 4
        assert qt['Q100 2hr TP01'].iloc[:,0].tolist()[:3] == [0.0, 0.083, 0.167]
        assert qt['Q100 2hr TP01'].iloc[:,1].tolist()[:3] == [0.0, 0.84, 3.31]
        wl = db.value('FC02', event_groups=events, event_db=event_db, variables={'WATER_LEVEL': '15.5'})
        assert len(wl) == 1
    except Exception as e:
        raise e
    finally:
        p.unlink()
        (Path(__file__).parent / '100yr2hr_001.csv').unlink()
        (Path(__file__).parent / '100yr1hr_001.csv').unlink()


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
        var_names = ['_event1_', '_event2_']
        db.load_variables(var_names)
        files = db.get_files()
        assert sorted(files) == sorted([file1, file2, file3, file4, file5, file6, file7, file8, file9])
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


def test_bc_dbase_scope_property():
    command = Command('Set Code == 0', Settings())
    input_ = InputBuildState(None, command)
    bc_dbase = BCDatabase('bc_dbase.csv', scope=input_.scope(False))
    assert bc_dbase._scope == [Scope('GLOBAL')]
    assert repr(bc_dbase) == '<BCDatabase> bc_dbase.csv (not found)'


def test_bc_base_empty_repr():
    bc_dbase = BCDatabase()
    assert repr(bc_dbase) == '<BCDatabase> (empty)'


def test_bc_dbase_file_to_scope_empty():
    file = Path(__file__).parent / 'bc_dbase.csv'
    with file.open('w') as f:
        f.write('Name,Source,Column 1,Column 2,Add Col 1,Mult Col 2,Add Col 2,Column 3,Column 4\n'
                'FC01,_event1__event2__001.csv,inflow_time_hr,inflow_FC01,,,,,\n'
                'FC02,,,15.5,,,,,')
    try:
        bc_dbase = BCDatabase(file)
        bc_dbase._df = None
        bc_dbase._file_scopes()
        assert bc_dbase
    except Exception as e:
        raise e
    finally:
        file.unlink()


def test_bc_dbase_scenario_groups():
    p = Path(__file__).parent / 'bc_dbase.csv'
    with p.open('w') as f:
        f.write('Name,Source,Column 1,Column 2,Add Col 1,Mult Col 2,Add Col 2,Column 3,Column 4\n'
                'FC01,_event1__event2__<<~s1~>>.csv,inflow_time_hr,inflow__TP_,,,,,\n'
                'FC02,,,<<WATER_LEVEL>>,,,,,')
    with (Path(__file__).parent / '100yr2hr_001.csv').open('w') as f:
        f.write(
            'inflow_time_hr,inflow_TP01,inflow_TP02\n0.000,0,0\n0.083,0.84,1.5\n0.167,3.31,6.2\n0.250,4.6,8\n0.333,7.03,12\n0.417,12.39,15\n0.500,22.63,50')
    with (Path(__file__).parent / '100yr1hr_001.csv').open('w') as f:
        f.write(
            'inflow_time_hr,inflow_TP01,inflow_TP02\n0.000,0,0\n0.083,0.1,5\n0.167,0.5,10\n0.250,2,15\n0.333,5,20\n0.417,7.5,25\n0.500,10.5,30')
    try:
        events = {'e1': ['Q100'], 'e2': ['1hr', '2hr'], 'e3': ['TP01', 'TP02']}
        scenarios = {'s1': ['EXG', 'D01'], 's2': ['001']}
        event_db = EventDatabase({'Q100': Event('Q100', '_event1_', '100yr'), 'Q50': Event('Q50', '_event1_', '50yr'),
                                  '1hr': Event('1hr', '_event2_', '1hr'), '2hr': Event('2hr', '_event2_', '2hr'),
                                  'TP01': Event('TP01', '_TP_', 'TP01'), 'TP02': Event('TP02', '_TP_', 'TP02')})
        db = BCDatabase(p)
        qt = db.value('FC01', event_groups=events, scenario_groups=scenarios, event_db=event_db, variables={'WATER_LEVEL': '15.5'})
        assert len(qt) == 4
        assert qt['Q100 2hr TP01 001'].iloc[:, 0].tolist()[:3] == [0.0, 0.083, 0.167]
        assert qt['Q100 2hr TP01 001'].iloc[:, 1].tolist()[:3] == [0.0, 0.84, 3.31]
        wl = db.value('FC02', event_groups=events, scenario_groups=scenarios, event_db=event_db, variables={'WATER_LEVEL': '15.5'})
        assert len(wl) == 1
    except Exception as e:
        raise e
    finally:
        p.unlink()
        (Path(__file__).parent / '100yr2hr_001.csv').unlink()
        (Path(__file__).parent / '100yr1hr_001.csv').unlink()


def test_bc_dbase_scenario_multi_var():
    p = Path(__file__).parent / 'bc_dbase.csv'
    with p.open('w') as f:
        f.write('Name,Source,Column 1,Column 2,Add Col 1,Mult Col 2,Add Col 2,Column 3,Column 4\n'
                'FC01,_event1__event2__<<~s1~>>.csv,inflow_time_hr,inflow__TP_,,,,,\n'
                'FC02,,,<<WATER_LEVEL>>,,,,,')
    with (Path(__file__).parent / '100yr2hr_001.csv').open('w') as f:
        f.write(
            'inflow_time_hr,inflow_TP01,inflow_TP02\n0.000,0,0\n0.083,0.84,1.5\n0.167,3.31,6.2\n0.250,4.6,8\n0.333,7.03,12\n0.417,12.39,15\n0.500,22.63,50')
    with (Path(__file__).parent / '100yr1hr_001.csv').open('w') as f:
        f.write(
            'inflow_time_hr,inflow_TP01,inflow_TP02\n0.000,0,0\n0.083,0.1,5\n0.167,0.5,10\n0.250,2,15\n0.333,5,20\n0.417,7.5,25\n0.500,10.5,30')
    try:
        events = {'e1': ['Q100'], 'e2': ['1hr', '2hr'], 'e3': ['TP01', 'TP02']}
        scenarios = {'s1': ['D01', 'D02'], 's2': ['001']}
        event_db = EventDatabase({'Q100': Event('Q100', '_event1_', '100yr'), 'Q50': Event('Q50', '_event1_', '50yr'),
                                  '1hr': Event('1hr', '_event2_', '1hr'), '2hr': Event('2hr', '_event2_', '2hr'),
                                  'TP01': Event('TP01', '_TP_', 'TP01'), 'TP02': Event('TP02', '_TP_', 'TP02')})
        var_inputs = Inputs([])
        command = Command('Set Variable WATER_LEVEL == 15.5', Settings())
        input = InputBuildState(None, command)
        input._scope = ScopeList([Scope('SCENARIO', 'D01')])
        var_inputs.append(input)
        command = Command('Set Variable WATER_LEVEL == 10.5', Settings())
        input = InputBuildState(None, command)
        input._scope = ScopeList([Scope('SCENARIO', 'D02')])
        var_inputs.append(input)
        db = BCDatabase(p)
        qt = db.value('FC01', event_groups=events, scenario_groups=scenarios, event_db=event_db, variables={'WATER_LEVEL': var_inputs})
        assert len(qt) == 4
        assert qt['Q100 2hr TP01 001'].iloc[:, 0].tolist()[:3] == [0.0, 0.083, 0.167]
        assert qt['Q100 2hr TP01 001'].iloc[:, 1].tolist()[:3] == [0.0, 0.84, 3.31]
        wl = db.value('FC02', event_groups=events, scenario_groups=scenarios, event_db=event_db, variables={'WATER_LEVEL': var_inputs})
        assert len(wl) == 2
        assert wl['D01'] == 15.5
        assert wl['D02'] == 10.5
    except Exception as e:
        raise e
    finally:
        p.unlink()
        (Path(__file__).parent / '100yr2hr_001.csv').unlink()
        (Path(__file__).parent / '100yr1hr_001.csv').unlink()


def test_not_implemented_error():
    db = DatabaseBuildState()
    with pytest.raises(NotImplementedError):
        db.get_value('path', None, 0)


def test_load_later():
    file = Path(__file__).parent / 'bc_dbase.csv'
    with file.open('w') as f:
        f.write('Name,Source,Column 1,Column 2,Add Col 1,Mult Col 2,Add Col 2,Column 3,Column 4\n'
                'FC01,_event1__event2__001.csv,inflow_time_hr,inflow_FC01,,,,,\n'
                'FC02,,,15.5,,,,,')
    try:
        bc_dbase = BCDatabase()
        bc_dbase.load(file)
        assert bc_dbase._path == file
    except Exception as e:
        raise e
    finally:
        file.unlink()


def test_load_variables_on_empty():
    bc_dbase = BCDatabase()
    bc_dbase.load_variables(['_ARI_'])
    assert bc_dbase._var_names == ['(<<.{1,}?>>)', '_ARI_']


def test_get_files_on_empty():
    bc_dbase = BCDatabase()
    assert bc_dbase.get_files() == []


def test_file_scope():
    file = Path(__file__).parent / 'bc_dbase.csv'
    with file.open('w') as f:
        f.write('Name,Source,Column 1,Column 2,Add Col 1,Mult Col 2,Add Col 2,Column 3,Column 4\n'
                'FC01,_event1__event2__001.csv,inflow_time_hr,inflow_FC01,,,,,\n'
                'FC02,,,15.5,,,,,')
    try:
        bc_dbase = BCDatabase(file)
        assert bc_dbase.file_scope(Path(__file__).parent / '_event1__event2__001.csv') == ScopeList([Scope('GLOBAL')])
        bc_dbase.load_variables(['_event1_', '_event2_'])
        assert bc_dbase.file_scope(Path(__file__).parent / '_event1__event2__001.csv') == \
               ScopeList([Scope('EVENT VARIABLE', '_event1_', var='_event1_'), Scope('EVENT VARIABLE', '_event2_', var='_event2_')])
    except Exception as e:
        raise e
    finally:
        file.unlink()


def test_value_errors():
    file = Path(__file__).parent / 'bc_dbase.csv'
    with file.open('w') as f:
        f.write('Name,Source,Column 1,Column 2,Add Col 1,Mult Col 2,Add Col 2,Column 3,Column 4\n'
                'FC01,_event1__event2__001.csv,inflow_time_hr,inflow_FC01,,,,,\n'
                'FC02,,,15.5,,,,,')
    try:
        bc_dbase = BCDatabase(file)
        with pytest.raises(KeyError):
            bc_dbase.value('FC03')
        with pytest.raises(AttributeError):
            bc_dbase.value('FC01', dummy=True)
    except Exception as e:
        raise e
    finally:
        file.unlink()
