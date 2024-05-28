from pathlib import Path
import os

import pytest

from tmf.convert_tuflow_model_gis_format.conv_tf_gis_format.helpers.parser import DefineBlock
from tmf.convert_tuflow_model_gis_format.conv_tf_gis_format.helpers.settings import ConvertSettings
from tmf.tuflow_model_files.inp._inp_build_state import *
from tmf.tuflow_model_files import *
from tmf.tuflow_model_files.inp.db import DatabaseInput
from tmf.tuflow_model_files.inp.file import FileInput
from tmf.tuflow_model_files.inp.gis import GisInput
from tmf.tuflow_model_files.inp.grid import GridInput
from tmf.tuflow_model_files.inp.setting import SettingInput
from tmf.tuflow_model_files.inp.tin import TinInput
from tmf.tuflow_model_files.dataclasses.file import TuflowPath
from tmf.tuflow_model_files import const


def test_input_init_blank():
    settings = ConvertSettings()
    line = ''
    command = Command(line, settings)
    input = InputBuildState(None, command)
    assert input.command is None
    assert input.value is None
    assert input._input == command
    assert input.get_files() == []


def test_input_init_fail():
    with pytest.raises(AttributeError):
        InputBuildState(None, '')

    with pytest.raises(TypeError):
        InputBuildState()


def test_input_init_setting():
    settings = ConvertSettings()
    line = 'Tutorial Model == ON'
    command = Command(line, settings)
    input = InputBuildState(None, command)
    assert isinstance(input, SettingInput)
    assert input.command == 'Tutorial Model'
    assert input.value == 'ON'
    assert input._input == command
    assert repr(input) == '<SettingInput> Tutorial Model == ON'
    assert input.TUFLOW_TYPE == const.INPUT.SETTING


def test_input_init_gis():
    settings = ConvertSettings()
    line = 'Read GIS Z Shape == gis/2d_zsh_brkline_001_L.shp'
    command = Command(line, settings)
    input = InputBuildState(None, command)
    assert isinstance(input, GisInput)
    assert input.command == 'Read GIS Z Shape'
    assert input.value == 'gis/2d_zsh_brkline_001_L.shp'
    assert input._input == command
    assert repr(input) == '<GisInput> Read GIS Z Shape == gis/2d_zsh_brkline_001_L.shp'
    assert input.TUFLOW_TYPE == const.INPUT.GIS


def test_input_init_grid():
    settings = ConvertSettings()
    line = 'Read GRID Zpts == grid/DEM_5m.tif'
    command = Command(line, settings)
    input = InputBuildState(None, command)
    assert isinstance(input, GridInput)
    assert input.command == 'Read GRID Zpts'
    assert input.value == 'grid/DEM_5m.tif'
    assert input._input == command
    assert repr(input) == '<GridInput> Read GRID Zpts == grid/DEM_5m.tif'
    assert input.TUFLOW_TYPE == const.INPUT.GRID


def test_input_init_tin():
    settings = ConvertSettings()
    line = 'Read TIN Zpts == tin/survey.12da'
    command = Command(line, settings)
    input = InputBuildState(None, command)
    assert isinstance(input, TinInput)
    assert input.command == 'Read TIN Zpts'
    assert input.value == 'tin/survey.12da'
    assert input._input == command
    assert repr(input) == '<TinInput> Read TIN Zpts == tin/survey.12da'
    assert input.TUFLOW_TYPE == const.INPUT.TIN


def test_input_init_database():
    settings = ConvertSettings()
    line = 'Read Material File == ../model/materials.csv'
    command = Command(line, settings)
    input = InputBuildState(None, command)
    assert isinstance(input, DatabaseInput)
    assert input.command == 'Read Material File'
    assert input.value == '../model/materials.csv'
    assert input._input == command
    assert repr(input) == '<DatabaseInput> Read Material File == ../model/materials.csv'
    assert input.TUFLOW_TYPE == const.INPUT.DB


def test_input_init_file():
    settings = ConvertSettings()
    line = 'Read File == ../model/read_grids.trd'
    command = Command(line, settings)
    input = InputBuildState(None, command)
    assert isinstance(input, FileInput)
    assert input.command == 'Read File'
    assert input.value == '../model/read_grids.trd'
    assert input._input == command
    assert repr(input) == '<ControlFileInput> Read File == ../model/read_grids.trd'
    assert input.TUFLOW_TYPE == const.INPUT.CF


def test_input_str_no_value():
    settings = ConvertSettings()
    line = 'Tutorial Model'
    command = Command(line, settings)
    input = InputBuildState(None, command)
    assert str(input) == 'Tutorial Model'


def test_input_float_tuple_value():
    settings = ConvertSettings()
    line = 'Model Origin (X,Y) == 0.0, 0.0'
    command = Command(line, settings)
    input = InputBuildState(None, command)
    assert input.value == (0.0, 0.0)


def test_input_str():
    settings = ConvertSettings()
    line = 'Tutorial Model == ON'
    command = Command(line, settings)
    input = InputBuildState(None, command)
    assert str(input) == 'Tutorial Model == ON'


def test_input_str_blank():
    settings = ConvertSettings()
    line = ''
    command = Command(line, settings)
    input = InputBuildState(None, command)
    assert str(input) == ''


def test_input_is_start_block():
    settings = ConvertSettings()
    line = 'If Scenario == EXG'
    command = Command(line, settings)
    input = InputBuildState(None, command)
    assert input.is_start_block() is True

    line = 'Tutorial Model == ON'
    command = Command(line, settings)
    input = InputBuildState(None, command)
    assert input.is_start_block() is False


def test_input_is_end_block():
    settings = ConvertSettings()
    line = 'End If'
    command = Command(line, settings)
    input = InputBuildState(None, command)
    assert input.is_end_block() is True

    line = 'Tutorial Model == ON'
    command = Command(line, settings)
    input = InputBuildState(None, command)
    assert input.is_end_block() is False


def test_input_scope_global():
    settings = ConvertSettings()
    line = 'Tutorial Model == ON'
    command = Command(line, settings)
    input = InputBuildState(None, command)
    assert input._scope == [Scope('GLOBAL', '')]


def test_input_scope_scenario():
    settings = ConvertSettings()
    line = 'Tutorial Model == ON'
    command = Command(line, settings)
    define_blocks = [DefineBlock('SCENARIO', 'EXG')]
    command.define_blocks = define_blocks
    input = InputBuildState(None, command)
    assert input._scope == [Scope('SCENARIO', 'EXG')]


def test_input_scope_scenario_else_replacement():
    settings = ConvertSettings()
    line = 'Tutorial Model == ON'
    command = Command(line, settings)
    define_blocks = [DefineBlock('SCENARIO', 'EXG'), DefineBlock('SCENARIO (ELSE)', 'EXG')]
    command.define_blocks = define_blocks
    input = InputBuildState(None, command)
    assert input._scope == [Scope('SCENARIO', 'EXG')]


def test_input_scope_1d_domain():
    settings = ConvertSettings()
    line = 'Tutorial Model == ON'
    command = Command(line, settings)
    define_blocks = [DefineBlock('1D DOMAIN', '')]
    command.define_blocks = define_blocks
    input = InputBuildState(None, command)
    assert input._scope == [Scope('GLOBAL', ''), Scope('1D DOMAIN', '')]


def test_input_scope_event():
    settings = ConvertSettings()
    line = 'BC Event Source == ARI | 100yr'
    command = Command(line, settings)
    define_blocks = [DefineBlock('EVENT', '100yr')]
    command.define_blocks = define_blocks
    input = InputBuildState(None, command)
    assert input._scope == [Scope('EVENT', '100yr')]


def test_input_multi_file():
    line = 'Read File == scenario_<<~s1~>>_test.trd'
    p = Path(__file__).parent / 'test_control_file.tcf'
    with p.open('w') as f:
        f.write(line)
    with (Path(__file__).parent / 'scenario_exg_test.trd').open('w') as f:
        f.write('banana')
    with (Path(__file__).parent / 'scenario_dev_test.trd').open('w') as f:
        f.write('pineapple')
    try:
        settings = ConvertSettings(*['-tcf', str(p)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        assert sorted([x.name for x in input.files]) == sorted(['scenario_dev_test.trd', 'scenario_exg_test.trd'])
    except Exception as e:
        raise e
    finally:
        p.unlink()
        (Path(__file__).parent / 'scenario_exg_test.trd').unlink()
        (Path(__file__).parent / 'scenario_dev_test.trd').unlink()


def test_input_multi_gis_file_scenarios():
    line = 'Read GIS Z Shape == <<~s1~>>_zsh_brkline_001_L.shp'
    p = Path(__file__).parent / 'test_control_file.tcf'
    with p.open('w') as f:
        f.write(line)
    with (Path(__file__).parent / 'dev_zsh_brkline_001_L.shp').open('w') as f:
        f.write('banana')
    with (Path(__file__).parent / 'exg_zsh_brkline_001_L.shp').open('w') as f:
        f.write('pineapple')
    try:
        settings = ConvertSettings(*['-tcf', str(p)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        assert sorted([x.name for x in input.files]) == sorted(['dev_zsh_brkline_001_L.shp >> dev_zsh_brkline_001_L',
                                                 'exg_zsh_brkline_001_L.shp >> exg_zsh_brkline_001_L'])
    except Exception as e:
        raise e
    finally:
        p.unlink()
        (Path(__file__).parent / 'dev_zsh_brkline_001_L.shp').unlink()
        (Path(__file__).parent / 'exg_zsh_brkline_001_L.shp').unlink()

def test_input_multi_gis_file_pipe():
    line = 'Read GIS Z Shape == exg_zsh_brkline_001_L.shp | exg_zsh_brkline_001_P.shp'
    p = Path(__file__).parent / 'test_control_file.tcf'
    with p.open('w') as f:
        f.write(line)
    with (Path(__file__).parent / 'exg_zsh_brkline_001_L.shp').open('w') as f:
        f.write('banana')
    with (Path(__file__).parent / 'exg_zsh_brkline_001_P.shp').open('w') as f:
        f.write('pineapple')
    try:
        settings = ConvertSettings(*['-tcf', str(p)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        assert sorted([x.name for x in input.files]) == sorted(['exg_zsh_brkline_001_L.shp >> exg_zsh_brkline_001_L',
                                                 'exg_zsh_brkline_001_P.shp >> exg_zsh_brkline_001_P'])
    except Exception as e:
        raise e
    finally:
        p.unlink()
        (Path(__file__).parent / 'exg_zsh_brkline_001_L.shp').unlink()
        (Path(__file__).parent / 'exg_zsh_brkline_001_P.shp').unlink()

def test_input_multi_gis_file_pipe_scenarios():
    line = 'Read GIS Z Shape == exg_zsh_brkline_001_P.shp | <<~s1~>>_zsh_brkline_001_L.shp'
    p = Path(__file__).parent / 'test_control_file.tcf'
    with p.open('w') as f:
        f.write(line)
    with (Path(__file__).parent / 'exg_zsh_brkline_001_P.shp').open('w') as f:
        f.write('banana')
    with (Path(__file__).parent / 'dev_zsh_brkline_001_L.shp').open('w') as f:
        f.write('banana')
    with (Path(__file__).parent / 'exg_zsh_brkline_001_L.shp').open('w') as f:
        f.write('pineapple')
    try:
        settings = ConvertSettings(*['-tcf', str(p)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        assert sorted([x.name for x in input.files]) == sorted(['exg_zsh_brkline_001_P.shp >> exg_zsh_brkline_001_P',
                                                 'dev_zsh_brkline_001_L.shp >> dev_zsh_brkline_001_L',
                                                 'exg_zsh_brkline_001_L.shp >> exg_zsh_brkline_001_L'])
    except Exception as e:
        raise e
    finally:
        p.unlink()
        (Path(__file__).parent / 'exg_zsh_brkline_001_P.shp').unlink()
        (Path(__file__).parent / 'dev_zsh_brkline_001_L.shp').unlink()
        (Path(__file__).parent / 'exg_zsh_brkline_001_L.shp').unlink()


def test_input_multi_gis_file_pipe_value():
    line = 'Read GIS Z Shape == exg_zsh_brkline_001_L.shp | 10'
    p = Path(__file__).parent / 'test_control_file.tcf'
    with p.open('w') as f:
        f.write(line)
    with (Path(__file__).parent / 'exg_zsh_brkline_001_L.shp').open('w') as f:
        f.write('banana')
    try:
        settings = ConvertSettings(*['-tcf', str(p)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        assert sorted([x.name for x in input.files]) == sorted(['exg_zsh_brkline_001_L.shp >> exg_zsh_brkline_001_L'])
    except Exception as e:
        raise e
    finally:
        p.unlink()
        (Path(__file__).parent / 'exg_zsh_brkline_001_L.shp').unlink()


def test_input_multi_grid_file_scenarios():
    line = 'Read Grid Zpts == <<~s1~>>_grid_001.tif'
    p = Path(__file__).parent / 'test_control_file.tcf'
    with p.open('w') as f:
        f.write(line)
    with (Path(__file__).parent / 'dev_grid_001.tif').open('w') as f:
        f.write('banana')
    with (Path(__file__).parent / 'exg_grid_001.tif').open('w') as f:
        f.write('pineapple')
    try:
        settings = ConvertSettings(*['-tcf', str(p)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        assert sorted([x.name for x in input.files]) == sorted(['dev_grid_001.tif >> dev_grid_001',
                                                 'exg_grid_001.tif >> exg_grid_001'])
    except Exception as e:
        raise e
    finally:
        p.unlink()
        (Path(__file__).parent / 'dev_grid_001.tif').unlink()
        (Path(__file__).parent / 'exg_grid_001.tif').unlink()

def test_input_multi_grid_file_pipe():
    line = 'Read Grid Zpts == exg_grid_001.tif | polygon.shp'
    p = Path(__file__).parent / 'test_control_file.tcf'
    with p.open('w') as f:
        f.write(line)
    with (Path(__file__).parent / 'exg_grid_001.tif').open('w') as f:
        f.write('banana')
    with (Path(__file__).parent / 'polygon.shp').open('w') as f:
        f.write('banana')
    try:
        settings = ConvertSettings(*['-tcf', str(p)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        assert sorted([x.name for x in input.files]) == sorted(['exg_grid_001.tif >> exg_grid_001',
                                                 'polygon.shp >> polygon'])
    except Exception as e:
        raise e
    finally:
        p.unlink()
        (Path(__file__).parent / 'exg_grid_001.tif').unlink()
        (Path(__file__).parent / 'polygon.shp').unlink()

def test_input_multi_grid_file_pipe_scenario():
    line = 'Read Grid Zpts == exg_grid_001.tif | polygon_<<~s1~>>.shp'
    p = Path(__file__).parent / 'test_control_file.tcf'
    with p.open('w') as f:
        f.write(line)
    with (Path(__file__).parent / 'exg_grid_001.tif').open('w') as f:
        f.write('banana')
    with (Path(__file__).parent / 'polygon_exg.shp').open('w') as f:
        f.write('banana')
    with (Path(__file__).parent / 'polygon_dev.shp').open('w') as f:
        f.write('banana')
    try:
        settings = ConvertSettings(*['-tcf', str(p)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        assert sorted([x.name for x in input.files]) == sorted(['exg_grid_001.tif >> exg_grid_001',
                                                 'polygon_dev.shp >> polygon_dev',
                                                 'polygon_exg.shp >> polygon_exg'])
    except Exception as e:
        raise e
    finally:
        p.unlink()
        (Path(__file__).parent / 'exg_grid_001.tif').unlink()
        (Path(__file__).parent / 'polygon_exg.shp').unlink()
        (Path(__file__).parent / 'polygon_dev.shp').unlink()


def test_input_multi_tin_file_scenarios():
    line = 'Read Tin Zpts == <<~s1~>>_tin_001.12da'
    p = Path(__file__).parent / 'test_control_file.tcf'
    with p.open('w') as f:
        f.write(line)
    with (Path(__file__).parent / 'dev_tin_001.12da').open('w') as f:
        f.write('banana')
    with (Path(__file__).parent / 'exg_tin_001.12da').open('w') as f:
        f.write('pineapple')
    try:
        settings = ConvertSettings(*['-tcf', str(p)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        assert sorted([x.name for x in input.files]) == sorted(['dev_tin_001.12da', 'exg_tin_001.12da'])
    except Exception as e:
        raise e
    finally:
        p.unlink()
        (Path(__file__).parent / 'dev_tin_001.12da').unlink()
        (Path(__file__).parent / 'exg_tin_001.12da').unlink()

def test_input_multi_tin_file_pipe():
    line = 'Read Tin Zpts == exg_tin_001.12da | polygon.shp'
    p = Path(__file__).parent / 'test_control_file.tcf'
    with p.open('w') as f:
        f.write(line)
    with (Path(__file__).parent / 'exg_tin_001.12da').open('w') as f:
        f.write('banana')
    with (Path(__file__).parent / 'polygon.shp').open('w') as f:
        f.write('banana')
    try:
        settings = ConvertSettings(*['-tcf', str(p)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        assert sorted([x.name for x in input.files]) == sorted(['exg_tin_001.12da', 'polygon.shp >> polygon'])
    except Exception as e:
        raise e
    finally:
        p.unlink()
        (Path(__file__).parent / 'exg_tin_001.12da').unlink()
        (Path(__file__).parent / 'polygon.shp').unlink()


def test_input_multi_tin_file_pipe_scenario():
    line = 'Read Tin Zpts == exg_tin_001.12da | polygon_<<~s1~>>.shp'
    p = Path(__file__).parent / 'test_control_file.tcf'
    with p.open('w') as f:
        f.write(line)
    with (Path(__file__).parent / 'exg_tin_001.12da').open('w') as f:
        f.write('banana')
    with (Path(__file__).parent / 'polygon_exg.shp').open('w') as f:
        f.write('banana')
    with (Path(__file__).parent / 'polygon_dev.shp').open('w') as f:
        f.write('banana')
    try:
        settings = ConvertSettings(*['-tcf', str(p)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        assert sorted([x.name for x in input.files]) == sorted(['exg_tin_001.12da',
                                                 'polygon_dev.shp >> polygon_dev',
                                                 'polygon_exg.shp >> polygon_exg'])
    except Exception as e:
        raise e
    finally:
        p.unlink()
        (Path(__file__).parent / 'exg_tin_001.12da').unlink()
        (Path(__file__).parent / 'polygon_exg.shp').unlink()
        (Path(__file__).parent / 'polygon_dev.shp').unlink()


def test_input_file_scope_scenarios_simple():
    line = 'Read File == <<~s1~>>_001.trd'
    p = Path(__file__).parent / 'test_control_file.tcf'
    with p.open('w') as f:
        f.write(line)
    with (Path(__file__).parent / 'test_001.trd').open('w') as f:
        f.write('banana')
    try:
        settings = ConvertSettings(*['-tcf', str(p)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        assert sorted([input.file_scope(x) for x in input.files]) == sorted([[Scope('SCENARIO', 'test')]])
    except Exception as e:
        raise e
    finally:
        p.unlink()
        (Path(__file__).parent / 'test_001.trd').unlink()


def test_input_file_scope_scenarios_simple_2():
    line = 'Read GIS Z Shape == <<~s1~>>_zsh_brkline_001_L.shp'
    p = Path(__file__).parent / 'test_control_file.tcf'
    with p.open('w') as f:
        f.write(line)
    with (Path(__file__).parent / 'dev_zsh_brkline_001_L.shp').open('w') as f:
        f.write('banana')
    with (Path(__file__).parent / 'exg_zsh_brkline_001_L.shp').open('w') as f:
        f.write('pineapple')
    try:
        settings = ConvertSettings(*['-tcf', str(p)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        assert sorted([input.file_scope(x) for x in input.files]) == sorted([[Scope('SCENARIO', 'dev')], [Scope('SCENARIO', 'exg')]])
    except Exception as e:
        raise e
    finally:
        p.unlink()
        (Path(__file__).parent / 'dev_zsh_brkline_001_L.shp').unlink()
        (Path(__file__).parent / 'exg_zsh_brkline_001_L.shp').unlink()


def test_input_file_scope_scenarios_ambiguous():
    line = 'Read File == <<~s1~>><<~s2~>>_001.trd'
    p = Path(__file__).parent / 'test_control_file.tcf'
    with p.open('w') as f:
        f.write(line)
    with (Path(__file__).parent / 'testexample_001.trd').open('w') as f:
        f.write('banana')
    try:
        settings = ConvertSettings(*['-tcf', str(p)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        assert sorted([input.file_scope(x) for x in input.files]) == sorted([[Scope('SCENARIO', '<<~s1~>>'), Scope('SCENARIO', '<<~s2~>>')]])
    except Exception as e:
        raise e
    finally:
        p.unlink()
        (Path(__file__).parent / 'testexample_001.trd').unlink()

def test_input_file_scope_scenarios_ambiguous_2():
    line = 'Read File == <<~s1~>><<~s2~>>_<<~s1~>>_001.trd'
    p = Path(__file__).parent / 'test_control_file.tcf'
    with p.open('w') as f:
        f.write(line)
    with (Path(__file__).parent / 'testexample_test_001.trd').open('w') as f:
        f.write('banana')
    try:
        settings = ConvertSettings(*['-tcf', str(p)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        assert sorted([input.file_scope(x) for x in input.files]) == sorted([[Scope('SCENARIO', 'test'), Scope('SCENARIO', '<<~s2~>>')]])
    except Exception as e:
        raise e
    finally:
        p.unlink()
        (Path(__file__).parent / 'testexample_test_001.trd').unlink()

def test_input_file_scope_scenarios_ambiguous_3():
    line = 'Read File == <<~s1~>><<~s2~>>_<<~s2~>>_002.trd'
    p = Path(__file__).parent / 'test_control_file.tcf'
    with p.open('w') as f:
        f.write(line)
    with (Path(__file__).parent / 'testexample_example_002.trd').open('w') as f:
        f.write('banana')
    try:
        settings = ConvertSettings(*['-tcf', str(p)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        assert sorted([input.file_scope(x) for x in input.files]) == sorted([[Scope('SCENARIO', '<<~s1~>>'), Scope('SCENARIO', 'example')]])
    except Exception as e:
        raise e
    finally:
        p.unlink()
        (Path(__file__).parent / 'testexample_example_002.trd').unlink()

def test_input_file_scope_scenarios_ambiguous_4():
    line = 'Read File == <<~s1~>>_<<~s1~>><<~s2~>>_002.trd'
    p = Path(__file__).parent / 'test_control_file.tcf'
    with p.open('w') as f:
        f.write(line)
    with (Path(__file__).parent / 'test_testexample_002.trd').open('w') as f:
        f.write('banana')
    try:
        settings = ConvertSettings(*['-tcf', str(p)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        assert sorted([input.file_scope(x) for x in input.files]) == sorted([[Scope('SCENARIO', 'test'), Scope('SCENARIO', '<<~s2~>>')]])
    except Exception as e:
        raise e
    finally:
        p.unlink()
        (Path(__file__).parent / 'test_testexample_002.trd').unlink()

def test_input_file_scope_scenarios_ambiguous_5():
    line = 'Read File == <<~s2~>>_<<~s1~>><<~s2~>>_002.trd'
    p = Path(__file__).parent / 'test_control_file.tcf'
    with p.open('w') as f:
        f.write(line)
    with (Path(__file__).parent / 'example_testexample_002.trd').open('w') as f:
        f.write('banana')
    try:
        settings = ConvertSettings(*['-tcf', str(p)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        assert sorted([input.file_scope(x) for x in input.files]) == sorted([[Scope('SCENARIO', 'example'), Scope('SCENARIO', '<<~s1~>>')]])
    except Exception as e:
        raise e
    finally:
        p.unlink()
        (Path(__file__).parent / 'example_testexample_002.trd').unlink()


def test_input_file_scope_scenarios_ambiguous_6():
    line = 'Read File == <<~s1~>><<~s2~>>_<<~s1~>><<~s2~>>_002.trd'
    p = Path(__file__).parent / 'test_control_file.tcf'
    with p.open('w') as f:
        f.write(line)
    with (Path(__file__).parent / 'testexample_testexample_002.trd').open('w') as f:
        f.write('banana')
    try:
        settings = ConvertSettings(*['-tcf', str(p)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        assert sorted([input.file_scope(x) for x in input.files]) == sorted([[Scope('SCENARIO', '<<~s1~>>'), Scope('SCENARIO', '<<~s2~>>')]])
    except Exception as e:
        raise e
    finally:
        p.unlink()
        (Path(__file__).parent / 'testexample_testexample_002.trd').unlink()


def test_input_file_scope_scenario_no_file():
    line = 'Read File == <<~s1~>>_001.trd'
    p = Path(__file__).parent / 'test_control_file.tcf'
    with p.open('w') as f:
        f.write(line)
    try:
        settings = ConvertSettings(*['-tcf', str(p)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        assert sorted([input.file_scope(x) for x in input.files]) == sorted([[Scope('SCENARIO', '<<~s1~>>')]])
    except Exception as e:
        raise e
    finally:
        p.unlink()


def test_input_file_scope_events_simple():
    line = 'Read File == <<~e1~>>_001.trd'
    p = Path(__file__).parent / 'test_control_file.tcf'
    with p.open('w') as f:
        f.write(line)
    with (Path(__file__).parent / 'test_001.trd').open('w') as f:
        f.write('banana')
    try:
        settings = ConvertSettings(*['-tcf', str(p)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        assert sorted([input.file_scope(x) for x in input.files]) == sorted([[Scope('EVENT', 'test')]])
    except Exception as e:
        raise e
    finally:
        p.unlink()
        (Path(__file__).parent / 'test_001.trd').unlink()


def test_input_file_scope_events_simple_2():
    line = 'Read GIS Z Shape == <<~e1~>>_zsh_brkline_001_L.shp'
    p = Path(__file__).parent / 'test_control_file.tcf'
    with p.open('w') as f:
        f.write(line)
    with (Path(__file__).parent / 'dev_zsh_brkline_001_L.shp').open('w') as f:
        f.write('banana')
    with (Path(__file__).parent / 'exg_zsh_brkline_001_L.shp').open('w') as f:
        f.write('pineapple')
    try:
        settings = ConvertSettings(*['-tcf', str(p)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        assert sorted([input.file_scope(x) for x in input.files]) == sorted([[Scope('EVENT', 'dev')], [Scope('EVENT', 'exg')]])
    except Exception as e:
        raise e
    finally:
        p.unlink()
        (Path(__file__).parent / 'dev_zsh_brkline_001_L.shp').unlink()
        (Path(__file__).parent / 'exg_zsh_brkline_001_L.shp').unlink()


def test_input_file_scope_events_ambiguous():
    line = 'Read File == <<~e1~>><<~e2~>>_001.trd'
    p = Path(__file__).parent / 'test_control_file.tcf'
    with p.open('w') as f:
        f.write(line)
    with (Path(__file__).parent / 'testexample_001.trd').open('w') as f:
        f.write('banana')
    try:
        settings = ConvertSettings(*['-tcf', str(p)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        assert sorted([input.file_scope(x) for x in input.files]) == sorted([[Scope('EVENT', '<<~e1~>>'), Scope('EVENT', '<<~e2~>>')]])
    except Exception as e:
        raise e
    finally:
        p.unlink()
        (Path(__file__).parent / 'testexample_001.trd').unlink()

def test_input_file_scope_events_ambiguous_2():
    line = 'Read File == <<~e1~>><<~e2~>>_<<~e1~>>_001.trd'
    p = Path(__file__).parent / 'test_control_file.tcf'
    with p.open('w') as f:
        f.write(line)
    with (Path(__file__).parent / 'testexample_test_001.trd').open('w') as f:
        f.write('banana')
    try:
        settings = ConvertSettings(*['-tcf', str(p)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        assert sorted([input.file_scope(x) for x in input.files]) == sorted([[Scope('EVENT', 'test'), Scope('EVENT', '<<~e2~>>')]])
    except Exception as e:
        raise e
    finally:
        p.unlink()
        (Path(__file__).parent / 'testexample_test_001.trd').unlink()

def test_input_file_scope_events_ambiguous_3():
    line = 'Read File == <<~e1~>><<~e2~>>_<<~e2~>>_002.trd'
    p = Path(__file__).parent / 'test_control_file.tcf'
    with p.open('w') as f:
        f.write(line)
    with (Path(__file__).parent / 'testexample_example_002.trd').open('w') as f:
        f.write('banana')
    try:
        settings = ConvertSettings(*['-tcf', str(p)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        assert sorted([input.file_scope(x) for x in input.files]) == sorted([[Scope('EVENT', '<<~e1~>>'), Scope('EVENT', 'example')]])
    except Exception as e:
        raise e
    finally:
        p.unlink()
        (Path(__file__).parent / 'testexample_example_002.trd').unlink()

def test_input_file_scope_events_ambiguous_4():
    line = 'Read File == <<~e1~>>_<<~e1~>><<~e2~>>_002.trd'
    p = Path(__file__).parent / 'test_control_file.tcf'
    with p.open('w') as f:
        f.write(line)
    with (Path(__file__).parent / 'test_testexample_002.trd').open('w') as f:
        f.write('banana')
    try:
        settings = ConvertSettings(*['-tcf', str(p)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        assert sorted([input.file_scope(x) for x in input.files]) == sorted([[Scope('EVENT', 'test'), Scope('EVENT', '<<~e2~>>')]])
    except Exception as e:
        raise e
    finally:
        p.unlink()
        (Path(__file__).parent / 'test_testexample_002.trd').unlink()

def test_input_file_scope_events_ambiguous_5():
    line = 'Read File == <<~e2~>>_<<~e1~>><<~e2~>>_002.trd'
    p = Path(__file__).parent / 'test_control_file.tcf'
    with p.open('w') as f:
        f.write(line)
    with (Path(__file__).parent / 'example_testexample_002.trd').open('w') as f:
        f.write('banana')
    try:
        settings = ConvertSettings(*['-tcf', str(p)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        assert sorted([input.file_scope(x) for x in input.files]) == sorted([[Scope('EVENT', 'example'), Scope('EVENT', '<<~e1~>>')]])
    except Exception as e:
        raise e
    finally:
        p.unlink()
        (Path(__file__).parent / 'example_testexample_002.trd').unlink()


def test_input_file_scope_event_no_file():
    line = 'Read File == <<~e1~>>_001.trd'
    p = Path(__file__).parent / 'test_control_file.tcf'
    with p.open('w') as f:
        f.write(line)
    try:
        settings = ConvertSettings(*['-tcf', str(p)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        assert [input.file_scope(x) for x in input.files] == [[Scope('EVENT', '<<~e1~>>')]]
    except Exception as e:
        raise e
    finally:
        p.unlink()


def test_input_file_scope_variables_simple():
    line = 'Read File == <<CELL_SIZE>>_<<CELL_SIZE>>_001.trd'
    p = Path(__file__).parent / 'test_control_file.tcf'
    with p.open('w') as f:
        f.write(line)
    with (Path(__file__).parent / '10m_10m_001.trd').open('w') as f:
        f.write('banana')
    try:
        settings = ConvertSettings(*['-tcf', str(p)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        assert [input.file_scope(x) for x in input.files] == [[Scope('VARIABLE', '<<CELL_SIZE>>')]]
    except Exception as e:
        raise e
    finally:
        p.unlink()
        (Path(__file__).parent / '10m_10m_001.trd').unlink()


def test_input_resolve_scope():
    line = 'Read File == <<~s1~>><<~s2~>>_001.trd\n'
    p = Path(__file__).parent / 'test_control_file.tcf'
    with p.open('w') as f:
        f.write(line)
    with (Path(__file__).parent / 'testexample_001.trd').open('w') as f:
        f.write('banana')
    try:
        settings = ConvertSettings(*['-tcf', str(p)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        scopes = [Scope('SCENARIO', 'test'), Scope('SCENARIO', 'example')]
        input.figure_out_file_scopes(scopes)
        assert [input.file_scope(x) for x in input.files] == [scopes]
    except Exception as e:
        raise e
    finally:
        p.unlink()
        (Path(__file__).parent / 'testexample_001.trd').unlink()


def test_input_resolve_scope_known():
    line = 'Read File == <<~s1~>>_001.trd\n'
    p = Path(__file__).parent / 'test_control_file.tcf'
    with p.open('w') as f:
        f.write(line)
    with (Path(__file__).parent / 'test_001.trd').open('w') as f:
        f.write('banana')
    try:
        settings = ConvertSettings(*['-tcf', str(p)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        scopes = [Scope('SCENARIO', 'test')]
        input.figure_out_file_scopes(scopes)
        assert [input.file_scope(x) for x in input.files] == [[Scope('SCENARIO', 'test')]]
    except Exception as e:
        raise e
    finally:
        p.unlink()
        (Path(__file__).parent / 'test_001.trd').unlink()


def test_input_get_files_basic():
    line = 'Read GIS Z Shape == 2d_zsh_brkline_scen1_001_P.shp\n'
    tcf = Path(__file__).parent / 'test_control_file.tcf'
    with tcf.open('w') as f:
        f.write(line)
    file = Path(__file__).parent / '2d_zsh_brkline_scen1_001_P.shp'
    with file.open('w') as f:
        f.write('banana')
    try:
        settings = ConvertSettings(*['-tcf', str(tcf)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        files = input.get_files()
        assert files == [file]
    except Exception as e:
        raise e
    finally:
        tcf.unlink()
        file.unlink()


def test_input_get_files_basic_2():
    line = 'Read GIS Z Shape == 2d_zsh_brkline_scen1_001_P.shp | 2d_zsh_brkline_scen1_001_L.shp\n'
    tcf = Path(__file__).parent / 'test_control_file.tcf'
    with tcf.open('w') as f:
        f.write(line)
    file1 = Path(__file__).parent / '2d_zsh_brkline_scen1_001_P.shp'
    with file1.open('w') as f:
        f.write('banana')
    file2 = Path(__file__).parent / '2d_zsh_brkline_scen1_001_L.shp'
    with file2.open('w') as f:
        f.write('banana')
    try:
        settings = ConvertSettings(*['-tcf', str(tcf)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        files = input.get_files()
        assert files == [file1, file2]
    except Exception as e:
        raise e
    finally:
        tcf.unlink()
        file1.unlink()
        file2.unlink()


def test_input_get_files():
    line = 'Read GIS Z Shape == 2d_zsh_brkline_<<~s~>>_001_P.shp | 2d_zsh_brkline_<<~s~>>_001_L.shp\n'
    tcf = Path(__file__).parent / 'test_control_file.tcf'
    with tcf.open('w') as f:
        f.write(line)
    file1 = Path(__file__).parent / '2d_zsh_brkline_scen1_001_P.shp'
    with file1.open('w') as f:
        f.write('banana')
    file2 = Path(__file__).parent / '2d_zsh_brkline_scen1_001_L.shp'
    with file2.open('w') as f:
        f.write('banana')
    file3 = Path(__file__).parent / '2d_zsh_brkline_scen2_001_P.shp'
    with file3.open('w') as f:
        f.write('banana')
    file4 = Path(__file__).parent / '2d_zsh_brkline_scen2_001_L.shp'
    with file4.open('w') as f:
        f.write('banana')
    try:
        settings = ConvertSettings(*['-tcf', str(tcf)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        files = input.get_files()
        assert sorted(files) == sorted([file1, file2, file3, file4])
    except Exception as e:
        raise e
    finally:
        tcf.unlink()
        file1.unlink()
        file2.unlink()
        file3.unlink()
        file4.unlink()


def test_input_get_files_2():
    line = 'Read GIS Z Shape == 2d_zsh_brkline_<<~s1~>><<~s2~>>_001_P.shp | 2d_zsh_brkline_<<~s1~>><<~s2~>>_001_L.shp\n'
    tcf = Path(__file__).parent / 'test_control_file.tcf'
    with tcf.open('w') as f:
        f.write(line)
    file1 = Path(__file__).parent / '2d_zsh_brkline_scen15m_001_P.shp'
    with file1.open('w') as f:
        f.write('banana')
    file2 = Path(__file__).parent / '2d_zsh_brkline_scen15m_001_L.shp'
    with file2.open('w') as f:
        f.write('banana')
    file3 = Path(__file__).parent / '2d_zsh_brkline_scen25m_001_P.shp'
    with file3.open('w') as f:
        f.write('banana')
    file4 = Path(__file__).parent / '2d_zsh_brkline_scen25m_001_L.shp'
    with file4.open('w') as f:
        f.write('banana')
    file5 = Path(__file__).parent / '2d_zsh_brkline_scen22.5m_001_P.shp'
    with file5.open('w') as f:
        f.write('banana')
    file6 = Path(__file__).parent / '2d_zsh_brkline_scen22.5m_001_L.shp'
    with file6.open('w') as f:
        f.write('banana')
    try:
        settings = ConvertSettings(*['-tcf', str(tcf)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        files = input.get_files()
        assert sorted(files) == sorted([file1, file2, file3, file4, file5, file6])
    except Exception as e:
        raise e
    finally:
        tcf.unlink()
        file1.unlink()
        file2.unlink()
        file3.unlink()
        file4.unlink()
        file5.unlink()
        file6.unlink()


def test_input_get_files_basic_grid():
    line = 'Read GRID Zpts == 2d_zsh_brkline_scen1_001_P.tif | 2d_zsh_brkline_scen1_001_R.shp\n'
    tcf = Path(__file__).parent / 'test_control_file.tcf'
    with tcf.open('w') as f:
        f.write(line)
    file1 = Path(__file__).parent / '2d_zsh_brkline_scen1_001_P.tif'
    with file1.open('w') as f:
        f.write('banana')
    file2 = Path(__file__).parent / '2d_zsh_brkline_scen1_001_R.shp'
    with file2.open('w') as f:
        f.write('banana')
    try:
        settings = ConvertSettings(*['-tcf', str(tcf)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        files = input.get_files()
        assert sorted(files) == sorted([file1, file2])
    except Exception as e:
        raise e
    finally:
        tcf.unlink()
        file1.unlink()
        file2.unlink()


def test_input_get_files_grid():
    line = 'Read GRID Zpts == 2d_zsh_brkline_<<~s1~>><<~s2~>>_001_P.tif | 2d_zsh_brkline_<<~s1~>><<~s2~>>_001_L.shp\n'
    tcf = Path(__file__).parent / 'test_control_file.tcf'
    with tcf.open('w') as f:
        f.write(line)
    file1 = Path(__file__).parent / '2d_zsh_brkline_scen15m_001_P.tif'
    with file1.open('w') as f:
        f.write('banana')
    file2 = Path(__file__).parent / '2d_zsh_brkline_scen15m_001_L.shp'
    with file2.open('w') as f:
        f.write('banana')
    file3 = Path(__file__).parent / '2d_zsh_brkline_scen25m_001_P.tif'
    with file3.open('w') as f:
        f.write('banana')
    file4 = Path(__file__).parent / '2d_zsh_brkline_scen25m_001_L.shp'
    with file4.open('w') as f:
        f.write('banana')
    file5 = Path(__file__).parent / '2d_zsh_brkline_scen22.5m_001_P.tif'
    with file5.open('w') as f:
        f.write('banana')
    file6 = Path(__file__).parent / '2d_zsh_brkline_scen22.5m_001_L.shp'
    with file6.open('w') as f:
        f.write('banana')
    try:
        settings = ConvertSettings(*['-tcf', str(tcf)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        files = input.get_files()
        assert sorted(files) == sorted([file1, file2, file3, file4, file5, file6])
    except Exception as e:
        raise e
    finally:
        tcf.unlink()
        file1.unlink()
        file2.unlink()
        file3.unlink()
        file4.unlink()
        file5.unlink()
        file6.unlink()


def test_input_get_files_basic_tin():
    line = 'Read TIN Zpts == 2d_zsh_brkline_scen1_001_P.12da | 2d_zsh_brkline_scen1_001_R.shp\n'
    tcf = Path(__file__).parent / 'test_control_file.tcf'
    with tcf.open('w') as f:
        f.write(line)
    file1 = Path(__file__).parent / '2d_zsh_brkline_scen1_001_P.12da'
    with file1.open('w') as f:
        f.write('banana')
    file2 = Path(__file__).parent / '2d_zsh_brkline_scen1_001_R.shp'
    with file2.open('w') as f:
        f.write('banana')
    try:
        settings = ConvertSettings(*['-tcf', str(tcf)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        files = input.get_files()
        assert sorted(files) == sorted([file1, file2])
    except Exception as e:
        raise e
    finally:
        tcf.unlink()
        file1.unlink()
        file2.unlink()


def test_input_get_files_tin():
    line = 'Read TIN Zpts == 2d_zsh_brkline_<<~s1~>><<~s2~>>_001_P.12da | 2d_zsh_brkline_<<~s1~>><<~s2~>>_001_L.shp\n'
    tcf = Path(__file__).parent / 'test_control_file.tcf'
    with tcf.open('w') as f:
        f.write(line)
    file1 = Path(__file__).parent / '2d_zsh_brkline_scen15m_001_P.12da'
    with file1.open('w') as f:
        f.write('banana')
    file2 = Path(__file__).parent / '2d_zsh_brkline_scen15m_001_L.shp'
    with file2.open('w') as f:
        f.write('banana')
    file3 = Path(__file__).parent / '2d_zsh_brkline_scen25m_001_P.12da'
    with file3.open('w') as f:
        f.write('banana')
    file4 = Path(__file__).parent / '2d_zsh_brkline_scen25m_001_L.shp'
    with file4.open('w') as f:
        f.write('banana')
    file5 = Path(__file__).parent / '2d_zsh_brkline_scen22.5m_001_P.12da'
    with file5.open('w') as f:
        f.write('banana')
    file6 = Path(__file__).parent / '2d_zsh_brkline_scen22.5m_001_L.shp'
    with file6.open('w') as f:
        f.write('banana')
    try:
        settings = ConvertSettings(*['-tcf', str(tcf)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        files = input.get_files()
        assert sorted(files) == sorted([file1, file2, file3, file4, file5, file6])
    except Exception as e:
        raise e
    finally:
        tcf.unlink()
        file1.unlink()
        file2.unlink()
        file3.unlink()
        file4.unlink()
        file5.unlink()
        file6.unlink()


def test_input_files_ref_in_gis():
    line = 'Read GIS Network == test_datasets/1d_nwk_EG11_001_L.shp'
    ecf = Path(__file__).parent / 'test_control_file.ecf'
    file0 = Path(__file__).parent / 'test_datasets/1d_nwk_EG11_001_L.shp'
    file1 = Path(__file__).parent / 'matrix.csv'
    file2 = Path(__file__).parent / 'flow.csv'
    file3 = Path(__file__).parent / 'area.csv'
    file4 = Path(__file__).parent / 'q_flow.csv'
    file5 = Path(__file__).parent / 'scen1_matrix.csv'
    file6 = Path(__file__).parent / 'scen2_matrix.csv'
    with ecf.open('w') as f:
        f.write(line)
    with file1.open('w') as f:
        f.write('banana')
    with file2.open('w') as f:
        f.write('banana')
    with file3.open('w') as f:
        f.write('banana')
    with file4.open('w') as f:
        f.write('banana')
    with file5.open('w') as f:
        f.write('banana')
    with file6.open('w') as f:
        f.write('banana')
    try:
        settings = ConvertSettings(*['-tcf', str(ecf)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        files = input.get_files()
        assert sorted(files) == sorted([file0, file1, file2, file3, file4, file5, file6])
        assert repr(input._attr_inputs[0]) == '<AttrInput> ATTRIBUTE FILE REFERENCE == ../matrix.csv'
    except Exception as e:
        raise e
    finally:
        ecf.unlink()
        file1.unlink()
        file2.unlink()
        file3.unlink()
        file4.unlink()
        file5.unlink()
        file6.unlink()


def test_input_file():
    settings = ConvertSettings()
    line = 'Is a file == file.txt'
    command = Command(line, settings)
    input = InputBuildState(None, command)
    assert isinstance(input, FileInput)
    assert input.command == 'Is a file'
    assert input.value == 'file.txt'
    assert repr(input) == '<FileInput> Is a file == file.txt'


def test_input_path_no_control_file():
    settings = ConvertSettings()
    line = 'Is a file == file.txt'
    command = Command(line, settings)
    input = InputBuildState(None, command)
    assert input.files == [TuflowPath('file.txt')]


def test_input_path_cf_exists_file_doesnt():
    cf = Path(__file__).parent / 'test_control_file.tcf'
    line = 'Is a file == file.txt'
    with cf.open('w') as f:
        f.write(line)
    try:
        settings = ConvertSettings(*['-tcf', str(cf)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        assert input.files == [cf.parent / 'file.txt']
    except Exception as e:
        raise e
    finally:
        cf.unlink()


def test_input_path_no_control_file_gis():
    settings = ConvertSettings()
    line = 'Read GIS Code == 2d_code.shp'
    command = Command(line, settings)
    input = InputBuildState(None, command)
    assert input.files == [TuflowPath('2d_code.shp')]


def test_input_path_no_control_file_gis_multi():
    settings = ConvertSettings()
    line = 'Read GIS Code == 2d_code.shp | 2d_trim.shp'
    command = Command(line, settings)
    input = InputBuildState(None, command)
    assert sorted(input.files) == sorted([TuflowPath('2d_code.shp'), TuflowPath('2d_trim.shp')])
    assert sorted(input.multi_layer_value) == sorted(input.files)
    assert input.user_def_index == 0


def test_input_path_no_control_file_gis_multi_with_value():
    settings = ConvertSettings()
    line = 'Read GIS Code == 2d_code.shp | 5'
    command = Command(line, settings)
    input = InputBuildState(None, command)
    assert input.files == [TuflowPath('2d_code.shp')]
    assert input.multi_layer_value == [TuflowPath('2d_code.shp'), 5]


def test_input_path_cf_exists_file_doesnt_gis():
    cf = Path(__file__).parent / 'test_control_file.tcf'
    line = 'Read GIS Code == 2d_code.shp'
    with cf.open('w') as f:
        f.write(line)
    try:
        settings = ConvertSettings(*['-tcf', str(cf)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        assert input.files == [cf.parent / '2d_code.shp']
    except Exception as e:
        raise e
    finally:
        cf.unlink()


def test_input_path_cf_exists_file_doesnt_gis_multi():
    cf = Path(__file__).parent / 'test_control_file.tcf'
    line = 'Read GIS Code == 2d_code.shp | 2d_trim.shp'
    with cf.open('w') as f:
        f.write(line)
    try:
        settings = ConvertSettings(*['-tcf', str(cf)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        assert sorted(input.files) == sorted([cf.parent / '2d_code.shp', cf.parent / '2d_trim.shp'])
        assert sorted(input.multi_layer_value) == sorted(input.files)
        assert input.numeric_type is None
    except Exception as e:
        raise e
    finally:
        cf.unlink()


def test_input_path_cf_exists_file_doesnt_gis_multi_with_value():
    cf = Path(__file__).parent / 'test_control_file.tcf'
    line = 'Read GIS Code == 2d_code.shp | 5'
    with cf.open('w') as f:
        f.write(line)
    try:
        settings = ConvertSettings(*['-tcf', str(cf)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        assert input.files == [cf.parent / '2d_code.shp']
        assert input.multi_layer_value == [cf.parent / '2d_code.shp', 5]
        assert input.numeric_type is int
        assert input.user_def_index == 5
    except Exception as e:
        raise e
    finally:
        cf.unlink()


def test_input_path_no_control_file_grid():
    settings = ConvertSettings()
    line = 'Read GRID Zpts == dem.tif'
    command = Command(line, settings)
    input = InputBuildState(None, command)
    assert input.files == [TuflowPath('dem.tif')]


def test_input_path_no_control_file_grid_multi():
    settings = ConvertSettings()
    line = 'Read GRID Zpts == dem.tif | 2d_trim.shp'
    command = Command(line, settings)
    input = InputBuildState(None, command)
    assert sorted(input.files) == sorted([TuflowPath('dem.tif'), TuflowPath('2d_trim.shp')])
    assert sorted(input.multi_layer_value) == sorted(input.files)


def test_input_path_no_control_file_grid_multi_with_value():
    settings = ConvertSettings()
    line = 'Read GRID Zpts == dem.tif | 5'
    command = Command(line, settings)
    input = InputBuildState(None, command)
    assert input.files == [TuflowPath('dem.tif')]


def test_input_path_cf_exists_file_doesnt_grid():
    cf = Path(__file__).parent / 'test_control_file.tcf'
    line = 'Read GRID Zpts == dem.tif'
    with cf.open('w') as f:
        f.write(line)
    try:
        settings = ConvertSettings(*['-tcf', str(cf)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        assert input.files == [cf.parent / 'dem.tif']
    except Exception as e:
        raise e
    finally:
        cf.unlink()


def test_input_path_cf_exists_file_doesnt_grid_multi():
    cf = Path(__file__).parent / 'test_control_file.tcf'
    line = 'Read GRID Zpts == dem.tif | 2d_trim.shp'
    with cf.open('w') as f:
        f.write(line)
    try:
        settings = ConvertSettings(*['-tcf', str(cf)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        assert sorted(input.files) == sorted([cf.parent / 'dem.tif', cf.parent / '2d_trim.shp'])
        assert sorted(input.multi_layer_value) == sorted(input.files)
    except Exception as e:
        raise e
    finally:
        cf.unlink()


def test_input_path_cf_exists_file_doesnt_grid_multi_with_value():
    cf = Path(__file__).parent / 'test_control_file.tcf'
    line = 'Read GRID Zpts == dem.tif | 5'
    with cf.open('w') as f:
        f.write(line)
    try:
        settings = ConvertSettings(*['-tcf', str(cf)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        assert input.files == [cf.parent / 'dem.tif']
    except Exception as e:
        raise e
    finally:
        cf.unlink()


def test_input_path_no_control_file_tin():
    settings = ConvertSettings()
    line = 'Read TIN Zpts == dem.12da'
    command = Command(line, settings)
    input = InputBuildState(None, command)
    assert input.files == [TuflowPath('dem.12da')]


def test_input_path_no_control_file_tin_multi():
    settings = ConvertSettings()
    line = 'Read TIN Zpts == dem.12da | 2d_trim.shp'
    command = Command(line, settings)
    input = InputBuildState(None, command)
    assert sorted(input.files) == sorted([TuflowPath('dem.12da'), TuflowPath('2d_trim.shp')])
    assert sorted(input.multi_layer_value) == sorted(input.files)


def test_input_path_no_control_file_tin_multi_with_value():
    settings = ConvertSettings()
    line = 'Read TIN Zpts == dem.12da | 5'
    command = Command(line, settings)
    input = InputBuildState(None, command)
    assert input.files == [TuflowPath('dem.12da')]


def test_input_path_cf_exists_file_doesnt_tin():
    cf = Path(__file__).parent / 'test_control_file.tcf'
    line = 'Read TIN Zpts == dem.12da'
    with cf.open('w') as f:
        f.write(line)
    try:
        settings = ConvertSettings(*['-tcf', str(cf)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        assert input.files == [cf.parent / 'dem.12da']
    except Exception as e:
        raise e
    finally:
        cf.unlink()


def test_input_path_cf_exists_file_doesnt_tin_multi():
    cf = Path(__file__).parent / 'test_control_file.tcf'
    line = 'Read TIN Zpts == dem.12da | 2d_trim.shp'
    with cf.open('w') as f:
        f.write(line)
    try:
        settings = ConvertSettings(*['-tcf', str(cf)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        assert sorted(input.files) == sorted([cf.parent / 'dem.12da', cf.parent / '2d_trim.shp'])
        assert sorted(input.multi_layer_value) == sorted(input.files)
    except Exception as e:
        raise e
    finally:
        cf.unlink()


def test_input_path_cf_exists_file_doesnt_tin_multi_with_value():
    cf = Path(__file__).parent / 'test_control_file.tcf'
    line = 'Read TIN Zpts == dem.12da | 5'
    with cf.open('w') as f:
        f.write(line)
    try:
        settings = ConvertSettings(*['-tcf', str(cf)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        assert input.files == [cf.parent / 'dem.12da']
    except Exception as e:
        raise e
    finally:
        cf.unlink()


def test_input_path_no_control_file_gis_conveyance():
    settings = ConvertSettings()
    line = 'Read GIS Zpts Modify Conveyance == shapefile.shp | 12.4 | grid.tif'
    command = Command(line, settings)
    input = InputBuildState(None, command)
    assert sorted(input.files) == sorted([TuflowPath('shapefile.shp'), TuflowPath('grid.tif')])
    assert input.multi_layer_value == [TuflowPath('shapefile.shp'), 12.4, TuflowPath('grid.tif')]
    assert input.numeric_type == float


def test_input_path_control_file_gis_conveyance_2():
    cf = Path(__file__).parent / 'test_control_file.tcf'
    line = 'Read GIS Zpts Modify Conveyance == shapefile.shp | 12.4 | grid.tif'
    with cf.open('w') as f:
        f.write(line)
    try:
        settings = ConvertSettings(*['-tcf', str(cf)])
        command = Command(line, settings)
        input = InputBuildState(None, command)
        assert sorted(input.files) == sorted([cf.parent / 'shapefile.shp', cf.parent / 'grid.tif'])
        assert input.multi_layer_value == [cf.parent / 'shapefile.shp', 12.4, cf.parent / 'grid.tif']
        assert input.numeric_type == float
    except Exception as e:
        raise e
    finally:
        cf.unlink()


def test_input_path_variable_index():
    line = 'Read GIS Code == shapefile.shp | <<index>>'
    command = Command(line, ConvertSettings())
    input = InputBuildState(None, command)
    assert input.files == [TuflowPath('shapefile.shp')]
    assert input.multi_layer_value == [TuflowPath('shapefile.shp'), '<<index>>']
    assert input.numeric_type == int


def test_input_figure_out_file_scopes():
    cf = TuflowPath(__file__).parent / 'test_control_file.tcf'
    txt = Path(__file__).parent / 'test_file_testexample.txt'
    with txt.open('w') as f:
        f.write('banana')
    try:
        line = 'Read Text == test_file_<<~s1~>><<~s2~>>.txt'
        settings = ConvertSettings()
        settings.control_file = cf
        command = Command(line, settings)
        input = InputBuildState(None, command)
        scope_list = ScopeList([Scope('SCENARIO', 'test'), Scope('SCENARIO', 'example')])
        input.figure_out_file_scopes(scope_list)
        assert sorted(input.file_scope(input.files[0])) == sorted([x for x in scope_list])
    except Exception as e:
        raise e
    finally:
        txt.unlink()


def test_input_figure_out_file_scopes_gis():
    cf = TuflowPath(__file__).parent / 'test_control_file.tcf'
    txt = Path(__file__).parent / '2d_zsh_brkline_testexample_001_P.shp'
    with txt.open('w') as f:
        f.write('banana')
    try:
        line = 'Read GIS Z Shape == 2d_zsh_brkline_<<~s1~>><<~s2~>>_001_P.shp'
        settings = ConvertSettings()
        settings.control_file = cf
        command = Command(line, settings)
        input = InputBuildState(None, command)
        scope_list = ScopeList([Scope('SCENARIO', 'test'), Scope('SCENARIO', 'example')])
        input.figure_out_file_scopes(scope_list)
        assert sorted(input.file_scope(input.files[0])) == sorted([x for x in scope_list])
    except Exception as e:
        raise e
    finally:
        txt.unlink()


def test_input_figure_out_file_scopes_grid():
    cf = TuflowPath(__file__).parent / 'test_control_file.tcf'
    txt = Path(__file__).parent / 'DEM_testexample.asc'
    with txt.open('w') as f:
        f.write('banana')
    try:
        line = 'Read GRID Zpts == DEM_<<~s1~>><<~s2~>>.asc'
        settings = ConvertSettings()
        settings.control_file = cf
        command = Command(line, settings)
        input = InputBuildState(None, command)
        scope_list = ScopeList([Scope('SCENARIO', 'test'), Scope('SCENARIO', 'example')])
        input.figure_out_file_scopes(scope_list)
        assert sorted(input.file_scope(input.files[0])) == sorted([x for x in scope_list])
    except Exception as e:
        raise e
    finally:
        txt.unlink()


def test_input_figure_out_file_scopes_tin():
    cf = TuflowPath(__file__).parent / 'test_control_file.tcf'
    txt = Path(__file__).parent / 'DEM_testexample.12da'
    with txt.open('w') as f:
        f.write('banana')
    try:
        line = 'Read TIN Zpts == DEM_<<~s1~>><<~s2~>>.12da'
        settings = ConvertSettings()
        settings.control_file = cf
        command = Command(line, settings)
        input = InputBuildState(None, command)
        scope_list = ScopeList([Scope('SCENARIO', 'test'), Scope('SCENARIO', 'example')])
        input.figure_out_file_scopes(scope_list)
        assert sorted(input.file_scope(input.files[0])) == sorted([x for x in scope_list])
    except Exception as e:
        raise e
    finally:
        txt.unlink()


def test_input_figure_out_file_scopes_gis_multi():
    cf = TuflowPath(__file__).parent / 'test_control_file.tcf'
    file1 = Path(__file__).parent / '2d_zsh_brkline_testexample_001_P.shp'
    with file1.open('w') as f:
        f.write('banana')
    file2 = Path(__file__).parent / '2d_zsh_brkline_helloexample_001_R.shp'
    with file2.open('w') as f:
        f.write('banana')
    try:
        line = 'Read GIS Z Shape == 2d_zsh_brkline_<<~s1~>><<~s2~>>_001_P.shp | 2d_zsh_brkline_<<~s3~>><<~s2~>>_001_R.shp'
        settings = ConvertSettings()
        settings.control_file = cf
        command = Command(line, settings)
        input = InputBuildState(None, command)
        scope_list = ScopeList([Scope('SCENARIO', 'test'), Scope('SCENARIO', 'example'), Scope('SCENARIO', 'hello')])
        input.figure_out_file_scopes(scope_list)
        assert sorted(input.file_scope(input.files[0])) == sorted([x for x in scope_list[:2]])
        assert sorted(input.file_scope(input.files[1])) == sorted([x for x in scope_list[1:]])
    except Exception as e:
        raise e
    finally:
        file1.unlink()
        file2.unlink()


def test_input_figure_out_file_scopes_gis_multi_2():
    cf = TuflowPath(__file__).parent / 'test_control_file.tcf'
    file1 = Path(__file__).parent / '2d_zsh_brkline_testexample_001_P.shp'
    with file1.open('w') as f:
        f.write('banana')
    file2 = Path(__file__).parent / '2d_zsh_brkline_helloexample_001_R.shp'
    with file2.open('w') as f:
        f.write('banana')
    try:
        line = 'Read GIS Z Shape == 2d_zsh_brkline_<<~s1~>><<~s2~>>_001_P.shp | <<cell_size>>'
        settings = ConvertSettings()
        settings.control_file = cf
        command = Command(line, settings)
        input = InputBuildState(None, command)
        scope_list = ScopeList([Scope('SCENARIO', 'test'), Scope('SCENARIO', 'example')])
        input.figure_out_file_scopes(scope_list)
        assert sorted(input.file_scope(input.files[0])) == sorted([x for x in scope_list[:2]])
    except Exception as e:
        raise e
    finally:
        file1.unlink()
        file2.unlink()


def test_input_figure_out_file_scopes_grid_multi():
    cf = TuflowPath(__file__).parent / 'test_control_file.tcf'
    file1 = Path(__file__).parent / 'DEM_testexample.asc'
    with file1.open('w') as f:
        f.write('banana')
    file2 = Path(__file__).parent / '2d_zsh_brkline_helloexample_001_R.shp'
    with file2.open('w') as f:
        f.write('banana')
    try:
        line = 'Read GRID Zpts == DEM_<<~s1~>><<~s2~>>.asc | 2d_zsh_brkline_<<~s3~>><<~s2~>>_001_R.shp'
        settings = ConvertSettings()
        settings.control_file = cf
        command = Command(line, settings)
        input = InputBuildState(None, command)
        scope_list = ScopeList([Scope('SCENARIO', 'test'), Scope('SCENARIO', 'example'), Scope('SCENARIO', 'hello')])
        input.figure_out_file_scopes(scope_list)
        assert sorted(input.file_scope(input.files[0])) == sorted([x for x in scope_list[:2]])
        assert sorted(input.file_scope(input.files[1])) == sorted([x for x in scope_list[1:]])
    except Exception as e:
        raise e
    finally:
        file1.unlink()
        file2.unlink()


def test_input_figure_out_file_scopes_tin_multi():
    cf = TuflowPath(__file__).parent / 'test_control_file.tcf'
    file1 = Path(__file__).parent / 'DEM_testexample.12da'
    with file1.open('w') as f:
        f.write('banana')
    file2 = Path(__file__).parent / '2d_zsh_brkline_helloexample_001_R.shp'
    with file2.open('w') as f:
        f.write('banana')
    try:
        line = 'Read TIN Zpts == DEM_<<~s1~>><<~s2~>>.12da | 2d_zsh_brkline_<<~s3~>><<~s2~>>_001_R.shp'
        settings = ConvertSettings()
        settings.control_file = cf
        command = Command(line, settings)
        input = InputBuildState(None, command)
        scope_list = ScopeList([Scope('SCENARIO', 'test'), Scope('SCENARIO', 'example'), Scope('SCENARIO', 'hello')])
        input.figure_out_file_scopes(scope_list)
        assert sorted(input.file_scope(input.files[0])) == sorted([x for x in scope_list[:2]])
        assert sorted(input.file_scope(input.files[1])) == sorted([x for x in scope_list[1:]])
    except Exception as e:
        raise e
    finally:
        file1.unlink()
        file2.unlink()


def test_input_feat_iter_not_exist_error():
    line = 'Read GIS Network == test_datasets/1d_nwk_EG11_001_L_not_exist.shp'
    settings = ConvertSettings()
    settings.control_file = TuflowPath(__file__).parent / 'test_control_file.tcf'
    command = Command(line, settings)
    input = InputBuildState(None, command)
    input.load_attribute_file_ref()


def test_input_feat_iter_file_ogr_error():
    file = Path(__file__).parent / '1d_nwk_not_a_vector_file.shp'
    with file.open('w') as f:
        f.write('banana')
    line = 'Read GIS Network == 1d_nwk_not_a_vector_file.shp'
    try:
        settings = ConvertSettings()
        settings.control_file = TuflowPath(__file__).parent / 'test_control_file.tcf'
        command = Command(line, settings)
        input = InputBuildState(None, command)
        input.load_attribute_file_ref()
    except Exception as e:
        raise e
    finally:
        file.unlink()


def test_input_update_value():
    tcf = TCF()
    inp = tcf.append_input('Hardware == GPU    ! controls the hardware used for the simulation')
    inp.update_value('CPU')
    assert inp.value == 'CPU'
    assert inp._input.comment == '! controls the hardware used for the simulation'
    assert inp._input.original_text == 'Hardware == CPU    ! controls the hardware used for the simulation\n'
    assert inp.dirty


def test_input_update_map_output_format():
    tcf = TCF()
    inp = tcf.append_input('Map Output Format == XMDF TIF    ! output format')
    inp.update_value('NC HRNC')
    assert inp.value == 'NC HRNC'
    assert inp._input.comment == '! output format'
    assert inp._input.original_text == 'Map Output Format == NC HRNC    ! output format\n'
    assert inp.dirty


def test_input_update_file_no_cf():
    tcf = TCF()
    inp = tcf.append_input('Geometry Control File == geom_cf.tgc')
    inp.update_value('geom_cf2.tgc')
    assert inp.value == 'geom_cf2.tgc'
    assert inp.dirty


def test_input_update_file():
    tcf_ = Path(__file__).parent / 'test_001.tcf'
    tcf = TCF()
    tcf._path = TuflowPath(tcf_)
    inp = tcf.append_input('Geometry Control File == geom_cf.tgc  ! geometry control file')
    inp.update_value('geom_cf2.tgc')
    assert inp.value == 'geom_cf2.tgc'
    assert inp._input.comment == '! geometry control file'
    assert inp._input.original_text == 'Geometry Control File == geom_cf2.tgc  ! geometry control file\n'
    assert inp.dirty


def test_input_update_gis():
    tcf_ = Path(__file__).parent / 'test_001.tcf'
    tcf = TCF()
    tcf._path = TuflowPath(tcf_)
    inp = tcf.append_input(r'Read GIS PO == ..\model\gis\2d_po_001.shp   ! time series output object')
    new_path = Path(__file__).parent.parent / 'model' / 'gis' / '2d_po_002.shp'
    inp.update_value(new_path)
    test_path = os.sep.join(['..', 'model', 'gis', '2d_po_002.shp'])
    assert inp.value == test_path
    assert inp._input.comment == '! time series output object'
    assert inp._input.original_text == 'Read GIS PO == ' + test_path + '   ! time series output object\n'
    assert inp.dirty


def test_input_update_gis_2():
    tcf_ = Path(__file__).parent / 'test_001.tcf'
    tcf = TCF()
    tcf._path = TuflowPath(tcf_)
    inp = tcf.append_input(r'Read GIS Z Shape == ..\model\gis\2d_zsh_001_L.shp   ! zshape modifier')
    new_path1 = Path(__file__).parent.parent / 'model' / 'gis' / '2d_zsh_002_L.shp'
    new_path2 = Path(__file__).parent.parent / 'model' / 'gis' / '2d_zsh_002_P.shp'
    inp.update_value([new_path1, new_path2])
    test_paths = ' | '.join([os.sep.join(['..', 'model', 'gis', '2d_zsh_002_L.shp']),
                             os.sep.join(['..', 'model', 'gis', '2d_zsh_002_P.shp'])])
    assert inp.value == test_paths
    assert inp._input.comment == '! zshape modifier'
    assert inp._input.original_text == 'Read GIS Z Shape == ' + test_paths + '   ! zshape modifier\n'
    assert inp.dirty


def test_input_number_log_folder():
    settings = ConvertSettings()
    line = 'Log Folder == 001'
    command = Command(line, settings)
    input = InputBuildState(None, command)
    assert input.value == '001'


def test_input_number_log_folder_2():
    settings = ConvertSettings()
    line = r'Log Folder == log\001'
    command = Command(line, settings)
    input = InputBuildState(None, command)
    assert input.value == r'log\001'


def test_input_number_log_folder_3():
    settings = ConvertSettings()
    settings.variables = {'VERSION': '001'}
    line = r'Log Folder == log\<<VERSION>>'
    command = Command(line, settings)
    input = InputBuildState(None, command)
    assert input.value == r'log\<<VERSION>>'
    assert input.expanded_value == r'log\001'


def test_input_attrs():
    p = './tmf/convert_tuflow_model_gis_format/tests/shp/TUFLOW/runs/EG00_001.tcf'
    tcf = TCF(p)
    inp = tcf.find_input('Read Gis Z Shape')[0]
    assert inp.has_vector == True
    assert inp.has_raster == False
    assert inp.has_tin == False
    assert inp.has_number == False
    assert inp.geom_count == 2
    assert inp.layer_count == 2
    assert inp.file_count == 2
    assert inp.multi_layer == True
    assert inp.geoms == [2, 1]
    assert inp.uses_wild_card == False


def test_input_attrs_2():
    p = './tmf/convert_tuflow_model_gis_format/tests/shp/TUFLOW/runs/EG00_001.tcf'
    tcf = TCF(p)
    inp = tcf.find_input('Modify Conveyance')[0]
    assert inp.has_vector == True
    assert inp.has_raster == True
    assert inp.has_tin == False
    assert inp.has_number == True
    assert inp.geom_count == 1
    assert inp.layer_count == 3
    assert inp.file_count == 2
    assert inp.multi_layer == True
    assert inp.geoms == [3]
    assert inp.uses_wild_card == False


def test_input_attrs_3():
    p = './tmf/convert_tuflow_model_gis_format/tests/mif/TUFLOW/runs/EG00_001.tcf'
    tcf = TCF(p)
    inp = tcf.find_input('Read Gis Z Shape')[0]
    assert inp.has_vector == True
    assert inp.has_raster == False
    assert inp.has_tin == False
    assert inp.has_number == False
    assert inp.geom_count == 2
    assert inp.layer_count == 1
    assert inp.file_count == 1
    assert inp.multi_layer == False
    assert inp.geoms == [2, 1]
    assert inp.uses_wild_card == False


def test_input_attrs_4():
    p = './tmf/convert_tuflow_model_gis_format/tests/scenarios/TUFLOW/runs/test_scenarios_in_fname.tcf'
    tcf = TCF(p)
    inp = tcf.find_input('Read Gis PO')[1]
    assert inp.has_vector == True
    assert inp.has_raster == False
    assert inp.has_tin == False
    assert inp.has_number == False
    assert inp.geom_count == 1
    assert inp.layer_count == 1
    assert inp.file_count == 1
    assert inp.multi_layer == False
    assert inp.geoms == [1]
    assert inp.uses_wild_card == True


def test_input_attrs_5():
    p = './tmf/convert_tuflow_model_gis_format/tests/shp/TUFLOW/runs/EG00_001.tcf'
    tcf = TCF(p)
    inp = tcf.find_input('Read Grid')[0]
    assert inp.has_vector == True
    assert inp.has_raster == True
    assert inp.has_tin == False
    assert inp.has_number == False
    assert inp.geom_count == 1
    assert inp.layer_count == 2
    assert inp.file_count == 2
    assert inp.multi_layer == True
    assert inp.geoms == [3]
    assert inp.uses_wild_card == False


def test_input_attrs_6():
    p = './tmf/convert_tuflow_model_gis_format/tests/tins/TUFLOW/runs/tin_copy_test.tcf'
    tcf = TCF(p)
    inp = tcf.find_input('Read Tin')[0]
    assert inp.has_vector == True
    assert inp.has_raster == False
    assert inp.has_tin == True
    assert inp.has_number == False
    assert inp.geom_count == 1
    assert inp.layer_count == 2
    assert inp.file_count == 2
    assert inp.multi_layer == True
    assert inp.geoms == [3]
    assert inp.uses_wild_card == False


def test_input_match():
    line = r'Read GIS Network == ../model/gis/1d_nwk_EG15_001_L.shp'
    settings = ConvertSettings()
    settings.control_file = TuflowPath('./tmf/convert_tuflow_model_gis_format/tests/shp/TUFLOW/runs/EG00_001.tcf')
    command = Command(line, settings)
    inp = InputBuildState(None, command)
    assert inp.is_match('Read GIS')
    assert inp.is_match(command='Read GIS')
    assert inp.is_match(value='1d_nwk')
    assert inp.is_match('^Read GIS (Network|Table)?', regex=True)
    assert inp.is_match(tags=('missing_files', False))
    assert inp.is_match(tags='has_vector')
    assert inp.is_match(tags=('layer_count', 1))
    assert inp.is_match(tags=(('layer_count', 1), ('geom_count', 1)))
    assert inp.is_match('Read GRID') == False
    assert inp.is_match(command='Read GRID') == False
    assert inp.is_match(value='1d_nd') == False
    assert inp.is_match('^Read grid Zpts', regex=True) == False
    assert inp.is_match(tags=('missing_files', True)) == False
    assert inp.is_match(tags='has_raster') == False
    assert inp.is_match(tags=('file_count', 2)) == False
    f = lambda x: 2 in x
    assert inp.is_match(tags=('geoms', f))
    f = lambda x: 1 in x
    assert inp.is_match(tags=('geoms', f)) == False

    def callback(inp):
        return inp.layer_count == 1
    assert inp.is_match(callback=callback)

    def callback(inp):
        return inp.missing_files
    assert inp.is_match(callback=callback) == False
