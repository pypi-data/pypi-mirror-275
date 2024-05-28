import pytest

from tmf.tuflow_model_files.dataclasses.altered_input import (AlteredInput, AlteredInputUpdatedValue,
                                                              AlteredInputUpdatedCommand, AlteredInputAddedInput,
                                                              AlteredInputRemovedInput, AlteredInputSetScope,
                                                              AlteredInputs)
from tmf.tuflow_model_files.inp._inp_build_state import InputBuildState
from tmf.tuflow_model_files.cf._cf_build_state import ControlFileBuildState
from tmf.tuflow_model_files.utils.commands import Command
from tmf.tuflow_model_files.utils.settings import Settings
from tmf.tuflow_model_files.dataclasses.scope import Scope, ScopeList


def test_updated_value_undo():
    cf = ControlFileBuildState()
    cmd = Command('Hardware == GPU', Settings())
    inp = InputBuildState(cf, cmd)
    cf.inputs.append(inp)
    alt = AlteredInput(cmd, inp._scope, cf, None, 0, 0, 0, 'update_value')
    assert isinstance(alt, AlteredInputUpdatedValue)
    cmd = Command('Hardware == CPU', Settings())
    inp.set_raw_command_obj(cmd)
    assert str(inp.raw_command_obj()) == 'Hardware == CPU'
    alt.undo()
    assert str(inp.raw_command_obj()) == 'Hardware == GPU'


def test_updated_command_undo():
    cf = ControlFileBuildState()
    cmd = Command('Hardware == GPU', Settings())
    inp = InputBuildState(cf, cmd)
    cf.inputs.append(inp)
    alt = AlteredInput(cmd, inp._scope, cf, None, 0, 0, 0, 'update_command')
    assert isinstance(alt, AlteredInputUpdatedCommand)
    cmd = Command('Solution Scheme == HPC', Settings())
    inp.set_raw_command_obj(cmd)
    assert str(inp.raw_command_obj()) == 'Solution Scheme == HPC'
    alt.undo()
    assert str(inp.raw_command_obj()) == 'Hardware == GPU'


def test_add_input_undo():
    cf = ControlFileBuildState()
    cmd = Command('Hardware == GPU', Settings())
    inp = InputBuildState(cf, cmd)
    cf.inputs.append(inp)
    alt = AlteredInput(cmd, inp._scope, cf, None, 0, 0, 0, 'add_input')
    assert isinstance(alt, AlteredInputAddedInput)
    assert len(cf.inputs) == 1
    alt.undo()
    assert len(cf.inputs) == 0


def test_remove_input_undo():
    cf = ControlFileBuildState()
    cmd = Command('Hardware == GPU', Settings())
    inp = InputBuildState(cf, cmd)
    alt = AlteredInput(cmd, inp._scope, cf, None, 0, 0, 0, 'remove_input')
    assert isinstance(alt, AlteredInputRemovedInput)
    assert len(cf.inputs) == 0
    alt.undo()
    assert len(cf.inputs) == 1


def test_input_set_scope_undo():
    cf = ControlFileBuildState()
    cmd = Command('Hardware == GPU', Settings())
    inp = InputBuildState(cf, cmd)
    inp._scope = ScopeList([Scope('SCENARIO', 'DEV')])
    cf.inputs.append(inp)
    alt = AlteredInput(cmd, inp._scope, cf, None, 0, 0, 0, 'set_scope')
    assert isinstance(alt, AlteredInputSetScope)
    inp._scope = ScopeList([Scope('SCENARIO', 'BASE')])
    assert inp.scope() == [Scope('SCENARIO', 'BASE')]
    alt.undo()
    assert inp.scope() == [Scope('SCENARIO', 'DEV')]


def test_altered_inputs_undo_group():
    alt_inps = AlteredInputs()
    cf = ControlFileBuildState()
    cmd = Command('Solution Scheme == HPC', Settings())
    inp = InputBuildState(cf, cmd)
    cf.inputs.append(inp)
    alt_inps.add(inp, 0, 0, 0, 'add_input')
    cmd = Command('Hardware == GPU', Settings())
    inp = InputBuildState(cf, cmd)
    cf.inputs.append(inp)
    alt_inps.add(inp, 1, 1, 0, 'add_input')
    assert len(cf.inputs) == 2
    alt_inps.undo(cf, False)
    assert len(cf.inputs) == 0


def test_altered_inputs_check_dirty():
    alt_inps = AlteredInputs()
    cf = ControlFileBuildState()
    cmd = Command('Solution Scheme == HPC', Settings())
    inp = InputBuildState(cf, cmd)
    cf.inputs.append(inp)
    alt_inps.add(inp, 0, 0, 0, 'add_input')
    cmd = Command('Hardware == GPU', Settings())
    inp = InputBuildState(cf, cmd)
    cf.inputs.append(inp)
    alt_inps.add(inp, 1, 1, 0, 'add_input')
    assert alt_inps.is_dirty(cf) == True


def test_altered_inputs_clear():
    alt_inps = AlteredInputs()
    cf = ControlFileBuildState()
    cf.dirty = True
    cmd = Command('Solution Scheme == HPC', Settings())
    inp = InputBuildState(cf, cmd)
    inp.dirty = True
    cf.inputs.append(inp)
    alt_inps.add(inp, 0, 0, 0, 'add_input')
    alt_inps.clear()
    assert alt_inps.is_dirty(cf) == False
    assert cf.dirty == False
    assert inp.dirty == False
