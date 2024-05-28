import pytest

from tmf.convert_tuflow_model_gis_format.conv_tf_gis_format.helpers.command import Command
from tmf.convert_tuflow_model_gis_format.conv_tf_gis_format.helpers.settings import ConvertSettings
from tmf.tuflow_model_files.inp._inp_build_state import InputBuildState
from tmf.tuflow_model_files.dataclasses.inputs import Inputs
from tmf.tuflow_model_files.dataclasses.scope import Scope


def test_inputs_init_blank():
    inputs = Inputs()
    assert inputs is not None
    assert len(inputs) == 0
    inputs.resolve_scopes()


def test_inputs_init_blank_2():
    inputs = Inputs()
    settings = ConvertSettings()
    inputs.append(InputBuildState(None, Command('', settings)))
    assert inputs is not None
    assert len(inputs) == 0


def test_inputs_init():
    inputs = Inputs()
    settings = ConvertSettings()
    inputs.append(InputBuildState(None, Command('Tutorial Model == ON', settings)))
    assert inputs is not None
    assert len(inputs) == 1
    assert repr(inputs) == 'Inputs([\'Tutorial Model == ON\'])'
    assert inputs._known_scopes() == [Scope('GLOBAL', '')]
    inputs.resolve_scopes()


def test_inputs_iter():
    inputs = Inputs()
    settings = ConvertSettings()
    inputs.append(InputBuildState(None, Command('', settings)))
    inputs.append(InputBuildState(None, Command('', settings)))
    inputs.append(InputBuildState(None, Command('', settings)))
    for input in inputs:
        assert input is not None


def test_inputs_slice():
    inputs = Inputs()
    settings = ConvertSettings()
    inputs.append(InputBuildState(None, Command('Tutorial Model == ON', settings)))
    inputs.append(InputBuildState(None, Command('SGS == ON', settings)))
    assert inputs[:] == [InputBuildState(None, Command('Tutorial Model == ON', settings)), InputBuildState(None, Command('SGS == ON', settings))]


def test_inputs_get_item_error():
    inputs = Inputs()
    settings = ConvertSettings()
    inputs.append(InputBuildState(None, Command('Tutorial Model == ON', settings)))
    inputs.append(InputBuildState(None, Command('SGS == ON', settings)))
    with pytest.raises(TypeError):
        input = inputs['a']

